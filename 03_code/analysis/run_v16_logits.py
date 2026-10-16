# v16 additions: (a) H1 excluding 60-month loans issued in 2014 (not matured at the 2018Q4 release);
# (b) length-matched H2 with the Table 6, column (3) controls and state-clustered SE, reporting SE and AME.
# Baselines are re-estimated first as a reproduction check against step2_results.json. Output: v16_logits.json
import pandas as pd, numpy as np, json, warnings, time; warnings.filterwarnings("ignore")
import statsmodels.formula.api as smf
def robust_fit(model, groups, maxiter=100):
    kw=dict(cov_type='cluster',cov_kwds={'groups':groups})
    m=model.fit(method='newton',maxiter=maxiter,disp=0,**kw)
    if not m.mle_retvals.get('converged',False):
        m=model.fit(method='bfgs',start_params=m.params,maxiter=2000,disp=0,**kw)
    return m
def fit(formula, data, var):
    t=time.time(); m=robust_fit(smf.logit(formula, data=data), pd.factorize(data['st'])[0])
    key=[i for i in m.params.index if i.startswith(var)][0]
    X=m.model.exog.copy(); j=list(m.model.exog_names).index(key)
    X[:,j]=1; p1=m.model.cdf(X@m.params.values); X[:,j]=0; p0=m.model.cdf(X@m.params.values); ame=float(np.mean(p1-p0)); del X
    r=dict(n=int(m.nobs), n_treated=int(data[var].sum()), coef=float(m.params[key]), se=float(m.bse[key]), p=float(m.pvalues[key]), OR=float(np.exp(m.params[key])), AME=float(ame), converged=bool(m.mle_retvals.get('converged',None)), sec=round(time.time()-t))
    print(var, {k:(round(v,4) if isinstance(v,float) else v) for k,v in r.items()}, flush=True); return r
T=pd.read_pickle("T.pkl"); D=pd.read_pickle("D.pkl")
ctrl="C(grade) + C(yr) + int + fico + linc + dti + term60 + lamt + C(emp) + C(home) + C(ver) + C(purp) + C(st)"
TS=pd.concat([T[T.clergy], T[~T.clergy].sample(250000, random_state=1)]).copy()
res={}
res['check_H1_full']=fit(f"default ~ clergy + {ctrl}", TS, 'clergy')                      # target OR 0.692, SE 0.041
res['check_H1_2007_2014']=fit(f"default ~ clergy + {ctrl}", TS[TS.year<=2014], 'clergy')  # target 0.607, n 85,132
res['n_2007_in_TS']=int((TS.year==2007).sum()); res['n_2014_t60_in_TS']=int(((TS.year==2014)&(TS.term60==1)).sum())
mat=TS[~((TS.year==2014)&(TS.term60==1))]
res['H1_matured_excl_2014_60m']=fit(f"default ~ clergy + {ctrl}", mat[mat.year<=2014], 'clergy')   # loans issued through 2014 excluding 2014 60-month
res['H1_full_excl_2014_60m']=fit(f"default ~ clergy + {ctrl}", mat, 'clergy')
# ---- H2 length-matched, Table 6 column (3) controls
D['relig']=D.relig_strict.astype(int)
ctrl2=ctrl+" + llen + moral + hardship + gratitude + family + help + business"
res['check_H2_col3']=fit(f"default ~ relig + {ctrl2}", D, 'relig')                         # target OR 1.281, SE 0.103
rng=np.random.default_rng(0); keep=[]
for (g,y),grp in D.groupby(['grade','yr']):
    r=grp[grp.relig_strict]; c=grp[~grp.relig_strict]
    if len(r)==0 or len(c)==0: continue
    keep+=list(r.index); cl=c.desc_len.values; ci=c.index.values
    for L in r.desc_len.values:
        d=np.abs(cl-L); sel=np.argsort(d)[:5]; keep+=list(ci[sel])
M=D.loc[list(dict.fromkeys(keep))].copy()
res['H2_matched_table6_controls']=fit(f"default ~ relig + {ctrl2}", M, 'relig')
res['H2_matched_sample']=dict(n=int(len(M)), n_treated=int(M.relig.sum()), n_controls=int((1-M.relig).sum()), mean_len_treated=float(M[M.relig==1].desc_len.mean()), mean_len_controls=float(M[M.relig==0].desc_len.mean()))
print(res['H2_matched_sample'])
json.dump(res, open("v16_logits.json","w"), indent=1); print("done")
