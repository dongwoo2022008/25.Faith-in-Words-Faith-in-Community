# Exact edits that turned manuscript_v13.md into manuscript_v14.md (5 October 2026), after a flag-only review
# by three independent reviewers checked against the stored estimates. Run on a copy of v13 named manuscript_v14.md;
# each old string must occur exactly once.
s=open("manuscript_v14.md").read()
R=[
('date: "Draft v13, October 2026 (JEBO version)"','date: "Draft v14, October 2026 (JEBO version)"'),
("even under ZIP-level fixed effects","even under ZIP3 fixed effects"),
("and here it sits on the borrower's side of the transaction rather than the lender's","and here that community sits on the borrower's side of the transaction rather than the lender's"),
("Section 5 presents the results, Section 6 draws the results together","Section 5 presents the results, Section 6 draws them together"),
("discriminate between it and the main rival account, that church jobs are simply stable","discriminate between it and the main rival account, namely that church jobs are simply stable"),
("So non-clergy church employees should show the effect as strongly as clergy, since the community is the same. The effect should be larger where congregations are denser","So non-clergy church employees should show the gap as strongly as clergy, since the community is the same. The gap should be larger where congregations are denser"),
("Two free-text fields matter here: the job title the borrower typed in (`emp_title`) and the loan description (`desc`), which investors could read while the loan was listed.","Three free-text fields matter here: the job title the borrower typed in (`emp_title`), the short loan title (`title`) and the loan description (`desc`), the last two of which investors could read while the loan was listed."),
("The description subsample has 123,292 loans (15.3 percent defaulted) and is an earlier and somewhat riskier slice of the platform's history, which is why every specification carries origination-year fixed effects. Writing a description was a choice, and Appendix Table C2 shows that origination year, grade and loan size predict it while affiliation does not (odds ratio (OR) 1.02, p = 0.81), so the narrative results describe borrowers who chose to write.",
 "The description subsample has 123,292 loans (15.3 percent defaulted) and is an earlier slice of the platform's history with a lower default rate, which is why every specification carries origination-year fixed effects. Writing a description was a choice. Appendix Table C2 shows that origination year, grade and loan size predict it while affiliation does not, with an odds ratio (OR) of 1.02 (p = 0.81), so the narrative results describe borrowers who chose to write."),
("when the title or text matches a dictionary of religious terms","when the loan title or the description text matches a dictionary of religious terms"),
("Appendix B reports agreement with a second model (κ = 0.86) and a human coder (κ = 0.72 on the four-way type, lower on the religious/non-religious boundary), and a search for religious content the dictionary misses, which amounts to a few dozen descriptions in the whole file.",
 "Appendix B reports agreement with a second model (κ = 0.86) and a human coder (κ = 0.72 on the four-way type, lower on the religious/non-religious boundary). Appendix B also reports a search for religious content the dictionary misses, which amounts to a few dozen descriptions in the whole file."),
("(0.88, and 0.92 per log point)","(0.88 and 0.92 per log point, respectively)"),
("I use the 2010 U.S. Religion Census county file (Grammich et al., 2012), the source behind the religiosity measures used in corporate finance since Hilary and Hui (2009), linked to three-digit ZIP areas (ZIP3) through the Census ZCTA–county relationship file with population weights.",
 "I use the 2010 U.S. Religion Census county file (Grammich et al., 2012), the source behind the religiosity measures used in corporate finance since Hilary and Hui (2009). I link the county file to three-digit ZIP areas (ZIP3) through the Census ZIP Code Tabulation Area (ZCTA)–county relationship file with population weights."),
("I merge BLS county unemployment rates","I merge Bureau of Labor Statistics (BLS) county unemployment rates"),
("Λ the logistic function, and the *α*ₖ₍ᵢ₎ fixed effects for origination year, grade, purpose, employment length, homeownership, income verification and state.","Λ the logistic function. The *α*ₖ₍ᵢ₎ are fixed effects for origination year, grade, purpose, employment length, home ownership, income verification and state."),
("a draw made only to keep the fixed-effects logit tractable (the full sample and five further draws give the same estimate, Appendix Table C3).","a draw made only to keep the fixed-effects logit tractable. The full sample and five further draws give the same estimate (Appendix Table C3)."),
("*Mission-driven jobs.* If it came instead with the kind of person","*Mission-driven jobs.* If the advantage came instead with the kind of person"),
("re-estimate the residualized effect for each (a linear probability coefficient after partialling out the controls of the confirmatory specification), and place the religious estimate in that distribution.","re-estimate the residualized coefficient for each (a linear probability coefficient after partialling out the controls of the confirmatory specification). I then place the religious estimate in that distribution."),
("LendingClub's early years were small, its borrowers chose a market few had heard of, and its default rates were higher (Section 3.1).","LendingClub's early years were small, and its borrowers chose a market few had heard of."),
("2008–2014, the years in which descriptions exist and H2 is tested","2008–2014, the years the description sample covers and H2 is tested"),
("A vocation or job-security account","A vocation or job-stability account"),
("which measures how much the affiliation effect changes with a one standard deviation change","which measures how much the affiliation coefficient changes with a one standard deviation change"),
("since a denser congregation observes its members more closely","since members are observed more closely where congregations are denser"),
("moves the area under the ROC curve by less than 0.0001, and indicators that flag a quarter of one percent of borrowers cannot improve aggregate prediction.","moves the area under the receiver operating characteristic (ROC) curve by less than 0.0001, and indicators that flag a fraction of one percent of borrowers cannot materially improve aggregate prediction."),
("the comparison default rate falls from 20.1 to 17.5 percent","the comparison default rate in the random draw falls from 20.1 to 17.5 percent"),
("(ATTE −0.042, p<0.001)","(average treatment effect on the treated, ATTE, −0.042, p < 0.001)"),
("is −4.3 pp (standard error 0.6).","is −4.3 pp (standard error 0.6 pp)."),
("| Robustness value RV (q=1) |","| Robustness value (RV), q = 1 |"),
("the confirmatory specification of Section 4.1. Oster's δ is the ratio of selection on unobservables to selection on observables that would drive the coefficient to zero, computed from the uncontrolled and controlled coefficients and R² with R²max set to 1.3 times the controlled R² (Oster, 2019); β* is the coefficient that remains if that ratio is one.",
 "the confirmatory specification of Section 4.1. Oster's δ is the ratio of selection on unobservables to selection on observables that would drive the coefficient to zero. It is computed from the uncontrolled and controlled coefficients and R² with R²max set to 1.3 times the controlled R² (Oster, 2019). β* is the coefficient that remains if that ratio is one."),
("column (1) for H1 and, for H2, on the description sample with log length and the six text dictionaries added, the confirmatory specification of Section 4.1.","column (1) for H1. For H2, the sample is the description sample with log length and the six text dictionaries added, the confirmatory specification of Section 4.1."),
("and with the full set of controls the OR is 0.684 (p = 0.037), while the placebo occupations on Prosper (teachers, police, nurses) are all indistinguishable from one.","and with the full set of controls the OR is 0.684 (p = 0.037). The placebo occupations on Prosper (teachers, police, nurses) are all indistinguishable from one."),
("Replacing log length with length deciles (column (1)) changes nothing","Replacing log length with length deciles (column (1)) changes little (1.274)"),
("and +3.6 on the validated indicator (p = 0.028)","and +3.6 on the coded indicator (p = 0.028)"),
("It is +2.8 with a TF-IDF factorization (p = 0.059)","It is +2.8 with a term frequency–inverse document frequency (TF-IDF) factorization (p = 0.059)"),
("cannot pin down a three-point effect once","cannot pin down a three-point association once"),
("H2 passes its confirmatory test and every linear placebo","H2 passes its confirmatory test and both placebos (Table 8 and the random-word permutation below)"),
("give 0.948 (p = 0.88): the association sits in the religious content, not in the words.","give 0.948 (p = 0.88). The association sits in the religious content, not in the words."),
("formulaic invocations carry the effect (1.385, p = 0.001, 467 loans), identity claims point the same way on too few loans to tell (1.460, n = 34), and descriptions that report religious *practice* show no elevated default (0.988, n = 82). The split is exploratory and the cell is small,",
 "formulaic invocations carry the association (1.385, p = 0.001, n = 467). Identity claims point the same way on too few loans to tell (1.460, n = 34), and descriptions that report religious *practice* show no elevated default (0.988, n = 82). The split is exploratory and the identity-claims cell is small,"),
("against a permutation mean of −0.003 (SD 0.014), and one random word set in two hundred does as well","against a permutation mean of −0.003 (standard deviation 0.014), and only one random word set in two hundred reaches that value"),
("Neither estimate moves when the other is added.","The religious-language estimate is unchanged from Table 6 (1.281 alone)."),
("*Notes.* Specification of Table 6 column (3). 20 loans carry both indicators.","*Notes.* Specification of Table 6, column (3). Twenty loans carry both indicators."),
("If the affiliation effect came from the vocation, a pastor's vows or a professional identity in which unpaid debt is a scandal,","If the affiliation gap came from the vocation itself, from a pastor's vows or from a professional identity in which unpaid debt is a scandal,"),
("since only 606 affiliated titles name an institution","since only 606 of the 3,105 affiliated titles name a specific institution"),
("An exploratory split of the clerical titles in the same table puts senior, lead and executive pastors at 0.452 and associate and youth pastors at 0.696, against 0.743 for the remaining affiliated titles.","An exploratory split of the affiliation indicator in the same table puts senior, lead and executive pastors at 0.452 and associate, youth and assistant pastors at 0.696, against 0.743 for the remaining affiliated titles, church staff included."),
("| Exploratory split of clerical titles: senior, lead or executive pastor |","| Exploratory split of the affiliation indicator: senior, lead or executive pastor |"),
("| — other affiliated titles | 0.743 |","| — other affiliated titles, church staff included | 0.743 |"),
("while the evangelical share is unrelated to default.","and the evangelical share, estimated without state fixed effects, is unrelated to default (1.030, p = 0.15)."),
("so the individual effect is not local religiosity in disguise","so the individual association is not local religiosity in disguise"),
("But the individual effect varies with local religiosity.","But the individual association varies with local religiosity."),
("*Labor-market shocks.* The income-stability account predicts","*Labor-market shocks.* The job-stability account predicts"),
("But the same interaction for teachers and government employees, a positive control, does not widen either. The shocks of a period that was mostly a recovery are too small to reveal an income-stability mechanism for any occupation.","But the gap for teachers and government employees, a positive control, does not widen either. The shocks of a period that was mostly a recovery are too small to reveal a job-stability mechanism for any occupation."),
("as that account predicts, but it remains below one among them (0.795, p = 0.036).","as that account predicts, but the affiliation OR remains below one among them (0.795, p = 0.036)."),
("as they did in the Indonesian crisis (Chen, 2010), which would cushion an affiliated borrower before the loan, although shared ties can spread default as well (Adbi et al., 2024).","as they did in the Indonesian crisis (Chen, 2010). Such insurance would cushion an affiliated borrower before default, although shared ties can spread default as well (Adbi et al., 2024)."),
("puts the affiliation hazard ratio at 0.686 and flat over the life of the loan, while religious language has no effect on hazard in the first year (0.956, p = 0.85) and its effect appears only later (1.274, p = 0.027).","puts the affiliation hazard ratio (HR) at 0.686, flat over the life of the loan. Religious language is unrelated to hazard in the first year (0.956, p = 0.85), and its association appears only later (1.274, p = 0.027)."),
("In corporate debt county religiosity earns a lower spread","In corporate debt, county religiosity earns a lower spread"),
("If they resemble the ones I find the omission biases","If they resemble the ones I find, the omission biases"),
("*Notes.* cloglog on loan-month panels,","*Notes.* Complementary log-log (cloglog) model on loan-month panels,"),
("as a reason to trust them (","as a reason to trust him or her ("),
("Primary coding by an LLM coder over all 820","Primary coding by a large language model (LLM) coder over all 820"),
("and 0.48 for frame; the human coder reads 11 of the 40","and 0.48 for frame. The human coder reads 11 of the 40"),
("The disagreements sit at two boundaries, formulaic invocation against non-religious (17 records) and identity claim against non-religious (8 records), rather than in the practice category, where the two agree on 36 of 40.","Most of the 31 disagreements sit at two boundaries, formulaic invocation against non-religious (17 records) and identity claim against non-religious (8 records). In the practice category the two agree on 36 of 40."),
("Measurement completeness: a classifier trained with all explicit religious words masked (CV AUC 0.92) ranked the 122,611 unflagged descriptions, and the LLM coder found","Measurement completeness: a classifier trained with all explicit religious words masked (cross-validated area under the ROC curve 0.92) ranked the 122,611 unflagged descriptions. The LLM coder found"),
("| Grade B / C / D / E / F / G (vs. A) |","| Grade B / C / D / E / F / G (vs A) |"),
("| + spaCy word vectors, PCA-50 |","| + spaCy word vectors, 50 principal components (PCA-50) |"),
("| + TF-IDF-SVD100 |","| + TF-IDF, 100 singular-value-decomposition (SVD) components |"),
("*Notes.* BLS LAUS county annual unemployment 2008–2018","*Notes.* BLS Local Area Unemployment Statistics (LAUS) county annual unemployment 2008–2018"),
# applied after a first render
("in an anonymous trust game (Kirchmaier et al., 2018), and in lending, unverifiable self-description","in an anonymous trust game (Kirchmaier et al., 2018). In lending, unverifiable self-description"),
]
for old,new in R:
    c=s.count(old); assert c==1,(c,old[:70]); s=s.replace(old,new)
