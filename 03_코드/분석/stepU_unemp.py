import pandas as pd, numpy as np, glob, json, warnings; warnings.filterwarnings("ignore")
import statsmodels.api as sm, statsmodels.formula.api as smf
# 1. county-year unemployment
rows=[]
for f in sorted(glob.glob("ext/bls/*laucnty*.xlsx")):
    x=pd.read_excel(f,header=None,skiprows=2); x=x[[1,2,4,8]]; x.columns=['st','cty','year','ur']; x=x.dropna(subset=['st','cty','year'])
    x['GEOID']=x.st.astype(int).astype(str).str.zfill(2)+x.cty.astype(int).astype(str).str.zfill(3); x['year']=x.year.astype(int); x['ur']=pd.to_numeric(x.ur,errors='coerce'); rows.append(x[['GEOID','year','ur']])
U=pd.concat(rows); print("county-years",len(U), U.year.min(), U.year.max())
# 2. zip3-year unemployment, population weighted via ZCTA-county file
rel=pd.read_csv("/root/.claude/uploads/6fc5949e-7a7e-5a39-a0ca-18d9d5045a2b/50678666-zcta_county_rel_10.txt", dtype={'ZCTA5':str,'GEOID':str}); rel['zip3']=rel.ZCTA5.str[:3]
wz=rel.groupby(['zip3','GEOID']).POPPT.sum().reset_index()
m=wz.merge(U,on='GEOID'); m['w']=m.POPPT.astype(float)+1e-9
Z=m.groupby(['zip3','year']).apply(lambda d: np.average(d.ur.fillna(d.ur.mean()),weights=d.w)).rename('ur').reset_index(); Z=Z.dropna()
print("zip3-years",len(Z)); Zp=Z.pivot(index='zip3',columns='year',values='ur')
# 3. attach to loans: ur at origination year; change over loan life = max UR in [yr+1, min(yr+term_years, 2018)] - ur_orig
T=pd.read_pickle("T.pkl"); zp=pd.read_pickle("out/zip3.pkl"); zp['zip3']=zp.zip3.astype(str).str.zfill(3)
et=pd.read_pickle("lc_final.pkl")['emp_title'].fillna('').str.lower().str.strip().loc[T.index]
role=et.str.contains(r"\bpastor\b|\bminister\b|\bclergy\b|\bpriest\b|\bchaplain\b|\brabbi\b|\bmissionar|\breverend\b|\bevangelist\b|\bdeacon\b|\bimam\b",regex=True)
org=et.str.contains(r"\bchurch\b|\bparish\b|\bdiocese\b|\bcongregation\b|\bsynagogue\b|\bministr",regex=True)
inst=et.str.contains(r"hospital|health|medical|charit|university|college|school|academy|insurance|bank|credit union|hospice|clinic",regex=True)
T['relaff']=(role|(org&~inst)); print("religious-institution affiliation n",int(T.relaff.sum()))
S=pd.concat([T[T.relaff], T[~T.relaff].sample(250000,random_state=1)]).copy(); S['id']=pd.to_numeric(S.id,errors='coerce').astype('Int64'); S=S.merge(zp[['id','zip3']],on='id',how='left')
S=S[S.zip3.isin(Zp.index)].reset_index(drop=True); yr=S.year.astype(int).values; z=S.zip3.values; ty=np.where(S.term60==1,5,3)
ur0=np.array([Zp.at[a,b] if b in Zp.columns else np.nan for a,b in zip(z,yr)])
urmax=np.array([np.nanmax([Zp.at[a,c] for c in range(b+1,min(b+t,2018)+1) if c in Zp.columns] or [np.nan]) for a,b,t in zip(z,yr,ty)])
S['ur0']=ur0; S['dur']=urmax-ur0; S=S.dropna(subset=['ur0','dur']).reset_index(drop=True)
S['ur0_z']=(S.ur0-S.ur0.mean())/S.ur0.std(); S['dur_z']=(S.dur-S.dur.mean())/S.dur.std()
print("n",len(S),"relaff",int(S.relaff.sum()),"ur0 mean",round(S.ur0.mean(),2),"dur mean",round(S.dur.mean(),2),"sd",round(S.dur.std(),2))
ctrl="C(grade) + C(yr) + int + fico + linc + dti + term60 + lamt + C(emp) + C(home) + C(ver) + C(purp) + C(st)"
def fit(f,keys):
    G=pd.factorize(S['st'])[0]; mdl=smf.logit(f,data=S); m=mdl.fit(method='newton',maxiter=100,disp=0,cov_type='cluster',cov_kwds={'groups':G})
    if not m.mle_retvals.get('converged'): m=mdl.fit(method='bfgs',start_params=m.params,maxiter=2000,disp=0,cov_type='cluster',cov_kwds={'groups':G})
    return {k:dict(OR=float(np.exp(m.params[k])),p=float(m.pvalues[k])) for k in keys}
res={}
res['main']=fit(f"default ~ relaff + ur0_z + dur_z + {ctrl}",['relaff[T.True]','ur0_z','dur_z']); print("main:",res['main'])
res['x_shock']=fit(f"default ~ relaff*dur_z + ur0_z + {ctrl}",['relaff[T.True]','relaff[T.True]:dur_z','dur_z']); print("relaff x unemployment shock:",res['x_shock'])
res['x_level']=fit(f"default ~ relaff*ur0_z + dur_z + {ctrl}",['relaff[T.True]','relaff[T.True]:ur0_z']); print("relaff x unemployment level:",res['x_level'])
# terciles of shock
S['sh_t']=pd.qcut(S.dur.rank(method='first'),3,labels=['small','mid','large'])
for t in ['small','mid','large']:
    s=S[S.sh_t==t].reset_index(drop=True); G=pd.factorize(s['st'])[0]; m=smf.logit(f"default ~ relaff + {ctrl}",data=s).fit(method='newton',maxiter=100,disp=0,cov_type='cluster',cov_kwds={'groups':G})
    res[f'tercile_{t}']=dict(OR=float(np.exp(m.params['relaff[T.True]'])),p=float(m.pvalues['relaff[T.True]']),n_aff=int(s.relaff.sum()),mean_shock=float(s.dur.mean())); print("shock tercile",t,res[f'tercile_{t}'])
# placebo: teachers/nurses x shock (stable-income occupations should show protective interaction if mechanism is income stability)
S['teacher']=et.loc[S.index if False else S.index].values if False else 0
json.dump(res,open("out/stepU_unemp.json","w"),indent=1)
Zp.to_pickle("out/zip3_unemp.pkl")
