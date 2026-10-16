# v22 (16 Oct 2026): panel A title "terminated sample" to match the caption; y-axis extended so the legend clears the curves
import pandas as pd, numpy as np, json, warnings; warnings.filterwarnings("ignore")
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
plt.rcParams.update({"font.family":"serif","font.size":9,"axes.spines.top":False,"axes.spines.right":False})
T=pd.read_pickle("T.pkl"); D=pd.read_pickle("D.pkl")
ex=pd.concat([c for c in pd.read_csv("/mnt/attach/outputs/25_FaithInWords/04_데이터/원데이터/LendingClub/accepted_2007_to_2018Q4.csv.gz", usecols=['id','last_pymnt_d','issue_d'], chunksize=400000, low_memory=False)])
ex['id']=pd.to_numeric(ex.id,errors='coerce'); ex=ex[ex.id.notna()]; ex['id']=ex.id.astype(int)
def evtime(df):
    s=df.copy(); s['id']=pd.to_numeric(s.id,errors='coerce').astype('Int64'); s=s.merge(ex,on='id',how='left',suffixes=('','_ex'))
    lp=pd.to_datetime(s.last_pymnt_d,format='%b-%Y',errors='coerce'); iss=pd.to_datetime(s.issue_d_ex if 'issue_d_ex' in s else s.issue_d,format='%b-%Y',errors='coerce')
    months=((lp.dt.year-iss.dt.year)*12+(lp.dt.month-iss.dt.month)).fillna(0).clip(lower=0); tm=np.where(s.term60==1,60,36)
    s['t']=np.where(s.default==1, np.minimum(months+4,tm), tm).astype(int); s['tm']=tm; return s
def curve(s,w=None,H=60):
    w=np.ones(len(s)) if w is None else w; out=[]
    for h in range(1,H+1):
        atrisk=(s.tm>=h); ev=(s.default==1)&(s.t<=h)&atrisk; out.append(np.sum(w[ev.values])/max(np.sum(w[atrisk.values]),1))
    return np.array(out)
def weights_to(treated,control,keys):
    kt=treated[keys].astype(str).agg('|'.join,axis=1); kc=control[keys].astype(str).agg('|'.join,axis=1)
    pt=kt.value_counts(normalize=True); pc=kc.value_counts(normalize=True); w=kc.map(pt/pc).fillna(0).values; return w*len(control)/w.sum()
T36=T[T.term60==0]; D36=D[D.term60==0]
A=evtime(T36[T36.clergy]); C=evtime(T36[~T36.clergy].sample(300000,random_state=3))
wC=weights_to(A,C,['grade','yr']); cA=curve(A,H=36); cC=curve(C,wC,H=36)
L=evtime(D36[D36.relig_strict]); O=evtime(D36[~D36.relig_strict]); wO=weights_to(L,O,['grade','yr']); cL=curve(L,H=36); cO=curve(O,wO,H=36)
print(dict(n_aff=len(A),n_lang=len(L),aff_12=cA[11],ctrl_12=cC[11],aff_36=cA[35],ctrl_36=cC[35],lang_12=cL[11],other_12=cO[11],lang_36=cL[35],other_36=cO[35]))
fig,axs=plt.subplots(1,2,figsize=(7.2,3.2)); m=np.arange(1,37)
axs[0].plot(m,100*cA,color="#1f4e79",lw=1.6,label=f"Religious-institution affiliation (n={len(A):,})"); axs[0].plot(m,100*cC,color="#999",lw=1.6,ls="--",label="Other borrowers, reweighted to grade × year")
axs[1].plot(m,100*cL,color="#8c3b3b",lw=1.6,label=f"Religious language (n={len(L):,})"); axs[1].plot(m,100*cO,color="#999",lw=1.6,ls="--",label="Other descriptions, reweighted")
for ax,t in zip(axs,["A. Affiliation (terminated sample)","B. Religious language (description sample)"]):
    ax.set_title(t,fontsize=8.5,loc="left"); ax.set_xlabel("Months since origination"); ax.set_ylabel("Cumulative default (%)"); ax.set_ylim(0,ax.get_ylim()[1]*1.22); ax.legend(frameon=False,fontsize=7,loc="upper left"); ax.set_xlim(0,36)
plt.tight_layout(); plt.savefig("/home/claude/fig5_cumdefault.png",dpi=600); plt.close(); print("ok")
