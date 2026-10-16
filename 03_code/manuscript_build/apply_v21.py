# Exact edits that turn manuscript_v20.md into manuscript_v21.md (16 October 2026), after the repository audit:
# (1) the design note's kappa threshold and which checks meet it (Appendix B1); (2) the design note's named
# sentence-transformer model and the fallback that was applied (Appendix C5 note; run_log_2026-09-18.md records the
# blocked download); (3) the top-two-rates share corrected to 99.94 percent after verify_rate_schedule.py was rerun
# with five-decimal output (rate_schedule_by_year.csv: 0.99942).
s=open("manuscript_v20.md").read()
R=[
('date: "Draft v20, October 2026 (JEBO version)"','date: "Draft v21, October 2026 (JEBO version)"'),
("Because 80% of the sample is religious, the prevalence-adjusted κ for that binary is 0.69 (Byrt et al., 1993).",
 "Because 80% of the sample is religious, the prevalence-adjusted κ for that binary is 0.69 (Byrt et al., 1993). The design note set κ of 0.7 as the bar for the coding. The four-way type clears it in both checks; the human coder's religious versus non-religious binary (0.55, 0.69 prevalence-adjusted) and the frame (0.48) do not. The frame enters no estimate, and the binary enters only Table 8, which should be read with that in mind."),
("*Notes.* Description sample of Table 6. DML partially linear model with CatBoost nuisance functions and 5-fold cross-fitting, with doc2vec after Le and Mikolov (2014);",
 "*Notes.* Description sample of Table 6. DML partially linear model with CatBoost nuisance functions and 5-fold cross-fitting, with doc2vec after Le and Mikolov (2014). The design note named a sentence-transformer model (all-MiniLM-L6-v2) for the text representation; its download was blocked in the computing environment, so the note's fallback, TF-IDF with SVD, was used and the spaCy word vectors and doc2vec were added;"),
("99.95 percent of loans sit at one of the two most common rates of their cell","99.94 percent of loans sit at one of the two most common rates of their cell"),
]
for old,new in R:
    c=s.count(old); assert c==1,(c,old[:80]); s=s.replace(old,new)
open("manuscript_v21.md","w").write(s); print("applied",len(R))
