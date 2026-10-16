# Exact edits that turn manuscript_v16.md into manuscript_v17.md (16 October 2026): LLM coder identifiers
# supplied by the author (primary coder Claude Fable 5.1, second coder Claude Opus, both run in the Claude
# application on 18 September 2026 at default settings; see 02_results/실행결과_2026-09-18.md), and the Prosper
# file's distribution corrected to Kaggle (author's statement; the file is the Udacity-derived prosperLoanData.csv).
s=open("manuscript_v16.md").read()
R=[
('date: "Draft v16, October 2026 (JEBO version)"','date: "Draft v17, October 2026 (JEBO version)"'),
# 3.2
("Appendix B reports agreement with a second model (κ = 0.86)","Appendix B names the models and reports agreement with a second model (κ = 0.86)"),
# 3.5
("I use the public Prosper file in the Udacity distribution (113,937 listings, 2005–2014)","I use the public Prosper file in its Kaggle distribution, downloaded in June 2026 (113,937 listings, 2005–2014)"),
# 3.1 access date (author's statement: both files downloaded from Kaggle in June 2026)
("in the Kaggle distribution of the 2018Q4 release, with loan status as of that release.","in the Kaggle distribution of the 2018Q4 release, downloaded in June 2026, with loan status as of that release."),
# B1 note
("Primary coding by a large language model (LLM) coder over all 820 flagged records (717 with description text, 103 title-only), using the codebook above as the prompt [model name and version, coding date and sampling temperature of the primary and the second coder: to be supplied by the author]. Independent recoding of a stratified 200-record sample by a second LLM coder of a different model family gives κ = 0.86",
 "Primary coding by a large language model (LLM) coder over all 820 flagged records (717 with description text, 103 title-only), using the codebook above as the prompt. The coder was Claude Fable 5.1 (Anthropic), run as twelve parallel instances in the Claude application on 18 September 2026 at the application's default settings; no sampling temperature was set. Independent recoding of a stratified 200-record sample by a second LLM coder (Claude Opus, Anthropic, same application, date and settings) gives κ = 0.86"),
]
for old,new in R:
    c=s.count(old); assert c==1,(c,old[:80]); s=s.replace(old,new)
open("manuscript_v17.md","w").write(s); print("applied",len(R))
