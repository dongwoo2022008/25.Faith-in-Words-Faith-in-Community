import pandas as pd, numpy as np, json, glob, warnings; warnings.filterwarnings("ignore")
from sklearn.metrics import cohen_kappa_score
import statsmodels.formula.api as smf
res={}
for name,idc in [("lc","loan_id"),("pf","listing_id")]:
    base=pd.read_pickle(f"coding/{name}.pkl"); base[idc]=base[idc].astype(str)
    coded=pd.concat([pd.read_json(f,lines=True) for f in sorted(glob.glob(f"coding/{name}_batch*_coded.jsonl"))]); coded['id']=coded['id'].astype(str)
    m=base.merge(coded,left_on=idc,right_on='id',how='left'); assert m.type.notna().all() and len(m)==len(base) and m.id.is_unique
    auto_t=m.auto_type_1st.str[0].str.lower().replace({'검':'a'})  # '검토필요' -> treat as 'a'?? no: keep separate
    auto_t=m.auto_type_1st.map(lambda s: 'a' if s.startswith('a') else ('b' if s.startswith('b') else ('c' if s.startswith('c') else 'u')))
    auto_f=m.auto_frame_1st.fillna('종교').replace({'':'종교'})
    k_type=cohen_kappa_score(auto_t, m.type); k_type_rel=cohen_kappa_score(auto_t[m.type!='x'], m.type[m.type!='x'])
    k_frame=cohen_kappa_score(auto_f, m.frame)
    res[name]=dict(n=len(m), llm_type_dist=m.type.value_counts().to_dict(), llm_frame_dist=m.frame.value_counts().to_dict(), auto_type_dist=auto_t.value_counts().to_dict(), kappa_type_rule_vs_llm=float(k_type), kappa_type_excl_x=float(k_type_rel), kappa_frame_rule_vs_llm=float(k_frame), false_positive_rate_x=float((m.type=='x').mean()))
    print(name, {k:(round(v,3) if isinstance(v,float) else v) for k,v in res[name].items()})
    m.to_csv(f"out/코딩결과_{name}.csv",index=False)
# H2 re-estimation with validated indicator and by subtype (LC)
lc=pd.read_csv("out/코딩결과_lc.csv"); lc['loan_id']=lc.loan_id.astype(int)
D=pd.read_pickle("D.pkl"); D['loan_id']=pd.to_numeric(D.id,errors='coerce').astype('Int64')
D=D.merge(lc[['loan_id','type','frame']],on='loan_id',how='left')
D['relig_valid']=(D.relig_strict & D.type.isin(['a','b','c'])).astype(int); D['relig_x']=(D.relig_strict & (D.type=='x')).astype(int)
for t_ in ['a','b','c']: D[f'rel_{t_}']=(D.relig_strict & (D.type==t_)).astype(int)
print("validated relig n",int(D.relig_valid.sum()),"x n",int(D.relig_x.sum()), {t_:int(D[f'rel_{t_}'].sum()) for t_ in 'abc'})
ctrl="C(grade) + C(yr) + int + fico + linc + dti + term60 + lamt + C(emp) + C(home) + C(ver) + C(purp) + C(st) + llen + moral + hardship + gratitude + family + help + business"
G=pd.factorize(D['st'])[0]
def fit(f,keys):
    m=smf.logit(f,data=D).fit(method='newton',maxiter=100,disp=0,cov_type='cluster',cov_kwds={'groups':G})
    if not m.mle_retvals.get('converged'): m=smf.logit(f,data=D).fit(method='bfgs',start_params=m.params,maxiter=2000,disp=0,cov_type='cluster',cov_kwds={'groups':G})
    return {k:dict(OR=float(np.exp(m.params[k])),p=float(m.pvalues[k]),n=int(D[k].sum())) for k in keys}
res['H2_validated']=fit(f"default ~ relig_valid + relig_x + {ctrl}",['relig_valid','relig_x']); print("H2 validated/x:",res['H2_validated'])
res['H2_subtypes']=fit(f"default ~ rel_a + rel_b + rel_c + relig_x + {ctrl}",['rel_a','rel_b','rel_c']); print("H2 subtypes:",res['H2_subtypes'])
raw=D[D.relig_strict].groupby('type').default.agg(['size','mean']); print(raw); res['raw_default_by_type']=raw.to_dict()
json.dump(res,open("out/step7_coding.json","w"),indent=1,default=str)
