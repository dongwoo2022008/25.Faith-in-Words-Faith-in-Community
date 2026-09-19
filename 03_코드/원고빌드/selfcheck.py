import re,sys,statistics as st
p=sys.argv[1]; s=open(p).read(); body=s.split("# References")[0]
paras=[x for x in body.split("\n\n") if x.strip() and not x.startswith(("#","---","*Keywords","![","**Abstract","**H"))]
banned=["It is important to note","It is worth noting","It should be noted","Interestingly","Surprisingly","Importantly","Notably","Clearly","Obviously","Crucially","novel","unprecedented","to the best of my knowledge","to the best of our knowledge"]
print("== banned"); 
for b in banned:
    for m in re.finditer(r"\b"+re.escape(b)+r"\b",body): print(f"  {b!r} ... {body[max(0,m.start()-60):m.end()+40].replace(chr(10),' ')}")
print("== causal verbs (review manually)")
for v in [r"\bcauses?\b",r"\bcausal\b",r"\bleads? to\b",r"\bdrives?\b",r"\bproves?\b",r"\bdemonstrates?\b",r"\breduces?\b",r"\braises?\b",r"\bincreases?\b",r"\bdecreases?\b",r"\blowers?\b"]:
    for m in re.finditer(v,body): print(f"  {m.group()!r:14} ... {body[max(0,m.start()-70):m.end()+50].replace(chr(10),' ')}")
print("== paragraph stats")
sl=[len(re.split(r'(?<=[.!?])\s+(?=[A-Z"“(])',x)) for x in paras]
print("  n paras",len(paras),"sentences/para median",st.median(sl),"min",min(sl),"max",max(sl),"one-sentence paras",sum(1 for x in sl if x==1))
starts=[x.split()[0].strip(",") for x in paras]
from collections import Counter
print("  first words:",Counter(starts).most_common(8))
print("== topic sentences")
for x in paras: print("  -",re.split(r'(?<=[.!?])\s+',x)[0][:140])
a=s[s.index("**Abstract.**")+13:s.index("*Keywords:*")]; print("== abstract words",len(a.split()),"| body words",len(body.split()))
