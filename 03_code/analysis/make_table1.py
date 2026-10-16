# Descriptive statistics and sample counts quoted in the manuscript but not produced by any step script
# (added 16 October 2026 after the sixth check). Runs on the rebuilt T.pkl / D.pkl (rebuild_TD.py) plus
# three raw-file columns (emp_title, zip_code, plus Prosper for Table 5). Output: descriptive_statistics.json
# and descriptive_statistics_table1.csv. Every entry names the manuscript location it supports.
import pandas as pd, numpy as np, json, re, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
RAW="/mnt/attach/outputs/25_FaithInWords/04_데이터/원데이터/LendingClub/accepted_2007_to_2018Q4.csv.gz"
PROSPER="/mnt/attach/outputs/25_FaithInWords/04_데이터/원데이터/Prosper/prosperLoanData.csv"
ZCTA="/mnt/attach/outputs/25_FaithInWords/04_데이터/외부자료/zcta_county_rel_10.txt"
T=pd.read_pickle("T.pkl"); D=pd.read_pickle("D.pkl"); out={}
# --- raw columns: emp_title and zip_code by id; affiliation count in the full file (Section 3.2: 5,014)
role_re=r"\bpastor\b|\bminister\b|\bministry\b|\bclergy\b|\bpriest\b|\bchaplain\b|\brabbi\b|\bmissionar|\breverend\b|\bevangelist\b|\bdeacon\b|\bworship\b|\bimam\b|\bseminar(y|ian)\b"
org_re=r"\bchurch\b|\bparish\b|\bdiocese\b|\bcongregation\b|\bsynagogue\b|\bmosque\b"
inst_re=r"hospital|health|medical|charit|university|college|school|academy|insurance|bank|credit union|hospice|clinic|services inc|mutual"
parts=[]; n_full=0; n_aff_full=0
for ch in pd.read_csv(RAW, usecols=['id','emp_title','zip_code'], chunksize=300000, low_memory=False, dtype={'id':str}):
    ch=ch[ch['id'].notna()]; n_full+=len(ch)
    et=ch['emp_title'].fillna('').str.lower().str.strip()
    aff=et.str.contains(role_re,regex=True)|(et.str.contains(org_re,regex=True)&~et.str.contains(inst_re,regex=True))
    n_aff_full+=int(aff.sum()); parts.append(ch)
ex=pd.concat(parts).drop_duplicates('id').set_index('id'); del parts
out['full_file']=dict(loans=n_full, affiliated=n_aff_full, note="Section 3.2: 5,014 affiliated loans in the full file; Appendix Table B3 row 4")
T['id']=T['id'].astype(str); T=T.join(ex,on='id'); D['id']=D['id'].astype(str); D=D.join(ex[['zip_code']],on='id')
# --- Table 1
def row(df):
    return dict(N=int(len(df)), default_rate=round(float(df.default.mean()),3), fico_mean=round(float(df.fico.mean()),1), income_median=float(df.annual_inc.median()),
                dti_mean=round(float(df.dti.mean()),1), rate_mean=round(float(df['int'].mean()),2), amount_mean=round(float(df.loan_amnt.mean()),0),
                share_60month=round(float(df.term60.mean()),3), share_grade_AB=round(float(df.grade.isin(['A','B']).mean()),3),
                defaults=int(df.default.sum()), fico_mean_exact=float(df.fico.mean()), amount_mean_exact=float(df.loan_amnt.mean()), share_grade_AB_exact=float(df.grade.isin(['A','B']).mean()), dti_mean_exact=float(df.dti.mean()), rate_mean_exact=float(df['int'].mean()))
et=T['emp_title'].fillna('').str.lower().str.strip(); T['role']=et.str.contains(role_re,regex=True)
groups={'Religious-institution affiliation':T[T.clergy], '- clergy role':T[T.clergy&T.role], '- church staff (non-clergy)':T[T.clergy&~T.role],
        'All other borrowers':T[~T.clergy], 'All terminated loans':T,
        'Religious language (description sample)':D[D.relig_strict], 'Other descriptions':D[~D.relig_strict], 'All descriptions':D}
t1=pd.DataFrame({k:row(v) for k,v in groups.items()}).T; t1.index.name='group'; t1.to_csv("descriptive_statistics_table1.csv")
out['table1']=t1.to_dict(orient='index'); print(t1)
# --- Section 3.3 and Table 1 notes: description length and dictionary shares, religious vs other descriptions
r=D[D.relig_strict]; o=D[~D.relig_strict]
out['section_3_3']=dict(median_words=[float(r.desc_len.median()),float(o.desc_len.median())], mean_words=[round(float(r.desc_len.mean()),1),round(float(o.desc_len.mean()),1)],
    shares={k:[round(float(r[k].mean()),3),round(float(o[k].mean()),3)] for k in ['moral','hardship','gratitude','family','help','business']},
    note="Section 3.3 (median 68 vs 23 words; shares) and Table 1 notes (mean words 116 vs 36; shares)")
