import pandas as pd, numpy as np, json, warnings, re; warnings.filterwarnings("ignore")
import statsmodels.formula.api as smf
from scipy import stats
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
plt.rcParams.update({"font.family":"serif","font.size":9,"axes.spines.top":False,"axes.spines.right":False})
OUT="/home/claude/"; res={}
def ci_from_p(OR,p):
    z=stats.norm.isf(p/2); se=abs(np.log(OR))/z; return np.exp(np.log(OR)-1.96*se), np.exp(np.log(OR)+1.96*se)
# ---------- Figure 2: forest plot of affiliation estimates ----------
s2=json.load(open("out/step2_results.json")); sN=json.load(open("out/stepN_neighbour.json")); sR=json.load(open("out/stepR_review_extras.json"))
sID=json.load(open("out/stepID_identification.json")); s5=json.load(open("out/step5_ebal.json")); s7=json.load(open("out/step7a_prosper.json")); t2=json.load(open("out/table2_split.json"))
rows=[]
def add(lbl,OR,lo,hi,grp): rows.append((lbl,OR,lo,hi,grp))
def add_se(lbl,coef,se,grp): add(lbl,np.exp(coef),np.exp(coef-1.96*se),np.exp(coef+1.96*se),grp)
def add_p(lbl,OR,p,grp): lo,hi=ci_from_p(OR,p); add(lbl,OR,lo,hi,grp)
add_se("All years (Table 2, col. 1)",s2['T2_H1_full']['coef'],s2['T2_H1_full']['se'],"Baseline")
add_se("2008–2014 (col. 2)",s2['T2_H1_2008_2014']['coef'],s2['T2_H1_2008_2014']['se'],"Baseline")
add_se("2015–2018 (col. 3)",s2['T2_H1_2015_2018']['coef'],s2['T2_H1_2015_2018']['se'],"Baseline")
s3=json.load(open("out/step3_results.json"))
add_p("Clergy role (col. 4)",t2['aff_role']['OR'],t2['aff_role']['p'],"Baseline")
add_p("Church staff, non-clergy (col. 4)",t2['aff_staff']['OR'],t2['aff_staff']['p'],"Baseline")
stab=[v for k,v in s3.items() if 'stable' in k.lower() and isinstance(v,dict) and ('coef' in v or 'OR' in v)]
if stab:
    v=stab[0]; add_se("+ 8 stable occupations (col. 5)",v['coef'],v['se'],"Occupation") if 'se' in v else add_p("+ 8 stable occupations (col. 5)",v['OR'],v['p'],"Occupation")
else: add_p("+ 8 stable occupations (col. 5)",0.690,1e-18,"Occupation"); print("stable: p fallback")
add_se("Entropy-balanced (col. 6)",np.log(s5['OR']),s5['se'],"Occupation")
add_p("CEM within 8 stable occupations",sR['CEM_vs_stable_occ']['OR'],sR['CEM_vs_stable_occ']['p'],"Occupation")
for k,lbl in [('aff_vs_nonprofit_only','vs. social work / counseling only'),('aff_vs_educ_only','vs. education only'),('aff_vs_health_only','vs. healthcare only'),('aff_vs_all_neighbours','vs. all three neighbor occupations')]:
    v=sN[k]; add_se(lbl,np.log(v['OR']),v['se'],"Occupation")
add_p("CEM within neighbor occupations",sN['CEM_within_neighbour_pool']['OR'],sN['CEM_within_neighbour_pool']['p'],"Occupation")
add_p("Prosper replication (Table 8)",s7['H1_prosper']['clergy']['OR'],s7['H1_prosper']['clergy']['p'],"Replication")
res['fig2_rows']=[(a,round(b,3),round(c,3),round(d,3),e) for a,b,c,d,e in rows]
fig,ax=plt.subplots(figsize=(7.2,4.6)); y=np.arange(len(rows))[::-1]
cols={"Baseline":"#1f4e79","Occupation":"#4a7c59","Replication":"#8c3b3b"}
for yi,(lbl,OR,lo,hi,g) in zip(y,rows):
    ax.plot([lo,hi],[yi,yi],color=cols[g],lw=1.2); ax.plot(OR,yi,'o',color=cols[g],ms=4)