s=s.replace("comparing affiliated borrowers with those jobs alone should shrink it","comparing affiliated borrowers with borrowers in those jobs alone should shrink it")  # two occurrences
s=s.replace("Table 6 column (","Table 6, column (")
s=s.replace("homeownership","home ownership")
for a,b in [("terminal description sample","terminated description sample"),("terminal loans","terminated loans"),("terminal sample","terminated sample")]:
    s=s.replace(a,b)
old_hdr="| | OR | p-value | AME |\n|---|---:|---:|---:|\n| Religious-institution affiliation | 1.017 | 0.81 | +0.2 pp |\n| Interest rate (per SD) |"
assert s.count(old_hdr)==1
s=s.replace(old_hdr,"| | OR (per unit) | p-value | AME (per SD) |\n|---|---:|---:|---:|\n| Religious-institution affiliation | 1.017 | 0.81 | +0.2 pp |\n| Interest rate |")
for lab in ["FICO","Log income","DTI","Log amount"]:
    assert s.count(f"| {lab} (per SD) |")==1; s=s.replace(f"| {lab} (per SD) |",f"| {lab} |")
oldn="Same controls and state fixed effects as Table 2, with SE clustered by state. Pseudo-R² 0.24"
assert s.count(oldn)==1
s=s.replace(oldn,"Same controls and state fixed effects as Table 2, with SE clustered by state. ORs are per unit of the variable (one percentage point of rate, one FICO point, one log point of income or amount, one DTI point); AMEs are per standard deviation. Pseudo-R² 0.24")
open("manuscript_v14.md","w").write(s); print("applied",len(R)+9)
