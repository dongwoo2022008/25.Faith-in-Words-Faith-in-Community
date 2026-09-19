import pandas as pd, numpy as np, json, time, warnings; warnings.filterwarnings("ignore")
import spacy
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from sklearn.decomposition import PCA
from catboost import CatBoostClassifier, CatBoostRegressor
import doubleml as dml
D=pd.read_pickle("D.pkl"); txt=D['txt'].tolist()
# (a) spaCy en_core_web_md 300-d pretrained word vectors, mean-pooled (tok2vec/parser disabled for speed)
t=time.time(); nlp=spacy.load("en_core_web_md", disable=["parser","ner","tagger","lemmatizer","attribute_ruler"])
V=np.zeros((len(txt),300),dtype=np.float32)
for i,doc in enumerate(nlp.pipe(txt, batch_size=512)): V[i]=doc.vector
print("spacy vectors", V.shape, round(time.time()-t),"s"); np.save("out/spacy_vec.npy",V)
# (b) doc2vec trained on the corpus itself
t=time.time(); docs=[TaggedDocument(s.split(),[i]) for i,s in enumerate(txt)]
d2v=Doc2Vec(vector_size=100, min_count=5, epochs=20, workers=2, seed=0, dm=1, window=5); d2v.build_vocab(docs); d2v.train(docs, total_examples=len(docs), epochs=d2v.epochs)
W=np.vstack([d2v.dv[i] for i in range(len(txt))]); print("doc2vec", W.shape, round(time.time()-t),"s"); np.save("out/doc2vec_vec.npy",W)
def prep(df, extra):
    X=pd.get_dummies(df[['grade','yr','emp','home','ver','purp','st']].astype(str),drop_first=True).astype(float).reset_index(drop=True)
    X=pd.concat([X, df[['int','fico','linc','dti','term60','lamt','llen','moral','hardship','gratitude','family','help','business']].astype(float).reset_index(drop=True), extra.reset_index(drop=True)],axis=1)
    X.columns=[f"x{i}" for i in range(X.shape[1])]; return X
def run(X,label,seed=0):
    t=time.time(); data=pd.concat([D[['default']].astype(int).reset_index(drop=True), pd.Series(D.relig_strict.astype(int).values,name='d'), X],axis=1)
    obj=dml.DoubleMLData(data,'default','d',list(X.columns))
    plr=dml.DoubleMLPLR(obj, CatBoostRegressor(iterations=400,depth=6,learning_rate=0.08,verbose=0,thread_count=2,random_seed=seed), CatBoostClassifier(iterations=400,depth=6,learning_rate=0.08,verbose=0,thread_count=2,random_seed=seed), n_folds=5); plr.fit(); s=plr.summary
    irm=dml.DoubleMLIRM(obj, CatBoostClassifier(iterations=400,depth=6,learning_rate=0.08,verbose=0,thread_count=2,random_seed=seed), CatBoostClassifier(iterations=400,depth=6,learning_rate=0.08,verbose=0,thread_count=2,random_seed=seed), n_folds=5, score='ATTE', trimming_threshold=0.001); irm.fit(); s2=irm.summary
    r=dict(PLR_theta=float(s['coef'].iloc[0]),SE=float(s['std err'].iloc[0]),p=float(s['P>|t|'].iloc[0]),CI_low=float(s['2.5 %'].iloc[0]),CI_high=float(s['97.5 %'].iloc[0]),ATTE=float(s2['coef'].iloc[0]),ATTE_p=float(s2['P>|t|'].iloc[0]),n_features=int(X.shape[1]),sec=round(time.time()-t)); print(label,r); return r
res={}
Vp=pd.DataFrame(PCA(50,random_state=0).fit_transform(V),columns=[f"sp{i}" for i in range(50)])
res['DML_H2_dict_spacy300_pca50']=run(prep(D,Vp),'spaCy md 300->PCA50')
res['DML_H2_dict_spacy300_full']=run(prep(D,pd.DataFrame(V,columns=[f"sv{i}" for i in range(300)])),'spaCy md 300 full')
res['DML_H2_dict_doc2vec100']=run(prep(D,pd.DataFrame(W,columns=[f"dv{i}" for i in range(100)])),'doc2vec100')
# seeds robustness on the pca50 spec
for sd in [1,2]: res[f'DML_H2_dict_spacy300_pca50_seed{sd}']=run(prep(D,Vp),f'spaCy pca50 seed{sd}',seed=sd)
res['note']='pretrained embeddings: spaCy en_core_web_md (300-d word vectors, mean-pooled); sentence-transformers unavailable (download blocked)'
json.dump(res,open("out/step4b_embed_dml.json","w"),indent=1); pd.DataFrame([dict(model=k,**v) for k,v in res.items() if isinstance(v,dict)]).to_csv("out/표6b_DML_임베딩.csv",index=False)
