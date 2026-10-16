# Exact edits that turn manuscript_v18.md into manuscript_v19.md (16 October 2026), after the fourth check.
# New numbers from run_v19_extras.py / v19_extras.json on the rebuilt T.pkl/D.pkl: Table 2 column (4) SE and AME
# (OR 0.690 reproduced), column (5) AME (OR 0.697 and SE 0.043 reproduced), and the Appendix Table C7 cell
# comparison reproduced exactly (net loss = default x (1 - payments/funded); mean "life" = mean contractual term)
# and recomputed with term in the cell definition and with realized life. AUC CI digits from
# lc_two_signal_analysis_results.json and v18_auc.json. Coding partition: 820 records, one label each (coding CSV).
s=open("manuscript_v18.md").read()
R=[
('date: "Draft v18, October 2026 (JEBO version)"','date: "Draft v19, October 2026 (JEBO version)"'),
# Table 2 columns (4) and (5)
("| SE | 0.041 | 0.087 | 0.060 | | 0.043 | 0.006 |","| SE | 0.041 | 0.087 | 0.060 | 0.041 | 0.043 | 0.006 |"),
("| AME | −4.8 pp | −5.6 pp | −4.2 pp | | | −4.3 pp |","| AME | −4.8 pp | −5.6 pp | −4.2 pp | −4.9 pp | −4.3 pp | −4.3 pp |"),
# 6.3 loss definition and term
("That is a gap of 2.2 cents over an average 41.5-month life, or an annualized realized net-loss gap of roughly 64 basis points relative to the cell.","That is a gap of 2.2 cents over an average 41.5-month term, or an annualized net-loss gap of roughly 64 basis points relative to the cell."),
("or over a 42.1-month average life an annualized net-loss gap of about 28 basis points the other way (Appendix Table C7).","or over a 42.1-month average term an annualized net-loss gap of about 28 basis points the other way (Appendix Table C7)."),
("Loss is realized cash flow, one dollar minus total payments received per dollar funded, so it nets out interest and recoveries. The benchmark weights sub-grade-year cells by the distribution of the flagged loans, and the annual figure divides the cumulative gap by the average loan life.",
 "Loss is the realized shortfall on defaulted loans, one dollar minus total payments received per dollar funded, recoveries included, and zero for repaid loans. The benchmark weights sub-grade-year cells by the distribution of the flagged loans, and the annual figure divides the cumulative gap by the average contractual term. Adding term to the cell definition moves the two figures to 67 and 29 basis points."),
# C7 rows
("| Net loss per dollar funded, flagged / cells (cents) | 5.51 / 7.72 | 7.08 / 6.09 |","| Net loss on defaulted loans per dollar funded, flagged / cells (cents) | 5.51 / 7.72 | 7.08 / 6.09 |"),
("| Mean loan life (months) | 41.5 | 42.1 |","| Mean contractual term (months) | 41.5 | 42.1 |"),
("| Annualized realized net-loss gap (basis points) | −64 | +28 |","| Annualized net-loss gap (basis points) | −64 | +28 |"),
("| Change in AUC (bootstrap 95% CI) | 0.0002 (0.0001 to 0.0003) | 0.00002 (−0.0001 to 0.0001) |","| Change in AUC (bootstrap 95% CI) | 0.00018 (0.00005 to 0.00029) | 0.00002 (−0.00010 to 0.00014) |"),
# C7 note
("*Notes.* Rows 1–4: terminated loans, cells defined by sub-grade and origination year, cell values weighted by the flagged loans' distribution across cells, net loss = 1 − total payments received per dollar funded, annualized gap = cumulative gap ÷ (mean life / 12), computed from unrounded values. Rows 5–7: description sample (N = 123,292), Table 6, column (3) controls. Rows 8–9:",
 "*Notes.* Rows 1–4: terminated loans, cells defined by sub-grade and origination year (254 cells for affiliation, 165 for religious language), cell values weighted by the flagged loans' distribution across cells; net loss = default × (1 − total payments received per dollar funded), so repaid loans count as zero; annualized gap = cumulative gap ÷ (mean contractual term of the flagged loans / 12), computed from unrounded values. With term added to the cell definition the gaps are −67 and +29 basis points; dividing by realized life to the last payment (23.3 and 28.2 months) instead of contractual term gives −114 and +42. Rows 5 and 7: OLS; row 6: logit; description sample (N = 123,292), Table 6, column (3) controls, SE clustered by state. Rows 8–9:"),
# 4.4 AUC digits
("Adding affiliation on the H1 sample moves it by 0.0002, from 0.7150 to 0.7151 (Appendix Table C7).","Adding affiliation on the H1 sample moves it by 0.00018, from 0.7150 to 0.7151 (Appendix Table C7)."),
# B1 coder description
("The coder was Claude Fable 5.1 (Anthropic), run as twelve parallel instances in the Claude application on 18 September 2026 at the application's default settings; no sampling temperature was set.",
 "The coder was Claude Fable 5.1 (Anthropic, model ID claude-fable-5-1), run as twelve parallel instances in the Claude application on 18 September 2026, each instance reading a disjoint share of the records so that every record received one label; the application does not expose a sampling temperature or other decoding settings, so the coding ran at its defaults."),
]
for old,new in R:
    c=s.count(old); assert c==1,(c,old[:80]); s=s.replace(old,new)
open("manuscript_v19.md","w").write(s); print("applied",len(R))
