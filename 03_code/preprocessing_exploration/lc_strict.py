import pandas as pd, re
df=pd.read_pickle("lc_small3.pkl")
txt=(df['title'].fillna('')+' || '+df['desc_c']).str.lower()
strict={'god':r"\bgod\b(?! ?father)|\bgod's\b", 'jesus/christ':r"\bjesus\b|\bchrist\b", 'christian':r"\bchristians?\b", 'church':r"\bchurch(es)?\b",
 'pray/prayer':r"\bpray(s|ed|ing|er|ers)?\b", 'bless (God bless / blessed / blessing)':r"\bbless(ed|ing|ings)?\b",
 'faith (religious use only)':r"\bfaith\b(?! in (me|us|you|him|her|them|one another|people|the|my|our|this|humanity))(?<!good )(?<!bad )|\bfaithful\b",
 'lord (religious)':r"\bthe lord\b|\bpraise the lord\b|\blord bless\b|\blord willing\b|\blord (and|&) savio(u)?r\b|\bgood lord\b|\bhelp me lord\b|\bmy lord\b",
 'bible/scripture':r"\bbible\b|\bbiblical\b|\bscripture\b", 'tithe':r"\btith(e|es|ing|er)\b", 'ministry/pastor/missionary':r"\bministr(y|ies)\b|\bmissionar(y|ies)\b|\bmission trip\b|\bpastor\b|\bcongregation\b|\bclergy\b|\brabbi\b|\bseminary\b",
 'amen':r"\bamen\b", 'religion/religious':r"\breligio(n|us)\b", 'catholic/baptist/etc denomination':r"\bcatholic\b|\bbaptist\b|\bmethodist\b|\blutheran\b|\bpresbyterian\b|\bmormon\b|\bevangelical\b|\bpentecostal\b",
 'muslim/islam':r"\bmuslim\b|\bislam(ic)?\b|\bmosque\b|\ballah\b", 'jewish/synagogue':r"\bjewish\b|\bsynagogue\b|\bjudaism\b", 'buddhist/hindu':r"\bbuddhis(t|m)\b|\bhindu\b"}
H=pd.DataFrame({k:txt.str.contains(p,regex=True) for k,p in strict.items()})
hd=df.has_desc
for k in strict: print(f"{k:42s} all={H[k].sum():4d}  has_desc={H[k][hd].sum():4d}")
df['relig_strict']=H.any(axis=1)
print("STRICT any:", df.relig_strict.sum(), "among has_desc:", df.relig_strict[hd].sum(), f"{100*df.relig_strict[hd].mean():.2f}%", "among meaningful(>=10w):", df.relig_strict[df.meaningful].sum())
chr_=[k for k in strict if k not in ('muslim/islam','jewish/synagogue','buddhist/hindu','religion/religious')]
df['relig_christian']=H[chr_].any(axis=1); print("Christian-specific:", df.relig_christian[hd].sum())
print(df[hd].groupby('year').relig_strict.agg(['size','sum']).assign(pct=lambda x:(100*x['sum']/x['size']).round(2)))
term=df[hd & df.loan_status.isin(['Fully Paid','Charged Off','Default'])].copy(); term['default']=term.loan_status.isin(['Charged Off','Default']).astype(int)
print("terminal has_desc n",len(term)); print(term.groupby('relig_strict').default.agg(['size','mean']).round(4))
print(term.groupby('grade').apply(lambda g: pd.Series({'n_relig':g.relig_strict.sum(),'def_relig':g[g.relig_strict].default.mean(),'def_other':g[~g.relig_strict].default.mean()})).round(3))
# text length comparison
print("desc words: relig", term[term.relig_strict].desc_len.median(), "other", term[~term.relig_strict].desc_len.median())
# emp_title relig occupation stats overall (all years)
t2=df[df.loan_status.isin(['Fully Paid','Charged Off','Default'])].copy(); t2['default']=t2.loan_status.isin(['Charged Off','Default']).astype(int)
print("relig_occ terminal:", t2.groupby('relig_occ').default.agg(['size','mean']).round(4))
print(t2.groupby(['grade','relig_occ']).default.mean().unstack().round(3))
df.to_pickle("lc_final.pkl"); H.to_pickle("lc_hits_strict.pkl")
