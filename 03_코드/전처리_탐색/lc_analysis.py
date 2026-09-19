import pandas as pd, numpy as np, re, warnings, json
warnings.filterwarnings("ignore")
import statsmodels.formula.api as smf, statsmodels.api as sm
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
df=pd.read_pickle("lc_final.pkl")
et=df['emp_title'].fillna('').str.lower().str.strip()
role=et.str.contains(r"\bpastor\b|\bminister\b|\bministry\b|\bclergy\b|\bpriest\b|\bchaplain\b|\brabbi\b|\bmissionar|\breverend\b|\bevangelist\b|\bdeacon\b|\bworship\b|\bimam\b|\bseminar(y|ian)\b", regex=True)
org=et.str.contains(r"\bchurch\b|\bparish\b|\bdiocese\b|\bcongregation\b|\bsynagogue\b|\bmosque\b", regex=True)
inst=et.str.contains(r"hospital|health|medical|charit|university|college|school|academy|insurance|bank|credit union|hospice|clinic|services inc|mutual", regex=True)
df['clergy']=role | (org & ~inst)
T=df[df.loan_status.isin(['Fully Paid','Charged Off','Default'])].copy()
T['default']=T.loan_status.isin(['Charged Off','Default']).astype(int)
T['yr']=T.year.astype('Int64').astype(str); T['int']=T.int_rate.astype(str).str.rstrip('%').astype(float)
T['fico']=(T.fico_range_low+T.fico_range_high)/2; T['linc']=np.log1p(T.annual_inc.fillna(0)); T['term60']=T.term.astype(str).str.contains('60').astype(int)
T['lamt']=np.log(T.loan_amnt); T['emp']=T.emp_length.fillna('na').astype(str); T['home']=T.home_ownership.fillna('na'); T['ver']=T.verification_status.fillna('na'); T['purp']=T.purpose.fillna('na'); T['st']=T.addr_state.fillna('na')
T=T.dropna(subset=['dti','fico','int'])
out={}
print("Terminal loans:",len(T),"clergy:",T.clergy.sum(),"default rate clergy/other:",T[T.clergy].default.mean().round(4),T[~T.clergy].default.mean().round(4))
# ---------- H1: clergy ----------
ctrl="C(grade) + C(yr) + int + fico + linc + dti + term60 + lamt + C(emp) + C(home) + C(ver) + C(purp) + C(st)"
TS=pd.concat([T[T.clergy], T[~T.clergy].sample(250000, random_state=1)])
print("H1 sample (all clergy + 250k random controls):",len(TS))
m1=smf.logit(f"default ~ clergy + {ctrl}", data=TS).fit(disp=0, maxiter=200)
out['H1_full']=dict(n=int(m1.nobs), coef=m1.params['clergy[T.True]'], se=m1.bse['clergy[T.True]'], p=m1.pvalues['clergy[T.True]'], OR=np.exp(m1.params['clergy[T.True]']))
print("H1 clergy (full controls):", out['H1_full'])
# by period
for lab,cond in [('2008-2014',T.year<=2014),('2015-2018',T.year>=2015)]:
    mm=smf.logit(f"default ~ clergy + {ctrl}", data=TS[cond.loc[TS.index]]).fit(disp=0, maxiter=200)
    out[f'H1_{lab}']=dict(n=int(mm.nobs), n_clergy=int(TS[cond.loc[TS.index]].clergy.sum()), OR=np.exp(mm.params['clergy[T.True]']), p=mm.pvalues['clergy[T.True]']); print(lab, out[f'H1_{lab}'])
# placebo: other stable public-service occupations (teacher, nurse, police) vs clergy
for lab,pat in [('teacher',r"\bteacher\b"),('nurse',r"\bnurse\b|\brn\b"),('police',r"\bpolice\b|\bofficer\b")]:
    TS[lab]=et.loc[TS.index].str.contains(pat,regex=True)
