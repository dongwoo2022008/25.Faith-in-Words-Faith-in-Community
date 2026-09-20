import pandas as pd, numpy as np, json, gc, warnings; warnings.filterwarnings("ignore")
import statsmodels.api as sm, patsy
T=pd.read_pickle("T.pkl")
cols=['default','clergy','grade','yr','int','fico','linc','dti','term60','lamt','emp','home','ver','purp','st']
T=T[cols].copy(); gc.collect()
y,X=patsy.dmatrices("default ~ clergy + C(grade) + C(yr) + int + fico + linc + dti + term60 + lamt + C(emp) + C(home) + C(ver) + C(purp) + C(st)",T,return_type='dataframe')
G=pd.factorize(T.loc[y.index,'st'])[0]; del T; gc.collect()
X=X.astype(np.float32).astype(np.float64); print(X.shape,flush=True)
m=sm.Logit(y,X).fit(method='newton',maxiter=50,disp=0,cov_type='cluster',cov_kwds={'groups':G})
k='clergy[T.True]'; b=m.params[k]; se=m.bse[k]
r=dict(OR=float(np.exp(b)),coef=float(b),se=float(se),p2=float(m.pvalues[k]),n=int(m.nobs),lo=float(np.exp(b-1.96*se)),hi=float(np.exp(b+1.96*se)),converged=bool(m.mle_retvals.get('converged')))
print(r,flush=True)
res=json.load(open("out/stepR2a.json")); res['H1_full']=r; json.dump(res,open("out/stepR2a.json","w"),indent=1)
