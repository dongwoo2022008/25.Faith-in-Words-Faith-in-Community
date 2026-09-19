import re,sys
s=open("manuscript_v7.md").read()
tmap={'1':'1','2':'2','5':'3','8':'4','3':'5','4':'6','6':'7','7':'8'}
fmap={'1':'1','2':'2','5':'3','3':'4','4':'5'}
# explicit multi-number phrase
assert s.count("Tables 2, 3 and 6")==1
s=s.replace("Tables 2, 3 and 6","Tables 2, §T5§ and §T7§")
s=re.sub(r'\bTable (\d)\b',lambda m:'Table §T'+tmap[m.group(1)]+'§',s)
s=re.sub(r'\bFigure (\d)\b',lambda m:'Figure §F'+fmap[m.group(1)]+'§',s)
s=re.sub(r'\bfig(\d)_',lambda m:'fig§F'+fmap[m.group(1)]+'§_',s)
s=re.sub(r'§[TF](\d)§',r'\1',s)
s=s.replace('date: "Draft v7','date: "Draft v7b')
open("manuscript_v7b.md","w").write(s); print("ok")
