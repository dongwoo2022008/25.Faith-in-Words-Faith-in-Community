# Nearest-neighbour occupation design: religious-institution affiliation vs nonprofit / social-service / education / healthcare workers
import pandas as pd, numpy as np, json, warnings, time; warnings.filterwarnings("ignore")
import statsmodels.formula.api as smf
exec(open("step2.py").read().split("import statsmodels.api as sm")[0])  # robust_fit
T=pd.read_pickle("T.pkl")
et=T['emp_title'].fillna('').str.lower().str.strip()
nonprofit=et.str.contains(r"non-?\s?profit|social work|social service|human services|case manager|caseworker|counsel(or|er)|charit|foundation|ymca|ywca|community (center|action|service|outreach|develop)|habitat for humanity|salvation army|red cross|united way|goodwill|outreach|advocate|boys (and|&) girls club|big brothers", regex=True) & ~T.clergy
educ=et.str.contains(r"\bteacher\b|\bprofessor\b|\beducat|\bschool\b|\bprincipal\b|\bteaching\b|\binstructor\b|\bfaculty\b", regex=True) & ~T.clergy
health=et.str.contains(r"\bnurse\b|\brn\b|\blpn\b|\bhospital\b|\bmedical\b|\bhealth|\bphysician\b|\btherapist\b|\bclinic", regex=True) & ~T.clergy
T['nonprofit']=nonprofit; T['educ']=educ; T['health']=health
ctrl="C(grade) + C(yr) + int + fico + linc + dti + term60 + lamt + C(emp) + C(home) + C(ver) + C(purp) + C(st)"
res=dict(n_nonprofit=int(nonprofit.sum()), n_educ=int(educ.sum()), n_health=int(health.sum()), n_aff=int(T.clergy.sum()),
         raw_default=dict(aff=float(T.default[T.clergy].mean()), nonprofit=float(T.default[nonprofit].mean()), educ=float(T.default[educ].mean()), health=float(T.default[health].mean()), other=float(T.default[~(T.clergy|nonprofit|educ|health)].mean())))
print(res)
ex=T.loc[nonprofit,'emp_title'].value_counts().head(25); print(ex); res['nonprofit_top_titles']=ex.to_dict()
def fit(data, var, label, extra=""):
    t=time.time(); m=robust_fit(smf.logit(f"default ~ {var} + {ctrl}{extra}", data=data), pd.factorize(data['st'])[0])
    k=[i for i in m.params.index if i.startswith(var)][0]
    r=dict(OR=float(np.exp(m.params[k])), se=float(m.bse[k]), p=float(m.pvalues[k]), n=int(m.nobs), n_treated=int(data[var].sum()), converged=bool(m.mle_retvals.get('converged')), sec=round(time.time()-t))
    print(label, r, flush=True); return r
# (a) each neighbour group vs the general population (does the 'helping/mission-driven occupation' show the same effect?)
rng=np.random.RandomState(7); base=T[~(T.clergy|nonprofit|educ|health)].sample(250000, random_state=7)
for g in ['nonprofit','educ','health']:
    S=pd.concat([T[T[g]], base]).copy(); S[g]=S[g].astype(int); res[f'{g}_vs_general']=fit(S,g,f'{g} vs general')
# (b) affiliation with the neighbour occupations as the ONLY comparison group
for g,name in [('nonprofit','nonprofit/social-service'),('educ','education'),('health','healthcare')]:
    S=pd.concat([T[T.clergy], T[T[g]]]).copy(); S['aff']=S.clergy.astype(int); res[f'aff_vs_{g}_only']=fit(S,'aff',f'affiliation vs {name} only')
S=pd.concat([T[T.clergy], T[nonprofit|educ|health]]).copy(); S['aff']=S.clergy.astype(int); res['aff_vs_all_neighbours']=fit(S,'aff','affiliation vs nonprofit+educ+health')
# (c) coarsened exact matching inside the neighbour pool: grade x year x FICO(20) x income quartile x emp_length x home x term
P=pd.concat([T[T.clergy], T[nonprofit|educ|health]]).copy(); P['aff']=P.clergy.astype(int)
P['fb']=(P.fico//20).astype(int); P['ib']=pd.qcut(P.linc,4,labels=False,duplicates='drop'); P['key']=P[['grade','yr','fb','ib','emp','home','term60']].astype(str).agg('|'.join,axis=1)
c=P.groupby('key').aff.agg(['sum','count']); ok=c[(c['sum']>0)&(c['count']>c['sum'])].index; Q=P[P.key.isin(ok)].copy()
w=Q.groupby('key').aff.transform(lambda a: np.where(a==1,1.0,(a.sum()/(len(a)-a.sum()))))
Q['w']=w*np.where(Q.aff==1,1.0,(Q.aff==0).sum()/w[Q.aff==0].sum())
m=smf.glm(f"default ~ aff + {ctrl}", data=Q, family=__import__('statsmodels.api').api.families.Binomial(), freq_weights=Q.w).fit(cov_type='cluster',cov_kwds={'groups':pd.factorize(Q['st'])[0]})
res['CEM_within_neighbour_pool']=dict(OR=float(np.exp(m.params['aff'])), p=float(m.pvalues['aff']), n_aff=int(Q.aff.sum()), n_ctrl=int((Q.aff==0).sum()), strata=int(len(ok)))
print('CEM neighbour pool', res['CEM_within_neighbour_pool'])
json.dump(res,open("out/stepN_neighbour.json","w"),indent=1); print("DONE")
