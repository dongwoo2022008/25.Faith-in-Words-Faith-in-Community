"""Post-charge-off recoveries by affiliation and religious language.
This analysis was removed from the manuscript (October 2026); the script is kept because its
numbers (268,599 charged-off loans; any recovery 74.6 vs 68.7 percent; 8.4 vs 7.5 cents per dollar;
OLS 0.9 cents, p 0.057; religious language 6.3 vs 7.1 cents) were verified against the raw file
and may be requested. Needs lc_final.pkl from lc_extract.py and the raw LendingClub file.
"""
import pandas as pd, numpy as np, warnings, json; warnings.filterwarnings("ignore")
import statsmodels.formula.api as smf
f="04_data/raw/LendingClub/accepted_2007_to_2018Q4.csv.gz"
cols=['id','recoveries','funded_amnt','loan_status']
ex=pd.concat([c for c in pd.read_csv(f, usecols=cols, chunksize=400000, low_memory=False)]); ex['id']=pd.to_numeric(ex.id,errors='coerce'); ex=ex[ex.id.notna()]; ex['id']=ex.id.astype(int)
df=pd.read_pickle("lc_final.pkl"); df['id']=pd.to_numeric(df.id,errors='coerce'); df=df[df.id.notna()]; df['id']=df.id.astype(int)
et=df['emp_title'].fillna('').str.lower().str.strip()
role=et.str.contains(r"\bpastor\b|\bminister\b|\bministry\b|\bclergy\b|\bpriest\b|\bchaplain\b|\brabbi\b|\bmissionar|\breverend\b|\bevangelist\b|\bdeacon\b|\bworship\b|\bimam\b|\bseminar(y|ian)\b", regex=True)
org=et.str.contains(r"\bchurch\b|\bparish\b|\bdiocese\b|\bcongregation\b|\bsynagogue\b|\bmosque\b", regex=True)
inst=et.str.contains(r"hospital|health|medical|charit|university|college|school|academy|insurance|bank|credit union|hospice|clinic|services inc|mutual", regex=True)
df['clergy']=role|(org&~inst)
m=df[['id','clergy','relig_strict','has_desc','grade','year','annual_inc','dti','loan_amnt','term','int_rate','loan_status']].merge(ex[['id','recoveries','funded_amnt']],on='id')
m['int']=m.int_rate.astype(str).str.rstrip('%').astype(float); m['linc']=np.log1p(m.annual_inc.fillna(0)); m['lamt']=np.log(m.loan_amnt); m['t60']=m.term.astype(str).str.contains('60').astype(int); m['yr']=m.year.astype('Int64').astype(str)
co=m[m.loan_status.isin(['Charged Off','Default'])].copy(); co['rec_rate']=co.recoveries/co.funded_amnt
out=dict(n_chargedoff=int(len(co)), n_clergy=int(co.clergy.sum()),
 any_rec_clergy=float((co[co.clergy].recoveries>0).mean()), any_rec_other=float((co[~co.clergy].recoveries>0).mean()),
 rec_clergy=float(co[co.clergy].rec_rate.mean()), rec_other=float(co[~co.clergy].rec_rate.mean()),
 rec_relig=float(co[co.has_desc&co.relig_strict].rec_rate.mean()), rec_otherdesc=float(co[co.has_desc&~co.relig_strict].rec_rate.mean()), n_relig_co=int((co.has_desc&co.relig_strict).sum()))
r=smf.ols("rec_rate ~ clergy + C(grade)+C(yr)+int+linc+dti+t60+lamt", data=co).fit()
out['ols_coef']=float(r.params['clergy[T.True]']); out['ols_p']=float(r.pvalues['clergy[T.True]'])
print(json.dumps(out,indent=1)); json.dump(out,open("out/verify_recovery.json","w"),indent=1)
