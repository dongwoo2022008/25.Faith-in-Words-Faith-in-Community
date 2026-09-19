import pandas as pd, numpy as np, json, warnings, time; warnings.filterwarnings("ignore")
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from catboost import CatBoostClassifier, CatBoostRegressor
import doubleml as dml
T=pd.read_pickle("T.pkl"); D=pd.read_pickle("D.pkl")
TS=pd.concat([T[T.clergy], T[~T.clergy].sample(250000, random_state=1)]).copy()
res={}
def prep(df, extra=None):
    X=pd.get_dummies(df[['grade','yr','emp','home','ver','purp','st']].astype(str),drop_first=True).astype(float)
    X=pd.concat([X, df[['int','fico','linc','dti','term60','lamt']].astype(float)],axis=1)
    X=X.reset_index(drop=True)
    if extra is not None: X=pd.concat([X,extra.reset_index(drop=True)],axis=1)
    X.columns=[f"x{i}" for i in range(X.shape[1])]; return X
def run_dml(df, X, treat, label, n_folds=5, seed=0):
    t=time.time()
    data=pd.concat([df[['default']].astype(int).reset_index(drop=True), pd.Series(df[treat].astype(int).values,name='d'), X.reset_index(drop=True)],axis=1)
    obj=dml.DoubleMLData(data,'default','d',list(X.columns))
    ml_l=CatBoostRegressor(iterations=400,depth=6,learning_rate=0.08,verbose=0,thread_count=2,random_seed=seed)
    ml_m=CatBoostClassifier(iterations=400,depth=6,learning_rate=0.08,verbose=0,thread_count=2,random_seed=seed)
    plr=dml.DoubleMLPLR(obj, ml_l, ml_m, n_folds=n_folds, score='partialling out'); plr.fit(); s=plr.summary
    r=dict(n=len(data), n_treated=int(data.d.sum()), PLR_theta=float(s['coef'].iloc[0]), SE=float(s['std err'].iloc[0]), p=float(s['P>|t|'].iloc[0]), CI_low=float(s['2.5 %'].iloc[0]), CI_high=float(s['97.5 %'].iloc[0]), sec=round(time.time()-t))
    # ATTE via IRM with low trimming, as a check (rare treatment -> ATE weights unstable)
    ml_g=CatBoostClassifier(iterations=400,depth=6,learning_rate=0.08,verbose=0,thread_count=2,random_seed=seed)
    ml_m2=CatBoostClassifier(iterations=400,depth=6,learning_rate=0.08,verbose=0,thread_count=2,random_seed=seed)
    irm=dml.DoubleMLIRM(obj, ml_g, ml_m2, n_folds=n_folds, score='ATTE', trimming_threshold=0.001); irm.fit(); s2=irm.summary
    r.update(ATTE=float(s2['coef'].iloc[0]), ATTE_SE=float(s2['std err'].iloc[0]), ATTE_p=float(s2['P>|t|'].iloc[0]))
    print(label, r); return r
# H1
res['DML_H1_clergy']=run_dml(TS, prep(TS), 'clergy', 'DML H1')
# H2 without text
dicts=D[['llen','moral','hardship','gratitude','family','help','business']].astype(float)
res['DML_H2_dict']=run_dml(D, prep(D, dicts), 'relig_strict', 'DML H2 (+dict)')
# H2 with TF-IDF SVD text representation (embedding model download blocked -> fallback, recorded)
tf=TfidfVectorizer(min_df=10, max_features=20000, ngram_range=(1,2), sublinear_tf=True, token_pattern=r"(?u)\b[a-z]{2,}\b")
M=tf.fit_transform(D['txt']); svd=TruncatedSVD(100, random_state=0); Z=pd.DataFrame(svd.fit_transform(M), columns=[f"svd{i}" for i in range(100)])
print("SVD explained var:", round(svd.explained_variance_ratio_.sum(),3))
res['text_repr']='TF-IDF(1-2gram, 20k) + TruncatedSVD(100); sentence-transformers download blocked (403) in this environment'
res['DML_H2_dict_text']=run_dml(D, prep(D, pd.concat([dicts.reset_index(drop=True), Z],axis=1)), 'relig_strict', 'DML H2 (+dict+text SVD)')
json.dump(res,open("out/step4_dml.json","w"),indent=1)
pd.DataFrame([dict(model=k,**v) for k,v in res.items() if isinstance(v,dict)]).to_csv("out/표6_DML.csv",index=False)
