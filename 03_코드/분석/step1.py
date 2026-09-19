import pandas as pd, numpy as np, re, warnings; warnings.filterwarnings("ignore")
df=pd.read_pickle("lc_final.pkl")
et=df['emp_title'].fillna('').str.lower().str.strip()
role=et.str.contains(r"\bpastor\b|\bminister\b|\bministry\b|\bclergy\b|\bpriest\b|\bchaplain\b|\brabbi\b|\bmissionar|\breverend\b|\bevangelist\b|\bdeacon\b|\bworship\b|\bimam\b|\bseminar(y|ian)\b", regex=True)
org=et.str.contains(r"\bchurch\b|\bparish\b|\bdiocese\b|\bcongregation\b|\bsynagogue\b|\bmosque\b", regex=True)
inst=et.str.contains(r"hospital|health|medical|charit|university|college|school|academy|insurance|bank|credit union|hospice|clinic|services inc|mutual", regex=True)
df['clergy']=role|(org&~inst)
T=df[df.loan_status.isin(['Fully Paid','Charged Off','Default'])].copy()
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
D['txt']=txt
# stable occupations (7-C)
e2=et.loc[T.index]
occ={'teacher':r"\bteacher\b|\bprofessor\b|\beducator\b|\binstructor\b",'police':r"\bpolice\b|\bcorrection|\bsheriff\b|\bdeputy\b|\btrooper\b",'fire':r"\bfire ?fighter\b|\bfireman\b|\bfire dept",'military':r"\bus army\b|\bus navy\b|\bair force\b|\bmarine corps\b|\bmilitary\b|\bsoldier\b|\barmy\b|\bnavy\b",'govt':r"\bgovernment\b|\bfederal\b|\bstate of\b|\bcity of\b|\bcounty of\b|\bcounty\b|\bmunicipal",'nurse':r"\bnurse\b|\brn\b|\blpn\b",'postal':r"\busps\b|\bpostal\b|\bpost office\b",'transit':r"\btransit\b|\bmta\b|\bbus driver\b|\bbus operator\b"}
for k,p in occ.items(): T[k]=e2.str.contains(p,regex=True).astype(int)
T['stable_any']=T[list(occ)].max(axis=1)
print("stable occ counts:",{k:int(T[k].sum()) for k in occ},"any",int(T.stable_any.sum()),"clergy&stable",int((T.clergy&(T.stable_any==1)).sum()))
T.to_pickle("T.pkl"); D.to_pickle("D.pkl")
