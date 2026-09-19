import pandas as pd, numpy as np, json, warnings, re, time; warnings.filterwarnings("ignore")
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
from sklearn.feature_extraction.text import CountVectorizer
T=pd.read_pickle("T.pkl"); D=pd.read_pickle("D.pkl")
ctrl="C(grade) + C(yr) + int + fico + linc + dti + term60 + lamt + C(emp) + C(home) + C(ver) + C(purp) + C(st)"
TS=pd.concat([T[T.clergy], T[~T.clergy].sample(250000, random_state=1)]).copy()
res=json.load(open('out/step3_results.json')) if __import__('os').path.exists('out/step3_results.json') else {}
# ---- fake dictionary permutation (FWL residualization, LPM) ----
t0=time.time()
X=pd.get_dummies(D[['grade','yr','emp','home','ver','purp','st']].astype(str),drop_first=True).astype(float)
X=pd.concat([X, D[['int','fico','linc','dti','term60','lamt','llen','moral','hardship','gratitude','family','help','business']].astype(float)],axis=1); X=sm.add_constant(X)
Xv=X.values.astype(float)
Q,_=np.linalg.qr(Xv, mode='reduced'); yv=D.default.values.astype(float); ry=yv-Q@(Q.T@yv)
def coef(x):
    x=x.astype(float); rx=x-Q@(Q.T@x); return float((rx@ry)/(rx@rx)), rx
actual,_=coef(D.relig_strict.values.astype(float)); print("actual LPM coef (residualized):",actual)
cv=CountVectorizer(min_df=20, binary=True, token_pattern=r"(?u)\b[a-z]{3,}\b"); M=cv.fit_transform(D['txt']); vocab=np.array(cv.get_feature_names_out()); dfreq=np.asarray(M.sum(axis=0)).ravel()
# exclude religious vocabulary from candidate pool
relig_words=set("god gods jesus christ christian christians church churches pray prays prayed praying prayer prayers bless blessed blessing blessings faith faithful lord bible biblical scripture tithe tithes tithing ministry ministries missionary missionaries pastor congregation clergy rabbi amen religion religious catholic baptist methodist lutheran presbyterian mormon evangelical pentecostal muslim islam mosque allah jewish synagogue buddhist hindu".split())
pool=np.array([i for i,w in enumerate(vocab) if w not in relig_words and dfreq[i]<=2000])
target=int(D.relig_strict.sum()); rng=np.random.default_rng(42); dist=[]; sizes=[]
Mc=M.tocsc()
for it in range(1000):
    chosen=[]; cover=np.zeros(M.shape[0],dtype=bool)
    order=rng.permutation(pool)
    for i in order:
        chosen.append(i); cover|=Mc[:,i].toarray().ravel().astype(bool)
        if cover.sum()>=target: break
    c,_=coef(cover.astype(float)); dist.append(c); sizes.append(cover.sum())
dist=np.array(dist); perm_p=float((dist>=actual).mean())
res['fake_dict']=dict(actual_coef=actual, perm_mean=float(dist.mean()), perm_sd=float(dist.std()), perm_p_onesided=perm_p, perm_p_twosided=float((np.abs(dist)>=abs(actual)).mean()), mean_docs=float(np.mean(sizes)), n_iter=1000, sec=round(time.time()-t0))
print("fake dict:",res['fake_dict'])
np.save("out/fake_dict_dist.npy",dist)
json.dump(res,open("out/step3_results.json","w"),indent=1)
