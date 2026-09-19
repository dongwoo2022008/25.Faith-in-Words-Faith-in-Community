import sys
p="/home/claude/manuscript_v3.md"; s=open(p).read()
def rep(old,new):
    global s
    if s.count(old)!=1: print("!! count",s.count(old),old[:80]); sys.exit(1)
    s=s.replace(old,new)
rep('date: "Draft v2 — September 2026 (JEBO version)"','date: "Draft v3 — September 2026 (JEBO version)"')
# ---- Intro: H1 positioning after "opposite signs." paragraph -> add to 'This paper is about that contrast' paragraph end
rep("stronger where there are more churches nearby, and reproduced on a second platform.",
    "stronger where there are more churches nearby, and reproduced on a second platform. Online lenders are known to read soft information of this kind — the borrower's appearance (Duarte, Siegel and Young, 2012), verified friendships (Lin, Prabhala and Viswanathan, 2013), the job title itself (Davaadorj, Enkhtaivan and Lu, 2025) — and to price some of it. The one such signal that has been shown to lower default is a community tie, the verified friendship on Prosper; the affiliation I study is a community tie of a much thicker kind, and I look at default rather than funding.")
# ---- Intro literature paragraph: third literature rewrite
rep("The third literature is the work on borrower text in credit markets (Netzer et al., 2019; Nowak, Ross and Yencha, 2018; Sanz-Guerrero and Arroyo, 2025), which has established that words predict default — Netzer et al. list mentions of God among them — and has been less interested in which words carry information of their own rather than proxying for circumstance.",
    "The third literature is the work on borrower-supplied information in online credit markets, where lenders infer creditworthiness from what lies outside the credit score (Iyer, Khwaja, Luttmer and Shue, 2016) and where the text of the request has received the most attention (Herzenstein, Sonenshein and Dholakia, 2011; Michels, 2012; Dorfleitner et al., 2016; Nowak, Ross and Yencha, 2018; Netzer et al., 2019; Kriebel and Stitz, 2022; Gao, Lin and Sias, 2023; Sanz-Guerrero and Arroyo, 2025). That work has established that words predict default — Netzer et al. list mentions of God among them — and that self-authored identity claims can raise funding while predicting worse repayment (Herzenstein et al., 2011). It has been less interested in which words carry information of their own rather than proxying for circumstance.")
# ---- 2.1 first paragraph
rep("and the lender can rely on that cost even though it cannot contract on it (Besley and Coate, 1995).",
    "and the lender can rely on that cost even though it cannot contract on it (Stiglitz, 1990; Besley and Coate, 1995); the channels through which this works — who is admitted, who is watched, who is sanctioned — have been catalogued (Ghatak and Guinnane, 1999).")
rep("and the effect runs through monitoring and enforcement rather than through selection alone (Karlan, 2007).",
    "and the effect runs through monitoring and enforcement rather than through selection alone (Karlan, 2007). Trustworthiness revealed in a game predicts repayment where trust does not (Karlan, 2005); randomly more frequent group meetings cut default on the next loan by two thirds (Feigenberg, Field and Pande, 2013); removing joint liability while keeping the meetings does not raise default (Giné and Karlan, 2014), which is to say the community disciplines even when the lender holds no contract with it; and in Jordanian lending groups the borrower's own religiosity raises repayment alongside the group's social ties (Al-Azzam, Hill and Sarangi, 2012).")
rep("and interpret the result as trust lowering the cost of enforcement.",
    "and interpret the result as trust lowering the cost of enforcement. In U.S. consumer credit, borrowers in communities with more social capital default less, most markedly when default would be strategic (Clark, Hasan, Lai, Li and Siddique, 2021), and willingness to default strategically depends on moral views and on watching neighbors do it (Guiso, Sapienza and Zingales, 2013).")
# ---- 2.1 congregation paragraph: surveys
rep("Iannaccone (1992) argued that the demands religious groups place on members,",
    "The economics of religion has long treated the congregation as a club that produces goods its members cannot buy elsewhere (Iannaccone, 1998; Iyer, 2016). Iannaccone (1992) argued that the demands religious groups place on members,")
# ---- 2.2
rep("and whether it carries information depends on who chooses to send it rather than on what it says (Spence, 1973; Crawford and Sobel, 1982; Farrell and Rabin, 1996).",
    "and whether it carries information depends on who chooses to send it rather than on what it says (Spence, 1973; Crawford and Sobel, 1982; Farrell and Rabin, 1996). If misreporting carries even a small moral cost to the sender, such talk becomes partly informative (Kartik, 2009) — but the information need not run in the direction the sender intends. Two facts about religious people bear on this. Their stated moral attitudes are stricter than average, yet in an unobserved trust game they betray at the same rate as everyone else (Kirchmaier, Prüfer and Trautmann, 2018); and in lending, unverifiable self-description has been found to raise funding while predicting worse repayment (Herzenstein et al., 2011; Wang, Wang, Wu and Zhang, 2023), and voluntary repayment promises to predict better repayment among new borrowers and worse among returning ones (Lun, Meng and Xu, 2024).")
