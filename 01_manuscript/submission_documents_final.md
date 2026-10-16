# Submission documents for "Faith in Words, Faith in Community" (final manuscript, 16 October 2026)

Items in [square brackets] are for the author to confirm or fill in. Everything else matches the final manuscript (manuscript_JEBO.md / .docx / .pdf).

---

## 1. Title page (separate file)

**Faith in Words, Faith in Community: Religious Affiliation, Religious Language, and Default in Online Consumer Credit**

Dongwoo Kim
Division of Advanced IT, Baekseok University, [postal address], Cheonan, Republic of Korea
E-mail: dongwoo.kim@bu.ac.kr
ORCID: 0000-0003-2219-083X

Corresponding author: Dongwoo Kim (dongwoo.kim@bu.ac.kr)

*Keywords:* religion, social capital, consumer credit, credit risk, online lending, text analysis, signaling
*JEL:* D14, G21, G41, Z12

Funding: This work was supported by the Baekseok University Research Fund.

[Acknowledgements, if any. Suggested: "I thank the 2010 U.S. Religion Census (Association of Statisticians of American Religious Bodies) for the county file." Delete if not wanted.]

---

## 2. Highlights (separate file; 3–5 bullets, each at most 85 characters including spaces)

- Borrowers employed by religious institutions default less (odds ratio 0.69)
- Borrowers who invoke faith in their loan request default more, not less
- The affiliation advantage holds for church secretaries as well as clergy
- The advantage grows where congregations are denser, within and across ZIP areas
- Neither signal is reflected in LendingClub's grade-based interest rates

---

## 3. Declarations

**Declaration of competing interest.** The author declares that he has no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

**Funding.** This work was supported by the Baekseok University Research Fund. [Add a grant number if the university assigned one.] The same statement appears in the manuscript in the section "Funding" above the references and on the title page.

