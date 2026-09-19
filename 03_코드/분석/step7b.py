import pandas as pd, numpy as np, json, warnings; warnings.filterwarnings("ignore")
import statsmodels.formula.api as smf
D=pd.read_pickle("D.pkl")
ex=pd.concat([c for c in pd.read_csv("/mnt/user-data/uploads/Lending Club/accepted_2007_to_2018Q4.csv.gz", usecols=['id','initial_list_status','funded_amnt','funded_amnt_inv','loan_amnt'], chunksize=400000, low_memory=False)])
ex['id']=pd.to_numeric(ex.id,errors='coerce'); ex=ex.dropna(subset=['id']); ex['id']=ex.id.astype(int)
D['id']=pd.to_numeric(D.id,errors='coerce').astype('Int64')
m=D.merge(ex[['id','initial_list_status','funded_amnt_inv']].rename(columns={'funded_amnt_inv':'fai'}),on='id',how='left')
m['inv_share']=m.fai/m.funded_amnt; m['full_inv']=(m.inv_share>=0.999).astype(int); m['exec_ratio']=m.funded_amnt/m.loan_amnt; m['ils']=m.initial_list_status.fillna('na')
print("n",len(m),"inv_share mean",m.inv_share.mean().round(4),"full_inv rate",m.full_inv.mean().round(4),"exec<1 rate",(m.exec_ratio<0.999).mean().round(4))
print(m.groupby('relig_strict')[['inv_share','full_inv','exec_ratio']].mean().round(4))
ctrl="C(grade) + C(yr) + int + fico + linc + dti + term60 + lamt + C(emp) + C(home) + C(ver) + C(purp) + C(st) + llen + moral + hardship + gratitude + family + help + business + C(ils)"
res={}
for sub,lab in [(m,'all_2008_2014'),(m[m.year<=2012],'2008_2012')]:
    G=pd.factorize(sub['st'])[0]
    a=smf.ols(f"inv_share ~ relig_strict + {ctrl}",data=sub).fit(cov_type='cluster',cov_kwds={'groups':G})
    b=smf.logit(f"full_inv ~ relig_strict + {ctrl}",data=sub).fit(method='newton',maxiter=100,disp=0,cov_type='cluster',cov_kwds={'groups':G})
    c=smf.ols(f"exec_ratio ~ relig_strict + {ctrl}",data=sub).fit(cov_type='cluster',cov_kwds={'groups':G})
    res[lab]=dict(n=int(a.nobs), n_relig=int(sub.relig_strict.sum()), inv_share_coef=float(a.params['relig_strict[T.True]']), inv_share_p=float(a.pvalues['relig_strict[T.True]']), full_inv_OR=float(np.exp(b.params['relig_strict[T.True]'])), full_inv_p=float(b.pvalues['relig_strict[T.True]']), exec_ratio_coef=float(c.params['relig_strict[T.True]']), exec_ratio_p=float(c.pvalues['relig_strict[T.True]']))
    print(lab,res[lab])
json.dump(res,open("out/step7b_investor.json","w"),indent=1); pd.DataFrame([dict(sample=k,**v) for k,v in res.items()]).to_csv("out/표8_투자자반응.csv",index=False)
