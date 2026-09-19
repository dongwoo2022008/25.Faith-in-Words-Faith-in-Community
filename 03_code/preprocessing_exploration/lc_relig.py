import pandas as pd, re, numpy as np
df=pd.read_pickle("lc_small2.pkl")
kw={
 'god':r"\bgod\b", 'jesus':r"\bjesus\b", 'christ':r"\bchrist\b", 'christian':r"\bchristians?\b",
 'church':r"\bchurch(es)?\b", 'pray':r"\bpray(s|ed|ing|er|ers)?\b", 'bless':r"\bbless(ed|ing|ings)?\b",
 'faith':r"\bfaith(ful)?\b", 'bible':r"\bbible\b|\bbiblical\b|\bscripture\b", 'lord':r"\bthe lord\b|\blord\b",
 'ministry':r"\bministr(y|ies)\b|\bmissionar(y|ies)\b|\bmission trip\b|\bpastor\b|\bcongregation\b",
 'religion':r"\breligio(n|us)\b", 'tithe':r"\btith(e|es|ing)\b", 'amen':r"\bamen\b", 'holy':r"\bholy\b|\bheaven\b",
 'muslim':r"\bmuslim\b|\bislam(ic)?\b|\bmosque\b|\ballah\b|\bhajj\b|\bramadan\b",
 'jewish':r"\bjewish\b|\bsynagogue\b|\btemple\b|\bbar mitzvah\b|\bbat mitzvah\b",
 'other':r"\bbuddhis(t|m)\b|\bhindu\b|\bcatholic\b|\bbaptist\b|\bmethodist\b|\blutheran\b|\bpresbyterian\b|\bmormon\b|\blds\b|\bevangelical\b",
}
txt=(df['title'].fillna('')+' || '+df['desc_c']).str.lower()
hits={}
for k,p in kw.items():
    m=txt.str.contains(p, regex=True)
    hits[k]=m
    print(f"{k:10s} {m.sum():6d}")
H=pd.DataFrame(hits); df['any_relig']=H.any(axis=1)
# narrow core Christian set
core=['god','jesus','christ','christian','church','pray','bless','faith','bible','lord','ministry','amen','holy','tithe']
df['core_relig']=H[core].any(axis=1)
print("any:",df.any_relig.sum(),"core:",df.core_relig.sum())
# among has_desc only
hd=df[df.has_desc]
print("has_desc n",len(hd),"core hits",hd.core_relig.sum(), f"{100*hd.core_relig.mean():.2f}%")
print(hd.groupby('year').core_relig.agg(['size','sum']).assign(pct=lambda x:(100*x['sum']/x['size']).round(2)))
# default among terminal loans
term=hd[hd.loan_status.isin(['Fully Paid','Charged Off','Default'])].copy()
term['default']=term.loan_status.isin(['Charged Off','Default']).astype(int)
print("terminal n",len(term))
print(term.groupby('core_relig')['default'].agg(['size','mean']))
for k in core:
    s=term[H.loc[term.index,k]]
    if len(s)>0: print(f"{k:10s} n={len(s):5d} default={s.default.mean():.3f}")
# also emp_title religious occupation
et=df['emp_title'].fillna('').str.lower()
occ=et.str.contains(r"church|pastor|minist|clergy|priest|chaplain|diocese|parish|christian|catholic|baptist|lutheran|methodist|synagogue|mosque|rabbi|missionar|seminary|youth pastor|worship", regex=True)
print("emp_title religious n", occ.sum()); print(df.loc[occ,'emp_title'].str.lower().value_counts().head(25))
df['relig_occ']=occ
df.to_pickle("lc_small3.pkl"); H.to_pickle("lc_hits.pkl")