**Declaration of generative AI and AI-assisted technologies in the writing process.** Placed in the manuscript itself, as a section immediately above the references (Elsevier's instruction), in the final manuscript: "During the preparation of this work the author used Claude (Anthropic) in order to edit the English text, check the consistency of numbers between the text and the tables, and format the manuscript. After using this tool, the author reviewed and edited the content as needed and takes full responsibility for the content of the publication. The use of a large language model as a text coder in the research method is described in Section 3.2 and Appendix B." Repeat the same text in the submission system's declarations form if it asks for it.

**Data availability.** The LendingClub loan file (2007–2018Q4 release, Kaggle distribution) and the Prosper loan file (2005–2014, Kaggle distribution) are public and are not redistributed; the repository documents where to obtain them and how the analysis samples are rebuilt from them (`rebuild_TD.py`). The 2010 U.S. Religion Census county file is available from the Association of Religion Data Archives, the ZCTA–county relationship file from the U.S. Census Bureau, and county unemployment rates from the Bureau of Labor Statistics (Local Area Unemployment Statistics). All code, the estimates behind every table, the LLM coding prompt (codebook) and its record-level output, the coding validation samples and agreement statistics, the scripts that draw every figure, the exact edit history of the manuscript, and the dated design note of 17 September 2026 are available in the public repository at https://github.com/dongwoo2022008/25.Faith-in-Words-Faith-in-Community.

---

## 4. Figure captions (separate list)

**Figure 1.** Two channels through which religion enters a consumer-credit file. Solid boxes: institutional affiliation revealed by the job title, its proposed mechanism, and the confirmatory test H1; dashed boxes: religious language volunteered in the loan description, its mechanism, and H2. Local congregation density (2010 U.S. Religion Census) moderates H1 only. Estimates from Tables 2, 6 and 11; pricing gap from Section 6.3.

**Figure 2.** Religious-institution affiliation and default across specifications. ORs with 95% confidence intervals (log scale), grouped by the items of Section 5.1, with the dotted line at an OR of one. For the five estimates stored with a p-value but no standard error, the interval is the one implied by that p-value under normality.

**Figure 3.** Religious language and default: DML estimates by text representation. Partially linear DML with CatBoost nuisance functions and 5-fold cross-fitting, grouped by the specifications of Table 7 and Appendix Table C5; "twenty splits" aggregates twenty repeated sample splits by the median. Bars are 95% confidence intervals, and the dotted line marks zero.

**Figure 4.** Heterogeneity by local religiosity. Panel A: affiliation OR by quintile of congregation density in the borrower's ZIP3 area, full controls and state fixed effects. Panel B: religious-language OR by quintile of the adherence rate, Table 6, column (3) specification. Bars are 95% confidence intervals.

**Figure 5.** Cumulative default by months since origination, 36-month loans. Default is dated four months after the last payment. Comparison groups are reweighted to the treated group's grade × origination-year distribution. Panel A: 2,398 affiliated loans in the terminated sample; Panel B: 507 religious-language loans in the description sample.

**Appendix Figure C1.** Fake-dictionary permutation. Distribution of the residualized linear probability coefficient on an indicator for 1,000 random sets of non-religious words matched to the religious dictionary's document frequency, Table 6, column (3) controls partialled out. The solid line marks the coefficient of the actual dictionary (0.035); the dotted line marks the permutation mean (−0.003, SD 0.014). Five of the 1,000 random sets reach the actual value (one-sided p = 0.005).

Files: Figure1_channels.png, Figure2_forest.png, Figure3_dml.png, Figure4_density.png, Figure5_cumdefault.png, FigureC1_permutation.png (all 600 dpi).

---

## 5. Cover letter

Dongwoo Kim
Division of Advanced IT, Baekseok University
dongwoo.kim@bu.ac.kr

[Date]

The Editors
*Journal of Economic Behavior & Organization*

Dear Editors,

I am submitting the manuscript "Faith in Words, Faith in Community: Religious Affiliation, Religious Language, and Default in Online Consumer Credit" for consideration as a research article in the *Journal of Economic Behavior & Organization*.

The paper asks what a credit market can learn from religion, and its answer is about organization rather than belief. Religion enters a consumer-credit file in two ways: as an affiliation a borrower reports in a job title, and as language a borrower chooses to write in a loan request. In 1.34 million terminated LendingClub loans issued in 2007–2018, the two carry opposite information. Borrowers whose job titles place them in religious institutions, church secretaries and administrators as well as pastors, default about five percentage points less than borrowers with the same grade, credit score, income, debt burden, loan terms, state and origination year. The gap is larger where congregations are denser, including within ZIP areas, shows no detectable response to the period's small local unemployment shocks, and has the same sign on Prosper. Borrowers who invoke faith in their description default about three percentage points more in the confirmatory specification. Once the full text is represented the estimate keeps its size but can no longer be distinguished from zero, and I report it that way. Neither signal is reflected in the platform's grade-based rates, and neither is a field in the public file: I construct both from free text (job titles and loan descriptions) and link them to county religious membership and unemployment data.

I believe the paper fits the journal for three reasons. First, its central claim concerns an institution: a religious congregation appears to work for its members the way the group works in a group-lending scheme, which may enforce repayment through ties the lender never sees. Second, the second half of the paper is about communication under asymmetric information. A short framework shows why a costless, unverifiable message can carry information opposite to its sender's intent, and why the two religious signals can take opposite signs without any difference in belief. Third, the paper connects work this journal has published on religion and economic behavior (Valencia Caicedo, Dohmen and Pondorfer, 2023; Bentzen, 2021; Kirchmaier, Prüfer and Trautmann, 2018) with its work on default in the same LendingClub market (Croux, Jagtiani, Korivi and Vulanovic, 2020), which documents that occupation predicts default but does not ask what a religious occupation reveals.

The design is observational and does not identify either mechanism. The two hypotheses, the specification and the rule for lowering the claim on the second hypothesis were fixed in a dated design note before the confirmatory estimates were run, and I report where that rule applied. The analysis uses the public LendingClub and Prosper loan files and public county data from the U.S. Religion Census and the Bureau of Labor Statistics. The code, the estimates behind every table, the coding materials and the design note are in a public repository (https://github.com/dongwoo2022008/25.Faith-in-Words-Faith-in-Community). A large language model was used as a text coder in the method, which Appendix B documents, and for editing the English, which the declarations state.

The manuscript has not been published and is not under consideration elsewhere. I have no competing interests to declare. This work was supported by the Baekseok University Research Fund.

Thank you for considering the paper.

Sincerely,

Dongwoo Kim
