import pandas as pd, numpy as np, json, warnings; warnings.filterwarnings("ignore")
import statsmodels.formula.api as smf
T=pd.read_pickle("T.pkl"); zp=pd.read_pickle("out/zip3.pkl"); zp['zip3']=zp.zip3.astype(str).str.zfill(3); Zp=pd.read_pickle("out/zip3_unemp.pkl")
et=pd.read_pickle("lc_final.pkl")['emp_title'].fillna('').str.lower().str.strip().loc[T.index]
T['teacher']=et.str.contains(r"\bteacher\b",regex=True); T['govt']=et.str.contains(r"\bgovernment\b|\bfederal\b|\bstate of\b|\bcity of\b|\bcounty\b|\busps\b|\bpostal\b",regex=True)
S=pd.concat([T[T.teacher|T.govt], T[~T.teacher&~T.govt].sample(200000,random_state=2)]).copy(); S['id']=pd.to_numeric(S.id,errors='coerce').astype('Int64'); S=S.merge(zp[['id','zip3']],on='id',how='left'); S=S[S.zip3.isin(Zp.index)].reset_index(drop=True)
yr=S.year.astype(int).values; z=S.zip3.values; ty=np.where(S.term60==1,5,3)
S['ur0']=[Zp.at[a,b] if b in Zp.columns else np.nan for a,b in zip(z,yr)]
S['dur']=np.array([np.nanmax([Zp.at[a,c] for c in range(b+1,min(b+t,2018)+1) if c in Zp.columns] or [np.nan]) for a,b,t in zip(z,yr,ty)])-S.ur0
S=S.dropna(subset=['ur0','dur']).reset_index(drop=True); S['ur0_z']=(S.ur0-S.ur0.mean())/S.ur0.std(); S['dur_z']=(S.dur-S.dur.mean())/S.dur.std()
ctrl="C(grade) + C(yr) + int + fico + linc + dti + term60 + lamt + C(emp) + C(home) + C(ver) + C(purp) + C(st)"
G=pd.factorize(S['st'])[0]; m=smf.logit(f"default ~ teacher*dur_z + govt*dur_z + ur0_z + {ctrl}",data=S).fit(method='newton',maxiter=100,disp=0,cov_type='cluster',cov_kwds={'groups':G})
r={k:dict(OR=float(np.exp(m.params[k])),p=float(m.pvalues[k])) for k in ['teacher[T.True]','teacher[T.True]:dur_z','govt[T.True]','govt[T.True]:dur_z']}; print("positive control (stable public jobs x shock):",r, "n teacher",int(S.teacher.sum()),"govt",int(S.govt.sum()))
res=json.load(open("out/stepU_unemp.json")); res['positive_control_teacher_govt']=r; json.dump(res,open("out/stepU_unemp.json","w"),indent=1)
