# v19 additions (16 October 2026), all on the rebuilt T.pkl/D.pkl (rebuild_TD.py) plus three raw-file columns:
# (a) Table 2 column (4): SE and AME of the affiliation coefficient with the eight stable-occupation indicators
#     (step1.py keyword rules, step3.py specification); (b) Table 2 column (5): AME on the entropy-balanced
#     sample (step5c.py reproduced); (c) Appendix Table C7 rows 1-4 recomputed, first with the sub-grade x year
#     cells of stepC_economic.json (reproduction check) and then with sub-grade x year x term cells.
import pandas as pd, numpy as np, json, warnings, time, re; warnings.filterwarnings("ignore")
import statsmodels.formula.api as smf
RAW="/mnt/attach/outputs/25_FaithInWords/04_데이터/원데이터/LendingClub/accepted_2007_to_2018Q4.csv.gz"
T=pd.read_pickle("T.pkl"); D=pd.read_pickle("D.pkl")
ex=pd.concat([c for c in pd.read_csv(RAW, usecols=['id','emp_title','total_pymnt','last_pymnt_d'], chunksize=300000, low_memory=False, dtype={'id':str})])
ex=ex.drop_duplicates('id').set_index('id')
T['id']=T['id'].astype(str); T=T.join(ex, on='id')
et=T['emp_title'].fillna('').str.lower().str.strip()
occ={'teacher':r"\bteacher\b|\bprofessor\b|\beducator\b|\binstructor\b",'police':r"\bpolice\b|\bcorrection|\bsheriff\b|\bdeputy\b|\btrooper\b",'fire':r"\bfire ?fighter\b|\bfireman\b|\bfire dept",'military':r"\bus army\b|\bus navy\b|\bair force\b|\bmarine corps\b|\bmilitary\b|\bsoldier\b|\barmy\b|\bnavy\b",'govt':r"\bgovernment\b|\bfederal\b|\bstate of\b|\bcity of\b|\bcounty of\b|\bcounty\b|\bmunicipal",'nurse':r"\bnurse\b|\brn\b|\blpn\b",'postal':r"\busps\b|\bpostal\b|\bpost office\b",'transit':r"\btransit\b|\bmta\b|\bbus driver\b|\bbus operator\b"}
for k,p in occ.items(): T[k]=et.str.contains(p,regex=True).astype(int)
res={'occ_counts_T':{k:int(T[k].sum()) for k in occ}}
def robust_fit(model, groups, maxiter=100):
    kw=dict(cov_type='cluster',cov_kwds={'groups':groups})
    m=model.fit(method='newton',maxiter=maxiter,disp=0,**kw)
    if not m.mle_retvals.get('converged',False):
        m=model.fit(method='bfgs',start_params=m.params,maxiter=2000,disp=0,**kw)
    return m
def fit(formula, data, var):
    t=time.time(); m=robust_fit(smf.logit(formula, data=data), pd.factorize(data['st'])[0])
    key=[i for i in m.params.index if i.startswith(var)][0]
    X=m.model.exog.copy(); j=list(m.model.exog_names).index(key)
    X[:,j]=1; p1=m.model.cdf(X@m.params.values); X[:,j]=0; p0=m.model.cdf(X@m.params.values); ame=float(np.mean(p1-p0)); del X
    r=dict(n=int(m.nobs), coef=float(m.params[key]), se=float(m.bse[key]), p=float(m.pvalues[key]), OR=float(np.exp(m.params[key])), AME=float(ame), converged=bool(m.mle_retvals.get('converged',None)), sec=round(time.time()-t))
    print(var, {k:(round(v,4) if isinstance(v,float) else v) for k,v in r.items()}, flush=True); return r,m