# ---- 3.3 text controls: Kriebel & Stitz
rep("so that anything the text says that a linear dictionary misses is still conditioned on.",
    "so that anything the text says that a linear dictionary misses is still conditioned on. On this same platform, Kriebel and Stitz (2022) find that even short descriptions carry default information and that a simple embedding average predicts as well as a transformer, which is the representation I use.")
# ---- 3.4 ARDA precedent
rep("I merge the 2010 U.S. Religion Census county file (Grammich et al., 2012)",
    "I merge the 2010 U.S. Religion Census county file (Grammich et al., 2012), the source of the county religiosity measures used in corporate finance since Hilary and Hui (2009),")
# ---- 5.3: Noussair
rep("It is the congregation.",
    "It is the congregation. The pattern has a parallel in survey data: the financial risk aversion associated with church membership runs through the social side of membership rather than through belief (Noussair, Trautmann, van de Kuilen and Vellekoop, 2013).")
# ---- 5.4: Dehejia insurance for unemployment null
rep("what it can say is that the affiliation effect is not visibly a shock-absorption effect, while it is visibly a community-density effect.",
    "what it can say is that the affiliation effect is not visibly a shock-absorption effect, while it is visibly a community-density effect. One further reading is consistent with both facts: religious organizations insure their members' consumption against income shocks (Dehejia, DeLeire and Luttmer, 2007), so an affiliated borrower who loses income may be cushioned before the loan is, in which case local unemployment would not have to widen the gap.")
# ---- 5.5: parallels and Hasan
rep("I flag it as a contrast with the county literature rather than a contradiction of it.",
    "I flag it as a contrast with the county literature rather than a contradiction of it; the sign of local religious composition is not fixed even there — in Germany, regions where Catholics outnumber Protestants show less household over-indebtedness (Hasan, Kiesel and Noth, 2025). The split between an individual effect and a null regional one has parallels elsewhere: personal trust among group members predicts loan repayment where generalized trust does not (Cassar, Crowley and Wydick, 2007), and in German regions individual church attendance predicts trust while regional devoutness has no contextual effect (Traunmüller, 2011).")
# ---- 6.1 pricing
rep("They are the size of the information the market left on the table, stated in the units the market uses.",
    "They are the size of the information the market left on the table, stated in the units the market uses. That it was left there is itself informative. On Prosper, where investors bid on rates, unverifiable disclosures lowered the rate (Michels, 2012) and text was priced, if not fully (Gao, Lin and Sias, 2023); in corporate debt, a firm's county religiosity earns a lower spread (Jiang, John, Li and Qian, 2018). LendingClub's grade-based pricing used none of this, and even the private information its borrowers reveal through their own contract choices goes unpriced (Hertzberg, Liberman and Paravisini, 2018).")
# ---- 6.4 Renneboog
rep("on any of which church employees may differ from other borrowers.",
    "on any of which church employees may differ from other borrowers; nor does it record the thrift, planning horizon and trust that religious households report more of (Renneboog and Spaenjers, 2012), which could lower default without any community watching.")
