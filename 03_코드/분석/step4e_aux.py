# Auxiliary (non-preregistered) H2 analyses: intensity measure, net-loss outcome, MDE/power
import pandas as pd, numpy as np, json, re, warnings, time; warnings.filterwarnings("ignore")
import statsmodels.formula.api as smf
from scipy import stats
exec(open("step2.py").read().split("import statsmodels.api as sm")[0])  # robust_fit
D=pd.read_pickle("D.pkl")
ctrl="C(grade) + C(yr) + int + fico + linc + dti + term60 + lamt + C(emp) + C(home) + C(ver) + C(purp) + C(st)"
txtc="llen + moral + hardship + gratitude + family + help + business"
strict={'god':r"\bgod\b(?! ?father)|\bgod's\b", 'jesus/christ':r"\bjesus\b|\bchrist\b", 'christian':r"\bchristians?\b", 'church':r"\bchurch(es)?\b",
 'pray/prayer':r"\bpray(s|ed|ing|er|ers)?\b", 'bless':r"\bbless(ed|ing|ings)?\b",
 'faith':r"\bfaith\b(?! in (me|us|you|him|her|them|one another|people|the|my|our|this|humanity))(?<!good )(?<!bad )|\bfaithful\b",
 'lord':r"\bthe lord\b|\bpraise the lord\b|\blord bless\b|\blord willing\b|\blord (and|&) savio(u)?r\b|\bgood lord\b|\bhelp me lord\b|\bmy lord\b",
 'bible':r"\bbible\b|\bbiblical\b|\bscripture\b", 'tithe':r"\btith(e|es|ing|er)\b", 'ministry':r"\bministr(y|ies)\b|\bmissionar(y|ies)\b|\bmission trip\b|\bpastor\b|\bcongregation\b|\bclergy\b|\brabbi\b|\bseminary\b",
 'amen':r"\bamen\b", 'religion':r"\breligio(n|us)\b", 'denom':r"\bcatholic\b|\bbaptist\b|\bmethodist\b|\blutheran\b|\bpresbyterian\b|\bmormon\b|\bevangelical\b|\bpentecostal\b",
 'muslim':r"\bmuslim\b|\bislam(ic)?\b|\bmosque\b|\ballah\b", 'jewish':r"\bjewish\b|\bsynagogue\b|\bjudaism\b", 'buddhist':r"\bbuddhis(t|m)\b|\bhindu\b"}
big=re.compile("|".join(f"(?:{p})" for p in strict.values()))
low=(D['title'].fillna('')+' || '+D['desc_c'].fillna('')).str.lower()
D['rtok']=low.apply(lambda s: len(big.findall(s)))
D['nw']=D['desc_len'].clip(lower=1)
D['rshare']=100*D['rtok']/D['nw']          # religious tokens per 100 words
D['lrtok']=np.log1p(D['rtok'])
res={}
chk=dict(n_flag=int(D.relig_strict.sum()), n_rtok_pos=int((D.rtok>0).sum()), agree=int(((D.rtok>0)==D.relig_strict).sum()),
         rtok_dist_flagged=D.loc[D.relig_strict,'rtok'].describe().round(2).to_dict(), rshare_flagged=D.loc[D.relig_strict,'rshare'].describe().round(3).to_dict())
print(chk); res['check']=chk
def fit(formula, var, data=D):
    m=robust_fit(smf.logit(formula, data=data), pd.factorize(data['st'])[0])
    r={k:dict(coef=float(m.params[k]),se=float(m.bse[k]),p=float(m.pvalues[k]),OR=float(np.exp(m.params[k]))) for k in m.params.index if any(k.startswith(v) for v in var)}
    r['n']=int(m.nobs); r['converged']=bool(m.mle_retvals.get('converged')); print(formula[:60], {k:v for k,v in r.items()}); return r