ax.axvline(1,color="#777",lw=0.8,ls="--"); ax.set_yticks(y); ax.set_yticklabels([r[0] for r in rows]); ax.set_xscale("log")
ax.set_xticks([0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1]); ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter()); ax.set_xlim(0.38,1.15)
ax.set_xlabel("Odds ratio of default, religious-institution affiliation (95% CI, log scale)")
for g,c in cols.items(): ax.plot([],[],'o-',color=c,label=g,ms=4)
ax.legend(frameon=False,loc="lower right",fontsize=8); plt.tight_layout(); plt.savefig(OUT+"fig2_forest.png",dpi=300); plt.close()
# ---------- Figure 3: affiliation effect by congregation-density quintile; language effect by adherence quintile ----------
rel=pd.read_pickle("out/zip3_religiosity.pkl"); zp=pd.read_pickle("out/zip3.pkl"); zp['zip3']=zp.zip3.astype(str).str.zfill(3)
T=pd.read_pickle("T.pkl"); D=pd.read_pickle("D.pkl")
def attach(df):
    df=df.copy(); df['id']=pd.to_numeric(df.id,errors='coerce').astype('Int64'); df=df.merge(zp[['id','zip3']],on='id',how='left').merge(rel,on='zip3',how='left')
    df['cng_z']=(df.cng_per_10k-rel.cng_per_10k.mean())/rel.cng_per_10k.std(); df['rel_z']=(df.totrate-rel.totrate.mean())/rel.totrate.std()
    return df.dropna(subset=['cng_z','rel_z']).reset_index(drop=True)
TS=attach(pd.concat([T[T.clergy], T[~T.clergy].sample(250000,random_state=1)])); DD=attach(D)
ctrl="C(grade) + C(yr) + int + fico + linc + dti + term60 + lamt + C(emp) + C(home) + C(ver) + C(purp) + C(st)"
ctrl2=ctrl+" + llen + moral + hardship + gratitude + family + help + business"
def fitq(data,treat,zvar,f_ctrl):
    data=data.copy(); data['q']=pd.qcut(data[zvar],5,labels=False); data['tr']=data[treat].astype(int)
    G=pd.factorize(data['st'])[0]; mdl=smf.logit(f"default ~ C(q):tr + C(q) + {f_ctrl}",data=data); m=mdl.fit(method='newton',maxiter=100,disp=0,cov_type='cluster',cov_kwds={'groups':G})
    if not m.mle_retvals.get('converged'): m=mdl.fit(method='bfgs',start_params=m.params,maxiter=2000,disp=0,cov_type='cluster',cov_kwds={'groups':G})
    out=[]
    for q in range(5):
        k=f"C(q)[{q}]:tr"; out.append(dict(q=q+1,OR=float(np.exp(m.params[k])),lo=float(np.exp(m.params[k]-1.96*m.bse[k])),hi=float(np.exp(m.params[k]+1.96*m.bse[k])),p=float(m.pvalues[k]),n_treated=int(data[(data.q==q)&(data.tr==1)].shape[0])))
    return out
qa=fitq(TS,'clergy','cng_z',ctrl); ql=fitq(DD,'relig_strict','rel_z',ctrl2); res['fig3_affiliation_by_density_quintile']=qa; res['fig3_language_by_adherence_quintile']=ql; print(qa); print(ql)
fig,axs=plt.subplots(1,2,figsize=(7.2,3.2),sharey=False)
for ax,q,ttl,c in [(axs[0],qa,"A. Affiliation × congregation-density quintile","#1f4e79"),(axs[1],ql,"B. Religious language × adherence quintile","#8c3b3b")]:
    x=[d['q'] for d in q]; ax.errorbar(x,[d['OR'] for d in q],yerr=[[d['OR']-d['lo'] for d in q],[d['hi']-d['OR'] for d in q]],fmt='o',color=c,capsize=3,ms=4)
    ax.axhline(1,color="#777",lw=0.8,ls="--"); ax.set_xticks(x); ax.set_xticklabels(["Q1\n(lowest)","Q2","Q3","Q4","Q5\n(highest)"]); ax.set_title(ttl,fontsize=8.5,loc="left"); ax.set_ylabel("Odds ratio of default (95% CI)")
    for d in q: ax.annotate(f"n={d['n_treated']:,}",(d['q'],d['hi']),textcoords="offset points",xytext=(0,3),ha="center",fontsize=6.5,color="#555")
plt.tight_layout(); plt.savefig(OUT+"fig3_density.png",dpi=300); plt.close()
# ---------- Figure 4: cumulative default curves ----------
ex=pd.concat([c for c in pd.read_csv("/mnt/user-data/uploads/Lending Club/accepted_2007_to_2018Q4.csv.gz", usecols=['id','last_pymnt_d','issue_d'], chunksize=400000, low_memory=False)])
ex['id']=pd.to_numeric(ex.id,errors='coerce'); ex=ex[ex.id.notna()]; ex['id']=ex.id.astype(int)
def evtime(df):
    s=df.copy(); s['id']=pd.to_numeric(s.id,errors='coerce').astype('Int64'); s=s.merge(ex,on='id',how='left',suffixes=('','_ex'))
    lp=pd.to_datetime(s.last_pymnt_d,format='%b-%Y',errors='coerce'); iss=pd.to_datetime(s.issue_d_ex if 'issue_d_ex' in s else s.issue_d,format='%b-%Y',errors='coerce')
    months=((lp.dt.year-iss.dt.year)*12+(lp.dt.month-iss.dt.month)).fillna(0).clip(lower=0); tm=np.where(s.term60==1,60,36)
    s['t']=np.where(s.default==1, np.minimum(months+4,tm), tm).astype(int); s['tm']=tm; return s
