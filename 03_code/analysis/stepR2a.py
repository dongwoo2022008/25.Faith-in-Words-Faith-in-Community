# Re-analysis after external review (2026-09-20): one canonical affiliation definition (step1 T.clergy)
import pandas as pd, numpy as np, json, warnings, gc; warnings.filterwarnings("ignore")
import statsmodels.formula.api as smf
from scipy import stats
T=pd.read_pickle("T.pkl"); zp=pd.read_pickle("out/zip3.pkl"); zp['zip3']=zp.zip3.astype(str).str.zfill(3)
Zp=pd.read_pickle("out/zip3_unemp.pkl"); z3=pd.read_pickle("out/zip3_religiosity.pkl")
et=pd.read_pickle("lc_final.pkl")['emp_title'].fillna('').str.lower().str.strip().loc[T.index]
role=et.str.contains(r"\bpastor\b|\bminister\b|\bministry\b|\bclergy\b|\bpriest\b|\bchaplain\b|\brabbi\b|\bmissionar|\breverend\b|\bevangelist\b|\bdeacon\b|\bworship\b|\bimam\b|\bseminar(y|ian)\b", regex=True)
T['aff_role']=(T.clergy&role).astype(int); T['aff_staff']=(T.clergy&~role).astype(int)
T['teacher_x']=et.str.contains(r"\bteacher\b",regex=True).astype(int)
T['govt_x']=et.str.contains(r"\bgovernment\b|\bfederal\b|\bstate of\b|\bcity of\b|\bcounty\b|\busps\b|\bpostal\b",regex=True).astype(int)
T['emp10']=(T.emp_length.astype(str).str.contains(r"10\+")).astype(int); T['verified']=(T.ver!='Not Verified').astype(int)
ctrl="C(grade) + C(yr) + int + fico + linc + dti + term60 + lamt + C(emp) + C(home) + C(ver) + C(purp) + C(st)"
def fitm(f,S,groups='st'):
    G=pd.factorize(S[groups])[0]; mdl=smf.logit(f,data=S)
    m=mdl.fit(method='newton',maxiter=100,disp=0,cov_type='cluster',cov_kwds={'groups':G})
    if not m.mle_retvals.get('converged',False): m=mdl.fit(method='bfgs',start_params=m.params,maxiter=3000,disp=0,cov_type='cluster',cov_kwds={'groups':G})
    return m
def rep(m,k):
    b=m.params[k]; se=m.bse[k]; return dict(coef=float(b),se=float(se),OR=float(np.exp(b)),lo=float(np.exp(b-1.96*se)),hi=float(np.exp(b+1.96*se)),p2=float(m.pvalues[k]),n=int(m.nobs))
res={}
TS=pd.concat([T[T.clergy], T[~T.clergy].sample(250000, random_state=1)]).copy()
m=fitm(f"default ~ clergy + {ctrl}",TS); res['H1_seed1']=rep(m,'clergy[T.True]'); print('H1 seed1',res['H1_seed1'],flush=True)
m=fitm(f"default ~ aff_role + aff_staff + {ctrl}",TS); res['split_role']=rep(m,'aff_role'); res['split_staff']=rep(m,'aff_staff')
w=m.wald_test('aff_role = aff_staff',scalar=True); res['split_equal_p']=float(w.pvalue); print('split',res['split_role'],res['split_staff'],'eq p',res['split_equal_p'],flush=True)
del m; gc.collect()
res['H1_seeds']={}
for sd in [2,3,4,5,6]:
    S=pd.concat([T[T.clergy], T[~T.clergy].sample(250000, random_state=sd)])
    m=fitm(f"default ~ clergy + {ctrl}",S); res['H1_seeds'][sd]=rep(m,'clergy[T.True]'); print('seed',sd,res['H1_seeds'][sd]['OR'],flush=True); del m,S; gc.collect()
