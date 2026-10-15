import json, numpy as np, matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
plt.rcParams.update({"font.family":"serif","font.size":9,"axes.spines.top":False,"axes.spines.right":False})
s=json.load(open("out/stepF_figures.json")); qa=s['fig3_affiliation_by_density_quintile']; ql=s['fig3_language_by_adherence_quintile']
fig,axs=plt.subplots(1,2,figsize=(7.2,3.2))
for ax,q,ttl,mk in [(axs[0],qa,"A. Affiliation × congregation-density quintile","o"),(axs[1],ql,"B. Religious language × adherence quintile","s")]:
    x=[d['q'] for d in q]; o=[d['OR'] for d in q]; lo=[d['lo'] for d in q]; hi=[d['hi'] for d in q]
    ax.errorbar(x,o,yerr=[np.array(o)-np.array(lo),np.array(hi)-np.array(o)],fmt=mk,color="black",ms=5,capsize=3,lw=1.4)
    for xi,hi_,d in zip(x,hi,q): ax.text(xi,hi_*1.01,f"n={d['n_treated']:,}",ha="center",va="bottom",fontsize=7,color="#444")
    ax.axhline(1,color="black",lw=0.8,ls=":"); ax.set_title(ttl,fontsize=9,loc="left"); ax.set_ylabel("Odds ratio of default (95% CI)")
    ax.set_xticks([1,2,3,4,5]); ax.set_xticklabels(["Q1\n(lowest)","Q2","Q3","Q4","Q5\n(highest)"])
plt.tight_layout(); plt.savefig("fig4_density.png",dpi=600,bbox_inches="tight"); plt.close(); print("ok")
