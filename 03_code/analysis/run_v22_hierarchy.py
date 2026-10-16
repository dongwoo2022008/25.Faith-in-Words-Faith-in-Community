# Table 10 exploratory rows re-estimated with a documented rule (16 October 2026, sixth check). The original script
# (stepR_review_extras) was lost; its counts (497 / 253 / 2,355) could not be reproduced from the job titles, so the
# manuscript now reports this run. Rule on the lower-cased job title of affiliated borrowers: "associate" group if the
# title contains associate/assoc/youth/assistant/asst; otherwise "senior" group if it contains senior/sr/lead/executive;
# otherwise "other affiliated". Specification of Table 2, column (1) with the three indicators in place of affiliation.
import pandas as pd, numpy as np, json, warnings, time, os; warnings.filterwarnings("ignore")
import statsmodels.formula.api as smf
os.chdir(os.path.dirname(os.path.abspath(__file__)))
T=pd.read_pickle("T.pkl"); T['id']=T['id'].astype(str)
A=pd.read_pickle("A_aff.pkl")   # affiliated loans with emp_title (built by make_table1.py / the same raw-file join)
t=A.emp_title.fillna('').str.lower()
asc=t.str.contains(r"\b(?:associate|assoc|youth|assistant|asst)\b",regex=True)
sen=t.str.contains(r"\b(?:senior|sr|lead|executive)\b",regex=True)&~asc
lab=pd.Series(np.where(asc,'assoc',np.where(sen,'senior','other')),index=A['id'].values)
T['hier']=T['id'].map(lab).fillna('none')
TS=pd.concat([T[T.clergy], T[~T.clergy].sample(250000, random_state=1)]).copy()
for k in ['senior','assoc','other']: TS[k]=(TS.hier==k).astype(int)
ctrl="C(grade) + C(yr) + int + fico + linc + dti + term60 + lamt + C(emp) + C(home) + C(ver) + C(purp) + C(st)"
t0=time.time(); kw=dict(cov_type='cluster',cov_kwds={'groups':pd.factorize(TS['st'])[0]}); model=smf.logit(f"default ~ senior + assoc + other + {ctrl}", data=TS)
m=model.fit(method='newton',maxiter=100,disp=0,**kw)
if not m.mle_retvals.get('converged',False): m=model.fit(method='bfgs',start_params=m.params,maxiter=2000,disp=0,**kw)   # same fallback as run_v19_extras.py
res={'rule':'assoc if title has associate/assoc/youth/assistant/asst; else senior if senior/sr/lead/executive; else other affiliated',
     'converged':bool(m.mle_retvals.get('converged')),'n':int(m.nobs),'sec':round(time.time()-t0)}
for k in ['senior','assoc','other']:
    res[k]=dict(n=int(TS[k].sum()), raw_default=round(float(TS[TS[k]==1].default.mean()),4), OR=float(np.exp(m.params[k])), se=float(m.bse[k]), p=float(m.pvalues[k]))
print(json.dumps(res,indent=1)); json.dump(res,open("v22_hierarchy.json","w"),indent=1)
