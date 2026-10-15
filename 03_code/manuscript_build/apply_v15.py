# Exact edits that turned manuscript_v14.md into manuscript_v15.md (5 October 2026), in response to an external
# review of v14 checked against the stored estimates. Run on a copy of v14; each old string must occur exactly once.
s=open("manuscript_v14.md").read()
R=[
('date: "Draft v14, October 2026 (JEBO version)"','date: "Draft v15, October 2026 (JEBO version)"'),
("The same platform contains a second, quieter trace of religion that points the other way.","The LendingClub file contains a second, quieter trace of religion that points the other way."),
("Same platform, same years, same controls, opposite signs.","Same platform, same controls, opposite signs."),
("historical missionary activity left a lasting trace in local trust (Deng et al., 2025)","historical missionary activity left a lasting trace in local social capital (Deng et al., 2025)"),
("I use the public LendingClub loan-level file covering loans issued from June 2007 through December 2018 (2,260,701 loans).","I use the public LendingClub loan-level file covering loans issued from June 2007 through December 2018 (2,260,701 loans), with loan status as of the 2018Q4 release."),
("Descriptions that contain it are three times longer than the median (68 versus 23 words).","The median description that contains it is three times as long as the median other description (68 versus 23 words)."),
("and compute, for each loan, the rate at issue and the largest rise over the loan's term.","and compute, for each loan, the rate at issue and the largest subsequent change over the loan's term, truncated at 2018 for loans whose term runs past the data."),
("A vocation or job-stability account predicts *β*₁ < *β*₂, since only the clergy carry the vows and the tenure.","A vocation or job-stability account predicts *β*₁ < *β*₂, on the added assumption that clergy carry the vows and the more secure tenure."),
("The advantage is weaker in the later, lower-default years but far from gone, so the finding is not a property of the platform's early, self-selected borrowers.","The advantage is weaker in the later years but far from gone, so the finding is not a property of the platform's early, self-selected borrowers. The 2008–2014 column also serves as a check on sample selection. Every loan issued in those years had reached maturity by the 2018Q4 release, so keeping only terminated loans selects nothing there, whereas among 2015–2018 loans a terminated status can mean early repayment or early default."),
("Column (6): DML partially linear model, CatBoost nuisance, 5-fold cross-fitting, reported on the probability scale (average treatment effect on the treated, ATTE, −0.042, p < 0.001), so no OR is shown.","Column (6): DML partially linear model, CatBoost nuisance, 5-fold cross-fitting; the entry is the partially linear coefficient on the probability scale, so no OR is shown. The average treatment effect on the treated (ATTE) from the same run is −0.042 (p < 0.001)."),
("Intervals for estimates reported with p-values only are recovered from the p-value.","Intervals for estimates stored with p-values only are recovered from the exact Wald p-value."),
("Column (2): each flagged loan matched to five nearest in length within grade×year.","Column (2): each flagged loan matched with replacement to its five nearest neighbors in length within grade×year; N counts distinct loans (681 treated, 2,891 controls)."),
("Religious wording cannot be separated from the information the rest of the text already carries, although the point estimate gives no sign that the text absorbs it.","The rich-text specifications do not estimate a distinct association for religious wording with enough precision to separate it from the rest of the text, although the point estimate gives no sign that the text absorbs it."),
("Table 10 splits the indicator.","Table 10 splits the indicator by whether the title contains a clerical role word. That is a keyword split, not a judgment of each role, and the audit in Appendix Table B2 shows how close the two are: of 200 random affiliated titles, a reader classed 146 as clerical and 48 as non-clerical staff, against the 80:20 keyword split. Misclassification of the few titles such as \"Director of Music Ministry\" that carry a clerical word in a staff role would make the two groups more alike, which works against finding a difference."),
("The differential remains under 601 ZIP3 fixed effects, which absorb every time-invariant feature of the area:","The differential remains under 601 ZIP3 fixed effects, which absorb every time-invariant feature of the area, including density itself, so the interaction asks whether the within-area affiliation gap is larger in denser areas:"),
("and the tie is visible to a congregation that will know if the loan goes unpaid.","and the tie is visible to a congregation that can learn if the loan goes unpaid."),
("An unobserved trait could account for the estimate only if it were several times as strong as all observed controls combined.","Under Oster's proportional-selection assumption, an unobserved trait could account for the estimate only if it were several times as strong as all observed controls combined."),
("Borrowers who invoke faith do not fail early, as they would if the language marked distress at application. Instead, they fail after a year.","Religious language is not associated with a higher hazard in the first year, as it would be if the language marked distress at application. The positive association appears only after a year."),
("The advantage grows where congregations are denser in the borrower's ZIP area, and it grows within ZIP areas as well as across them.","The advantage grows where congregations are denser in the borrower's ZIP area, and the within-area gap is larger in denser areas once ZIP3 fixed effects are added."),
("or roughly 64 basis points a year of yield above the cell.","or an annualized realized net-loss gap of roughly 64 basis points relative to the cell."),
("about 28 basis points a year below the cell.","an annualized net-loss gap of about 28 basis points the other way."),
("| Affiliation (clergy definition) |","| Affiliation (all 3,105 affiliated loans) |"),
("Comparison groups subsampled.","Comparison groups subsampled (30,000 loans for affiliation, 8,000 for religious language)."),
("Primary coding by a large language model (LLM) coder over all 820 flagged records (717 with description text, 103 title-only) against the codebook above.","Primary coding by a large language model (LLM) coder over all 820 flagged records (717 with description text, 103 title-only) against the codebook above; the prompt, model identifiers and settings are in the replication package."),
("\"Rise\" = maximum rate in years after origination within term, minus rate at origination (mean −0.62 pp, SD 0.55); the period is mostly a recovery.","\"Rise\" = maximum rate in the years after origination within term, truncated at 2018, minus rate at origination (mean −0.62 pp, SD 0.55, so the measure is a maximum subsequent change and is negative for most loans); the period is mostly a recovery."),
# applied after a first render
("With each group as the only comparison the affiliation OR is 0.690, 0.679 and 0.747, and exact matching gives","Against social-work borrowers alone the affiliation OR is 0.690, against healthcare workers alone 0.679, and against education workers alone 0.747. Exact matching gives"),
("If the affiliation effect were a property of mission-driven","If the affiliation gap were a property of mission-driven"),
("**Table 3. Occupation-selection tests for the affiliation effect**","**Table 3. Occupation-selection tests for the affiliation estimate**"),
("Appendix Table A2. Affiliation effect by tercile","Appendix Table A2. Affiliation estimate by tercile"),
]
for old,new in R:
    c=s.count(old); assert c==1,(c,old[:70]); s=s.replace(old,new)
old="| H1 estimation sample (treated plus random draw of 250,000) | 253,105 |"
assert s.count(old)==1
s=s.replace(old, old+"\n| — of which issued in 2007 | 0 |")
open("manuscript_v15.md","w").write(s); print("applied",len(R)+1)
