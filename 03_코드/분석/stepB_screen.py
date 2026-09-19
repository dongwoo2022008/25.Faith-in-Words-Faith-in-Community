import pandas as pd, numpy as np, re, json, warnings; warnings.filterwarnings("ignore")
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import cross_val_predict, StratifiedKFold
from sklearn.metrics import roc_auc_score, average_precision_score
from scipy.sparse import hstack, csr_matrix
D=pd.read_pickle("D.pkl"); D['loan_id']=pd.to_numeric(D.id,errors='coerce').astype('Int64')
lc=pd.read_csv("out/코딩결과_lc.csv"); lc['loan_id']=lc.loan_id.astype(int)
D=D.merge(lc[['loan_id','type']],on='loan_id',how='left')
V=np.load("out/spacy_vec.npy"); assert V.shape[0]==len(D)
pos=D.index[D.type.isin(['a','b','c'])]; negx=D.index[D.type=='x']
rng=np.random.default_rng(0); unl=D.index[~D.relig_strict]; neg=rng.choice(unl, 4000, replace=False)
tr=np.concatenate([pos,negx,neg]); y=np.r_[np.ones(len(pos)),np.zeros(len(negx)+len(neg))]
# remove explicit religious vocabulary from text so the classifier learns context/implicit cues, not the dictionary itself
relig=r"\b(god|gods|god's|jesus|christ|christian|christians|church|churches|pray|prays|prayed|praying|prayer|prayers|bless|blessed|blessing|blessings|faith|faithful|lord|bible|biblical|scripture|tithe|tithes|tithing|ministry|ministries|missionary|missionaries|pastor|congregation|clergy|rabbi|amen|religion|religious|catholic|baptist|methodist|lutheran|presbyterian|mormon|evangelical|pentecostal)\b"
txt_m=D['txt'].str.replace(relig," ",regex=True)
tf=TfidfVectorizer(min_df=5,max_features=30000,ngram_range=(1,2),sublinear_tf=True); Xt=tf.fit_transform(txt_m)
Xv=csr_matrix(V/ (np.linalg.norm(V,axis=1,keepdims=True)+1e-9))
X=hstack([Xt,Xv]).tocsr()
clf=LogisticRegression(C=2.0,max_iter=3000,class_weight='balanced')
cv=cross_val_predict(clf,X[tr],y,cv=StratifiedKFold(5,shuffle=True,random_state=0),method='predict_proba')[:,1]
print("CV AUC (masked text, implicit cues):",round(roc_auc_score(y,cv),3),"AP",round(average_precision_score(y,cv),3))
clf.fit(X[tr],y); D['p_relig']=clf.predict_proba(X)[:,1]
cand=D[(~D.relig_strict)].sort_values('p_relig',ascending=False)
print("unflagged with p>0.5:",int((cand.p_relig>0.5).sum()),"p>0.3:",int((cand.p_relig>0.3).sum()))
# implicit-cue dictionary as a second net
impl=r"\bhigher power\b|\bman upstairs\b|\bthe good lord\b|\bprayers? up\b|\bkeep(ing)? (me|us) in (your )?prayers\b|\bgodsend\b|\bmiracle\b|\bheaven(ly)? father\b|\bsavio(u)?r\b|\bworship\b|\bsunday school\b|\bbible study\b|\byouth group\b|\bmission trip\b|\bchapel\b|\bparish\b|\bdiocese\b|\bsermon\b|\bgospel\b|\bpsalm\b|\bproverbs\b|\bmatthew \d|\bjohn 3:16\b|\bin his name\b|\bhis will\b|\bthy will\b|\bhallelujah\b|\bpraise\b.*\bhim\b|\bhe has blessed\b|\bwalk(ing)? by faith\b|\bthank the heavens\b|\bkarma\b|\bnamaste\b|\bmosque\b|\bsynagogue\b|\btemple\b.*\b(hindu|buddhist|jewish)\b|\bislam\b|\bmuslim\b|\bjewish\b|\bbuddhis"
D['impl']=D['txt'].str.contains(impl,regex=True)
print("implicit-dictionary hits among unflagged:",int((D.impl & ~D.relig_strict).sum()))
sel=D[(~D.relig_strict)&((D.p_relig>0.3)|D.impl)].sort_values('p_relig',ascending=False)
print("candidates to code:",len(sel))
sel[['loan_id','p_relig','impl','txt']].to_pickle("out/B_candidates.pkl"); D[['loan_id','p_relig','impl']].to_pickle("out/B_scores.pkl")
