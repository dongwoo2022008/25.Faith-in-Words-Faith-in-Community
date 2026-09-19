import pandas as pd, numpy as np, json, warnings, re; warnings.filterwarnings("ignore")
import statsmodels.formula.api as smf
from scipy import stats
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
plt.rcParams.update({"font.family":"serif","font.size":9,"axes.spines.top":False,"axes.spines.right":False})
OUT="/home/claude/"; res={}
def ci_from_p(OR,p):
    z=stats.norm.isf(p/2); se=abs(np.log(OR))/z; return np.exp(np.log(OR)-1.96*se), np.exp(np.log(OR)+1.96*se)
# ---------- Figure 2: forest plot of affiliation estimates ----------
s2=json.load(open("out/step2_results.json")); sN=json.load(open("out/stepN_neighbour.json")); sR=json.load(open("out/stepR_review_extras.json"))
sID=json.load(open("out/stepID_identification.json")); s5=json.load(open("out/step5_ebal.json")); s7=json.load(open("out/step7a_prosper.json")); t2=json.load(open("out/table2_split.json"))
rows=[]
def add(lbl,OR,lo,hi,grp): rows.append((lbl,OR,lo,hi,grp))
def add_se(lbl,coef,se,grp): add(lbl,np.exp(coef),np.exp(coef-1.96*se),np.exp(coef+1.96*se),grp)
def add_p(lbl,OR,p,grp): lo,hi=ci_from_p(OR,p); add(lbl,OR,lo,hi,grp)
add_se("All years (Table 2, col. 1)",s2['T2_H1_full']['coef'],s2['T2_H1_full']['se'],"Baseline")
add_se("2008–2014 (col. 2)",s2['T2_H1_2008_2014']['coef'],s2['T2_H1_2008_2014']['se'],"Baseline")
add_se("2015–2018 (col. 3)",s2['T2_H1_2015_2018']['coef'],s2['T2_H1_2015_2018']['se'],"Baseline")
s3=json.load(open("out/step3_results.json"))
add_p("Clergy role (col. 4)",t2['aff_role']['OR'],t2['aff_role']['p'],"Baseline")
add_p("Church staff, non-clergy (col. 4)",t2['aff_staff']['OR'],t2['aff_staff']['p'],"Baseline")
add_p("+ 8 stable-occupation controls (col. 5)",s3["T5b_stable_ctrl"]["clergy_OR"],s3["T5b_stable_ctrl"]["clergy_p"],"Occupation")
add_p("Within the 8 stable occupations only",s3["T5b_within_stable"]["OR"],s3["T5b_within_stable"]["p"],"Occupation")
add_se("Entropy-balanced (col. 6)",np.log(s5['OR']),s5['se'],"Occupation")
add_p("CEM within 8 stable occupations",sR['CEM_vs_stable_occ']['OR'],sR['CEM_vs_stable_occ']['p'],"Occupation")
for k,lbl in [('aff_vs_nonprofit_only','vs. social work / counseling only'),('aff_vs_educ_only','vs. education only'),('aff_vs_health_only','vs. healthcare only'),('aff_vs_all_neighbours','vs. all three neighbor occupations')]:
    v=sN[k]; add_se(lbl,np.log(v['OR']),v['se'],"Occupation")
add_p("CEM within neighbor occupations",sN['CEM_within_neighbour_pool']['OR'],sN['CEM_within_neighbour_pool']['p'],"Occupation")
add_p("Prosper replication (Table 4)",s7['H1_prosper']['clergy']['OR'],s7['H1_prosper']['clergy']['p'],"Replication")
res['fig2_rows']=[(a,round(b,3),round(c,3),round(d,3),e) for a,b,c,d,e in rows]
fig,ax=plt.subplots(figsize=(7.2,5.0)); y=np.arange(len(rows))[::-1]
mk={"Baseline":dict(marker="o",mfc="black"),"Occupation":dict(marker="s",mfc="black"),"Replication":dict(marker="^",mfc="white")}
for yi,(lbl,OR,lo,hi,g) in zip(y,rows):
    ax.plot([lo,hi],[yi,yi],color="black",lw=1.0); ax.plot(OR,yi,marker=mk[g]["marker"],mfc=mk[g]["mfc"],mec="black",color="black",ms=5,ls="none")
ax.axvline(1,color="black",lw=0.8,ls=":"); ax.set_yticks(y); ax.set_yticklabels([r[0] for r in rows]); ax.set_xscale("log")
ax.set_xticks([0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1]); ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter()); ax.set_xlim(0.38,1.15)
ax.set_xlabel("Odds ratio of default, religious-institution affiliation (95% CI, log scale)")
lab={"Baseline":"Table 2, Panel A","Occupation":"Occupation-selection tests (Table 2, Panel B)","Replication":"Prosper replication (Table 4)"}
for g in mk: ax.plot([],[],marker=mk[g]["marker"],mfc=mk[g]["mfc"],mec="black",color="black",ms=5,ls="none",label=lab[g])
ax.legend(frameon=False,loc="upper center",bbox_to_anchor=(0.35,-0.14),ncol=3,fontsize=7.5,handletextpad=0.4,columnspacing=1.2)
plt.tight_layout(); plt.savefig(OUT+"fig2_forest.png",dpi=300,bbox_inches="tight"); plt.close()
