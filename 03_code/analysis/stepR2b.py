import pandas as pd, numpy as np, json, warnings, gc; warnings.filterwarnings("ignore")
import statsmodels.formula.api as smf
exec(open("stepR2a.py").read().split("res={}")[0])   # reuse setup (T, maps, fitm, rep, ctrl)
res=json.load(open("out/stepR2a.json"))
TS=pd.concat([T[T.clergy], T[~T.clergy].sample(250000, random_state=1)]).copy()
S=TS.copy(); S['id']=pd.to_numeric(S.id,errors='coerce').astype('Int64'); S=S.merge(zp[['id','zip3']],on='id',how='left')
S=S[S.zip3.isin(Zp.index)].reset_index(drop=True); yr=S.year.astype(int).values; z=S.zip3.values; ty=np.where(S.term60==1,5,3)
S['ur0']=[Zp.at[a,b] if b in Zp.columns else np.nan for a,b in zip(z,yr)]
S['dur']=np.array([np.nanmax([Zp.at[a,c] for c in range(b+1,min(b+t,2018)+1) if c in Zp.columns] or [np.nan]) for a,b,t in zip(z,yr,ty)])-S.ur0
S=S.merge(z3[['cng_per_10k','totrate']],left_on='zip3',right_index=True,how='left').dropna(subset=['ur0','dur','cng_per_10k','totrate']).reset_index(drop=True)
# Table 7 standardization: across ZIP3 areas
S['cng_z']=(S.cng_per_10k-z3.cng_per_10k.mean())/z3.cng_per_10k.std(); S['rel_z']=(S.totrate-z3.totrate.mean())/z3.totrate.std()
S['ur0_z']=(S.ur0-S.ur0.mean())/S.ur0.std(); S['dur_z']=(S.dur-S.dur.mean())/S.dur.std()
S['aff']=S.clergy.astype(int); S['aff_emp10']=S.aff*S.emp10; S['aff_ver']=S.aff*S.verified
res['TB']={'n':int(len(S)),'aff':int(S.aff.sum())}
spec={'A1_density':f"default ~ aff*cng_z + rel_z + {ctrl}",
      'A2_shock':f"default ~ aff*dur_z + ur0_z + {ctrl}",
      'A3_stability':f"default ~ aff + aff_emp10 + aff_ver + {ctrl}",
      'A4_all':f"default ~ aff*cng_z + rel_z + aff*dur_z + ur0_z + aff_emp10 + aff_ver + {ctrl}"}
for k,f in spec.items():
    mm=fitm(f,S); keys=[x for x in ['aff','aff:cng_z','cng_z','aff:dur_z','aff_emp10','aff_ver'] if x in mm.params.index]
    res['TB'][k]={x:rep(mm,x) for x in keys}; print(k,{x:(round(v['OR'],3),round(v['p2'],3)) for x,v in res['TB'][k].items()},flush=True)
    if k=='A1_density':
        pp={}
        for a in [0,1]:
            for d in [-1,1]:
                X=S.copy(); X['aff']=a; X['cng_z']=d; pp[f'aff{a}_d{d:+d}']=float(mm.predict(X).mean())
        res['TB']['pred']=pp; print(pp,flush=True)
    del mm; gc.collect()
json.dump(res,open("out/stepR2a.json","w"),indent=1)
# Wild cluster bootstrap (WCR, Webb weights, 9,999 reps) on LPM analogues, clustered by state
from wildboottest.wildboottest import wildboottest
import statsmodels.api as sm
def wcb(formula,data,var):
    y,X=__import__('patsy').dmatrices(formula,data,return_type='dataframe')
    mod=sm.OLS(y,X); G=pd.factorize(data.loc[y.index,'st'])[0]
    r=wildboottest(mod,param=var,cluster=G,B=9999,weights_type='webb',impose_null=True,bootstrap_type='11',seed=12345,show=False)
    ols=mod.fit(cov_type='cluster',cov_kwds={'groups':G})
    out=dict(coef=float(ols.params[var]),cr1_p=float(ols.pvalues[var]),wcb_p=float(r['pvalue'].iloc[0] if hasattr(r['pvalue'],'iloc') else r['pvalue']),n=int(ols.nobs),clusters=int(len(set(G))))
    print(var,out,flush=True); return out
res['WCB']={}
res['WCB']['H1']=wcb(f"default ~ clergy + {ctrl}",TS,'clergy[T.True]'); json.dump(res,open("out/stepR2a.json","w"),indent=1)
D=pd.read_pickle("D.pkl")
res['WCB']['H2']=wcb(f"default ~ relig_strict + {ctrl} + llen + moral + hardship + gratitude + family + help + business",D,'relig_strict[T.True]')
json.dump(res,open("out/stepR2a.json","w"),indent=1); print("WCB done",flush=True)
