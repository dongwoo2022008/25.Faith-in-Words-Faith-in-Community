# Affiliation-indicator precision (200-title audit) and robustness excluding Louisiana civil-parish titles
import pandas as pd, numpy as np, json, warnings; warnings.filterwarnings("ignore")
import statsmodels.formula.api as smf
res={}
c=pd.read_csv("/tmp/claude-0/-home-claude/6fc5949e-7a7e-5a39-a0ca-18d9d5045a2b/scratchpad/aff_sample200_coded.csv")
cnt=c.code.value_counts().to_dict(); res['audit_counts']=cnt; res['precision_strict']=(cnt.get('A',0)+cnt.get('B',0))/len(c); res['precision_if_D_half']=(cnt.get('A',0)+cnt.get('B',0)+0.5*cnt.get('D',0))/len(c)
res['C_rows']=c[c.code=='C'][['emp_title','note']].to_dict('records'); res['D_rows']=c[c.code=='D'][['emp_title','note']].to_dict('records')
print(cnt,res['precision_strict'])
T=pd.read_pickle("T.pkl"); et=T.emp_title.fillna('').str.lower()
civil=T.clergy & et.str.contains(r"\bparish\b") & et.str.contains(r"sheriff|library|government|police jury|assessor|school board|clerk of court|jail|fire|council|hospital|anesthesia|consultants|juror|public works|coroner|utilities|water|housing|court", regex=True)
res['civil_parish_titles']=dict(n=int(civil.sum()),n_LA=int((civil&(T.addr_state=='LA')).sum()),default_rate=float(T[civil].default.mean()),examples=T[civil].emp_title.head(15).tolist())
print(res['civil_parish_titles'])
T2=T[~civil].copy(); TS=pd.concat([T2[T2.clergy], T2[~T2.clergy].sample(250000,random_state=1)]).reset_index(drop=True)
ctrl="C(grade) + C(yr) + int + fico + linc + dti + term60 + lamt + C(emp) + C(home) + C(ver) + C(purp) + C(st)"
m=smf.logit(f"default ~ clergy + {ctrl}",data=TS).fit(method='newton',maxiter=100,disp=0,cov_type='cluster',cov_kwds={'groups':pd.factorize(TS['st'])[0]})
k='clergy[T.True]'; res['H1_excluding_civil_parish']=dict(OR=float(np.exp(m.params[k])),se=float(m.bse[k]),p=float(m.pvalues[k]),n_treated=int(TS.clergy.sum()))
print(res['H1_excluding_civil_parish']); json.dump(res,open("out/stepH_precision.json","w"),indent=1); print("DONE")
