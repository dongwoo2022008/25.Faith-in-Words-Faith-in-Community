import pandas as pd, re, numpy as np
df=pd.read_pickle("lc_small.pkl")
df['year']=pd.to_datetime(df['issue_d'], format='%b-%Y', errors='coerce').dt.year
# loan status
print(df['loan_status'].value_counts())
# clean desc: strip "Borrower added on MM/DD/YY > " tags and <br>
def clean(s):
    if not isinstance(s,str): return ""
    s=re.sub(r'Borrower added on \d{2}/\d{2}/\d{2} >', ' ', s)
    s=re.sub(r'<br\s*/?>', ' ', s, flags=re.I)
    s=re.sub(r'\s+',' ',s).strip()
    return s
df['desc_c']=df['desc'].map(clean)
df['desc_len']=df['desc_c'].str.split().str.len().fillna(0).astype(int)
df['has_desc']=df['desc_c'].str.len()>0
df['meaningful']=df['desc_len']>=10
g=df.groupby('year').agg(n=('id','size'), has_desc=('has_desc','sum'), meaningful=('meaningful','sum'))
g['pct_desc']=(100*g.has_desc/g.n).round(1); g['pct_meaningful']=(100*g.meaningful/g.n).round(1)
print(g); print(g.sum())
print("median words among has_desc:", df.loc[df.has_desc,'desc_len'].median(), "mean", df.loc[df.has_desc,'desc_len'].mean().round(1))
print("title non-null:", df['title'].notna().sum(), "distinct titles:", df['title'].nunique())
print(df['title'].value_counts().head(15))
df.to_pickle("lc_small2.pkl")
