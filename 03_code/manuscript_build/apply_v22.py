# Exact edits that turn manuscript_v21.md into manuscript_v22.md (16 October 2026), after the sixth check.
# Sources: descriptive_statistics.json / descriptive_statistics_table1.csv (make_table1.py on the rebuilt T.pkl/D.pkl:
# Table 1 rounding, 583 named institutions), v22_hierarchy.json (run_v22_hierarchy.py: Table 10 exploratory rows
# re-estimated with a documented rule, the original script being lost), step7a_prosper.json (Table 5 placebo model),
# the design note of 17 September 2026 and the exploratory document of 5 September 2026 (Section 4.1 wording).
s=open("manuscript_v21.md").read()
R=[
('date: "Draft v21, October 2026 (JEBO version)"','date: "Draft v22, October 2026 (JEBO version)"'),
# 1. Introduction: fewer repetitions of the platform name; share of affiliated titles
("The LendingClub file contains a second, quieter trace of religion that points the other way. LendingClub also asked borrowers for their job title, and about one in four hundred wrote",
 "The same file contains a second, quieter trace of religion that points the other way. The platform also asked borrowers for their job title, and roughly one in 450 wrote"),
("Neither difference is reflected in the interest rate, because LendingClub priced loans by grade, so investors",
 "Neither difference is reflected in the interest rate, because loans were priced by grade, so investors"),
("which by a rule fixed in the design note before these estimates were run lowers the claim.",
 "which, by a rule fixed in the design note before these estimates were run, lowers the claim."),
# 2.1
("A borrower who works for a church is embedded in that community more deeply than an ordinary member, because their employer is the congregation and their reputation among its members is their professional reputation.",
 "Borrowers who work for a church are embedded in that community more deeply than ordinary members, because their employer is the congregation and their reputation among its members is their professional reputation."),
("That cost should scale with how much observing the community does.","That cost should scale with how closely the community observes its members."),
# 3.3
("and moral language and length with lower (0.88 and 0.92 per log point, respectively).","and moral language and length with lower (0.88, and 0.92 per log point of length)."),
# 4.1: what the design note fixed, what the exploratory pass contained
("The hypotheses, this specification, the one-sided Holm procedure, the robustness checks of Section 4.2 and the decision rule for the DML check in Section 5.2 were fixed in a dated design note (17 September 2026). The note followed an exploratory first pass on the data (5 September), which included preliminary versions of both estimates, and preceded the confirmatory estimates reported here (18 September).",
 "The hypotheses, this specification, the one-sided Holm procedure, most of the robustness checks of Section 4.2 and the decision rule for the DML check in Section 5.2 were fixed in a dated design note (17 September 2026); the split by period is not in the note, and the neighbor-occupation comparison was added after the confirmatory estimates. The note followed an exploratory first pass on the data (5 September), which included preliminary versions of both estimates and several of the checks, and preceded the confirmatory estimates reported here (18 September)."),
# 5.1
("Exact matching gives 0.703 against those neighbors and 0.741 against the eight stable occupations.","Coarsened exact matching gives 0.703 against those neighbors and 0.741 against the eight stable occupations."),
("| CEM within the eight stable occupations | 0.741 | <0.001 | 3,008 / 58,032 (1,746 cells) |","| CEM within the eight stable occupations | 0.741 | <0.001 | 3,008 / 58,032 |"),
# Table 1 rounding (descriptive_statistics_table1.csv): FICO 703.947, amount 14,826.76, grade A-B 0.5704, staff default 69/608 = 0.1135
("| Religious-institution affiliation | 3,105 | 0.133 | 704.0 | 60,000 | 19.0 | 12.28 | 14,826 | 0.228 | 0.571 |","| Religious-institution affiliation | 3,105 | 0.133 | 703.9 | 60,000 | 19.0 | 12.28 | 14,827 | 0.228 | 0.570 |"),
("| — church staff (non-clergy) | 608 | 0.114 | 708.3 |","| — church staff (non-clergy) | 608 | 0.113 | 708.3 |"),
# Table 5 notes: which model each row comes from
("\"Clergy\" and \"Religious\" are two of Prosper's own occupation categories. Raw default: 22.7% vs 30.5%.",
 "\"Clergy\" and \"Religious\" are two of Prosper's own occupation categories. Raw default: 22.7% vs 30.5%. The clergy row is from a model without the placebo indicators; the placebo rows are from a model that enters all four occupations together, in which the clergy OR is 0.686 (p = 0.039)."),
# 5.4: staff raw default, named institutions, exploratory split
("Their raw default rate, 11.4 percent, is if anything lower than the clergy's 13.8,","Their raw default rate, 11.3 percent, is if anything lower than the clergy's 13.8,"),
("since only 606 of the 3,105 affiliated titles name a specific institution and recurring names such as \"First Baptist Church\" belong to many unrelated churches.",
 "since only 583 of the 3,105 affiliated titles name a specific institution and recurring names such as \"First Baptist Church\" belong to many unrelated churches."),
("An exploratory split of the affiliation indicator in the same table puts senior, lead and executive pastors at 0.452 and associate, youth and assistant pastors at 0.696, against 0.743 for the remaining affiliated titles, church staff included.",
 "An exploratory split of the affiliation indicator in the same table puts titles marked senior, lead or executive at 0.459 and titles marked associate, youth or assistant at 0.636, against 0.751 for the remaining affiliated titles, church staff included."),
("| Raw default rate, clergy / staff / other borrowers (%) | 13.8 / 11.4 / 20.0 | | |","| Raw default rate, clergy / staff / other borrowers (%) | 13.8 / 11.3 / 20.0 | | |"),
("| Exploratory split of the affiliation indicator: senior, lead or executive pastor | 0.452 | <0.001 | 497 |\n| — associate, youth or assistant pastor | 0.696 | 0.08 | 253 |\n| — other affiliated titles, church staff included | 0.743 | <0.001 | 2,355 |",
 "| Exploratory split of the affiliation indicator: senior, lead or executive title | 0.459 | <0.001 | 509 |\n| — associate, youth or assistant title | 0.636 | 0.050 | 235 |\n| — other affiliated titles, church staff included | 0.751 | <0.001 | 2,361 |"),
("*Notes.* Specification of Table 2, column (1), with the affiliation indicator replaced by two indicators (equation 2) or, in the exploratory rows, by three. Same sample, controls and clustering as Table 2. Raw default rates from Table 1.",
 "*Notes.* Specification of Table 2, column (1), with the affiliation indicator replaced by two indicators (equation 2) or, in the exploratory rows, by three. Same sample, controls and clustering as Table 2. Raw default rates from Table 1. The exploratory split is a keyword rule on the job title: associate, assoc, youth, assistant or asst; otherwise senior, sr, lead or executive; otherwise other."),
# Table 11 header
("| | Affiliation OR | Interaction OR | p (interaction) | N |","| | Main-effect OR | Interaction OR | p (interaction) | N |"),
# 6.3
("It measures, in the units investors use, the difference in realized losses that grade-based pricing did not reflect.","It measures, in the units investors use, the difference in realized net losses that grade-based pricing did not reflect."),
]
for old,new in R:
    c=s.count(old); assert c==1,(c,old[:80]); s=s.replace(old,new)
open("manuscript_v22.md","w").write(s); print("applied",len(R))
