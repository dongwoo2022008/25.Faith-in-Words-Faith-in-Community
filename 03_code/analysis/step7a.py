import pandas as pd, numpy as np, json, warnings; warnings.filterwarnings("ignore")
import statsmodels.formula.api as smf

def robust_fit(model, groups=None, maxiter=100):
    kw=dict(cov_type='cluster',cov_kwds={'groups':groups}) if groups is not None else {}
    m=model.fit(method='newton',maxiter=maxiter,disp=0,**kw)
    if not m.mle_retvals.get('converged',False):
        m2=model.fit(method='bfgs',start_params=m.params,maxiter=2000,disp=0,**kw)
        m2.mle_retvals['refit']='bfgs'; m2.mle_retvals['grad_norm']=float(np.abs(m2.model.score(m2.params)).max())
        return m2
    return m

p=pd.read_csv("/mnt/user-data/uploads/P2P대출/Prosper/prosperLoanData.csv/prosperLoanData.csv", low_memory=False)
p=p[p.LoanStatus.isin(['Completed','Chargedoff','Defaulted'])].copy(); p['default']=p.LoanStatus.isin(['Chargedoff','Defaulted']).astype(int)
p['clergy']=p.Occupation.isin(['Clergy','Religious']); p['teacher']=(p.Occupation=='Teacher').astype(int); p['police']=(p.Occupation=='Police Officer/Correction Officer').astype(int); p['nurse']=(p.Occupation=='Nurse (RN)').astype(int)
p['yr']=pd.to_datetime(p.LoanOriginationDate).dt.year.astype(str); p['era2']=(pd.to_datetime(p.LoanOriginationDate)>='2009-07-01').astype(int)
p['rating']=p['ProsperRating (Alpha)'].fillna(p['CreditGrade']).fillna('NA'); p['score']=(p.CreditScoreRangeLower+p.CreditScoreRangeUpper)/200
p['linc']=np.log1p(p.StatedMonthlyIncome.fillna(0)); p['lamt']=np.log(p.LoanOriginalAmount); p['dti']=p.DebtToIncomeRatio; p['emp']=p.EmploymentStatus.fillna('na'); p['own']=p.IsBorrowerHomeowner.astype(int); p['verif']=p.IncomeVerifiable.astype(int); p['st']=p.BorrowerState.fillna('na')
p=p.dropna(subset=['score','dti','BorrowerRate'])
print("Prosper terminal n",len(p),"clergy",int(p.clergy.sum()),"raw default clergy/other",p[p.clergy].default.mean().round(4),p[~p.clergy].default.mean().round(4))
ctrl="C(rating) + C(yr) + BorrowerRate + score + linc + dti + C(Term) + lamt + C(emp) + own + verif + C(st)"
res={}
for lab,f in [('H1_prosper',f"default ~ clergy + {ctrl}"),('H1_prosper_placebo',f"default ~ clergy + teacher + police + nurse + {ctrl}")]:
    m=robust_fit(smf.logit(f,data=p), pd.factorize(p['st'])[0])
    r={'n':int(m.nobs),'converged':bool(m.mle_retvals.get('converged')),'clergy':dict(OR=float(np.exp(m.params['clergy[T.True]'])),p=float(m.pvalues['clergy[T.True]']),n=int(p.clergy.sum()))}
    for o in ['teacher','police','nurse']:
        if o in m.params: r[o]=dict(OR=float(np.exp(m.params[o])),p=float(m.pvalues[o]),n=int(p[o].sum()))
    res[lab]=r; print(lab,r)
# by era
for e in [0,1]:
    s=p[p.era2==e]; m=robust_fit(smf.logit(f"default ~ clergy + C(rating) + C(yr) + BorrowerRate + score + linc + dti + C(Term) + lamt + C(emp) + own + verif",data=s), None)
    res[f'era{e}']=dict(n=int(m.nobs),n_clergy=int(s.clergy.sum()),OR=float(np.exp(m.params['clergy[T.True]'])),p=float(m.pvalues['clergy[T.True]'])); print('era',e,res[f'era{e}'])
json.dump(res,open("out/step7a_prosper.json","w"),indent=1)
pd.DataFrame([dict(model=k,**{kk:(vv if not isinstance(vv,dict) else vv.get('OR')) for kk,vv in v.items()}) for k,v in res.items()]).to_csv("out/표7_Prosper_H1.csv",index=False)
