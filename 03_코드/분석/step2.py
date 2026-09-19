import pandas as pd, numpy as np, json, warnings, time; warnings.filterwarnings("ignore")
import statsmodels.formula.api as smf

def robust_fit(model, groups=None, maxiter=100):
    kw=dict(cov_type='cluster',cov_kwds={'groups':groups}) if groups is not None else {}
    m=model.fit(method='newton',maxiter=maxiter,disp=0,**kw)
    if not m.mle_retvals.get('converged',False):
        m2=model.fit(method='bfgs',start_params=m.params,maxiter=2000,disp=0,**kw)
        m2.mle_retvals['refit']='bfgs'; m2.mle_retvals['grad_norm']=float(np.abs(m2.model.score(m2.params)).max())
        return m2
    return m
import statsmodels.api as sm
from statsmodels.stats.multitest import multipletests
T=pd.read_pickle("T.pkl"); D=pd.read_pickle("D.pkl")
ctrl="C(grade) + C(yr) + int + fico + linc + dti + term60 + lamt + C(emp) + C(home) + C(ver) + C(purp) + C(st)"
TS=pd.concat([T[T.clergy], T[~T.clergy].sample(250000, random_state=1)]).copy()
def fit(formula, data, var):
    t=time.time()
    m=robust_fit(smf.logit(formula, data=data), pd.factorize(data['st'])[0])
    conv=m.mle_retvals.get('converged', None)
    key=[i for i in m.params.index if i.startswith(var)][0]
    X=m.model.exog.copy(); j=list(m.model.exog_names).index(key)
    X[:,j]=1; p1=m.model.cdf(X@m.params.values); X[:,j]=0; p0=m.model.cdf(X@m.params.values); ame=float(np.mean(p1-p0)); del X
    r=dict(n=int(m.nobs), coef=float(m.params[key]), se=float(m.bse[key]), z=float(m.tvalues[key]), p=float(m.pvalues[key]), OR=float(np.exp(m.params[key])), AME=float(ame), converged=bool(conv), llf=float(m.llf), sec=round(time.time()-t))
    import gc; gc.collect(); print(var, formula[:40], {k:(round(v,4) if isinstance(v,float) else v) for k,v in r.items()}); return r, m
res={}
res['T2_H1_full'],m1=fit(f"default ~ clergy + {ctrl}", TS, 'clergy')
res['T2_H1_2008_2014'],_=fit(f"default ~ clergy + {ctrl}", TS[TS.year<=2014], 'clergy')
res['T2_H1_2015_2018'],_=fit(f"default ~ clergy + {ctrl}", TS[TS.year>=2015], 'clergy')
res['T3_H2_col1_struct'],_=fit(f"default ~ relig_strict + {ctrl}", D, 'relig_strict')
res['T3_H2_col2_len'],_=fit(f"default ~ relig_strict + {ctrl} + llen", D, 'relig_strict')
res['T3_H2_col3_len_dict'],m2c=fit(f"default ~ relig_strict + {ctrl} + llen + moral + hardship + gratitude + family + help + business", D, 'relig_strict')
D['ldec']=pd.qcut(D.desc_len.rank(method='first'),10,labels=False)
res['T3_H2_col4_lendec_dict'],_=fit(f"default ~ relig_strict + {ctrl} + C(ldec) + moral + hardship + gratitude + family + help + business", D, 'relig_strict')
res['T3_dict_coefs']={k:dict(OR=float(np.exp(m2c.params[k])),p=float(m2c.pvalues[k])) for k in ['moral','hardship','gratitude','family','help','business','llen']}
res['T4_both'],_=fit(f"default ~ relig_strict + clergy + {ctrl} + llen + moral + hardship + gratitude + family + help + business", D, 'relig_strict')
m4=robust_fit(smf.logit(f"default ~ relig_strict + clergy + {ctrl} + llen + moral + hardship + gratitude + family + help + business", data=D), pd.factorize(D['st'])[0])
res['T4_both_clergy']=dict(n_clergy=int(D.clergy.sum()), OR=float(np.exp(m4.params['clergy[T.True]'])), p=float(m4.pvalues['clergy[T.True]']))
# Holm on the two confirmatory one-sided tests
p1=res['T2_H1_full']['p']/2 if res['T2_H1_full']['coef']<0 else 1-res['T2_H1_full']['p']/2
p2=res['T3_H2_col3_len_dict']['p']/2 if res['T3_H2_col3_len_dict']['coef']>0 else 1-res['T3_H2_col3_len_dict']['p']/2
rej,padj,_,_=multipletests([p1,p2],method='holm'); res['Holm']=dict(H1_onesided_p=p1,H2_onesided_p=p2,H1_holm=float(padj[0]),H2_holm=float(padj[1]))
print("Holm:",res['Holm'])
json.dump(res,open("out/step2_results.json","w"),indent=1)
rows=[]
for k,v in res.items():
    if isinstance(v,dict) and 'OR' in v and 'n' in v: rows.append(dict(model=k,**v))
pd.DataFrame(rows).to_csv("out/표2-4_기준모형.csv",index=False); print("saved")
