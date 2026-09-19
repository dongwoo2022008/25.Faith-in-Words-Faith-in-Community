import sys,re
p="/home/claude/manuscript_v4.md"; s=open(p).read()
def rep(old,new):
    global s
    if s.count(old)!=1: print("!! count",s.count(old),old[:80]); sys.exit(1)
    s=s.replace(old,new)
rep('date: "Draft v3 — September 2026 (JEBO version)"','date: "Draft v4 — September 2026 (JEBO version)"')
# Intro: soft information sentence -> add Freedman & Jin, Davaadorj 2024
rep("the job title itself (Davaadorj, Enkhtaivan and Lu, 2025) — and to price some of it.",
    "the job title itself (Davaadorj, Enkhtaivan and Lu, 2024, 2025) — and to price some of it, not always correctly (Freedman and Jin, 2017).")
# 2.1: social collateral formal term -> Karlan et al 2009 after Besley-Coate sentence
rep("the channels through which this works — who is admitted, who is watched, who is sanctioned — have been catalogued (Ghatak and Guinnane, 1999).",
    "the channels through which this works — who is admitted, who is watched, who is sanctioned — have been catalogued (Ghatak and Guinnane, 1999). Karlan, Möbius, Rosenblat and Szeidl (2009) give the idea its name and its model: the trust a borrower can draw on is the value of the network ties that a default would put at risk, and it is largest in dense, closely knit communities.")
# 2.1: P2P social capital evidence after Clark/GSZ sentence
rep("and willingness to default strategically depends on moral views and on watching neighbors do it (Guiso, Sapienza and Zingales, 2013).",
    "and willingness to default strategically depends on moral views and on watching neighbors do it (Guiso, Sapienza and Zingales, 2013). The same holds inside marketplace lending: borrowers from higher-social-capital regions default less on a Chinese platform (Hasan, He and Lu, 2022) and on LendingClub itself (Lu, Wang, Wang and Zhao, 2020), and making a borrower's default visible to his social contacts deters it (Ge, Feng, Gu and Zhang, 2017).")
# 2.2: Caldieraro
rep("If misreporting carries even a small moral cost to the sender, such talk becomes partly informative (Kartik, 2009)",
    "If misreporting carries even a small moral cost to the sender, such talk becomes partly informative (Kartik, 2009), and in peer-to-peer markets the relation between unverifiable disclosure and loan quality has been shown to be non-monotonic (Caldieraro, Zhang, Cunha and Shulman, 2018)")
# 5.1 Panel B paragraph: Agarwal et al 2017 + Davaadorj 2024
rep("Whatever the affiliation captures, it is not shared by the occupations that most resemble it in pay, tenure or purpose.",
    "Whatever the affiliation captures, it is not shared by the occupations that most resemble it in pay, tenure or purpose. Occupation has been found to carry default information beyond observables before — finance professionals are less often delinquent on their mortgages (Agarwal, Chomsisengphet and Zhang, 2017), and skilled job titles on LendingClub default less and are priced accordingly (Davaadorj et al., 2024) — but in those cases the natural reading is expertise; a church secretary has no financial expertise to point to.")
# 5.4: Chen 2010 and Adbi 2024
rep("so an affiliated borrower who loses income may be cushioned before the loan is, in which case local unemployment would not have to widen the gap.",
    "so an affiliated borrower who loses income may be cushioned before the loan is, in which case local unemployment would not have to widen the gap. Religious institutions do expand exactly this role in a crisis (Chen, 2010). The opposite possibility also exists — in Indian microfinance after demonetization, default spread fastest along religious ties (Adbi, Lee and Singh, 2024) — and it is another reason the shock interaction was worth testing and is worth reporting as flat.")
# References
refs=[
"Adbi, A., Lee, M., & Singh, J. (2024). Community influence on microfinance loan defaults under crisis conditions: Evidence from Indian demonetization. *Strategic Management Journal*, 45(3), 535–563.",
"Agarwal, S., Chomsisengphet, S., & Zhang, Y. (2017). How does working in a finance profession affect mortgage delinquency? *Journal of Banking & Finance*, 78, 1–13.",
"Caldieraro, F., Zhang, J. Z., Cunha, M., Jr., & Shulman, J. D. (2018). Strategic information transmission in peer-to-peer lending markets. *Journal of Marketing*, 82(2), 42–63.",
"Chen, D. L. (2010). Club goods and group identity: Evidence from Islamic resurgence during the Indonesian financial crisis. *Journal of Political Economy*, 118(2), 300–354.",
"Davaadorj, Z., Enkhtaivan, B., & Lu, W. (2024). The role of job titles in online peer-to-peer lending: An empirical investigation on skilled borrowers. *Journal of Behavioral and Experimental Finance*, 41, 100890.",
"Freedman, S., & Jin, G. Z. (2017). The information value of online social networks: Lessons from peer-to-peer lending. *International Journal of Industrial Organization*, 51, 185–222.",
"Ge, R., Feng, J., Gu, B., & Zhang, P. (2017). Predicting and deterring default with social media information in peer-to-peer lending. *Journal of Management Information Systems*, 34(2), 401–424.",
"Hasan, I., He, Q., & Lu, H. (2022). Social capital, trusting, and trustworthiness: Evidence from peer-to-peer lending. *Journal of Financial and Quantitative Analysis*, 57(4), 1409–1453.",
"Karlan, D., Möbius, M., Rosenblat, T., & Szeidl, A. (2009). Trust and social collateral. *Quarterly Journal of Economics*, 124(3), 1307–1361.",
"Lu, H., Wang, B., Wang, H., & Zhao, T. (2020). Does social capital matter for peer-to-peer lending? Empirical evidence. *Pacific-Basin Finance Journal*, 61, 101338.",
]
head,tail=s.split("# References\n")
entries=[l.strip() for l in tail.strip().split("\n\n") if l.strip()]+refs
def key(e):
    e2=e.replace("\"","")
    authors=e2.split("(")[0]
    surnames=[re.sub(r"[^a-zé ]","",a.strip().split(",")[0].lower()) for a in re.split(r", & |, (?=[A-Z][a-zé]+, )",authors)]
    return (surnames, e2.split("(")[1][:4])
entries=sorted(set(entries),key=key)
s=head+"# References\n\n"+"\n\n".join(entries)+"\n"
open(p,"w").write(s); print("ok refs",len(entries))
# cross-check
body,refs_=s.split("# References")
ref_first=set()
for l in refs_.split("\n\n"):
    l=l.strip().replace("\"","")
    if not l: continue
    m=re.match(r"([A-Z][A-Za-zéö\-' ]+?),.*?\((\d{4})\)",l); ref_first.add((m.group(1).split()[0],m.group(2)))
print("never cited:",[(n,y) for n,y in ref_first if not re.search(re.escape(n)+r"[^\n]{0,90}?"+y, body)])
