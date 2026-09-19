import pandas as pd, numpy as np, json, warnings; warnings.filterwarnings("ignore")
import statsmodels.formula.api as smf, statsmodels.api as sm
T=pd.read_pickle("T.pkl"); D=pd.read_pickle("D.pkl")
ex=pd.concat([c for c in pd.read_csv("/mnt/user-data/uploads/Lending Club/accepted_2007_to_2018Q4.csv.gz", usecols=['id','last_pymnt_d','issue_d'], chunksize=400000, low_memory=False)])
ex['id']=pd.to_numeric(ex.id,errors='coerce'); ex=ex.dropna(subset=['id']); ex['id']=ex.id.astype(int)
def build(df, treat, n_ctrl, seed):
    s=pd.concat([df[df[treat]], df[~df[treat]].sample(n_ctrl, random_state=seed)]).copy()
    s['id']=pd.to_numeric(s.id,errors='coerce').astype('Int64'); s=s.drop(columns=['issue_d'],errors='ignore').merge(ex,on='id',how='left')
    lp=pd.to_datetime(s.last_pymnt_d,format='%b-%Y',errors='coerce'); iss=pd.to_datetime(s.issue_d,format='%b-%Y',errors='coerce')
    months=((lp.dt.year-iss.dt.year)*12+(lp.dt.month-iss.dt.month)).fillna(0).clip(lower=0)
    tm=np.where(s.term60==1,60,36)
    # event time: default -> last payment + 4 (charge-off ~120 dpd), capped at term; paid -> last payment month (censored)
    s['tstop']=np.where(s.default==1, np.minimum(months+4, tm), np.maximum(months,1)).astype(int); s['tstop']=s.tstop.clip(lower=1)
    s['tm']=tm
    rows=[]; ids=np.repeat(s.index.values, s.tstop.values); t=np.concatenate([np.arange(1,k+1) for k in s.tstop.values])
    cols=[treat,'default','grade','yr','int','fico','linc','dti','term60','lamt','st','tm']+[c for c in ['llen','moral','hardship','gratitude','family','help','business'] if c in s.columns]; P=s.loc[ids,cols].reset_index(drop=True)
    P['t']=t; P['event']=((P.t==s.loc[ids,'tstop'].values)&(P.default.values==1)).astype(int)
    P['prog']=P.t/P.tm; P['early']=(P.t<=12).astype(int); P['tr']=P[treat].astype(int)
    return s,P
res={}
for lab,df,treat,n,extra in [('H1_clergy',T,'clergy',30000,''),('H2_relig',D,'relig_strict',8000,' + llen + moral + hardship + gratitude + family + help + business')]:
    s,P=build(df,treat,n,1); print(lab,"loans",len(s),"treated",int(s[treat].sum()),"loan-months",len(P),"events",int(P.event.sum()))
    f=f"event ~ tr + prog + I(prog**2) + I(prog**3) + C(yr) + C(grade) + int + fico + linc + dti + term60 + lamt{extra}"
    m=smf.glm(f, data=P, family=sm.families.Binomial(link=sm.families.links.CLogLog())).fit(cov_type='cluster',cov_kwds={'groups':P.index.values//1 if False else pd.factorize(np.repeat(s.index.values, s.tstop.values))[0]})
    f2=f.replace("event ~ tr","event ~ tr:early + tr:I(1-early) + early")
    m2=smf.glm(f2, data=P, family=sm.families.Binomial(link=sm.families.links.CLogLog())).fit(cov_type='cluster',cov_kwds={'groups':pd.factorize(np.repeat(s.index.values, s.tstop.values))[0]})
    import gc; gc.collect()
    r=dict(loans=len(s),treated=int(s[treat].sum()),loan_months=len(P),events=int(P.event.sum()),HR=float(np.exp(m.params['tr'])),p=float(m.pvalues['tr']),HR_early=float(np.exp(m2.params['tr:early'])),p_early=float(m2.pvalues['tr:early']),HR_late=float(np.exp(m2.params['tr:I(1 - early)'])),p_late=float(m2.pvalues['tr:I(1 - early)']))
    print(lab,r); res[lab]=r
res['note']='event time = last_pymnt_d + 4 months (approx. 120-dpd charge-off), capped at term; Fully Paid censored at last payment month; clustered by loan'
json.dump(res,open("out/step6_hazard.json","w"),indent=1); pd.DataFrame([dict(model=k,**v) for k,v in res.items() if isinstance(v,dict)]).to_csv("out/부록A_hazard.csv",index=False)
