# Exact edits that turn manuscript_v17.md into manuscript_v18.md (16 October 2026), after the third external
# check (C7 cross-check and wording). New numbers: v18_auc.json (affiliation AUC change with bootstrap CI,
# reproduces lc_two_signal_analysis_results.json exactly; 42 description-sample loans issued after 2014),
# stepC_economic.json (net loss to two decimals), rate_schedule_by_year.csv and verify_rate_schedule.py
# (7,642 cells, 94.7 percent at the modal rate, at most 5 distinct rates), step7b_investor.json (N 123,292).
s=open("manuscript_v17.md").read()
R=[
('date: "Draft v17, October 2026 (JEBO version)"','date: "Draft v18, October 2026 (JEBO version)"'),
# abstract: antecedent of "which"
("and shows no detectable response to the period's small local unemployment shocks, which a job-stability account would predict.","and shows no detectable response to the period's small local unemployment shocks, the response a job-stability account would predict."),
# 3.2 affiliation rule
("so I report what the rule fixed in advance produces.","so I report what the rule fixed in the design note produces."),
# Table 1 note: description sample includes 42 loans issued after 2014
("Description sample: loans with non-empty borrower text after removing platform boilerplate, issued 2007–2014.","Description sample: loans with non-empty borrower text after removing platform boilerplate, all but 42 of them issued 2007–2014."),
# 4.1 chronology
("The note followed an exploratory first pass on the data (5 September) and preceded the estimates reported here (18 September).","The note followed an exploratory first pass on the data (5 September), which included preliminary versions of both estimates, and preceded the confirmatory estimates reported here (18 September)."),
# 4.3 and appendix: one name for the shock variable
("and *λ* near zero for the unemployment rise, since observation does not depend on the local labor market.","and *λ* near zero for the unemployment change, since observation does not depend on the local labor market."),
("no role for density and *λ* < 0 for the unemployment rise, since a secure paycheck matters most when neighbors lose theirs.","no role for density and *λ* < 0 for the unemployment change, since a secure paycheck matters most when neighbors lose theirs."),
("| Affiliation × rise in unemployment (per SD) | | 0.975 (0.58) | | 0.988 (0.80) |","| Affiliation × subsequent change in unemployment (per SD) | | 0.975 (0.58) | | 0.988 (0.80) |"),
("| Rise in unemployment over loan life (per SD) | 1.028 | 0.001 |","| Largest subsequent change in unemployment over loan life (per SD) | 1.028 | 0.001 |"),
("| Affiliation × rise | 0.975 | 0.58 |","| Affiliation × change | 0.975 | 0.58 |"),
("| Positive control: teacher × rise; government × rise | 1.057; 1.004 | 0.29; 0.93 |","| Positive control: teacher × change; government × change | 1.057; 1.004 | 0.29; 0.93 |"),
('"Rise" = maximum rate in the years after origination within term, truncated at 2018, minus rate at origination (mean −0.62 pp, SD 0.55, so the measure is a maximum subsequent change and is negative for most loans); the period is mostly a recovery.','"Change" = maximum rate in the years after origination within term, truncated at 2018, minus rate at origination (mean −0.62 pp, SD 0.55, so the measure is a maximum subsequent change and is negative for most loans); the period is mostly a recovery.'),
# 4.4 AUC
("Adding affiliation on the H1 sample moves it from 0.7150 to 0.7151 (Appendix Table C7).","Adding affiliation on the H1 sample moves it by 0.0002, from 0.7150 to 0.7151 (Appendix Table C7)."),
# 5.1 maturity sentence
("Loans issued through 2013 had all reached maturity by the 2018Q4 release (10 of the 34,392 60-month loans issued in 2013 were still open), and so had the 36-month loans of 2014.","All but 10 of the loans issued through 2013 had reached maturity by the 2018Q4 release (the 10 were among the 34,392 60-month loans issued in 2013), and so had the 36-month loans of 2014."),
# 5.4 who did the B2 audit
("of 200 random affiliated titles, a reader classed 146 as clerical and 48 as non-clerical staff","of 200 random affiliated titles, the LLM coder of Appendix B classed 146 as clerical and 48 as non-clerical staff"),
("*Notes.* Precision 97 percent (98 percent counting D as half).","*Notes.* Codes assigned by the primary LLM coder of Appendix Table B1. Precision 97 percent (98 percent counting D as half)."),
# 5.5 wording
("Across quintiles of congregation density it is closer to one:","Across quintiles of congregation density it is closer to monotonic:"),
("Religious language shows no interaction with local religiosity (1.075, p = 0.50),","Religious language shows no detectable interaction with local religiosity (1.075, p = 0.50),"),
("0.763 in the middle and 0.721 where it fell least or rose, the reverse of the ordering a job-stability account predicts.","0.763 in the middle and 0.721 where it fell least or rose, not the ordering a job-stability account predicts, if anything the reverse."),
# 6.3 loan life to one decimal, as in Table C7
("That is a gap of 2.2 cents over an average 41-month life,","That is a gap of 2.2 cents over an average 41.5-month life,"),
("or over a 42-month average life an annualized net-loss gap of about 28 basis points the other way (Appendix Table C7).","or over a 42.1-month average life an annualized net-loss gap of about 28 basis points the other way (Appendix Table C7)."),
# C7 table rows
("| Net loss per dollar funded, flagged / cells (cents) | 5.5 / 7.7 | 7.1 / 6.1 |","| Net loss per dollar funded, flagged / cells (cents) | 5.51 / 7.72 | 7.08 / 6.09 |"),
("| Cross-validated AUC without / with the indicator | 0.7150 / 0.7151 | 0.6958 / 0.6958 |","| Cross-validated AUC without / with the indicator | 0.7150 / 0.7151 | 0.6958 / 0.6958 |\n| Change in AUC (bootstrap 95% CI) | 0.0002 (0.0001 to 0.0003) | 0.00002 (−0.0001 to 0.0001) |\n| Rate schedule: issue-month × sub-grade × term cells / loans at the cell's modal rate / most distinct rates in a cell | 7,642 / 94.7% / 5 | |"),
# C7 note
("*Notes.* Rows 1–4: terminated loans, cells defined by sub-grade and origination year, cell values weighted by the flagged loans' distribution across cells, net loss = 1 − total payments received per dollar funded, annualized gap = cumulative gap ÷ (mean life / 12). Rows 5–7: description sample, Table 6, column (3) controls, 2008–2014. Row 8: five-fold cross-validated logit on the H1 sample (affiliation) and the description sample (religious language, with the text dictionaries); the religious-language change is 0.00002 with a bootstrap 95% CI of −0.0001 to 0.0001. The rate-schedule check of Section 6.3 is tabulated in the replication package (rate_schedule_by_year.csv).",
 "*Notes.* Rows 1–4: terminated loans, cells defined by sub-grade and origination year, cell values weighted by the flagged loans' distribution across cells, net loss = 1 − total payments received per dollar funded, annualized gap = cumulative gap ÷ (mean life / 12), computed from unrounded values. Rows 5–7: description sample (N = 123,292), Table 6, column (3) controls. Rows 8–9: five-fold cross-validated logit on the H1 sample (affiliation, N = 253,105) and the description sample (religious language, with the text dictionaries), with a 300-draw paired bootstrap of the out-of-fold predictions. Row 10: all 2,260,668 loans in the file with a rate, grouped by issue month, sub-grade and term; 99.95 percent of loans sit at one of the two most common rates of their cell. The by-year version is in the replication package (rate_schedule_by_year.csv)."),
]
for old,new in R:
    c=s.count(old); assert c==1,(c,old[:80]); s=s.replace(old,new)
open("manuscript_v18.md","w").write(s); print("applied",len(R))
