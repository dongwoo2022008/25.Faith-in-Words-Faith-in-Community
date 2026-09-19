# Reviewer-anticipation extras: (2) selection into writing a description; (4) alternative SE clustering; (1) balance table export
import pandas as pd, numpy as np, json, warnings; warnings.filterwarnings("ignore")
import statsmodels.formula.api as smf
res={}
T=pd.read_pickle("T.pkl"); D=pd.read_pickle("D.pkl")
ctrl="C(grade) + C(yr) + int + fico + linc + dti + term60 + lamt + C(emp) + C(home) + C(ver) + C(purp) + C(st)"
txt="llen + moral + hardship + gratitude + family + help + business"
def fit(f,data,clusters,keys):
    data=data.reset_index(drop=True); G=pd.factorize(clusters.reset_index(drop=True))[0]
    mdl=smf.logit(f,data=data); m=mdl.fit(method='newton',maxiter=100,disp=0,cov_type='cluster',cov_kwds={'groups':G})
    if not m.mle_retvals.get('converged'): m=mdl.fit(method='bfgs',start_params=m.params,maxiter=2000,disp=0,cov_type='cluster',cov_kwds={'groups':G})
    return {k:dict(coef=float(m.params[k]),se=float(m.bse[k]),p=float(m.pvalues[k]),OR=float(np.exp(m.params[k]))) for k in keys}
# ---- (2) selection into description, 2008-2014 terminal loans
S0=T[T.year.between(2008,2014)]; S=pd.concat([S0[S0.clergy], S0[~S0.clergy].sample(150000,random_state=5)]).copy(); S['hd']=S.has_desc.astype(int); S['aff']=S.clergy.astype(int)
print("selection sample",len(S),"has_desc share",S.hd.mean())
m=smf.logit(f"hd ~ aff + {ctrl}",data=S).fit(method='newton',maxiter=100,disp=0,cov_type='cluster',cov_kwds={'groups':pd.factorize(S['st'])[0]})
keys=['aff','int','fico','linc','dti','term60','lamt']+[k for k in m.params.index if k.startswith('C(grade)')]
sel={k:dict(coef=float(m.params[k]),se=float(m.bse[k]),p=float(m.pvalues[k]),OR=float(np.exp(m.params[k]))) for k in keys}
# AME for continuous vars: one SD
X=m.model.exog; p=m.model.cdf(X@m.params.values)
ame={}
for k in ['aff','int','fico','linc','dti','lamt']:
    j=list(m.model.exog_names).index(k); X2=X.copy(); X2[:,j]+= (1 if k=='aff' else S[k].std()); ame[k]=float(np.mean(m.model.cdf(X2@m.params.values)-p))
res['selection_into_description']=dict(n=int(m.nobs),share=float(S.hd.mean()),coefs=sel,ame_per_unit_or_sd=ame,pseudo_r2=float(m.prsquared))
print("selection:",{k:round(v['OR'],3) for k,v in sel.items()}); print("AME",{k:round(v,4) for k,v in ame.items()})
# ---- (4) alternative clustering
zp=pd.read_pickle("out/zip3.pkl"); zp['zip3']=zp.zip3.astype(str).str.zfill(3)
TS=pd.concat([T[T.clergy], T[~T.clergy].sample(250000,random_state=1)]).copy(); TS['id']=pd.to_numeric(TS.id,errors='coerce').astype('Int64'); TS=TS.merge(zp[['id','zip3']],on='id',how='left'); TS['zip3']=TS.zip3.fillna('NA')
TS['ym']=TS.issue_d.astype(str)
D2=D.copy(); D2['id']=pd.to_numeric(D2.id,errors='coerce').astype('Int64'); D2=D2.merge(zp[['id','zip3']],on='id',how='left'); D2['zip3']=D2.zip3.fillna('NA'); D2['ym']=D2.issue_d.astype(str)
out={}
for lab,cl in [('state',TS['st']),('zip3',TS['zip3']),('issue_month',TS['ym'])]:
    r=fit(f"default ~ clergy + {ctrl}",TS,cl,['clergy[T.True]'])['clergy[T.True]']; out[f'H1_{lab}']=r; print('H1',lab,round(r['se'],4),r['p'])
for lab,cl in [('state',D2['st']),('zip3',D2['zip3']),('issue_month',D2['ym'])]:
    r=fit(f"default ~ relig_strict + {ctrl} + {txt}",D2,cl,['relig_strict[T.True]'])['relig_strict[T.True]']; out[f'H2_{lab}']=r; print('H2',lab,round(r['se'],4),r['p'])
# HC1 robust (no clustering)
for lab,data,f,k in [('H1',TS,f"default ~ clergy + {ctrl}",'clergy[T.True]'),('H2',D2,f"default ~ relig_strict + {ctrl} + {txt}",'relig_strict[T.True]')]:
    m=smf.logit(f,data=data.reset_index(drop=True)).fit(method='newton',maxiter=100,disp=0,cov_type='HC1'); out[f'{lab}_HC1']=dict(coef=float(m.params[k]),se=float(m.bse[k]),p=float(m.pvalues[k]),OR=float(np.exp(m.params[k]))); print(lab,'HC1',round(m.bse[k],4))
res['alt_clustering']=out
res['n_clusters']=dict(state=int(TS.st.nunique()),zip3=int(TS.zip3.nunique()),issue_month=int(TS.ym.nunique()))
# ---- (1) balance table already at out/표5c_균형표.csv (76 moments)
b=pd.read_csv("out/표5c_균형표.csv"); res['balance']=dict(n_moments=len(b),max_abs_smd_before=float(b.smd_before.abs().max()),n_smd_gt_0_1_before=int((b.smd_before.abs()>0.1).sum()),max_abs_smd_after=float(b.smd_after.abs().max()))
print(res['balance']); json.dump(res,open("out/stepG_extras.json","w"),indent=1); print("DONE")
