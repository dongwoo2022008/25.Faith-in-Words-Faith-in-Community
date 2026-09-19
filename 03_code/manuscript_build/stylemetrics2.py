import re,sys,statistics as st
B="/tmp/claude-0/-home-claude/6fc5949e-7a7e-5a39-a0ca-18d9d5045a2b/scratchpad/bench/"
HEDGE=r"\b(may|might|could|suggests?|suggestive|appears? to|seems? to|consistent with|likely|possibly|perhaps)\b"
PASS=r"\b(is|are|was|were|be|been|being)\s+(\w+ly\s+)?\w+(ed|en)\b"
CONN=r"^(However|Moreover|Furthermore|Additionally|Thus|Therefore|In addition|Consequently|Hence|Instead|Still|Yet|Also|First|Second|Finally)\b"
def prep(t):
    t=re.sub(r'\|.*\|','',t); t=re.sub(r'!\[.*?\]\(.*?\)(\{.*?\})?','',t); t=re.sub(r'\n#.*','\n',t)
    return re.sub(r'\s+',' ',t)
def m(t):
    t=prep(t); w=len(t.split()); k=lambda n:1000*n/w
    S=[s for s in re.split(r'(?<=[.?!])\s+(?=[A-Z"“(])',t) if len(s.split())>3]
    L=[len(s.split()) for s in S]
    starts=[s.split()[0] for s in S]
    narr=len(re.findall(r"[A-Z][a-zà-ÿ\-]+(?: et al\.| and [A-Z][a-z\-]+)? \(\d{4}",t))
    paren=len(re.findall(r"\([A-Z][^()]*?\d{4}[a-z]?\)",t))
    nomin=len(re.findall(r"\b\w{4,}(tion|tions|ment|ments|ness|ity|ities|ance|ence)\b",t))
    return dict(words=w,dash=k(t.count('—')),semi=k(t.count(';')),colon=k(len(re.findall(r':\s',t))),
        paren=k(len(re.findall(r'\(',t))),hedge=k(len(re.findall(HEDGE,t,re.I))),passive=k(len(re.findall(PASS,t))),
        nomin=k(nomin),sent=st.mean(L),sd=st.pstdev(L),
        conn_start=100*sum(bool(re.match(CONN,s)) for s in S)/len(S),
        this_start=100*sum(x in("This","These","That","Those","It") for x in starts)/len(S),
        cite_narr=100*narr/max(narr+paren,1))
docs={}
v=open(sys.argv[1]).read().split("# References")[0].split("---",2)[2]; docs['v8']=m(v)
for b in ["hlp","iyer","netzer"]:
    t=open(B+b+".txt",errors="ignore").read(); t=re.split(r'\n\s*References\s*\n|\nREFERENCES\n',t)[0]; docs[b]=m(t)
keys=[k for k in docs['v8'] if k!='words']
print("%-11s"%"metric"+"".join("%9s"%d for d in docs)+"   bench range  flag")
for k in keys:
    bv=[docs[b][k] for b in ["hlp","iyer","netzer"]]; lo,hi=min(bv),max(bv); x=docs['v8'][k]
    flag="" if lo<=x<=hi else ("HIGH" if x>hi else "LOW")
    print("%-11s"%k+"".join("%9.2f"%docs[d][k] for d in docs)+"   %5.2f–%-6.2f %s"%(lo,hi,flag))
