import pandas as pd, numpy as np, json, warnings, gc; warnings.filterwarnings("ignore")
import statsmodels.formula.api as smf
exec(open("stepR2a.py").read().split("res={}")[0])   # reuse setup (T, maps, fitm, rep, ctrl)
res=json.load(open('out/stepR2a.json'))
TS=pd.concat([T[T.clergy], T[~T.clergy].sample(250000, random_state=1)]).copy()
# Wild cluster bootstrap (WCR, Webb weights, 9,999 reps) on LPM analogues, clustered by state
from wildboottest.wildboottest import wildboottest
import statsmodels.api as sm
def wcb(formula,data,var):
    y,X=__import__('patsy').dmatrices(formula,data,return_type='dataframe')
    mod=sm.OLS(y,X); G=pd.factorize(data.loc[y.index,'st'])[0]
    r=wildboottest(mod,param=var,cluster=G,B=9999,weights_type='webb',impose_null=True,bootstrap_type='11',seed=12345,show=False)
    ols=mod.fit(cov_type='cluster',cov_kwds={'groups':G})
    out=dict(coef=float(ols.params[var]),cr1_p=float(ols.pvalues[var]),wcb_p=float(r['p-value'].iloc[0]),n=int(ols.nobs),clusters=int(len(set(G))))
    print(var,out,flush=True); return out
res['WCB']={}
res['WCB']['H1']=wcb(f"default ~ clergy + {ctrl}",TS,'clergy[T.True]'); json.dump(res,open("out/stepR2a.json","w"),indent=1)
D=pd.read_pickle("D.pkl")
res['WCB']['H2']=wcb(f"default ~ relig_strict + {ctrl} + llen + moral + hardship + gratitude + family + help + business",D,'relig_strict[T.True]')
json.dump(res,open("out/stepR2a.json","w"),indent=1); print("WCB done",flush=True)