mp=smf.logit(f"default ~ clergy + teacher + nurse + police + {ctrl}", data=TS).fit(disp=0, maxiter=200)
out['H1_vs_occ']={k:dict(OR=np.exp(mp.params[f'{k}[T.True]']),p=mp.pvalues[f'{k}[T.True]'], n=int(TS[k].sum())) for k in ['clergy','teacher','nurse','police']}; print("occupation placebo:", out['H1_vs_occ'])
# ---------- H2: narrative ----------
D=T[T.has_desc].copy()
txt=(D['title'].fillna('')+' '+D['desc_c']).str.lower()
D['llen']=np.log1p(D.desc_len); D['ldec']=pd.qcut(D.desc_len.rank(method='first'),10,labels=False)
dic={'moral':r"\bhonest(y|ly)?\b|\bpromise\b|\bintegrity\b|\bresponsib(le|ility)\b|\btrustworthy\b|\bcommit(ted|ment)\b|\bmy word\b|\bhonou?r\b|\bguarantee\b|\bnever (been )?late\b|\bnever missed\b|\breliable\b|\bhard[- ]?working\b",
     'hardship':r"\bstruggl|\bhard time|\blost my job\b|\blaid off\b|\bunemploy|\bmedical\b|\bdivorce|\bsick\b|\bhospital\b|\bemergency\b|\bbehind on\b|\bcan'?t afford\b|\bdesperate|\bdifficult\b|\bsurgery\b|\billness\b|\bdisab",
     'gratitude':r"\bthank(s| you)?\b|\bappreciat|\bgrateful\b",
     'family':r"\bfamily\b|\bwife\b|\bhusband\b|\bkids?\b|\bchildren\b|\bdaughter\b|\bson\b|\bmother\b|\bfather\b|\bmom\b|\bdad\b",
     'help':r"\bplease help\b|\bhelp me\b|\bneed help\b|\bhelp us\b",
     'business':r"\bbusiness\b|\bcompany\b|\bstart[- ]?up\b|\bcustomers?\b"}
for k,p in dic.items(): D[k]=txt.str.contains(p,regex=True).astype(int)
print("desc sample:",len(D),"relig:",D.relig_strict.sum()); print(D.groupby('relig_strict')[list(dic)].mean().round(3))
ctrl2=ctrl+" + llen"
m2a=smf.logit(f"default ~ relig_strict + {ctrl}", data=D).fit(disp=0, maxiter=200)
m2b=smf.logit(f"default ~ relig_strict + {ctrl2}", data=D).fit(disp=0, maxiter=200)
m2c=smf.logit(f"default ~ relig_strict + {ctrl2} + moral + hardship + gratitude + family + help + business", data=D).fit(disp=0, maxiter=200)
m2d=smf.logit(f"default ~ relig_strict + {ctrl} + C(ldec) + moral + hardship + gratitude + family + help + business", data=D).fit(disp=0, maxiter=200)
for lab,m in [('no text ctrl',m2a),('+loglen',m2b),('+loglen+dict',m2c),('+len deciles+dict',m2d)]:
    out[f'H2_{lab}']=dict(n=int(m.nobs), OR=np.exp(m.params['relig_strict[T.True]']), se=m.bse['relig_strict[T.True]'], p=m.pvalues['relig_strict[T.True]']); print("H2",lab,out[f'H2_{lab}'])
out['H2_dict_coefs']={k:dict(OR=np.exp(m2c.params[k]),p=m2c.pvalues[k]) for k in dic}; print({k:(round(v['OR'],3),round(v['p'],4)) for k,v in out['H2_dict_coefs'].items()})
# matched sample: for each relig loan, 5 nearest by desc_len within grade x yr
rng=np.random.default_rng(0); keep=[]
for (g,y),grp in D.groupby(['grade','yr']):
    r=grp[grp.relig_strict]; c=grp[~grp.relig_strict]
    if len(r)==0 or len(c)==0: continue
    keep+=list(r.index)
    cl=c.desc_len.values; ci=c.index.values
    for L in r.desc_len.values:
        d=np.abs(cl-L); sel=np.argsort(d)[:5]; keep+=list(ci[sel])