# --- Section 3.2 counts: dictionary matches in the analysis sample, both indicators in the description sample
out['section_3_2']=dict(relig_matches_analysis_sample=int(T.relig_strict.sum()), relig_matches_description_sample=int(D.relig_strict.sum()),
    affiliated_in_description_sample=int(D.clergy.sum()), both_in_description_sample=int((D.clergy&D.relig_strict).sum()),
    note="Section 3.2: 784 matches in the analysis sample; 372 affiliated and 681 religious-language loans in the description sample, 20 both; Appendix Table B3")
# --- Section 5.4: affiliated titles that name a specific institution (Table 10 paragraph: 606)
A=T[T.clergy].copy(); A.to_pickle("A_aff.pkl")   # affiliated loans with emp_title, read by run_v22_hierarchy.py
at=A['emp_title'].fillna('').str.strip()
org=at.str.lower().str.contains(org_re,regex=True)
# a title "names" an institution when it contains an organization word together with at least one further capitalized or
# proper-name token beyond the role words (e.g. "First Baptist Church", "St. Thomas Episcopal Church"); bare role phrases
# ("pastor", "church secretary", "director of music ministry") do not.
generic=set("church churches parish diocese congregation synagogue mosque pastor senior lead executive associate assistant youth minister ministry ministries clergy priest chaplain rabbi missionary reverend evangelist deacon worship imam seminary director of the and music administrator administrative secretary staff manager office coordinator assoc asst sr jr head leader employee worker teacher a an at for in".split())
def names_institution(s):
    toks=re.findall(r"[A-Za-z][A-Za-z.'&-]*", s)
    if not toks: return False
    low=[t.lower().strip(".'&-") for t in toks]
    if not any(re.fullmatch(org_re.replace('\\b',''),w) or re.search(org_re,w) for w in low): return False
    extra=[t for t,l in zip(toks,low) if l not in generic and len(l)>1]
    return len(extra)>=1
named=at.map(names_institution)
vc=at[named].str.lower().value_counts()
out['section_5_4_named_institution']=dict(n_named=int(named.sum()), distinct_strings=int(vc.shape[0]), repeated_strings=int((vc>=2).sum()), loans_in_repeated=int(vc[vc>=2].sum()),
    top=vc.head(5).to_dict(), rule="organization word plus at least one non-generic token (see names_institution)",
    note="Section 5.4 (manuscript v22: 583 of 3,105 titles name a specific institution, 497 distinct strings, 46 repeated). The mechanism plan of 20 September 2026 recorded 606 / 509 / 50 under a rule that was not preserved; from v22 the manuscript reports this reproducible count.")
# --- Table 10 exploratory split: see run_v22_hierarchy.py / v22_hierarchy.json
# --- Table 11 N: loans whose ZIP3 area has 2010 U.S. Religion Census coverage (ZCTA-county relationship file)
rel=pd.read_csv(ZCTA, dtype={'ZCTA5':str,'GEOID':str}); z3=set(rel.ZCTA5.str[:3].unique())
TS=pd.concat([T[T.clergy], T[~T.clergy].sample(250000, random_state=1)])
tz=TS.zip_code.fillna('').str[:3]; dz=D.zip_code.fillna('').str[:3]
out['table11_n']=dict(zip3_areas_in_relationship_file=len(z3), H1_sample_matched=int(tz.isin(z3).sum()), H1_sample=int(len(TS)), description_sample_matched=int(dz.isin(z3).sum()), description_sample=int(len(D)),
    share_all_terminated_matched=round(float(T.zip_code.fillna('').str[:3].isin(z3).mean()),5),
    note="Table 11 rows 1 and 8 (N = 253,038 and 123,260) and Section 3.4 (894 areas, 99.97 percent of loans)")
# --- Table 5: Prosper raw default rates
p=pd.read_csv(PROSPER, low_memory=False); p=p[p.LoanStatus.isin(['Completed','Chargedoff','Defaulted'])].copy()
p['default']=p.LoanStatus.isin(['Chargedoff','Defaulted']).astype(int); p['clergy']=p.Occupation.isin(['Clergy','Religious'])
p['score']=(p.CreditScoreRangeLower+p.CreditScoreRangeUpper)/200; p=p.dropna(subset=['score','DebtToIncomeRatio','BorrowerRate'])
out['table5_prosper_raw']=dict(n=int(len(p)), n_clergy=int(p.clergy.sum()), default_clergy=round(float(p[p.clergy].default.mean()),3), default_other=round(float(p[~p.clergy].default.mean()),3), note="Table 5 notes: raw default 22.7% vs 30.5%")
json.dump(out, open("descriptive_statistics.json","w"), indent=1, default=float, ensure_ascii=False)
print(json.dumps({k:v for k,v in out.items() if k!='table1'}, indent=1, default=float, ensure_ascii=False))
