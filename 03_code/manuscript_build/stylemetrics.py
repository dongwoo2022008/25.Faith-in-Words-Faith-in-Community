import re,sys,statistics as st
B="/tmp/claude-0/-home-claude/6fc5949e-7a7e-5a39-a0ca-18d9d5045a2b/scratchpad/bench/"
def metrics(t,name):
    t=re.sub(r'\|.*\|','',t); w=len(t.split())
    sents=[s for s in re.split(r'(?<=[.?!])\s+',t.replace("\n"," ")) if len(s.split())>3]
    L=[len(s.split()) for s in sents]
    per=lambda n:1000*n/w
    d=per(t.count('—')); sc=per(t.count(';')); co=per(len(re.findall(r':\s',t)))
    nb=per(len(re.findall(r"\bnot\b[^.;]{1,60}\bbut\b",t)))
    i1=per(len(re.findall(r'\bI\b',t))); we=per(len(re.findall(r'\b[Ww]e\b',t)))
    print("%-10s words %6d dash/k %5.2f semi/k %5.2f colon/k %5.2f notbut/k %4.2f I/k %5.2f we/k %5.2f sentlen %4.1f sd %4.1f"%(name,w,d,sc,co,nb,i1,we,st.mean(L),st.pstdev(L)))
if __name__=="__main__":
    f=sys.argv[1] if len(sys.argv)>1 else "manuscript_v7b.md"
    m=open(f).read().split("# References")[0].split("---",2)[2]
    metrics(m,f.split("_")[1][:8] if "_" in f else f)
    for b in ["hlp","iyer","netzer"]:
        t=open(B+b+".txt",errors="ignore").read()
        t=re.split(r'\n\s*References\s*\n|\nREFERENCES\n',t)[0]; metrics(t,b)