# (1) intensity: log(1+tokens); tokens per 100 words; categories 0/1/2/3+
res['int_lrtok']=fit(f"default ~ lrtok + {ctrl} + {txtc}", ['lrtok'])
res['int_rshare']=fit(f"default ~ rshare + {ctrl} + {txtc}", ['rshare'])
D['rcat']=pd.cut(D.rtok,[-1,0,1,2,99],labels=['0','1','2','3plus'])
res['int_cat']=fit(f"default ~ C(rcat) + {ctrl} + {txtc}", ['C(rcat)'])
# within flagged only: does intensity matter?
res['int_within_flagged']=fit(f"default ~ lrtok + C(grade) + C(yr) + int + fico + linc + dti + term60 + lamt + {txtc}", ['lrtok'], data=D[D.relig_strict])
# (2) net loss outcome
f="/mnt/user-data/uploads/Lending Club/accepted_2007_to_2018Q4.csv.gz"
ex=pd.concat([c for c in pd.read_csv(f, usecols=['id','total_pymnt','funded_amnt'], chunksize=400000, low_memory=False)])
ex['id']=pd.to_numeric(ex.id,errors='coerce'); ex=ex[ex.id.notna()]; ex['id']=ex.id.astype(int)
D['id']=pd.to_numeric(D.id,errors='coerce').astype('Int64')
M=D.merge(ex.rename(columns={'total_pymnt':'tp_ex','funded_amnt':'fa_ex'}),on='id',how='left'); M['netloss']=1-M.tp_ex/M.fa_ex
print("merged",M.netloss.notna().sum(), "netloss mean", M.netloss.mean().round(4), "flag", M.loc[M.relig_strict,'netloss'].mean().round(4), "other", M.loc[~M.relig_strict,'netloss'].mean().round(4))
o=smf.ols(f"netloss ~ relig_strict + {ctrl} + {txtc}", data=M).fit(cov_type='cluster',cov_kwds={'groups':pd.factorize(M['st'])[0]})
k='relig_strict[T.True]'; res['netloss_ols']=dict(coef=float(o.params[k]),se=float(o.bse[k]),p=float(o.pvalues[k]),n=int(o.nobs),mean_netloss=float(M.netloss.mean()))
o2=smf.ols(f"default ~ relig_strict + {ctrl} + {txtc}", data=M).fit(cov_type='cluster',cov_kwds={'groups':pd.factorize(M['st'])[0]})
res['default_lpm_same_spec']=dict(coef=float(o2.params[k]),se=float(o2.bse[k]),p=float(o2.pvalues[k]))
res['netloss_t_ratio_vs_lpm']=float((o.params[k]/o.bse[k])/(o2.params[k]/o2.bse[k]))
print("netloss", res['netloss_ols'], "| LPM default", res['default_lpm_same_spec'])
# (3) MDE / power: two-proportion, one-sided 5%, 80% power; treated n=681, control rate = sample rate
p0=float(D.default.mean()); n1=int(D.relig_strict.sum()); n0=int((~D.relig_strict).sum())
se=np.sqrt(p0*(1-p0)*(1/n1+1/n0)); mde=(stats.norm.ppf(0.95)+stats.norm.ppf(0.80))*se
# power for observed AME range
def power(eff): return float(1-stats.norm.cdf(stats.norm.ppf(0.95)-eff/se))
# regression-adjusted: use clustered SE from Table 3 col 3 LPM (0.035, se from o2)
res['power']=dict(p0=p0,n_treated=n1,n_control=n0,se_raw_diff=float(se),MDE_onesided_80=float(mde),power_at_0_023=power(0.023),power_at_0_031=power(0.031),power_at_0_035=power(0.035),
                  lpm_se_regression=float(o2.bse[k]), MDE_from_regression_se=float((stats.norm.ppf(0.95)+stats.norm.ppf(0.80))*o2.bse[k]))
print(res['power'])
json.dump(res,open("out/step4e_aux.json","w"),indent=1); print("DONE")