# ---- References
refs=[
"Al-Azzam, M., Hill, R. C., & Sarangi, S. (2012). Repayment performance in group lending: Evidence from Jordan. *Journal of Development Economics*, 97(2), 404–414.",
"Cassar, A., Crowley, L., & Wydick, B. (2007). The effect of social capital on group loan repayment: Evidence from field experiments. *The Economic Journal*, 117(517), F85–F106.",
"Clark, B., Hasan, I., Lai, H., Li, F., & Siddique, A. (2021). Consumer defaults and social capital. *Journal of Financial Stability*, 53, 100821.",
"Davaadorj, Z., Enkhtaivan, B., & Lu, W. (2025). Character and creditworthiness: Unveiling the role of job titles in peer-to-peer lending. *Journal of Financial Research*, 49(3), 1205–1228.",
"Dehejia, R., DeLeire, T., & Luttmer, E. F. P. (2007). Insuring consumption and happiness through religious organizations. *Journal of Public Economics*, 91(1–2), 259–279.",
"Dorfleitner, G., Priberny, C., Schuster, S., Stoiber, J., Weber, M., de Castro, I., & Kammler, J. (2016). Description-text related soft information in peer-to-peer lending: Evidence from two leading European platforms. *Journal of Banking & Finance*, 64, 169–187.",
"Duarte, J., Siegel, S., & Young, L. (2012). Trust and credit: The role of appearance in peer-to-peer lending. *Review of Financial Studies*, 25(8), 2455–2484.",
"Feigenberg, B., Field, E., & Pande, R. (2013). The economic returns to social interaction: Experimental evidence from microfinance. *Review of Economic Studies*, 80(4), 1459–1483.",
"Gao, Q., Lin, M., & Sias, R. (2023). Words matter: The role of readability, tone, and deception cues in online credit markets. *Journal of Financial and Quantitative Analysis*, 58(1), 1–28.",
"Ghatak, M., & Guinnane, T. W. (1999). The economics of lending with joint liability: Theory and practice. *Journal of Development Economics*, 60(1), 195–228.",
"Giné, X., & Karlan, D. (2014). Group versus individual liability: Short and long term evidence from Philippine microcredit lending groups. *Journal of Development Economics*, 107, 65–83.",
"Guiso, L., Sapienza, P., & Zingales, L. (2013). The determinants of attitudes toward strategic default on mortgages. *Journal of Finance*, 68(4), 1473–1515.",
"Hasan, I., Kiesel, K., & Noth, F. (2025). \"And forgive us our debts\": Christian moralities and over-indebtedness. *Journal of Financial Research*, 48(3), 1013–1031.",
"Hertzberg, A., Liberman, A., & Paravisini, D. (2018). Screening on loan terms: Evidence from maturity choice in consumer credit. *Review of Financial Studies*, 31(9), 3532–3567.",
"Herzenstein, M., Sonenshein, S., & Dholakia, U. M. (2011). Tell me a good story and I may lend you money: The role of narratives in peer-to-peer lending decisions. *Journal of Marketing Research*, 48(SPL), S138–S149.",
"Hilary, G., & Hui, K. W. (2009). Does religion matter in corporate decision making in America? *Journal of Financial Economics*, 93(3), 455–473.",
"Iannaccone, L. R. (1998). Introduction to the economics of religion. *Journal of Economic Literature*, 36(3), 1465–1495.",
"Iyer, R., Khwaja, A. I., Luttmer, E. F. P., & Shue, K. (2016). Screening peers softly: Inferring the quality of small borrowers. *Management Science*, 62(6), 1554–1577.",
"Iyer, S. (2016). The new economics of religion. *Journal of Economic Literature*, 54(2), 395–441.",
"Jiang, F., John, K., Li, C. W., & Qian, Y. (2018). Earthly reward to the religious: Religiosity and the costs of public and private debt. *Journal of Financial and Quantitative Analysis*, 53(5), 2131–2160.",
"Karlan, D. S. (2005). Using experimental economics to measure social capital and predict financial decisions. *American Economic Review*, 95(5), 1688–1699.",
"Kartik, N. (2009). Strategic communication with lying costs. *Review of Economic Studies*, 76(4), 1359–1395.",
"Kirchmaier, I., Prüfer, J., & Trautmann, S. T. (2018). Religion, moral attitudes and economic behavior. *Journal of Economic Behavior & Organization*, 148, 282–300.",
"Kriebel, J., & Stitz, L. (2022). Credit default prediction from user-generated text in peer-to-peer lending using deep learning. *European Journal of Operational Research*, 302(1), 309–323.",
"Lin, M., Prabhala, N. R., & Viswanathan, S. (2013). Judging borrowers by the company they keep: Friendship networks and information asymmetry in online peer-to-peer lending. *Management Science*, 59(1), 17–35.",
"Lun, X., Meng, X., & Xu, J. (2024). Is cheap talk just empty words? The signalling value of voluntary promises for loan repayment. *Applied Economics Letters*, 31(17), 1737–1741.",
"Michels, J. (2012). Do unverifiable disclosures matter? Evidence from peer-to-peer lending. *The Accounting Review*, 87(4), 1385–1413.",
"Noussair, C. N., Trautmann, S. T., van de Kuilen, G., & Vellekoop, N. (2013). Risk aversion and religion. *Journal of Risk and Uncertainty*, 47(2), 165–183.",
"Renneboog, L., & Spaenjers, C. (2012). Religion, economic attitudes, and household finance. *Oxford Economic Papers*, 64(1), 103–127.",
"Stiglitz, J. E. (1990). Peer monitoring and credit markets. *World Bank Economic Review*, 4(3), 351–366.",
"Traunmüller, R. (2011). Moral communities? Religion as a source of social trust in a multilevel analysis of 97 German regions. *European Sociological Review*, 27(3), 346–363.",
"Wang, C., Wang, J., Wu, C., & Zhang, Y. (2023). Voluntary disclosure in P2P lending: Information or hyperbole? *Pacific-Basin Finance Journal*, 79, 102024.",
]
head,tail=s.split("# References\n")
entries=[l for l in tail.strip().split("\n\n") if l.strip()]
entries+=refs
def key(e):
    import re
    e2=e.replace("\"","")
    return re.sub(r"[^a-z]","",e2.split("(")[0].lower())+e2.split("(")[1][:4]
entries=sorted(set(entries),key=key)
s=head+"# References\n\n"+"\n\n".join(entries)+"\n"
open(p,"w").write(s); print("ok refs",len(entries))
