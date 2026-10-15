import json, numpy as np, matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
plt.rcParams.update({"font.family":"serif","font.size":9,"axes.spines.top":False,"axes.spines.right":False})
s4=json.load(open("out/step4_dml.json")); s4d=json.load(open("out/step4d_rep_dml.json")); s4b=json.load(open("out/step4b_embed_dml.json"))
def th(v): return (v.get('theta_median',v.get('PLR_theta')), v['CI_low'], v['CI_high'])
groups=[
 ("Six dictionaries as controls\n(Table 7, column 3)",[
   ("Single split",s4['DML_H2_dict']),("Twenty splits, median",s4d['dict'])]),
 ("Dictionaries and a representation\nof the full text, single split\n(Table 7, column 4; Appendix Table C5)",[
   ("TF-IDF, 100 components",s4['DML_H2_dict_text']),("Word vectors, 50 components",s4b['DML_H2_dict_spacy300_pca50']),
   ("Word vectors, full 300 dimensions",s4b['DML_H2_dict_spacy300_full']),("Document embedding, 100 dimensions",s4b['DML_H2_dict_doc2vec100'])]),
 ("Same, twenty splits, median\n(Appendix Table C5)",[
   ("TF-IDF, 100 components",s4d['dict_tfidf_svd100']),("Word vectors, 50 components",s4d['dict_spacy_pca50']),("Document embedding, 100 dimensions",s4d['dict_doc2vec100'])]),
]
ys=[];labels=[];kinds=[];rows=[];seps=[];y=0
for gi,(title,items) in enumerate(groups):
    if gi>0: seps.append(y+0.55)
    ys.append(y); labels.append(title); kinds.append("H"); y-=(1.6 if title.startswith('Dictionaries and') else 1.3)
    for lbl,v in items:
        t,lo,hi=th(v); ys.append(y); labels.append(lbl); kinds.append("I"); rows.append((y,t,lo,hi)); y-=1
    y-=0.5
fig,ax=plt.subplots(figsize=(7.4,4.9))
for yy,t,lo,hi in rows:
    ax.plot([lo,hi],[yy,yy],color="black",lw=1.0); ax.plot(t,yy,marker="o",mfc=("black" if lo>0 else "white"),mec="black",color="black",ms=4.5,ls="none")
ax.axvline(0,color="black",lw=0.8,ls=":")
for sy in seps: ax.axhline(sy,color="#bbbbbb",lw=0.6)
ax.set_yticks(ys); ax.set_yticklabels(labels)
for tick,k in zip(ax.get_yticklabels(),kinds):
    if k=="H": tick.set_fontweight("bold"); tick.set_fontsize(8.5)
ax.set_ylim(y+0.5,0.8); ax.tick_params(axis='y',length=0)
ax.set_xlabel("DML estimate of religious language on default probability (95% CI)",fontsize=8.5)
ax.plot([],[],marker="o",mfc="black",mec="black",color="black",ms=4.5,ls="none",label="interval excludes zero")
ax.plot([],[],marker="o",mfc="white",mec="black",color="black",ms=4.5,ls="none",label="interval includes zero")
ax.legend(frameon=False,loc="upper center",bbox_to_anchor=(0.3,-0.17),ncol=2,fontsize=7.5)
plt.tight_layout(); plt.savefig("fig3_dml.png",dpi=600,bbox_inches="tight"); plt.close(); print("ok")
