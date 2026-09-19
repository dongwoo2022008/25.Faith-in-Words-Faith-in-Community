import pandas as pd, numpy as np, json, time, warnings; warnings.filterwarnings("ignore")
from sklearn.decomposition import PCA
from catboost import CatBoostClassifier, CatBoostRegressor
import doubleml as dml
D=pd.read_pickle("D.pkl"); lc=pd.read_csv("out/코딩결과_lc.csv"); D['loan_id']=pd.to_numeric(D.id,errors='coerce').astype('Int64')
D=D.merge(lc[['loan_id','type']],on='loan_id',how='left'); D['relig_valid']=(D.relig_strict & D.type.isin(['a','b','c'])).astype(int)
# drop the false-positive loans from the sample so they are neither treated nor control
keep=~(D.relig_strict & (D.type=='x')); D=D[keep].reset_index(drop=True); print("n",len(D),"treated",int(D.relig_valid.sum()))
V=np.load("out/spacy_vec.npy")[keep.values]
def prep(extra):
    X=pd.get_dummies(D[['grade','yr','emp','home','ver','purp','st']].astype(str),drop_first=True).astype(float).reset_index(drop=True)
    X=pd.concat([X, D[['int','fico','linc','dti','term60','lamt','llen','moral','hardship','gratitude','family','help','business']].astype(float).reset_index(drop=True)]+([extra.reset_index(drop=True)] if extra is not None else []),axis=1)
    X.columns=[f"x{i}" for i in range(X.shape[1])]; return X
def run(X,label,seed=0):
    t=time.time(); data=pd.concat([D[['default']].astype(int), pd.Series(D.relig_valid.values,name='d'), X],axis=1)
    obj=dml.DoubleMLData(data,'default','d',list(X.columns))
    plr=dml.DoubleMLPLR(obj, CatBoostRegressor(iterations=400,depth=6,learning_rate=0.08,verbose=0,thread_count=2,random_seed=seed), CatBoostClassifier(iterations=400,depth=6,learning_rate=0.08,verbose=0,thread_count=2,random_seed=seed), n_folds=5); plr.fit(); s=plr.summary
    r=dict(PLR_theta=float(s['coef'].iloc[0]),SE=float(s['std err'].iloc[0]),p=float(s['P>|t|'].iloc[0]),CI_low=float(s['2.5 %'].iloc[0]),CI_high=float(s['97.5 %'].iloc[0]),n_features=int(X.shape[1]),sec=round(time.time()-t)); print(label,r); return r
res={'DML_valid_dict':run(prep(None),'validated +dict'),'DML_valid_dict_spacy_pca50':run(prep(pd.DataFrame(PCA(50,random_state=0).fit_transform(V))),'validated +dict+spaCy pca50'),'DML_valid_dict_spacy300':run(prep(pd.DataFrame(V)),'validated +dict+spaCy300')}
json.dump(res,open("out/step4c_valid_dml.json","w"),indent=1)