json.dump(res,open("out/stepR2a.json","w"),indent=1)
# H2 main spec CI and two-sided p
D=pd.read_pickle("D.pkl")
m=fitm(f"default ~ relig_strict + {ctrl} + llen + moral + hardship + gratitude + family + help + business",D); res['H2_col3']=rep(m,'relig_strict[T.True]'); print('H2',res['H2_col3'],flush=True); del m,D; gc.collect()
json.dump(res,open("out/stepR2a.json","w"),indent=1)
# Local merge sample (canonical affiliation): unemployment + density
S=TS.copy(); S['id']=pd.to_numeric(S.id,errors='coerce').astype('Int64'); S=S.merge(zp[['id','zip3']],on='id',how='left')
S=S[S.zip3.isin(Zp.index)].reset_index(drop=True); yr=S.year.astype(int).values; z=S.zip3.values; ty=np.where(S.term60==1,5,3)
S['ur0']=[Zp.at[a,b] if b in Zp.columns else np.nan for a,b in zip(z,yr)]
S['dur']=np.array([np.nanmax([Zp.at[a,c] for c in range(b+1,min(b+t,2018)+1) if c in Zp.columns] or [np.nan]) for a,b,t in zip(z,yr,ty)])-S.ur0
S=S.merge(z3[['cng_per_10k']],left_on='zip3',right_index=True,how='left')
S=S.dropna(subset=['ur0','dur','cng_per_10k']).reset_index(drop=True)
for v in ['ur0','dur','cng_per_10k']: S[v+'_z']=(S[v]-S[v].mean())/S[v].std()
S['aff']=S.clergy.astype(int)
res['local_n']=int(len(S)); res['local_aff']=int(S.aff.sum()); res['dur_mean']=float(S.dur.mean()); res['dur_sd']=float(S.dur.std()); print('local n',len(S),S.aff.sum(),flush=True)
# Table 8 re-estimated with canonical indicator
m=fitm(f"default ~ aff*dur_z + ur0_z + {ctrl}",S)
res['T8']={k:rep(m,k) for k in ['aff','ur0_z','dur_z','aff:dur_z']}
m2=fitm(f"default ~ aff*ur0_z + dur_z + {ctrl}",S); res['T8']['aff:ur0_z']=rep(m2,'aff:ur0_z')
m3=fitm(f"default ~ aff + ur0_z + dur_z + {ctrl}",S); res['T8']['aff_main']=rep(m3,'aff'); res['T8']['ur0_main']=rep(m3,'ur0_z'); res['T8']['dur_main']=rep(m3,'dur_z')
S['sh_t']=pd.qcut(S.dur.rank(method='first'),3,labels=['small','mid','large'])
for t in ['small','mid','large']:
    s=S[S.sh_t==t].reset_index(drop=True); mm=fitm(f"default ~ aff + {ctrl}",s); res['T8']['terc_'+t]=rep(mm,'aff')
print('T8',{k:round(v['OR'],3) for k,v in res['T8'].items()},flush=True)
json.dump(res,open("out/stepR2a.json","w"),indent=1)
# Table A: competing explanations
S['aff_emp10']=S.aff*S.emp10; S['aff_ver']=S.aff*S.verified
spec={'A1_density':f"default ~ aff*cng_per_10k_z + {ctrl}",
      'A2_shock':f"default ~ aff*dur_z + ur0_z + {ctrl}",
      'A3_stability':f"default ~ aff + aff_emp10 + aff_ver + {ctrl}",
      'A4_all':f"default ~ aff*cng_per_10k_z + aff*dur_z + ur0_z + aff_emp10 + aff_ver + {ctrl}"}
res['TA']={}
for k,f in spec.items():
    mm=fitm(f,S); keys=[x for x in ['aff','aff:cng_per_10k_z','cng_per_10k_z','aff:dur_z','aff_emp10','aff_ver'] if x in mm.params.index]
    res['TA'][k]={x:rep(mm,x) for x in keys}; print(k,{x:(round(v['OR'],3),round(v['p2'],3)) for x,v in res['TA'][k].items()},flush=True)
    if k=='A1_density':
        # predicted default at density -1/+1 SD for aff vs non (average over sample)
        pp={}
        for a in [0,1]:
            for d in [-1,1]:
                X=S.copy(); X['aff']=a; X['cng_per_10k_z']=d; pp[f'aff{a}_d{d:+d}']=float(mm.predict(X).mean())
        res['TA']['pred']=pp; print('pred',pp,flush=True)
    del mm; gc.collect()
json.dump(res,open("out/stepR2a.json","w"),indent=1)
# positive control on same local sample definition (teacher, government) x shock
m=fitm(f"default ~ teacher_x*dur_z + govt_x*dur_z + ur0_z + {ctrl}",S)
res['T8']['teacher_x_dur']=rep(m,'teacher_x:dur_z'); res['T8']['govt_x_dur']=rep(m,'govt_x:dur_z'); res['T8']['n_teacher']=int(S.teacher_x.sum()); res['T8']['n_govt']=int(S.govt_x.sum())
print('poscontrol',res['T8']['teacher_x_dur'],res['T8']['govt_x_dur'],flush=True)
json.dump(res,open("out/stepR2a.json","w"),indent=1); print('DONE')
