import pandas as pd, numpy as np, json, warnings; warnings.filterwarnings("ignore")
import statsmodels.formula.api as smf
T=pd.read_pickle("T.pkl"); zp=pd.read_pickle("out/zip3.pkl"); zp['zip3']=zp.zip3.astype(str).str.zfill(3); z3=pd.read_pickle("out/zip3_religiosity.pkl")
S=pd.concat([T[T.clergy], T[~T.clergy].sample(150000,random_state=1)]).copy()
S['id']=pd.to_numeric(S.id,errors='coerce').astype('Int64'); S=S.merge(zp[['id','zip3']],on='id',how='left').merge(z3[['cng_per_10k']],left_on='zip3',right_index=True,how='left').dropna(subset=['cng_per_10k']).reset_index(drop=True)
S['cng_z']=(S.cng_per_10k-z3.cng_per_10k.mean())/z3.cng_per_10k.std()
big=S.zip3.value_counts(); S=S[S.zip3.isin(big[big>=50].index)].reset_index(drop=True); print("n",len(S),"zip3",S.zip3.nunique(),"clergy",int(S.clergy.sum()))
# LPM with zip3 FE (demeaned) for memory; cluster by zip3
import statsmodels.api as sm
X=pd.get_dummies(S[['grade','yr','emp','home','ver','purp']].astype(str),drop_first=True).astype(float)
for c in ['int','fico','linc','dti','term60','lamt']: X[c]=S[c].astype(float)
X['clergy']=S.clergy.astype(float); X['clergy_x_cng']=X.clergy*S.cng_z
y=S.default.astype(float); g=S.zip3
Xd=X-X.groupby(g).transform('mean'); yd=y-y.groupby(g).transform('mean')
m=sm.OLS(yd,Xd).fit(cov_type='cluster',cov_kwds={'groups':pd.factorize(g)[0]})
print("ZIP3-FE LPM: clergy %.4f (p %.2g) | clergy x cong density %.4f (p %.4f)"%(m.params['clergy'],m.pvalues['clergy'],m.params['clergy_x_cng'],m.pvalues['clergy_x_cng']))
r=json.load(open("out/stepID_identification.json")); r['zip3FE_LPM']=dict(n=len(S),zip3=int(S.zip3.nunique()),clergy=float(m.params['clergy']),clergy_p=float(m.pvalues['clergy']),inter=float(m.params['clergy_x_cng']),inter_p=float(m.pvalues['clergy_x_cng'])); json.dump(r,open("out/stepID_identification.json","w"),indent=1)