ctrl="C(grade) + C(yr) + int + fico + linc + dti + term60 + lamt + C(emp) + C(home) + C(ver) + C(purp) + C(st)"
TS=pd.concat([T[T.clergy], T[~T.clergy].sample(250000, random_state=1)]).copy()
# (a) column (4)
occs=list(occ)
res['T2_col4_stable_ctrl'],ms=fit(f"default ~ clergy + {' + '.join(occs)} + {ctrl}", TS, 'clergy')   # target OR 0.690
res['T2_col4_occ_ORs']={o:float(np.exp(ms.params[o])) for o in occs}
# (b) column (5): entropy balancing exactly as step5c.py, then AME on the weighted-resample logit
tr=TS.clergy.values.astype(bool)
num=['int','fico','linc','dti','lamt']; cat=['grade','yr','home','ver','emp','st']
X=pd.get_dummies(TS[cat].astype(str),drop_first=True).astype(float)
for c in num: X[c]=TS[c].astype(float); X[c+'_sq']=TS[c].astype(float)**2
X['term60']=TS.term60.astype(float)
keep=[c for c in X.columns if X.loc[tr,c].std()>0 and X.loc[~tr,c].std()>0 and X.loc[tr,c].mean()>0.002 and X.loc[tr,c].mean()<0.998]
X=X[keep]; Xc=X[~tr].values; Xt=X[tr].values
q,r,piv=__import__('scipy').linalg.qr(Xc-Xc.mean(0), mode='economic', pivoting=True); rank=(np.abs(np.diag(r))>1e-8*abs(r[0,0])).sum(); cols=np.sort(piv[:rank]); X=X.iloc[:,cols]; Xc=X[~tr].values; Xt=X[tr].values
target=Xt.mean(0); sd=Xc.std(0); Zc=(Xc-target)/sd
l=np.zeros(Zc.shape[1])
for it in range(200):
    a=Zc@l; a-=a.max(); w=np.exp(a); w/=w.sum()
    g=Zc.T@w; H=(Zc*w[:,None]).T@Zc - np.outer(g,g)
    step=np.linalg.solve(H+1e-8*np.eye(len(l)), g)
    f0=np.log(np.exp(Zc@l - (Zc@l).max()).sum())+(Zc@l).max(); t=1.0
    while True:
        ln=l-t*step; fn=np.log(np.exp(Zc@ln-(Zc@ln).max()).sum())+(Zc@ln).max()
        if fn<=f0-1e-4*t*g@step or t<1e-6: break
        t*=0.5
    l=ln
    if np.abs(g).max()<1e-7: break
a=Zc@l; w=np.exp(a-a.max()); w/=w.sum()
rng=np.random.default_rng(0); ci=np.where(~tr)[0]; draw=rng.choice(ci,size=len(ci),replace=True,p=w); RS=pd.concat([TS[tr],TS.iloc[draw]])
res['ebal']=dict(n_covariates=int(X.shape[1]), ess_control=float(1/np.sum(w**2)), weighted_default_control=float(np.average(TS[~tr].default.values,weights=w)))
res['T2_col5_ebal'],_=fit(f"default ~ clergy + {ctrl}", RS, 'clergy')   # target OR 0.697, SE 0.043
# (c) Appendix Table C7 rows 1-4. Definition that reproduces stepC_economic.json exactly: net loss = default x
#     (1 - total_pymnt / funded_amnt), i.e. zero for repaid loans; "mean life" = mean contractual term of the flagged loans.
T['netloss']=T.default*(1-T['total_pymnt']/T['funded_amnt']); T['termm']=36+24*T.term60
T['life']=(pd.to_datetime(T['last_pymnt_d'],format='%b-%Y')-pd.to_datetime(T['issue_d'],format='%b-%Y')).dt.days/30.4375
D['id']=D['id'].astype(str); D=D.join(T.set_index('id')[['netloss','termm','life']], on='id')
def cellcomp(frame, flag, keys):
    f=frame[flag]; cm=frame.groupby(keys).agg(d=('default','mean'), nl=('netloss','mean'))
    fk=f.groupby(keys).size(); fk=fk/fk.sum(); cm=cm.loc[fk.index]
    d_cell=float((cm.d*fk).sum()); nl_cell=float((cm.nl*fk).sum()); term=float(f.termm.mean()); life=float(f.life.mean())
    gap=100*(f.netloss.mean()-nl_cell)
    return dict(n=int(len(f)), default=round(float(f.default.mean()),5), default_cellmatched=round(d_cell,5), netloss_cents=round(100*float(f.netloss.mean()),3), netloss_cellmatched_cents=round(100*nl_cell,3), loss_gap_cents=round(float(gap),3), mean_term_months=round(term,2), mean_realized_life_months=round(life,2), annualized_bp_by_term=round(float(100*gap/(term/12)),1), annualized_bp_by_realized_life=round(float(100*gap/(life/12)),1), n_cells=int(len(fk)))
cells={}
for keys,lab in [(['sub_grade','year'],'subgrade_year'),(['sub_grade','year','term'],'subgrade_year_term')]:
    cells[f'affiliation_{lab}']=cellcomp(T, T.clergy.values.astype(bool), keys)
    cells[f'religious_{lab}']=cellcomp(D, D.relig_strict.values.astype(bool), keys)
    print(lab, cells[f'affiliation_{lab}'], cells[f'religious_{lab}'], flush=True)
res['C7_cells_v19']=cells
res['netloss_definition']='default x (1 - total_pymnt/funded_amnt), i.e. zero for repaid loans; reproduces stepC_economic.json exactly with sub_grade x year cells; mean_term_months = mean contractual term (36 + 24 x term60) of the flagged loans, which is what stepC called mean_term_months'
json.dump(res, open("v19_extras.json","w"), indent=1, default=float); print("done")
