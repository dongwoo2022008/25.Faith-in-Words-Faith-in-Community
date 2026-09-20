import pandas as pd, numpy as np, json, warnings, gc; warnings.filterwarnings("ignore")
import statsmodels.formula.api as smf
src=open("stepR2b.py").read(); exec(src.split("res['TB']=")[0].split("res=json.load")[0])
exec(src.split("res=json.load(open(\"out/stepR2a.json\"))")[1].split("res['TB']=")[0])
m=fitm(f"default ~ aff + aff_emp10 + aff_ver + {ctrl}",S)
t=m.t_test('aff + aff_emp10 = 0'); b=float(t.effect[0]); se=float(t.sd[0][0])
r=dict(OR=float(np.exp(b)),lo=float(np.exp(b-1.96*se)),hi=float(np.exp(b+1.96*se)),p2=float(t.pvalue))
print(r, 'n aff emp10', int(S.aff_emp10.sum()), 'aff',int(S.aff.sum()))
res=json.load(open("out/stepR2a.json")); res['TB']['aff_at_emp10']=r; res['TB']['n_aff_emp10']=int(S.aff_emp10.sum()); json.dump(res,open("out/stepR2a.json","w"),indent=1)
