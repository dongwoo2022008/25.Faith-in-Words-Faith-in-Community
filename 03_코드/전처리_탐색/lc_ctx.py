import pandas as pd, re, random
df=pd.read_pickle("lc_small3.pkl"); H=pd.read_pickle("lc_hits.pkl")
et=df['emp_title'].fillna('').str.lower()
occ=et.str.contains(r"\bchurch|\bpastor|\bminister\b|\bministry|\bclergy|\bpriest|\bchaplain|\bdiocese|\bparish|\bchristian|\bcatholic|\bbaptist|\blutheran|\bmethodist|\bsynagogue|\bmosque|\brabbi|\bmissionar|\bseminary|\bworship|\breverend|\barchdiocese|\bpresbyter", regex=True)
print("relig occupation n", occ.sum()); print(et[occ].value_counts().head(30))
df['relig_occ']=occ
term=df[df.loan_status.isin(['Fully Paid','Charged Off','Default'])].copy(); term['default']=term.loan_status.isin(['Charged Off','Default']).astype(int)
print(term.groupby('relig_occ').default.agg(['size','mean']))
print(term[term.relig_occ].groupby(term.year).default.agg(['size','mean']))
df.to_pickle("lc_small3.pkl")
# context windows
txt=(df['title'].fillna('')+' || '+df['desc_c'])
random.seed(1)
out=[]
for k in ['god','bless','faith','pray','church','lord','holy','tithe','ministry','christian']:
    idx=list(H.index[H[k]]); random.shuffle(idx)
    out.append(f"\n===== {k} (n={len(H[k].sum() and [1]*H[k].sum())}) =====")
    for i in idx[:12]:
        t=txt[i]; m=re.search(re.compile({'god':r"\bgod\b",'bless':r"\bbless",'faith':r"\bfaith",'pray':r"\bpray",'church':r"\bchurch",'lord':r"\blord\b",'holy':r"\bholy\b|\bheaven",'tithe':r"\btith",'ministry':r"\bministr|\bmissionar|\bpastor|\bcongregation|\bmission trip",'christian':r"\bchristian"}[k],re.I), t)
        a=max(0,m.start()-110); b=min(len(t),m.end()+110)
        out.append(f"[{df.loan_status[i]} | {int(df.year[i])}] ...{t[a:b]}...")
open("lc_context_samples.txt","w").write("\n".join(out)); print("\n".join(out))
