import pandas as pd, numpy as np, json, warnings; warnings.filterwarnings("ignore")
import statsmodels.formula.api as smf
T=pd.read_pickle("T.pkl"); TS=pd.concat([T[T.clergy], T[~T.clergy].sample(250000, random_state=1)]).copy()
tr=TS.clergy.values.astype(bool)
num=['int','fico','linc','dti','lamt']; cat=['grade','yr','home','ver','emp','st']
X=pd.get_dummies(TS[cat].astype(str),drop_first=True).astype(float)
for c in num: X[c]=TS[c].astype(float); X[c+'_sq']=TS[c].astype(float)**2
X['term60']=TS.term60.astype(float)
keep=[c for c in X.columns if X.loc[tr,c].std()>0 and X.loc[~tr,c].std()>0 and X.loc[tr,c].mean()>0.002 and X.loc[tr,c].mean()<0.998] if True else None
X=X[keep]
# drop collinear via QR pivoting
Xc=X[~tr].values; Xt=X[tr].values
q,r,piv=__import__('scipy').linalg.qr(Xc-Xc.mean(0), mode='economic', pivoting=True); rank=(np.abs(np.diag(r))>1e-8*abs(r[0,0])).sum(); cols=np.sort(piv[:rank]); X=X.iloc[:,cols]; Xc=X[~tr].values; Xt=X[tr].values
target=Xt.mean(0); sd=Xc.std(0); Zc=(Xc-target)/sd
# Newton on dual: minimize log sum exp(Zc @ l)
l=np.zeros(Zc.shape[1])
for it in range(200):
    a=Zc@l; a-=a.max(); w=np.exp(a); w/=w.sum()
    g=Zc.T@w; H=(Zc*w[:,None]).T@Zc - np.outer(g,g)
    step=np.linalg.solve(H+1e-8*np.eye(len(l)), g)
    # backtracking
    f0=np.log(np.exp(Zc@l - (Zc@l).max()).sum())+(Zc@l).max(); t=1.0
    while True:
        ln=l-t*step; fn=np.log(np.exp(Zc@ln-(Zc@ln).max()).sum())+(Zc@ln).max()
        if fn<=f0-1e-4*t*g@step or t<1e-6: break
        t*=0.5
    l=ln
    if np.abs(g).max()<1e-7: break
a=Zc@l; w=np.exp(a-a.max()); w/=w.sum()
def smd(j,wc=None):
    mc=np.average(Xc[:,j],weights=wc) if wc is not None else Xc[:,j].mean(); return (Xt[:,j].mean()-mc)/np.sqrt((Xt[:,j].var()+Xc[:,j].var())/2+1e-12)
bal=pd.DataFrame({'var':X.columns,'smd_before':[smd(j) for j in range(X.shape[1])],'smd_after':[smd(j,w) for j in range(X.shape[1])]})
print("iters",it,"max|g|",np.abs(g).max(),"max|SMD| before",bal.smd_before.abs().max().round(3),"after",bal.smd_after.abs().max().round(4),"ESS",round(1/np.sum(w**2)))
rng=np.random.default_rng(0); ci=np.where(~tr)[0]; draw=rng.choice(ci,size=len(ci),replace=True,p=w); RS=pd.concat([TS[tr],TS.iloc[draw]])
m=smf.logit("default ~ clergy + C(grade) + C(yr) + int + fico + linc + dti + term60 + lamt + C(emp) + C(home) + C(ver) + C(purp) + C(st)", data=RS).fit(method='newton',maxiter=100,disp=0,cov_type='cluster',cov_kwds={'groups':pd.factorize(RS['st'])[0]})
i='clergy[T.True]'
res=dict(n_covariates=int(X.shape[1]), max_smd_before=float(bal.smd_before.abs().max()), max_smd_after=float(bal.smd_after.abs().max()), ess_control=float(1/np.sum(w**2)), n_treated=int(tr.sum()), OR=float(np.exp(m.params[i])), se=float(m.bse[i]), p=float(m.pvalues[i]), raw_default_treated=float(TS[tr].default.mean()), weighted_default_control=float(np.average(TS[~tr].default.values,weights=w)), unweighted_default_control=float(TS[~tr].default.mean()))
print(res); json.dump(res,open("out/step5_ebal.json","w"),indent=1); bal.to_csv("out/표5c_균형표.csv",index=False)
