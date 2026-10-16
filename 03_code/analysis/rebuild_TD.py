# Rebuild T.pkl / D.pkl from the raw LendingClub file, replicating lc_extract -> lc_stats -> lc_strict -> step1
# chunk by chunk to stay within memory. Validation targets: T 1,344,976; clergy 3,105; D 123,292; relig 681.
# Run: python rebuild_TD.py  (edit the path f below to point at 04_data/raw/LendingClub/accepted_2007_to_2018Q4.csv.gz)
import pandas as pd, numpy as np, re, gc, time
f="04_data/raw/LendingClub/accepted_2007_to_2018Q4.csv.gz"
cols=['id','loan_amnt','funded_amnt','funded_amnt_inv','term','int_rate','grade','sub_grade','emp_title','emp_length','home_ownership','annual_inc','verification_status','issue_d','loan_status','desc','purpose','title','addr_state','dti','fico_range_low','fico_range_high','application_type']
def clean(s):
    if not isinstance(s,str): return ""
    s=re.sub(r'Borrower added on \d{2}/\d{2}/\d{2} >', ' ', s); s=re.sub(r'<br\s*/?>', ' ', s, flags=re.I); s=re.sub(r'\s+',' ',s).strip(); return s
strict={'god':r"\bgod\b(?! ?father)|\bgod's\b", 'jesus/christ':r"\bjesus\b|\bchrist\b", 'christian':r"\bchristians?\b", 'church':r"\bchurch(es)?\b",
 'pray/prayer':r"\bpray(s|ed|ing|er|ers)?\b", 'bless':r"\bbless(ed|ing|ings)?\b",
 'faith':r"\bfaith\b(?! in (me|us|you|him|her|them|one another|people|the|my|our|this|humanity))(?<!good )(?<!bad )|\bfaithful\b",
 'lord':r"\bthe lord\b|\bpraise the lord\b|\blord bless\b|\blord willing\b|\blord (and|&) savio(u)?r\b|\bgood lord\b|\bhelp me lord\b|\bmy lord\b",
 'bible':r"\bbible\b|\bbiblical\b|\bscripture\b", 'tithe':r"\btith(e|es|ing|er)\b", 'ministry':r"\bministr(y|ies)\b|\bmissionar(y|ies)\b|\bmission trip\b|\bpastor\b|\bcongregation\b|\bclergy\b|\brabbi\b|\bseminary\b",
 'amen':r"\bamen\b", 'religion':r"\breligio(n|us)\b", 'denom':r"\bcatholic\b|\bbaptist\b|\bmethodist\b|\blutheran\b|\bpresbyterian\b|\bmormon\b|\bevangelical\b|\bpentecostal\b",
 'muslim':r"\bmuslim\b|\bislam(ic)?\b|\bmosque\b|\ballah\b", 'jewish':r"\bjewish\b|\bsynagogue\b|\bjudaism\b", 'buddhist':r"\bbuddhis(t|m)\b|\bhindu\b"}
parts=[]; t=time.time()
for ch in pd.read_csv(f, usecols=cols, chunksize=200000, low_memory=False):
    ch=ch[ch['id'].notna()].copy()
    ch['year']=pd.to_datetime(ch['issue_d'], format='%b-%Y', errors='coerce').dt.year
    ch['desc_c']=ch['desc'].map(clean); ch['desc_len']=ch['desc_c'].str.split().str.len().fillna(0).astype(int); ch['has_desc']=ch['desc_c'].str.len()>0
    txt=(ch['title'].fillna('')+' || '+ch['desc_c']).str.lower()
    ch['relig_strict']=False
    for k,p in strict.items(): ch['relig_strict']|=txt.str.contains(p,regex=True)
    ch=ch[ch.loan_status.isin(['Fully Paid','Charged Off','Default'])]   # terminal only (T construction)
    ch=ch.drop(columns=['desc'])
    ch.loc[~ch.has_desc,'desc_c']=''   # keep text only where needed
    parts.append(ch); print(len(parts), len(ch), round(time.time()-t)); gc.collect()
df=pd.concat(parts, ignore_index=True); del parts; gc.collect()
et=df['emp_title'].fillna('').str.lower().str.strip()
role=et.str.contains(r"\bpastor\b|\bminister\b|\bministry\b|\bclergy\b|\bpriest\b|\bchaplain\b|\brabbi\b|\bmissionar|\breverend\b|\bevangelist\b|\bdeacon\b|\bworship\b|\bimam\b|\bseminar(y|ian)\b", regex=True)
org=et.str.contains(r"\bchurch\b|\bparish\b|\bdiocese\b|\bcongregation\b|\bsynagogue\b|\bmosque\b", regex=True)
inst=et.str.contains(r"hospital|health|medical|charit|university|college|school|academy|insurance|bank|credit union|hospice|clinic|services inc|mutual", regex=True)
df['clergy']=role|(org&~inst)
T=df; del df
T['default']=T.loan_status.isin(['Charged Off','Default']).astype(int)
T['yr']=T.year.astype('Int64').astype(str); T['int']=T.int_rate.astype(str).str.rstrip('%').astype(float)
T['fico']=(T.fico_range_low+T.fico_range_high)/2; T['linc']=np.log1p(T.annual_inc.fillna(0)); T['term60']=T.term.astype(str).str.contains('60').astype(int)
T['lamt']=np.log(T.loan_amnt); T['emp']=T.emp_length.fillna('na').astype(str); T['home']=T.home_ownership.fillna('na'); T['ver']=T.verification_status.fillna('na'); T['purp']=T.purpose.fillna('na'); T['st']=T.addr_state.fillna('na')
T=T.dropna(subset=['dti','fico','int'])
D=T[T.has_desc].copy()
print("terminal",len(T),"clergy",int(T.clergy.sum()),"desc",len(D),"relig",int(D.relig_strict.sum()))
txt=(D['title'].fillna('')+' '+D['desc_c']).str.lower()
D['llen']=np.log1p(D.desc_len)
dic={'moral':r"\bhonest(y|ly)?\b|\bpromise\b|\bintegrity\b|\bresponsib(le|ility)\b|\btrustworthy\b|\bcommit(ted|ment)\b|\bmy word\b|\bhonou?r\b|\bguarantee\b|\bnever (been )?late\b|\bnever missed\b|\breliable\b|\bhard[- ]?working\b",
     'hardship':r"\bstruggl|\bhard time|\blost my job\b|\blaid off\b|\bunemploy|\bmedical\b|\bdivorce|\bsick\b|\bhospital\b|\bemergency\b|\bbehind on\b|\bcan'?t afford\b|\bdesperate|\bdifficult\b|\bsurgery\b|\billness\b|\bdisab",
     'gratitude':r"\bthank(s| you)?\b|\bappreciat|\bgrateful\b",'family':r"\bfamily\b|\bwife\b|\bhusband\b|\bkids?\b|\bchildren\b|\bdaughter\b|\bson\b|\bmother\b|\bfather\b|\bmom\b|\bdad\b",
     'help':r"\bplease help\b|\bhelp me\b|\bneed help\b|\bhelp us\b",'business':r"\bbusiness\b|\bcompany\b|\bstart[- ]?up\b|\bcustomers?\b"}
for k,p in dic.items(): D[k]=txt.str.contains(p,regex=True).astype(int)
T=T.drop(columns=['desc_c','title','emp_title'])
T.to_pickle("T.pkl"); D.to_pickle("D.pkl"); print("saved", round(time.time()-t))
