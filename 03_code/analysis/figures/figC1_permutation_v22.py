# v22 (16 Oct 2026): minus sign in the label is U+2212, as in the caption
import numpy as np, matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
plt.rcParams.update({"font.family":"serif","font.size":9,"axes.spines.top":False,"axes.spines.right":False})
d=np.load("out/fake_dict_dist.npy"); actual=0.035
fig,ax=plt.subplots(figsize=(5.0,3.0))
ax.hist(d,bins=40,color="#bbbbbb",edgecolor="white",lw=0.5)
ax.axvline(actual,color="black",lw=1.4)
ax.text(actual-0.001,ax.get_ylim()[1]*0.95,f"Religious dictionary\n{actual:.3f}",ha="right",va="top",fontsize=8)
ax.axvline(d.mean(),color="black",lw=0.8,ls=":")
ax.text(d.mean()-0.002,ax.get_ylim()[1]*0.95,f"Permutation mean\n{d.mean():.3f} (SD {d.std():.3f})".replace("-","−"),ha="right",va="top",fontsize=8,color="#333")
ax.set_xlabel("Residualized linear probability coefficient, 1,000 random word sets")
ax.set_ylabel("Word sets")
plt.tight_layout(); plt.savefig("/home/claude/figC1_permutation.png",dpi=600,bbox_inches="tight"); plt.close()
print("ok", d.mean().round(4), d.std().round(4), (d>=actual).mean())
