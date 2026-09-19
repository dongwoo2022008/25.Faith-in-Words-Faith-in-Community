import pandas as pd, numpy as np, json, time, warnings; warnings.filterwarnings("ignore")
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD, PCA
from catboost import CatBoostClassifier, CatBoostRegressor
import doubleml as dml
NREP=20
D=pd.read_pickle("D.pkl")
def prep(df, extra=None):
    X=pd.get_dummies(df[['grade','yr','emp','home','ver','purp','st']].astype(str),drop_first=True).astype(float).reset_index(drop=True)
    parts=[X, df[['int','fico','linc','dti','term60','lamt','llen','moral','hardship','gratitude','family','help','business']].astype(float).reset_index(drop=True)]
    if extra is not None: parts.append(extra.reset_index(drop=True))
    X=pd.concat(parts,axis=1); X.columns=[f"x{i}" for i in range(X.shape[1])]; return X
def run(X,label):
    t=time.time(); data=pd.concat([D[['default']].astype(int).reset_index(drop=True), pd.Series(D.relig_strict.astype(int).values,name='d'), X],axis=1)
    obj=dml.DoubleMLData(data,'default','d',list(X.columns))
    plr=dml.DoubleMLPLR(obj, CatBoostRegressor(iterations=400,depth=6,learning_rate=0.08,verbose=0,thread_count=2,random_seed=0),
                        CatBoostClassifier(iterations=400,depth=6,learning_rate=0.08,verbose=0,thread_count=2,random_seed=0), n_folds=5, n_rep=NREP)
    plr.fit(); s=plr.summary
    thetas=np.array(plr.all_coef).ravel(); ses=np.array(plr.all_se).ravel()
    r=dict(theta_median=float(s['coef'].iloc[0]),SE_median=float(s['std err'].iloc[0]),p=float(s['P>|t|'].iloc[0]),CI_low=float(s['2.5 %'].iloc[0]),CI_high=float(s['97.5 %'].iloc[0]),
           theta_min=float(thetas.min()),theta_max=float(thetas.max()),theta_sd_across_splits=float(thetas.std(ddof=1)),share_reps_p_lt_05=float(np.mean(2*(1-__import__('scipy').stats.norm.cdf(np.abs(thetas/ses)))<0.05)),
           n_rep=NREP,n_features=int(X.shape[1]),sec=round(time.time()-t))
    print(label,r,flush=True); return r
res={}
res['dict']=run(prep(D),'dict only')
tf=TfidfVectorizer(min_df=10, max_features=20000, ngram_range=(1,2), sublinear_tf=True, token_pattern=r"(?u)\b[a-z]{2,}\b")
Z=pd.DataFrame(TruncatedSVD(100, random_state=0).fit_transform(tf.fit_transform(D['txt'])), columns=[f"svd{i}" for i in range(100)])
res['dict_tfidf_svd100']=run(prep(D,Z),'+TF-IDF SVD100')
V=np.load("out/spacy_vec.npy"); Vp=pd.DataFrame(PCA(50,random_state=0).fit_transform(V),columns=[f"sp{i}" for i in range(50)])
res['dict_spacy_pca50']=run(prep(D,Vp),'+spaCy PCA50')
W=np.load("out/doc2vec_vec.npy"); res['dict_doc2vec100']=run(prep(D,pd.DataFrame(W,columns=[f"dv{i}" for i in range(100)])),'+doc2vec100')
res['note']=f'DoubleML-PLR, CatBoost nuisance, 5-fold, n_rep={NREP} repeated sample splits; theta/SE aggregated by median (DoubleML default)'
json.dump(res,open("out/step4d_rep_dml.json","w"),indent=1)
pd.DataFrame([dict(spec=k,**v) for k,v in res.items() if isinstance(v,dict)]).to_csv("out/표6c_DML_반복교차적합.csv",index=False)
print("DONE")
