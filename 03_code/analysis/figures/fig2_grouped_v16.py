import pandas as pd, numpy as np, json, warnings; warnings.filterwarnings("ignore")
from scipy import stats
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
plt.rcParams.update({"font.family":"serif","font.size":9,"axes.spines.top":False,"axes.spines.right":False})
def ci_from_p(OR,p):
    z=stats.norm.isf(p/2); se=abs(np.log(OR))/z; return np.exp(np.log(OR)-1.96*se), np.exp(np.log(OR)+1.96*se)
s2=json.load(open("out/step2_results.json")); sN=json.load(open("out/stepN_neighbour.json")); sR=json.load(open("out/stepR_review_extras.json"))
s5=json.load(open("out/step5_ebal.json")); s7=json.load(open("out/step7a_prosper.json")); s3=json.load(open("out/step3_results.json"))
def se_row(lbl,coef,se): return (lbl,np.exp(coef),np.exp(coef-1.96*se),np.exp(coef+1.96*se))
def p_row(lbl,OR,p): lo,hi=ci_from_p(OR,p); return (lbl,OR,lo,hi)
groups=[
 ("Confirmatory estimate (Table 2, columns 1–3)",[
   se_row("All years",s2['T2_H1_full']['coef'],s2['T2_H1_full']['se']),
   se_row("2007–2014",s2['T2_H1_2008_2014']['coef'],s2['T2_H1_2008_2014']['se']),
   se_row("2015–2018",s2['T2_H1_2015_2018']['coef'],s2['T2_H1_2015_2018']['se'])]),
 ("Secure jobs and observables (Table 2, columns 4 and 5; Table 3, Panel A)",[
   p_row("+ eight stable-occupation indicators",s3["T5b_stable_ctrl"]["clergy_OR"],s3["T5b_stable_ctrl"]["clergy_p"]),
   se_row("Entropy-balanced",np.log(s5['OR']),s5['se']),
   p_row("Comparison: eight stable occupations only",s3["T5b_within_stable"]["OR"],s3["T5b_within_stable"]["p"]),
   p_row("CEM within the eight stable occupations",sR['CEM_vs_stable_occ']['OR'],sR['CEM_vs_stable_occ']['p'])]),
 ("Mission-driven jobs (Table 3, Panel B)",[
   se_row("Comparison: social work / counseling only",np.log(sN['aff_vs_nonprofit_only']['OR']),sN['aff_vs_nonprofit_only']['se']),
   se_row("Comparison: education only",np.log(sN['aff_vs_educ_only']['OR']),sN['aff_vs_educ_only']['se']),
   se_row("Comparison: healthcare only",np.log(sN['aff_vs_health_only']['OR']),sN['aff_vs_health_only']['se']),
   se_row("Comparison: all three neighbor occupations",np.log(sN['aff_vs_all_neighbours']['OR']),sN['aff_vs_all_neighbours']['se']),
   p_row("CEM within the neighbor occupations",sN['CEM_within_neighbour_pool']['OR'],sN['CEM_within_neighbour_pool']['p'])]),
 ("One platform (Table 5)",[
   p_row("Prosper, clergy and religious occupations",s7['H1_prosper']['clergy']['OR'],s7['H1_prosper']['clergy']['p'])]),
]
# layout: headers as bold y-tick labels (left column), gap between groups
heads_wrapped={
 "Confirmatory estimate (Table 2, columns 1–3)":"Confirmatory estimate\n(Table 2, columns 1–3)",
 "Secure jobs and observables (Table 2, columns 4 and 5; Table 3, Panel A)":"Secure jobs and observables\n(Table 2, columns 4 and 5;\nTable 3, Panel A)",
 "Mission-driven jobs (Table 3, Panel B)":"Mission-driven jobs\n(Table 3, Panel B)",
 "One platform (Table 5)":"One platform\n(Table 5)"}
ys=[];labels=[];kinds=[];rows=[];seps=[];y=0
for gi,(title,items) in enumerate(groups):
    if gi>0: seps.append(y+0.55)
    ys.append(y); labels.append(heads_wrapped[title]); kinds.append("H"); y-=(1.6 if title.startswith('Secure') else 1.3)
    for r in items: ys.append(y); labels.append(r[0]); kinds.append("I"); rows.append((y,)+r[1:]); y-=1
    y-=0.5
fig,ax=plt.subplots(figsize=(7.4,6.0))
for yy,OR,lo,hi in rows:
    ax.plot([lo,hi],[yy,yy],color="black",lw=1.0); ax.plot(OR,yy,marker="o",mfc="black",mec="black",color="black",ms=4.5,ls="none")
ax.axvline(1,color="black",lw=0.8,ls=":")
for sy in seps: ax.axhline(sy,color="#bbbbbb",lw=0.6)
ax.set_yticks(ys); ax.set_yticklabels(labels)
for tick,k in zip(ax.get_yticklabels(),kinds):
    if k=="H": tick.set_fontweight("bold"); tick.set_fontsize(8.5)
ax.set_xscale("log"); ax.set_xticks([0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1]); ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter()); ax.set_xlim(0.385,1.15)
ax.set_ylim(y+0.5,0.8); ax.tick_params(axis='y',length=0)
ax.set_xlabel("Odds ratio of default, affiliation (95% CI, log scale)")
plt.tight_layout(); plt.savefig("fig2_forest.png",dpi=600,bbox_inches="tight"); plt.close(); print("ok")