M=D.loc[list(dict.fromkeys(keep))]
mm=smf.logit("default ~ relig_strict + C(grade) + C(yr) + int + fico + linc + dti + term60 + lamt + llen + moral + hardship + gratitude + family + help", data=M).fit(disp=0, maxiter=200)
out['H2_matched']=dict(n=int(mm.nobs), n_relig=int(M.relig_strict.sum()), OR=np.exp(mm.params['relig_strict[T.True]']), p=mm.pvalues['relig_strict[T.True]'], len_relig=float(M[M.relig_strict].desc_len.mean()), len_ctrl=float(M[~M.relig_strict].desc_len.mean())); print("H2 matched:",out['H2_matched'])
# clergy x narrative in 2008-2014 desc sample
mx=smf.logit(f"default ~ relig_strict + clergy + {ctrl2} + moral + hardship + gratitude + family + help + business", data=D).fit(disp=0, maxiter=200)
out['both_signals_desc_sample']=dict(n=int(mx.nobs), n_clergy=int(D.clergy.sum()), OR_relig=np.exp(mx.params['relig_strict[T.True]']), p_relig=mx.pvalues['relig_strict[T.True]'], OR_clergy=np.exp(mx.params['clergy[T.True]']), p_clergy=mx.pvalues['clergy[T.True]']); print("both signals:",out['both_signals_desc_sample'])
# ---------- ΔAUC (5-fold CV, logistic) ----------
num=['int','fico','linc','dti','term60','lamt']; cat=['grade','yr','emp','home','ver','purp','st']
def cv_auc(cols_num, cols_cat, data, seed=0):
    X=data[cols_num+cols_cat]; y=data.default.values
    pre=ColumnTransformer([('n',StandardScaler(),cols_num),('c',OneHotEncoder(handle_unknown='ignore'),cols_cat)])
    pipe=Pipeline([('p',pre),('m',LogisticRegression(max_iter=2000, C=1.0))])
    skf=StratifiedKFold(5,shuffle=True,random_state=seed); pr=np.zeros(len(y))
    for tr,te in skf.split(X,y):
        pipe.fit(X.iloc[tr],y[tr]); pr[te]=pipe.predict_proba(X.iloc[te])[:,1]
    return roc_auc_score(y,pr), pr
D['relig']=D.relig_strict.astype(int); D['clergy_i']=D.clergy.astype(int)
a1,p1=cv_auc(num,cat,D); a2,p2=cv_auc(num+['llen'],cat,D); a3,p3=cv_auc(num+['llen']+list(dic),cat,D); a4,p4=cv_auc(num+['llen']+list(dic)+['relig'],cat,D); a5,p5=cv_auc(num+['llen']+list(dic)+['relig','clergy_i'],cat,D)
out['AUC']=dict(M1_struct=a1,M2_len=a2,M3_dict=a3,M4_relig=a4,M5_relig_clergy=a5); print("AUC:",{k:round(v,4) for k,v in out['AUC'].items()})
# DeLong-free bootstrap for ΔAUC M4-M3
y=D.default.values; rng=np.random.default_rng(1); diffs=[]
for b in range(300):
    idx=rng.integers(0,len(y),len(y)); diffs.append(roc_auc_score(y[idx],p4[idx])-roc_auc_score(y[idx],p3[idx]))
out['dAUC_M4_M3']=dict(mean=float(np.mean(diffs)), ci=[float(np.percentile(diffs,2.5)),float(np.percentile(diffs,97.5))]); print("ΔAUC M4-M3:",out['dAUC_M4_M3'])
# full-sample AUC with clergy
T['clergy_i']=T.clergy.astype(int)
S=TS.copy(); S['clergy_i']=S.clergy.astype(int)
b1,_=cv_auc(num,cat,S); b2,_=cv_auc(num+['clergy_i'],cat,S); out['AUC_clergy_fullsample']=dict(M1=b1,M1_clergy=b2,n=len(S)); print("clergy AUC:",out['AUC_clergy_fullsample'])
json.dump(out,open("lc_results.json","w"),indent=1,default=float)
D.to_pickle("lc_desc_sample.pkl")
