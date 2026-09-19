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
res={}
def lpm(formula,data): return smf.ols(formula,data=data).fit(cov_type='HC1')
# ---- Oster delta & RV (LPM) ----
def oster_rv(data, treat, ctrl_formula):
    m0=lpm(f"default ~ {treat}", data); m1=lpm(f"default ~ {treat} + {ctrl_formula}", data)
    k=[i for i in m1.params.index if i.startswith(treat)][0]
    b0=m0.params[[i for i in m0.params.index if i.startswith(treat)][0]]; b1=m1.params[k]; R0=m0.rsquared; R1=m1.rsquared; Rmax=min(1.0,1.3*R1)
    delta=(b1*(R1-R0))/((b0-b1)*(Rmax-R1)) if (b0-b1)!=0 else np.nan   # Oster (2019) approximation for beta=0
    # beta* under delta=1 (Oster simplified): b1 - (b0-b1)*(Rmax-R1)/(R1-R0)
    bstar=b1-(b0-b1)*(Rmax-R1)/(R1-R0)
    t=m1.tvalues[k]; dof=m1.df_resid; f2=t**2/dof
    RV=0.5*(np.sqrt(f2**2+4*f2)-f2)   # Cinelli & Hazlett (2020) robustness value, q=1
    RV_alpha=None
    # RV at alpha=0.05: f_q,alpha = f - t_crit/sqrt(dof)
    fa=abs(t)/np.sqrt(dof)-1.96/np.sqrt(dof); fa=max(fa,0); RV_alpha=0.5*(np.sqrt(fa**4+4*fa**2)-fa**2)
    # partial R2 of benchmark covariates (emp_length, verification) for comparison
    return dict(beta_uncontrolled=float(b0), beta_controlled=float(b1), R2_unc=float(R0), R2_ctrl=float(R1), Rmax=float(Rmax), oster_delta=float(delta), beta_star_delta1=float(bstar), t=float(t), RV_q1=float(RV), RV_q1_alpha05=float(RV_alpha))
res['Oster_RV_H1']=oster_rv(TS,'clergy',ctrl); print("H1 Oster/RV",res['Oster_RV_H1'])
res['Oster_RV_H2']=oster_rv(D,'relig_strict',ctrl+" + llen + moral + hardship + gratitude + family + help + business"); print("H2 Oster/RV",res['Oster_RV_H2'])
# benchmark partial R2 of emp_length and verification in H1 LPM
mfull=lpm(f"default ~ clergy + {ctrl}", TS); 
mno_emp=lpm(f"default ~ clergy + "+ctrl.replace(" + C(emp)",""), TS); mno_ver=lpm(f"default ~ clergy + "+ctrl.replace(" + C(ver)",""), TS)
res['benchmark_partialR2']={'emp_length':float((mfull.rsquared-mno_emp.rsquared)/(1-mno_emp.rsquared)),'verification':float((mfull.rsquared-mno_ver.rsquared)/(1-mno_ver.rsquared))}
print("benchmark partial R2:",res['benchmark_partialR2'])
# ---- occupation placebo (logit) ----
et=pd.read_pickle("lc_final.pkl")['emp_title'].fillna('').str.lower().str.strip().loc[TS.index]
TS['teacher_p']=et.str.contains(r"\bteacher\b",regex=True).astype(int); TS['nurse_p']=et.str.contains(r"\bnurse\b|\brn\b",regex=True).astype(int); TS['police_p']=et.str.contains(r"\bpolice\b|\bofficer\b",regex=True).astype(int)
mp=robust_fit(smf.logit(f"default ~ clergy + teacher_p + nurse_p + police_p + {ctrl}", data=TS), pd.factorize(TS['st'])[0])
res['occ_placebo']={k:dict(OR=float(np.exp(mp.params[key])),p=float(mp.pvalues[key]),n=int(TS[k.replace('clergy','clergy')].sum()) if k!='clergy' else int(TS.clergy.sum())) for k,key in [('clergy','clergy[T.True]'),('teacher_p','teacher_p'),('nurse_p','nurse_p'),('police_p','police_p')]}
print("occ placebo:",res['occ_placebo'])
# ---- 7-C stable occupation control ----
occs=['teacher','police','fire','military','govt','nurse','postal','transit']
ms=robust_fit(smf.logit(f"default ~ clergy + {' + '.join(occs)} + {ctrl}", data=TS), pd.factorize(TS['st'])[0])
res['T5b_stable_ctrl']=dict(clergy_OR=float(np.exp(ms.params['clergy[T.True]'])),clergy_p=float(ms.pvalues['clergy[T.True]']),**{o:dict(OR=float(np.exp(ms.params[o])),p=float(ms.pvalues[o]),n=int(TS[o].sum())) for o in occs})
print("stable ctrl:",res['T5b_stable_ctrl'])
# within stable-occupation subsample: clergy vs other stable
SS=pd.concat([T[T.clergy], T[(T.stable_any==1)&(~T.clergy)]]).copy()
mss=robust_fit(smf.logit(f"default ~ clergy + {ctrl}", data=SS), pd.factorize(SS['st'])[0])
res['T5b_within_stable']=dict(n=int(mss.nobs),n_clergy=int(SS.clergy.sum()),OR=float(np.exp(mss.params['clergy[T.True]'])),p=float(mss.pvalues['clergy[T.True]']),raw_default_clergy=float(SS[SS.clergy].default.mean()),raw_default_stable=float(SS[~SS.clergy].default.mean()))
print("within stable:",res['T5b_within_stable'])
# ---- fake dictionary permutation (FWL residualization, LPM) ----
t0=time.time()
X=pd.get_dummies(D[['grade','yr','emp','home','ver','purp','st']].astype(str),drop_first=True).astype(float)
X=pd.concat([X, D[['int','fico','linc','dti','term60','lamt','llen','moral','hardship','gratitude','family','help','business']].astype(float)],axis=1); X=sm.add_constant(X)
Xv=X.values.astype(float); Xv=Xv[:, np.linalg.matrix_rank(Xv)>0 or True]
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