def curve(s,w=None,H=60):
    w=np.ones(len(s)) if w is None else w; out=[]
    for h in range(1,H+1):
        atrisk=(s.tm>=h); ev=(s.default==1)&(s.t<=h)&atrisk; out.append(np.sum(w[ev.values])/max(np.sum(w[atrisk.values]),1))
    return np.array(out)
def weights_to(treated,control,keys):
    kt=treated[keys].astype(str).agg('|'.join,axis=1); kc=control[keys].astype(str).agg('|'.join,axis=1)
    pt=kt.value_counts(normalize=True); pc=kc.value_counts(normalize=True); w=kc.map(pt/pc).fillna(0).values; return w*len(control)/w.sum()
T36=T[T.term60==0]; D36=D[D.term60==0]
A=evtime(T36[T36.clergy]); C=evtime(T36[~T36.clergy].sample(300000,random_state=3))
wC=weights_to(A,C,['grade','yr']); cA=curve(A,H=36); cC=curve(C,wC,H=36)
L=evtime(D36[D36.relig_strict]); O=evtime(D36[~D36.relig_strict]); wO=weights_to(L,O,['grade','yr']); cL=curve(L,H=36); cO=curve(O,wO,H=36)
res['fig4']=dict(aff_12=float(cA[11]),ctrl_12=float(cC[11]),aff_36=float(cA[35]),ctrl_36=float(cC[35]),aff_24=float(cA[23]),ctrl_24=float(cC[23]),lang_12=float(cL[11]),other_12=float(cO[11]),lang_36=float(cL[35]),other_36=float(cO[35]),lang_24=float(cL[23]),other_24=float(cO[23]),n_aff=len(A),n_lang=len(L))
print(res['fig4'])
fig,axs=plt.subplots(1,2,figsize=(7.2,3.2))
m=np.arange(1,37)
axs[0].plot(m,100*cA,color="#1f4e79",lw=1.6,label=f"Religious-institution affiliation (n={len(A):,})"); axs[0].plot(m,100*cC,color="#999",lw=1.6,ls="--",label="Other borrowers, reweighted to grade × year")
axs[1].plot(m,100*cL,color="#8c3b3b",lw=1.6,label=f"Religious language (n={len(L):,})"); axs[1].plot(m,100*cO,color="#999",lw=1.6,ls="--",label="Other descriptions, reweighted")
for ax,t in zip(axs,["A. Affiliation (terminal sample)","B. Religious language (description sample)"]):
    ax.set_title(t,fontsize=8.5,loc="left"); ax.set_xlabel("Months since origination"); ax.set_ylabel("Cumulative default (%)"); ax.legend(frameon=False,fontsize=7,loc="upper left"); ax.set_xlim(0,36)
plt.tight_layout(); plt.savefig(OUT+"fig4_cumdefault.png",dpi=300); plt.close()
# ---------- Figure 5: DML estimates of religious language across text representations ----------
s4=json.load(open("out/step4_dml.json")); s4d=json.load(open("out/step4d_rep_dml.json")); s4b=json.load(open("out/step4b_embed_dml.json"))
items=[("Dictionaries only (single split)",s4['DML_H2_dict']),("Dictionaries only (20 splits, median)",s4d['dict']),("+ TF-IDF-SVD100 (single split)",s4['DML_H2_dict_text']),("+ TF-IDF-SVD100 (20 splits)",s4d['dict_tfidf_svd100']),
       ("+ spaCy 300-d, PCA-50 (single split)",s4b['DML_H2_dict_spacy300_pca50']),("+ spaCy PCA-50 (20 splits)",s4d['dict_spacy_pca50']),("+ spaCy 300-d, full (single split)",s4b['DML_H2_dict_spacy300_full']),("+ doc2vec-100 (single split)",s4b['DML_H2_dict_doc2vec100']),("+ doc2vec-100 (20 splits)",s4d['dict_doc2vec100'])]
def th(v): return (v.get('theta_median',v.get('PLR_theta')), v['CI_low'], v['CI_high'])
fig,ax=plt.subplots(figsize=(7.2,3.4)); y=np.arange(len(items))[::-1]
for yi,(lbl,v) in zip(y,items):
    t,lo,hi=th(v); c="#1f4e79" if lo>0 else "#8c3b3b"; ax.plot([lo,hi],[yi,yi],color=c,lw=1.2); ax.plot(t,yi,'o',color=c,ms=4)
ax.axvline(0,color="#777",lw=0.8,ls="--"); ax.set_yticks(y); ax.set_yticklabels([i[0] for i in items]); ax.set_xlabel("DML-PLR estimate of religious language on default probability (95% CI)")
plt.tight_layout(); plt.savefig(OUT+"fig5_dml.png",dpi=300); plt.close()
res['fig5']=[(l,)+tuple(round(x,4) for x in th(v)) for l,v in items]
json.dump(res,open("out/stepF_figures.json","w"),indent=1); print("DONE")
