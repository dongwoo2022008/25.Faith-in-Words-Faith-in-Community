import pandas as pd, numpy as np, json, warnings; warnings.filterwarnings("ignore")
import statsmodels.formula.api as smf
rel=pd.read_csv("/root/.claude/uploads/6fc5949e-7a7e-5a39-a0ca-18d9d5045a2b/50678666-zcta_county_rel_10.txt", dtype={'ZCTA5':str,'GEOID':str})
rel['zip3']=rel.ZCTA5.str[:3]; ar=pd.read_pickle("out/arda2010.pkl"); ar['GEOID']=ar.fips.astype(int).astype(str).str.zfill(5)
m=rel.merge(ar[['GEOID','totrate','cng_per_10k','evanrate','mprtrate','cathrate','bprtrate']],on='GEOID',how='left')
# zip3-level population-weighted county religiosity
w=m.POPPT.astype(float); g=m.assign(w=w).groupby('zip3')
z3=pd.DataFrame({k:g.apply(lambda d: np.average(d[k].fillna(d[k].mean()),weights=d.w+1e-9)) for k in ['totrate','cng_per_10k','evanrate','mprtrate','cathrate','bprtrate']})
z3['n_counties']=g.GEOID.nunique(); print("zip3 areas:",len(z3)); z3.to_pickle("out/zip3_religiosity.pkl")
zp=pd.read_pickle("out/zip3.pkl"); zp['zip3']=zp.zip3.astype(str).str.zfill(3)
T=pd.read_pickle("T.pkl"); D=pd.read_pickle("D.pkl")
def attach(df):
    df=df.copy(); df['id']=pd.to_numeric(df.id,errors='coerce').astype('Int64'); df=df.merge(zp[['id','zip3']],on='id',how='left').merge(z3,on='zip3',how='left')
    df['rel_z']=(df.totrate-z3.totrate.mean())/z3.totrate.std(); df['cng_z']=(df.cng_per_10k-z3.cng_per_10k.mean())/z3.cng_per_10k.std(); df['evan_z']=(df.evanrate-z3.evanrate.mean())/z3.evanrate.std()
    return df.dropna(subset=['rel_z','cng_z','evan_z']).reset_index(drop=True)
TS=attach(pd.concat([T[T.clergy], T[~T.clergy].sample(250000,random_state=1)])); DD=attach(D)
print("matched: TS",len(TS),"of",253105,"| D",len(DD),"of",len(D))
ctrl="C(grade) + C(yr) + int + fico + linc + dti + term60 + lamt + C(emp) + C(home) + C(ver) + C(purp) + C(st)"
ctrl2=ctrl+" + llen + moral + hardship + gratitude + family + help + business"
def fit(f,data,keys):
    data=data.reset_index(drop=True); G=pd.factorize(data['st'])[0]; mdl=smf.logit(f,data=data,missing='drop'); m=mdl.fit(method='newton',maxiter=100,disp=0,cov_type='cluster',cov_kwds={'groups':G})
    if not m.mle_retvals.get('converged'): m=mdl.fit(method='bfgs',start_params=m.params,maxiter=2000,disp=0,cov_type='cluster',cov_kwds={'groups':G})
    return {k:dict(OR=float(np.exp(m.params[k])),p=float(m.pvalues[k])) for k in keys if k in m.params}
res={}
# (1) regional religiosity itself, and (2) signals with regional religiosity controlled
res['H1_ctrl_regional']=fit(f"default ~ clergy + rel_z + cng_z + {ctrl}",TS,['clergy[T.True]','rel_z','cng_z']); print("H1 + regional:",res['H1_ctrl_regional'])
res['H2_ctrl_regional']=fit(f"default ~ relig_strict + rel_z + cng_z + {ctrl2}",DD,['relig_strict[T.True]','rel_z','cng_z']); print("H2 + regional:",res['H2_ctrl_regional'])
# regional religiosity alone without state FE (state FE absorbs most between-state variation) -> replicate Li & Ucar-style
res['regional_noStateFE']=fit(f"default ~ rel_z + cng_z + "+ctrl.replace(" + C(st)",""),TS,['rel_z','cng_z']); print("regional (no state FE):",res['regional_noStateFE'])
res['regional_evan_noStateFE']=fit(f"default ~ evan_z + "+ctrl.replace(" + C(st)",""),TS,['evan_z']); print("evangelical share:",res['regional_evan_noStateFE'])
# (3) interactions: community monitoring
res['H1_x_adherence']=fit(f"default ~ clergy*rel_z + cng_z + {ctrl}",TS,['clergy[T.True]','clergy[T.True]:rel_z']); print("clergy x adherence:",res['H1_x_adherence'])
res['H1_x_congdensity']=fit(f"default ~ clergy*cng_z + rel_z + {ctrl}",TS,['clergy[T.True]','clergy[T.True]:cng_z']); print("clergy x cong density:",res['H1_x_congdensity'])
res['H2_x_adherence']=fit(f"default ~ relig_strict*rel_z + cng_z + {ctrl2}",DD,['relig_strict[T.True]','relig_strict[T.True]:rel_z']); print("relig x adherence:",res['H2_x_adherence'])
# terciles for readability
TS['rel_t']=pd.qcut(TS.rel_z,3,labels=['low','mid','high'])
for t in ['low','mid','high']:
    s=TS[TS.rel_t==t]; r=fit(f"default ~ clergy + {ctrl}",s,['clergy[T.True]']); r['n_clergy']=int(s.clergy.sum()); res[f'H1_tercile_{t}']=r; print("clergy in",t,"religiosity tercile:",r)
print("clergy share by tercile:",TS.groupby('rel_t').clergy.mean().round(4).to_dict())
json.dump(res,open("out/stepA_arda.json","w"),indent=1)
