# v18 addition: bootstrap CI for the affiliation AUC change (Appendix Table C7, row 8), using the same
# 5-fold cross-validated logit as lc_two_signal_analysis.py (seed 0, 253,105-loan H1 sample, random_state=1 draw)
# and the same 300-draw paired bootstrap (seed 1) it used for the religious-language change.
# Also counts description-sample loans issued after 2014 (Table 1 note) and the step7b sample size.
import pandas as pd, numpy as np, json, warnings; warnings.filterwarnings("ignore")
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import roc_auc_score
T=pd.read_pickle("T.pkl"); D=pd.read_pickle("D.pkl")
num=['int','fico','linc','dti','term60','lamt']; cat=['grade','yr','emp','home','ver','purp','st']
def cv_auc(cols_num, cols_cat, data, seed=0):
    X=data[cols_num+cols_cat]; y=data.default.values
    pre=ColumnTransformer([('n',StandardScaler(),cols_num),('c',OneHotEncoder(handle_unknown='ignore'),cols_cat)])
    pipe=Pipeline([('p',pre),('m',LogisticRegression(max_iter=2000, C=1.0))])
    skf=StratifiedKFold(5,shuffle=True,random_state=seed); pr=np.zeros(len(y))
    for tr,te in skf.split(X,y):
        pipe.fit(X.iloc[tr],y[tr]); pr[te]=pipe.predict_proba(X.iloc[te])[:,1]
    return roc_auc_score(y,pr), pr
TS=pd.concat([T[T.clergy], T[~T.clergy].sample(250000, random_state=1)]).copy(); TS['clergy_i']=TS.clergy.astype(int)
a1,p1=cv_auc(num,cat,TS); a2,p2=cv_auc(num+['clergy_i'],cat,TS)
y=TS.default.values; rng=np.random.default_rng(1); diffs=[]
for b in range(300):
    idx=rng.integers(0,len(y),len(y)); diffs.append(roc_auc_score(y[idx],p2[idx])-roc_auc_score(y[idx],p1[idx]))
res=dict(n=int(len(TS)), AUC_without=float(a1), AUC_with=float(a2), dAUC=float(a2-a1),
         dAUC_boot_mean=float(np.mean(diffs)), dAUC_boot_ci=[float(np.percentile(diffs,2.5)),float(np.percentile(diffs,97.5))],
         D_n=int(len(D)), D_issued_after_2014=int((D.year>=2015).sum()), D_issued_2007=int((D.year==2007).sum()),
         D_by_year=D.year.value_counts().sort_index().astype(int).to_dict())
print(res); json.dump(res,open("v18_auc.json","w"),indent=1)
