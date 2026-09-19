import pandas as pd, numpy as np, json, warnings; warnings.filterwarnings("ignore")
import statsmodels.api as sm
from scipy.optimize import minimize
T=pd.read_pickle("T.pkl")
TS=pd.concat([T[T.clergy], T[~T.clergy].sample(250000, random_state=1)]).copy()
# balance covariates: numeric 1st+2nd moments, categorical shares
num=['int','fico','linc','dti','lamt','term60']; cat=['grade','yr','st','home','ver','emp']
X=pd.get_dummies(TS[cat].astype(str),drop_first=True).astype(float)
for c in num: X[c]=TS[c].astype(float); X[c+'_sq']=TS[c].astype(float)**2
X=X.loc[:, X.std()>0]
tr0=TS.clergy.values.astype(bool)
keep=[c for c in X.columns if (X.loc[tr0,c].std()>0) and (X.loc[~tr0,c].std()>0)]
X=X[keep]
tr=TS.clergy.values.astype(bool); Xt=X[tr].values; Xc=X[~tr].values
mu=X[tr].mean().values; sd=X.std().values+1e-9
Zc=(Xc-mu)/sd  # target moments = 0 after standardizing to treated means
def dual(l):
    a=Zc@l; a=a-a.max(); w=np.exp(a); return np.log(w.sum())+a.max()
def grad(l):
    a=Zc@l; a=a-a.max(); w=np.exp(a); w/=w.sum(); return Zc.T@w
r=minimize(dual, np.zeros(Zc.shape[1]), jac=grad, method='L-BFGS-B', options={'maxiter':20000,'gtol':1e-10,'ftol':1e-14})
a=Zc@r.x; w=np.exp(a-a.max()); w/=w.sum()
# balance check
def smd(x_t,x_c,wc=None):
    mc=np.average(x_c,weights=wc) if wc is not None else x_c.mean(); return (x_t.mean()-mc)/np.sqrt((x_t.var()+x_c.var())/2+1e-12)
bal=pd.DataFrame({'var':X.columns,'smd_before':[smd(Xt[:,j],Xc[:,j]) for j in range(X.shape[1])],'smd_after':[smd(Xt[:,j],Xc[:,j],w) for j in range(X.shape[1])]})
print("converged",r.success,"max|SMD| before",bal.smd_before.abs().max().round(3),"after",bal.smd_after.abs().max().round(4),"ESS control",round(1/np.sum(w**2)))
# weighted logit: treated weight 1, control weight w*n_c (mean 1)
wts=np.ones(len(TS)); wts[~tr]=w*(~tr).sum()
Xd=sm.add_constant(pd.concat([pd.Series(tr.astype(float),name='clergy',index=TS.index), X],axis=1))
# importance resampling of controls by entropy weights, then ordinary logit with cluster SE
rng=np.random.default_rng(0); ci=np.where(~tr)[0]; draw=rng.choice(ci, size=len(ci), replace=True, p=w)
RS=pd.concat([TS[tr], TS.iloc[draw]]).copy()
import statsmodels.formula.api as smf
m=smf.logit("default ~ clergy + C(grade) + C(yr) + int + fico + linc + dti + term60 + lamt + C(emp) + C(home) + C(ver) + C(purp) + C(st)", data=RS).fit(method='newton',maxiter=100,disp=0,cov_type='cluster',cov_kwds={'groups':pd.factorize(RS['st'])[0]})
class _P: pass
i='clergy[T.True]'
res=dict(converged=bool(r.success), max_smd_before=float(bal.smd_before.abs().max()), max_smd_after=float(bal.smd_after.abs().max()), ess_control=float(1/np.sum(w**2)), n_treated=int(tr.sum()), OR=float(np.exp(m.params[i])), se=float(m.bse[i]), p=float(m.pvalues[i]), raw_default_treated=float(TS[tr].default.mean()), weighted_default_control=float(np.average(TS[~tr].default.values,weights=w)))
print(res)
json.dump(res,open("out/step5_ebal.json","w"),indent=1); bal.to_csv("out/표5c_균형표.csv",index=False)
