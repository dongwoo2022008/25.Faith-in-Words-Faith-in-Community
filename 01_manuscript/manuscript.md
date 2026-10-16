---
title: "Faith in Words, Faith in Community: Religious Affiliation, Religious Language, and Default in Online Consumer Credit"
author: "Dongwoo Kim, Division of Advanced IT, Baekseok University"
date: "October 2026"
---

**Abstract.** Religion enters a consumer-credit file in two ways: as an affiliation a borrower reports in a job title, and as language a borrower chooses to use in a loan request. Using 1.34 million terminated LendingClub loans issued in 2007–2018, I find that the two are associated with default in opposite directions. Borrowers whose job titles place them in religious institutions (pastors and ministers, but also church secretaries and administrators) default about five percentage points less than borrowers with the same grade, credit score, income, debt burden, loan terms, state and origination year. The estimate changes little with controls for eight stable occupations, with matching to social-service, education and healthcare workers, who show no comparable advantage, and with entropy balancing and double machine learning. Its sign holds in a smaller Prosper sample. The gap is larger where local congregations are denser, including within ZIP areas, and shows no detectable response to the period's small local unemployment shocks, the response a job-stability account would predict. Borrowers who invoke faith in their loan description default about three percentage points more in the confirmatory specification. Once the full text is represented, the estimate keeps its size but is no longer distinguishable from zero, so religious wording cannot be separated from the rest of the text. Neither signal is reflected in the platform's grade-based rates. The pattern is consistent with religious community acting as borrower-side social collateral, and with religious language as a low-cost, unverifiable signal whose association with default works against its sender.

*Keywords:* religion, social capital, consumer credit, credit risk, online lending, text analysis, signaling.
*JEL:* D14, G21, G41, Z12.

# 1. Introduction

Borrowers on the early online lending platforms, then called peer-to-peer, were asked to say something about themselves, and LendingClub gave them a free-text box. Some wrote nothing, some wrote a paragraph about the debts they wanted to consolidate, and a small number wrote about God. "Thank you and God bless." "As a Christian I believe in paying my debts." "Monthly budget: tithe $529, rent $900…" These sentences are rare, 717 among 125,811 loan descriptions, and it is tempting to treat them as noise. Netzer et al. (2019) did not: in their study of Prosper applications, mentions of God were among the words that appeared more often in the text of borrowers who later defaulted.

The LendingClub file contains a second, quieter trace of religion that points the other way. The platform also asked borrowers for their job title, and roughly one in 450 wrote "pastor," "minister," "chaplain," "church administrator," or "church secretary." I call a borrower affiliated when the job title places the job inside a religious institution in this way. Those borrowers default less: 13.3 percent against 20.0 percent in the raw data, and about five percentage points less after I condition on grade, FICO, income, debt-to-income, loan terms, state and year. Borrowers who talk about faith in their loan request go the other way, defaulting about three percentage points more than their scores predict. Same platform, same controls, opposite signs. Neither difference is reflected in the interest rate, because loans were priced by grade, so investors earned more than the grade implied on loans to church employees and less on loans that invoked faith. I document both facts in LendingClub's public file of terminated loans, in which neither signal is a field, and replicate the first on Prosper.

This paper is about that contrast, and about what lies behind the second half of it. The question is whether the two traces religion leaves in a credit file carry the same information about repayment, and if they do not, what separates them. My claim is narrow. I do not argue that religion causes repayment, nor do I offer a religious credit score, since the signals are too rare to move a predictive model. What I argue is that religion reaches a credit market through two channels that carry different information. Faith that is *professed*, invoked in a request for money, looks like a low-cost signal. It costs nothing to write, cannot be verified, and travels with hardship and appeals for help. Its association with default is consistent in sign but not strong. Faith as *belonging*, a job inside a congregation, looks like a commitment with a community attached. Its association with default is large and stable across a decade. It is present for the church secretary as much as for the pastor, and it is stronger where there are more churches nearby. The broader point concerns organization rather than piety: a congregation may enforce repayment through ties that the lender never sees and cannot contract on.

The evidence within the affiliated group is what moves the paper from a curiosity about words to a claim about mechanism. The obvious alternative reading of the clergy result is that pastors have steady jobs, but three findings push against reading it that way alone. Non-clergy church employees, whose pay and job security resemble those of secretaries and administrators anywhere, default as little as the clergy do. The affiliation gap grows where congregations are denser in the borrower's ZIP area, which job stability alone would not produce, even under ZIP3 fixed effects. And it shows no detectable change when local unemployment rises over the life of the loan. None of these is a natural experiment. Still, together they fit the pattern one would expect if a religious congregation works, for its members, the way the group in a group-lending scheme works for its borrowers (Besley and Coate, 1995; Karlan, 2007). Such a group is a community that observes financial conduct and in which default has a cost beyond the credit file, and here that community sits on the borrower's side of the transaction rather than the lender's.

![Figure 1. Two channels through which religion enters a consumer-credit file. Solid boxes: institutional affiliation revealed by the job title, its proposed mechanism, and the confirmatory test H1; dashed boxes: religious language volunteered in the loan description, its mechanism, and H2. Local congregation density (2010 U.S. Religion Census) moderates H1 only. Estimates from Tables 2, 6 and 11; pricing gap from Section 6.3.](fig1_channels.png){width=6.3in}

The design has clear limits. There is no instrument, and the public file has no borrower identifiers that would allow within-borrower comparison, so church employees may differ from other borrowers in ways I cannot observe. I report how strong an unobserved confounder would have to be to erase the estimate (Section 5.1), and I name, for each piece of evidence, what it rules out and what it does not. The narrative result, the one from the loan descriptions, I treat more guardedly still. It is estimated from 681 loans, and once the full text is represented it can no longer be distinguished from zero, which, by a rule fixed in the design note before these estimates were run, lowers the claim.

The finding speaks to three literatures. The first is the work on religion, social capital and economic behavior. Religious belief is associated with trust, reciprocity and cooperation across countries (Guiso et al., 2003; Valencia Caicedo et al., 2023), counties with more congregations have more small business activity (Deller et al., 2018), and historical missionary activity left a lasting trace in local social capital (Deng et al., 2025). That literature establishes that religion builds the kind of network group-lending theory needs, but it does not observe an individual's place in such a network alongside a debt with money at stake. Here both appear in the same loan record, and the form of religion associated with lower default is an affiliation with a community rather than a clerical vocation, since church secretaries show the same gap as pastors. What a borrower believes is not something the file records.

The second is the finance literature on religion and credit, which has identified religion mostly through the lending contract or the borrower's surroundings. Islamic loans default less than conventional loans to comparable borrowers (Baele et al., 2014). Firms in more religious U.S. counties borrow at lower spreads and with fewer covenants (He and Hu, 2016; Chen et al., 2016), and credit unions there lend more cheaply and hold better loans (Davidson et al., 2026). County adherence predicts lower mortgage delinquency and less misrepresentation (Li and Ucar, 2022; Conklin et al., 2022). At the individual level, religious affiliation is associated with the kinds of debt a household carries (Clifton et al., 2023) and adolescent religiosity with less adult financial distress (Lei et al., 2024), but neither observes a loan and its repayment. What this paper adds is that religion enters an individual credit file in two observable forms, and that the two carry opposite information about the repayment of the same kind of loan in the same market. It also shows that the affiliation of the individual, not the religiosity of the place, is the one associated with lower default.

The third literature is the work on borrower-supplied information in online credit markets, where lenders infer creditworthiness from what lies outside the credit score (Iyer et al., 2016) and price soft information such as social-network ties, not always correctly (Freedman and Jin, 2017). What they read includes appearance (Duarte et al., 2012), verified friendships (Lin et al., 2013) and the job title itself (Davaadorj et al., 2024, 2026), and broad occupation classes predict LendingClub defaults beyond standard risk factors (Croux et al., 2020). The affiliation I study is a community tie of a much thicker kind than a platform friendship, and I look at default rather than funding. The text of the request has been studied most (Herzenstein et al., 2011; Michels, 2012; Dorfleitner et al., 2016; Nowak et al., 2018; Netzer et al., 2019; Kriebel and Stitz, 2022; Gao et al., 2023; Sanz-Guerrero and Arroyo, 2025). That work has established that words predict default and that self-authored identity claims can raise funding while predicting worse repayment (Herzenstein et al., 2011), but it has taken less interest in which words carry information of their own. Religious language, it turns out, cannot be separated from the circumstances it travels with once the full text is represented.

Section 2 sets out the argument and the two hypotheses, Section 3 the data, and Section 4 the empirical approach. Section 5 presents the results. Section 6 draws them together, discusses mechanism, magnitude and limits, and sets the signals against the religiosity literature. Section 7 concludes.

# 2. Religious community, religious language, and repayment

## 2.1 Community as collateral

Group-lending theory gives a clean account of why belonging can substitute for collateral. When borrowers are jointly liable, their peers have a stake in repayment and a reason to monitor one another (Stiglitz, 1990). When they can also sanction one another socially, default costs the defaulter standing in the group, a sanction the lender can rely on but cannot contract on (Besley and Coate, 1995; Ghatak and Guinnane, 1999). Karlan et al. (2009) give the idea its model: the trust a borrower can draw on is the value of the network ties a default would put at risk, largest in dense, closely knit communities. The microfinance evidence suggests the mechanism is real. Borrowers more socially connected to their quasi-randomly formed groups repay more (Karlan, 2007), and those who prove trustworthy in a trust game repay better (Karlan, 2005). More frequent meetings cut default by two thirds (Feigenberg et al., 2013), removing joint liability while keeping the meetings does not raise default (Giné and Karlan, 2014), and more religiously observant groups repay more promptly (Al-Azzam et al., 2012).

The insight travels beyond microfinance. Households in high-social-capital Italian provinces use more formal credit, most strongly where courts are slow (Guiso et al., 2004). U.S. borrowers in communities with more social capital default less, most markedly when default would be strategic (Clark et al., 2021; Guiso et al., 2013). The same holds inside marketplace lending (Hasan et al., 2022; Lu et al., 2020), and making a default visible to the borrower's social contacts deters it (Ge et al., 2017).

A religious congregation is a community of this kind, and often an intense one (Putnam, 2000): members meet weekly, know one another's families, and share explicit norms about money. The economics of religion treats the congregation as a club that produces goods its members cannot buy elsewhere (Iannaccone, 1998; Iyer, 2016), whose costly demands screen out the less committed and raise participation among those who remain (Iannaccone, 1992, 1994). Religious communes that imposed more such demands outlived those that imposed fewer, whereas secular communes did not (Sosis and Bressler, 2003). Believers also report more positive reciprocity, altruism and trust on validated preference measures (Valencia Caicedo et al., 2023). What this literature lacks is a link between an individual's membership in such a community and a financial outcome with money at stake.

Borrowers who work for a church are embedded in that community more deeply than ordinary members, because their employer is the congregation and their reputation among its members is their professional reputation. If a congregation functions as a group in the group-lending sense, its employees should be the members for whom the cost of default is highest, whether pastor or secretary. That cost should rise with how closely the community observes its members. I extend the logic of social collateral from groups a lender organizes to an affiliation a borrower reports. I do not, however, observe the community's monitoring directly. What I can observe is whether the pattern of default matches what that logic predicts and fails to match what its rivals predict.

The mechanism predicts three further things that discriminate between it and the main rival account, which holds that church jobs are simply stable. The social cost of default depends on how closely a community observes a member, not on the member's income shocks. So non-clergy church employees should show the gap as strongly as clergy, since the community is the same. The gap should be larger where congregations are denser, and it should not vary with local labor-market shocks. A job-stability account is silent on the first two and predicts the opposite of the third. The value of a steady paycheck shows itself when other borrowers lose theirs, so the affiliation advantage should widen when local unemployment rises. I did not specify these three as tests in advance, and I report them as evidence on mechanism rather than as confirmatory results.

**H1.** Conditional on grade, credit score, income, debt burden, loan terms, state and origination year, borrowers whose stated occupation places them in a religious institution default less (odds ratio below one).

## 2.2 Language as a low-cost signal

The description box gives borrowers a second channel, and signaling theory says what to expect from it. A message anyone can send at no cost, to an audience that would like to hear it, is cheap talk (Crawford and Sobel, 1982; Farrell and Rabin, 1996). Whether it carries information depends on who chooses to send it rather than on what it says. A costly signal is different, since it separates senders only when its cost differs across them (Spence, 1973). If misreporting carries even a small moral cost, such talk becomes partly informative (Kartik, 2009), and in online lending unverifiable disclosure relates non-monotonically to loan quality (Caldieraro et al., 2018). Yet the information need not run the way the sender intends. Religious people state stricter moral attitudes than the non-religious yet betray trust just as often in an anonymous trust game (Kirchmaier et al., 2018). In lending, unverifiable self-description and voluntary repayment promises raise funding while predicting worse repayment (Herzenstein et al., 2011; Wang et al., 2023; Lun et al., 2024). "God bless" costs nothing to write, cannot be verified, and is addressed to strangers deciding whether to lend. Two mechanisms make its expected association with default positive. The first is selection: the borrowers who feel moved to invoke faith in a request for money are disproportionately those whose situation gives them reason to, as the rise of religious practice in crises suggests (Chen, 2010; Bentzen, 2021). The same descriptions thank the reader in advance, describe hardship, and ask for help at several times the base rate. The second is substitution: a borrower with strong verifiable facts to offer tends to offer them, so appeals to faith concentrate where such facts are thin.

Under either mechanism the test is not whether religious language correlates with default, which Netzer et al. (2019) already showed, but whether it does so *after* the length, tone, hardship and gratitude content it travels with are held fixed. That residual is what the low-cost-signal reading predicts should remain, and what a "religious language is just distress language" reading predicts should not.

**H2.** Conditional on the same credit and loan controls and on the length, moral, hardship, gratitude, family, appeal and business content of the description, borrowers who use religious language default more (odds ratio above one).

The two signals can therefore take opposite signs even if affiliated borrowers and borrowers who invoke faith hold the same beliefs, because what matters is who observes the borrower and who chooses to speak, not the depth of anyone's faith. The theory also predicts something inside the description that can be checked. Suppose what makes a religious signal informative is that it costs something and ties the borrower to a community. Then a description that reports religious *practice* should resemble the affiliation signal more than "God bless." Examples are a tithe line in a monthly budget, a job at a church, or a mission trip to be paid for. Because the coded types are few and were not part of the confirmatory design, Section 5.2 reports this comparison as exploratory.

# 3. Data

## 3.1 LendingClub

I use the public LendingClub loan-level file covering loans issued from June 2007 through December 2018 (2,260,701 loans). The file is the Kaggle distribution of the 2018Q4 release, downloaded in June 2026, with loan status as of that release. Each record carries the borrower's FICO range at origination, annual income, debt-to-income ratio (DTI), home ownership, employment length, income-verification status, state and three-digit ZIP code, and the loan's amount, term, interest rate, sub-grade, purpose and status. Three free-text fields matter here: the job title the borrower typed in (`emp_title`), the short loan title (`title`) and the loan description (`desc`), the last two of which investors could read while the loan was listed. LendingClub stopped showing descriptions in 2014. Of the 125,811 loans with any description text after I strip the platform's boilerplate, 125,761 were issued between 2007 and 2014. The median description is 24 words.

The outcome is default. I keep loans whose status is terminal (Fully Paid, Charged Off, or Default) and drop loans still current, in grace or late, and the small "does not meet credit policy" group. After removing records with missing DTI, FICO or rate, the analysis sample has 1,344,976 loans, 20.0 percent of which were charged off or defaulted. The description subsample has 123,292 loans (15.3 percent defaulted) and is an earlier slice of the platform's history with a lower default rate, which is why every specification carries origination-year fixed effects. Writing a description was a choice. Appendix Table C2 shows that origination year, grade and loan size predict it while affiliation does not, with an odds ratio (OR) of 1.02 (p = 0.81), so the narrative results describe borrowers who chose to write. Table 1 reports descriptive statistics.

**Table 1. Descriptive statistics by group**

| Group | N | Default rate | FICO (mean) | Income (median, $) | DTI | Rate (%) | Amount ($) | 60-month | Grade A–B |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Religious-institution affiliation | 3,105 | 0.133 | 703.9 | 60,000 | 19.0 | 12.28 | 14,827 | 0.228 | 0.570 |
| — clergy role | 2,497 | 0.138 | 702.9 | 62,400 | 19.3 | 12.12 | 15,259 | 0.233 | 0.565 |
| — church staff (non-clergy) | 608 | 0.113 | 708.3 | 53,000 | 17.5 | 12.92 | 13,050 | 0.207 | 0.594 |
| All other borrowers | 1,341,871 | 0.200 | 698.2 | 65,000 | 18.3 | 13.24 | 14,418 | 0.241 | 0.466 |
| All terminated loans | 1,344,976 | 0.200 | 698.2 | 65,000 | 18.3 | 13.24 | 14,419 | 0.241 | 0.467 |
| Religious language (description sample) | 681 | 0.200 | 704.9 | 55,000 | 16.0 | 13.44 | 13,460 | 0.256 | 0.502 |
| Other descriptions | 122,611 | 0.153 | 703.7 | 62,000 | 16.3 | 13.42 | 13,982 | 0.232 | 0.535 |
| All descriptions | 123,292 | 0.153 | 703.7 | 62,000 | 16.3 | 13.42 | 13,979 | 0.232 | 0.535 |

*Notes.* Terminated LendingClub loans issued 2007–2018. Default rate is the share of loans charged off or in default. FICO is the mean of the midpoint of the borrower's FICO range at origination. Income is the median self-reported annual income. DTI is the mean debt-to-income ratio in percent. Rate is the mean interest rate and Amount the mean loan amount. 60-month is the share of loans with a 60-month rather than 36-month term, and Grade A–B is the share of loans in LendingClub's two highest grades. Description sample: loans with non-empty borrower text after removing platform boilerplate, all but 42 of them issued 2007–2014. Religious-language vs other descriptions: mean words 116 vs 36; share with moral language 0.19 vs 0.06, hardship 0.15 vs 0.07, gratitude 0.56 vs 0.14, family 0.33 vs 0.07, appeal for help 0.15 vs 0.04, business 0.16 vs 0.07.

## 3.2 Two religious indicators

*Religious-institution affiliation.* I flag a borrower as affiliated when the job title contains a clerical role word (pastor, minister, ministry, clergy, priest, chaplain, rabbi, missionary, reverend, evangelist, deacon, worship, imam, seminary) or a religious-organization word (church, parish, diocese, congregation, synagogue, mosque) that is not part of a hospital, school, insurer or bank name. This yields 5,014 loans in the full file and 3,105 in the terminated sample, of which 2,497 carry a clerical role word and 608 name a religious organization without one. I do not distinguish denominations, and the list is dominated by Christian titles because the borrowers are. An audit of 200 randomly drawn titles (Appendix Table B2) puts the rule's precision at 97 percent. The only clear errors are Louisiana civil parishes, and dropping them barely moves the estimate, so I report what the rule fixed in the design note produces.

*Religious language.* I flag a description as containing religious language when the loan title or the description text matches a dictionary of religious terms (God, Jesus, Christ, Christian, church, pray/prayer, bless/blessed/blessing, faith in its religious sense, the Lord, Bible/scripture, tithe, ministry/pastor/missionary, amen, and denominational names). Idiomatic uses ("good faith," "heaven forbid," "Lord & Taylor") are excluded. The dictionary flags 681 of the 123,292 descriptions in the terminated description sample (0.55 percent), and Appendix Table B3 traces the count from the full file. Because a dictionary cannot read context, every flagged description was also coded by a language model against a short codebook (Appendix B). The coding confirms 583 as religious, and it separates formulaic uses such as "Thank you and God bless" from identity claims and from concrete religious practice or expense. Appendix B names the models and reports agreement with a second model (κ = 0.86) and a human coder (κ = 0.72 on the four-way type, lower on the religious/non-religious boundary). Appendix B also reports a search for religious content the dictionary misses. It finds about a hundred such descriptions by extrapolation and eleven more through implicit phrases, with a wide upper bound. Any that remain sit in the comparison group and pull the H2 estimate toward zero. The confirmatory test uses the dictionary indicator, because that is what the design note fixed (Section 4.1). The coded indicator enters only as a robustness check, with the 98 rejected matches as a placebo, and the type breakdown is exploratory. The two indicators rarely coincide: in the description sample, 372 loans are affiliated and 681 carry religious language, and 20 are both.

## 3.3 Text controls

Religious language does not appear in a vacuum. The median description that contains it is three times as long as the median other description (68 versus 23 words). Descriptions that contain it are also far more likely to thank the reader (56 versus 14 percent), mention family (33 versus 7), describe hardship (15 versus 7), ask for help (15 versus 4), state a business purpose (16 versus 7) or make moral claims about reliability (19 versus 6). These features predict default in their own right. Hardship, gratitude and appeals for help are associated with higher default (ORs 1.17, 1.12 and 1.12), and moral language and length with lower (0.88, and 0.92 per log point of length). A raw comparison would therefore credit religious language with what the hardship or the appeal around it explains. I build six dictionary indicators (moral self-presentation, hardship, gratitude, family, appeal for help and business purpose) and the log of description length, and include them in every narrative specification. Six dictionaries cannot capture everything in a description, so the double machine learning (DML) specifications let a flexible learner also use a pretrained word-vector representation of the text, following Kriebel and Stitz (2022). The vectors are spaCy's en_core_web_md (300 dimensions), reduced to 50 principal components in the main specification and used in full as a check.

## 3.4 Local religiosity and local labor markets

To separate individual affiliation from the religiosity of the place a borrower lives in, I use the 2010 U.S. Religion Census county file (Grammich et al., 2012), the source behind the religiosity measures used in corporate finance since Hilary and Hui (2009). I link the county file to three-digit ZIP areas (ZIP3) through the Census Bureau's 2010 ZIP Code Tabulation Area (ZCTA)–county relationship file with population weights. This gives adherents per thousand residents and congregations per ten thousand for 894 areas covering 99.97 percent of loans. For labor-market shocks I merge Bureau of Labor Statistics (BLS) Local Area Unemployment Statistics annual county unemployment rates for 2008–2018 the same way. For each loan I compute the rate at issue and the largest subsequent change over the loan's term, truncated at 2018 for loans whose term runs past the data.

## 3.5 Prosper

To replicate the occupational result I use the public Prosper file in its Kaggle distribution, downloaded in June 2026 (113,937 listings, 2005–2014). The file has no free text but has an occupation code with the categories "Clergy" and "Religious." Among the 50,270 terminated loans with complete covariates, 141 fall in those categories, and the controls parallel LendingClub's.

# 4. Empirical approach

## 4.1 Confirmatory tests

H1 and H2 are the only confirmatory tests, and both use the same logit:

*Pr*(*D*ᵢ = 1) = Λ(*β R*ᵢ + *X*ᵢ′*γ* + Σₖ *α*ₖ₍ᵢ₎),\ \ \ \ \ \ \ \ (1)

where *D*ᵢ is default, *R*ᵢ the religious indicator (affiliation for H1, religious language for H2), *X*ᵢ the credit and loan variables listed in the notes to Table 2, Λ the logistic function. The *α*ₖ₍ᵢ₎ are fixed effects for origination year, grade, purpose, employment length, home ownership, income verification and state. Standard errors are clustered by state. H1 is estimated on all 3,105 affiliated loans together with a random draw of 250,000 other terminated loans, a draw made only to keep the fixed-effects logit tractable. The full sample and five further draws give the same estimate (Appendix Table C3). H2 is estimated on the full description sample, with the six text dictionaries and log length added to *X*ᵢ. Because Section 2 treats the two indicators as separate channels, I also enter them together in the H2 specification to check that each survives the other. Clustering by ZIP3 area or by month instead changes the standard errors but not what I conclude. Because 51 state clusters are few, I also report wild cluster bootstrap p-values (Cameron et al., 2008; Appendix Table C3). Both hypotheses are one-sided with a Holm correction across the pair. The hypotheses, this specification, the one-sided Holm procedure, most of the robustness checks of Section 4.2 and the decision rule for the DML check in Section 5.2 were fixed in a dated design note (17 September 2026). The split by period is not in the note, and the neighbor-occupation comparison was added after the confirmatory estimates. The note followed an exploratory first pass on the data (5 September), which included preliminary versions of both estimates and several of the checks, and preceded the confirmatory estimates reported here (18 September). It is in the replication package. I report ORs and average marginal effects (AME). The AME is the change in predicted default probability, in percentage points (pp), when the indicator switches from zero to one, averaged over the estimation sample.

## 4.2 Objections

Everything that follows the two tests answers a specific objection, and I say for each what it rules out and what it does not. Section 5 reports the outcomes.

*Secure jobs.* If the advantage came with a secure paycheck, it should shrink once secure jobs are controlled for. I add indicators for eight stable occupations (teachers, police, firefighters, military, government, nurses, postal and transit workers; keyword rules in Appendix B) and also restrict the comparison group to borrowers in those jobs, directly and within coarsened-exact-matching (CEM) cells (Iacus et al., 2012).

*Mission-driven jobs.* If the advantage came instead with the kind of person who takes modestly paid service work, the jobs nearest to church work should show the same advantage, and comparing affiliated borrowers with borrowers in those jobs alone should shrink it. I compare them with borrowers in nonprofit and social-service work, education or healthcare, again directly and within CEM cells.

*Observables.* Affiliated borrowers differ from others on observables (Table 1), and a logit removes those differences only if its functional form is right. If the estimate were an artifact of that form, it should move once the comparison is made without it. I therefore reweight the comparison group by entropy balancing (Hainmueller, 2012), which equates its covariate moments with the affiliated group's, and estimate a partially linear DML model (Chernozhukov et al., 2018), which lets a flexible learner absorb the controls. These guard against a misspecified functional form but not against unobserved confounding.

*Unobserved confounding.* A trait such as conscientiousness that the file does not record could raise affiliation and lower default at once, and I have no instrument to rule it out. What I can do is ask how strong such a trait would have to be. I report two measures. Oster's (2019) δ is the ratio of selection on unobservables to selection on observables that would reduce the estimate to zero. The Cinelli–Hazlett (2020) robustness value is the share of residual variance in both treatment and outcome that a confounder would have to explain, benchmarked against observed covariates.

*Length and tone.* Religious descriptions in this sample are longer and more emotional than others (Section 3.3), so the association may belong to length or tone rather than to religion. The confirmatory specification already holds length and the six tone dictionaries fixed, but six dictionaries are a coarse measure of tone. If the association belonged to length or tone, it should vanish once descriptions of equal length are compared and once the whole text, not six summaries of it, is represented. I match each flagged description to its five nearest neighbors in length within grade-year cells, and I replace the six dictionaries with a pretrained text representation of the full description inside the DML model.

*Any rare words.* A word set that flags half of one percent of descriptions picks out a small and possibly unusual group, and the estimate could reflect that rarity rather than religion. If so, random word sets of the same frequency should produce it about as often. I draw 1,000 such sets of non-religious words matched to the dictionary's document frequency, re-estimate the residualized coefficient for each (a linear probability coefficient after partialling out the controls of the confirmatory specification). I then place the religious estimate in that distribution.

*A distress marker.* Religious language might be what a borrower already in trouble writes, so that H2 picks up distress at application rather than anything about the borrower. If so, defaults among these borrowers should cluster early in the loan. I estimate a discrete-time hazard on loan-month panels and compare the first year with later years (Section 5.6, Appendix A).

*Early versus later borrowers.* LendingClub's early years were small, and its borrowers chose a market few had heard of. If the affiliation result were a property of that early population, it should fade in the later and much larger sample. I estimate H1 separately for loans issued in 2007–2014, the years in which descriptions were collected, and in 2015–2018.

*One platform.* If the affiliation result reflected something peculiar to LendingClub's borrowers or to its free-text job title, it should not reappear on a platform with a different population and a coded occupation. I estimate H1 on Prosper.

## 4.3 Mechanism

Community as collateral and job stability predict the same sign for H1 but part ways at the three points Section 2.1 set out. The first needs no interaction. Clergy and non-clergy church staff sit inside the same congregations but differ in vows and job security, so I split the affiliation indicator into the two groups and estimate

*Pr*(*D*ᵢ = 1) = Λ(*β*₁ *C*ᵢ + *β*₂ *S*ᵢ + *X*ᵢ′*γ* + Σₖ *α*ₖ₍ᵢ₎),\ \ \ \ \ \ \ \ (2)

where *C*ᵢ marks a clerical title and *S*ᵢ a non-clerical church job, and *X*ᵢ and the *α*ₖ₍ᵢ₎ are the controls and fixed effects of the confirmatory specification. Community as collateral predicts *β*₁ ≈ *β*₂, since the congregation that observes a pastor observes its secretary too. A vocation or job-stability account predicts *β*₁ < *β*₂, on the added assumption that clergy carry the vows and the more secure tenure.

The other two ask whether the affiliation advantage grows or shrinks with a local condition, which I test by interacting the affiliation indicator with that condition in a logit of default:

*Pr*(*D*ᵢ = 1) = Λ(*β R*ᵢ + *λ* (*R*ᵢ × *Z*ᵢ) + *θ Z*ᵢ + *X*ᵢ′*γ* + Σₖ *α*ₖ₍ᵢ₎),\ \ \ \ \ \ \ \ (3)

where *R*ᵢ is the affiliation indicator, *Z*ᵢ the moderator, standardized, and the controls and fixed effects are as before. The coefficient of interest is *λ*, which measures how much the affiliation coefficient changes with a one standard deviation change in *Z*ᵢ, while *θ* absorbs the moderator's own association with default. *Z*ᵢ is local congregation density in one set of estimates and the largest subsequent change in local unemployment over the loan's term in another, with job tenure as a third. The density interaction is estimated under state fixed effects and then under ZIP3 fixed effects, in the manner of Rajan and Zingales (1998), so that it reflects variation across areas within a state and then across borrowers within an area. Community as collateral predicts *λ* < 0 for density, since members are observed more closely where congregations are denser, and *λ* near zero for the unemployment change, since observation does not depend on the local labor market. Job stability predicts the reverse, no role for density and *λ* < 0 for the unemployment change, since a secure paycheck matters most when neighbors lose theirs. Teachers and government employees serve as a positive control for the unemployment interaction.

## 4.4 What I do not do

I do not estimate a prediction model. Adding religious language to a cross-validated logit on the description sample moves the area under the receiver operating characteristic (ROC) curve by 0.00002, from 0.6958 to 0.6958. Adding affiliation on the H1 sample moves it by 0.00018, from 0.7150 to 0.7151 (Appendix Table C7). Indicators that flag a fraction of one percent of borrowers cannot materially improve aggregate prediction. Nor do I fit a structural or mediation model, because the mediators of interest are not observed at the individual level.

# 5. Results

## 5.1 Affiliation (H1)

*Confirmatory estimate.* Table 2 reports the affiliation estimates. Column (1) gives the confirmatory specification: an OR of 0.692 (95 percent confidence interval 0.638 to 0.751) and an AME of −4.8 pp. Against the 20.0 percent default rate of other borrowers (Table 1), that is a reduction of 24 percent, about a quarter. Split by period, the OR is 0.607 for loans issued in 2007–2014 and 0.743 for 2015–2018. The advantage is weaker in the later years but far from gone, so the finding is not a property of the platform's early, self-selected borrowers. The 2007–2014 column also bears on sample selection. All but 10 of the loans issued through 2013 had reached maturity by the 2018Q4 release (the 10 were among the 34,392 60-month loans issued in 2013), and so had the 36-month loans of 2014. Among the 60-month loans issued in 2014, 17 percent were still open, so the terminated ones had repaid or defaulted early. Dropping the 2014 60-month cohort from the 2007–2014 column leaves the estimate at 0.608 (SE 0.112, 1,061 affiliated loans), and dropping it from the full sample gives 0.698. The one-sided Holm-adjusted p-value is below 10⁻¹⁸ and the wild cluster bootstrap p-value below 0.001. Using all 1.34 million terminated loans instead of the random draw gives 0.694, and five further draws give 0.689 to 0.701 (Appendix Table C3).

**Table 2. Religious-institution affiliation and default (H1): confirmatory estimates and robustness**

| | (1) All years | (2) 2007–2014 | (3) 2015–2018 | (4) + 8 stable occupations | (5) Entropy-balanced | (6) DML |
|---|---:|---:|---:|---:|---:|---:|
| Affiliation (OR) | 0.692 | 0.607 | 0.743 | 0.690 | 0.697 | |
| SE | 0.041 | 0.087 | 0.060 | 0.041 | 0.043 | 0.006 |
| p-value | <0.001 | <0.001 | <0.001 | <0.001 | <0.001 | <0.001 |
| AME | −4.8 pp | −5.6 pp | −4.2 pp | −4.9 pp | −4.3 pp | −4.3 pp |
| N | 253,105 | 85,132 | 167,973 | 253,105 | 253,105 | 253,105 |

*Notes.* Logit, default on affiliation and controls: grade, origination year, interest rate, FICO midpoint, log income, DTI, 60-month term, log amount, employment length, home ownership, income verification, purpose, state fixed effects. Standard errors (SE) clustered by state, on the log-odds scale in columns (1)–(5) and on the probability scale in column (6). OR = odds ratio; AME = average marginal effect in percentage points (pp); CI = confidence interval. Sample = all affiliated terminated loans plus 250,000 randomly drawn other terminated loans (3,105 affiliated: 2,497 clerical, 608 church staff). Column (4) adds indicators for teachers, police/corrections, firefighters, military, government, nurses, postal and transit workers (ORs 0.91, 0.93, 0.64, 0.93, 0.90, 1.06, 1.20, 1.10). Column (5): weights equate 76 covariate moments (Appendix Table C1). Column (6): DML partially linear model, CatBoost nuisance functions (Prokhorenkova et al., 2018), 5-fold cross-fitting; the entry is the partially linear coefficient on the probability scale, so no OR is shown. The average treatment effect on the treated (ATTE) from the same run is −0.042 (p < 0.001). Column (1): 95% CI 0.638–0.751, one-sided Holm-adjusted p < 10⁻¹⁸.

*Secure jobs and observables.* The most natural objection is that clergy simply have secure jobs, and column (4) adds the eight occupation indicators. Teachers (0.91), government employees (0.90) and police (0.93) default modestly less than other borrowers, and firefighters markedly less (0.64). Yet the affiliation coefficient does not move (0.690). Restricting the comparison group to the 118,022 borrowers in those stable jobs still leaves affiliated borrowers defaulting less (0.731, Table 3, Panel A). Entropy balancing (column (5)) tells the same story from the other side: after reweighting on 76 moments the comparison default rate in the random draw falls from 20.1 to 17.5 percent, affiliated borrowers remain at 13.3, and the weighted OR is 0.697. The DML estimate (column (6)) is −4.3 pp (standard error 0.6 pp).

*Mission-driven jobs.* Panel B of Table 3 takes the objection one step further. If the affiliation gap were a property of mission-driven, modestly paid service work, borrowers in the jobs nearest to church work should show it too, and comparing affiliated borrowers with borrowers in those jobs alone should shrink it. Neither happens. Social workers, case managers and counselors (11,592 loans) default no less than other borrowers (1.023), nor do healthcare workers (1.023), while education workers default modestly less (0.945). Against social-work borrowers alone the affiliation OR is 0.690, against healthcare workers alone 0.679, and against education workers alone 0.747. Coarsened exact matching gives 0.703 against those neighbors and 0.741 against the eight stable occupations. Whatever the affiliation captures is not shared by the jobs that most resemble it in pay, tenure or purpose. Occupation has carried default information before, for finance professionals (Agarwal et al., 2017) and for professional and skilled job titles (Croux et al., 2020; Davaadorj et al., 2024), but there the natural reading is expertise or earning power, and a church secretary has neither.

**Table 3. Occupation-selection tests for the affiliation estimate**

*Panel A. Secure jobs*

| | OR | p-value | N (affiliated / comparison) |
|---|---:|---:|---:|
| Affiliation vs the eight stable occupations only | 0.731 | <0.001 | 3,105 / 118,022 |
| CEM within the eight stable occupations | 0.741 | <0.001 | 3,008 / 58,032 |

*Panel B. Mission-driven jobs*

| | OR | p-value | N (affiliated / comparison) |
|---|---:|---:|---:|
| Nearest occupations vs all other borrowers: | | | |
| — social work, case management, counseling | 1.023 | 0.43 | 11,592 / 250,000 |
| — education | 0.945 | <0.001 | 54,998 / 250,000 |
| — healthcare | 1.023 | 0.14 | 76,981 / 250,000 |
| Affiliation with only this comparison group: | | | |
| — social work, case management, counseling | 0.690 | <0.001 | 3,105 / 11,592 |
| — education | 0.747 | <0.001 | 3,105 / 54,998 |
| — healthcare | 0.679 | <0.001 | 3,105 / 76,981 |
| — all three | 0.707 | <0.001 | 3,105 / 140,677 |
| CEM within the three neighbor occupations | 0.703 | <0.001 | 2,766 / 39,860 (2,234 cells) |

*Notes.* Same sample, controls and clustering as Table 2. Panel A: the eight stable occupations of Table 2, column (4). Panel B: nearest occupations are identified from job titles by the keyword rules in Appendix B. Coarsened exact matching on grade, origination year, FICO band, income, employment length, home ownership and term; N for the CEM rows counts matched affiliated and matched comparison loans. The three neighbor groups overlap (a school nurse counts in both education and healthcare), so their sum exceeds the 140,677 loans of the pooled row.


*Unobserved confounding.* Table 4 gives the sensitivity analysis. Oster's δ is 6.5, so unobserved selection would have to be six and a half times as strong as selection on observables to explain the estimate away. In addition, the robustness value of 0.015 is about twelve times the explanatory power of employment length.

**Table 4. Sensitivity to unobserved confounding**

| | H1 (affiliation) | H2 (religious language) |
|---|---:|---:|
| β uncontrolled / controlled (LPM) | −0.067 / −0.045 | +0.047 / +0.035 |
| R² uncontrolled / controlled | 0.000 / 0.094 | 0.000 / 0.065 |
| Oster δ (R²max = 1.3 R²) | 6.5 | 9.7 |
| β* at δ = 1 | −0.038 | +0.031 |
| Robustness value (RV), q = 1 | 0.015 | 0.0066 |
| RV at α = 0.05 | 0.011 | 0.0010 |
| Benchmark partial R²: employment length / verification | 0.00125 / 0.00027 | |

*Notes.* Linear probability models (LPM) with heteroskedasticity-robust (HC1) standard errors on the sample and controls of Table 2, column (1) for H1. For H2, the sample is the description sample with log length and the six text dictionaries added, the confirmatory specification of Section 4.1. Oster's δ is the ratio of selection on unobservables to selection on observables that would drive the coefficient to zero. It is computed from the uncontrolled and controlled coefficients and R² with R²max set to 1.3 times the controlled R² (Oster, 2019). β* is the coefficient that remains if that ratio is one. The robustness value is the partial R² that a confounder would need with both treatment and outcome to drive the coefficient to zero (q = 1), and at α = 0.05 to make it insignificant (Cinelli and Hazlett, 2020). Benchmark partial R² is the fall in R² from dropping the employment-length or income-verification indicators from the controlled model, divided by the unexplained variance.

*One platform.* Prosper replicates the affiliation result (Table 5). The 141 clergy and religious-occupation borrowers default at 22.7 percent against 30.5 percent, and with the full set of controls the OR is 0.684 (p = 0.037). The placebo occupations on Prosper (teachers, police, nurses) are all indistinguishable from one.

**Table 5. Prosper replication of H1**

| | OR | p-value | N |
|---|---:|---:|---:|
| Clergy / Religious occupation | 0.684 | 0.037 | 141 |
| Placebo: Teacher | 1.073 | 0.28 | 1,571 |
| Placebo: Police / corrections | 1.008 | 0.93 | 663 |
| Placebo: Nurse (RN) | 0.965 | 0.71 | 794 |

*Notes.* 50,270 terminated Prosper loans, 2005–2014. Controls: Prosper rating or pre-2009 credit grade, origination year, borrower rate, credit-score midpoint, log stated monthly income, DTI, term, log amount, employment status, home ownership, income verifiability, state FE, with SE clustered by state. "Clergy" and "Religious" are two of Prosper's own occupation categories. Raw default: 22.7% vs 30.5%. The clergy row is from a model without the placebo indicators; the placebo rows are from a model that enters all four occupations together, in which the clergy OR is 0.686 (p = 0.039).

Figure 2 collects the affiliation estimates of this section, from the confirmatory specification through the occupation tests to the Prosper replication. Every interval lies below one.

![Figure 2. Religious-institution affiliation and default across specifications. ORs with 95% confidence intervals (log scale), grouped by the items of Section 5.1, with the dotted line at an OR of one. For the five estimates stored with a p-value but no standard error, the interval is the one implied by that p-value under normality.](fig2_forest.png){width=6.3in}

## 5.2 Religious language (H2)

*Confirmatory estimate.* Table 6 builds the narrative estimate one control set at a time. With credit and loan controls only (column (1)), religious language carries an OR of 1.265 (p = 0.018). Adding log length (column (2)) moves it to 1.338, because long descriptions default less and religious descriptions are long. Adding the six text dictionaries (column (3), the specification fixed in the design note) brings it back to 1.281 (p = 0.016), an AME of +3.2 pp. Against the 15.3 percent default rate of other descriptions (Table 1), that is an increase of 21 percent, about a fifth. Across the three columns the estimate stays between 1.27 and 1.34, and the one-sided Holm-adjusted p-value for the confirmatory specification is 0.008 (wild cluster bootstrap p = 0.015).

**Table 6. Religious language and default (H2): confirmatory estimate**

| | (1) Credit controls | (2) + log length | (3) + text dictionaries |
|---|---:|---:|---:|
| Religious language (OR) | 1.265 | 1.338 | 1.281 |
| SE | 0.100 | 0.098 | 0.103 |
| p-value | 0.018 | 0.003 | 0.016 |
| AME | +3.1 pp | +3.8 pp | +3.2 pp |
| N | 123,292 | 123,292 | 123,292 |

*Notes.* Same controls as Table 2 plus, from column (2), log description length and, from column (3), six text indicators (moral, hardship, gratitude, family, appeal, business; ORs 0.88, 1.17, 1.12, 1.07, 1.12, 1.08). Column (3): 95% confidence interval (CI) 1.047–1.566, two-sided p 0.016, one-sided Holm-adjusted p 0.008, wild cluster bootstrap p 0.015; minimum detectable effect at 80% power 3.4 pp.

*Length and tone.* Table 7 varies the treatment of length and tone. Replacing log length with length deciles (column (1)) changes little (1.274), and in the length-matched sample (column (2)) the OR is 1.296 (p = 0.040). The DML estimates are where the narrative result shows its limits. With the six dictionaries as controls (column (3)) the partially linear estimate is +3.3 pp (p = 0.027), and +3.6 on the coded indicator (p = 0.028). Once the learner is also given a representation of the text itself, the point estimate barely moves but the interval widens. It is +2.8 with a term frequency–inverse document frequency (TF-IDF) factorization (p = 0.059), +2.6 with pretrained word vectors reduced to 50 components (column (4), p = 0.09), +2.3 with the full 300 dimensions (p = 0.14) and +2.4 with a document-embedding model (p = 0.11). The sign never changes and the coefficient shrinks by at most a third, but 681 treated loans cannot pin down a three-point association once several hundred text features are conditioned on. The design note set the rule that a confidence interval covering zero in this specification would lower the claim, and I apply it. The rich-text specifications do not estimate a distinct association for religious wording with enough precision to separate it from the rest of the text, although the point estimate gives no sign that the text absorbs it. H2 passes its confirmatory test and both placebos (Table 8 and the random-word permutation below), but I present it as an association whose sign is consistent, not as a result on the same footing as H1 (Figure 3).

**Table 7. Religious language and default: length and tone**

| | (1) + length deciles | (2) Length-matched | (3) DML + dictionaries | (4) DML + dictionaries + text |
|---|---:|---:|---:|---:|
| Religious language (OR) | 1.274 | 1.296 | | |
| SE | 0.101 | 0.126 | 0.015 | 0.015 |
| p-value | 0.016 | 0.040 | 0.027 | 0.091 |
| AME | +3.1 pp | +3.2 pp | +3.3 pp | +2.6 pp |
| N | 123,292 | 3,572 | 123,292 | 123,292 |

*Notes.* Controls of Table 6, column (3). Column (1) replaces log length with length-decile indicators. Column (2): each flagged loan matched with replacement to its five nearest neighbors in description length within grade×year, N counting distinct loans (681 treated, 2,891 controls; mean length 116 and 114 words), estimated with the full column (3) controls and state-clustered SE. Columns (3)–(4): DML partially linear model, CatBoost, reported on the probability scale with SE on that scale, so no OR is shown; column (4) adds 300-d word vectors (PCA-50); alternative representations, repeated cross-fitting and term counts in Appendix Table C5.

![Figure 3. Religious language and default: DML estimates by text representation. Partially linear DML with CatBoost nuisance functions and 5-fold cross-fitting, grouped by the specifications of Table 7 and Appendix Table C5; "twenty splits" aggregates twenty repeated sample splits by the median. Bars are 95% confidence intervals, and the dotted line marks zero.](fig3_dml.png){width=6.3in}

Two further checks put the imprecision in its place. The estimate does not depend on the sample split, since twenty repetitions of the cross-fitting give a median of +3.2 pp with the dictionary controls, significant in every split, and +3.0 with the TF-IDF representation, significant in twelve of twenty. And the imprecision is what the sample size implies: with 681 treated loans the smallest effect a one-sided test detects with 80 percent power is 3.4 pp, and more religious descriptions than exist would be needed to do better.

*Words or content.* The language-model coding separates the words from the content (Table 8). Flagging only the 583 descriptions confirmed as religious gives an OR of 1.335 (p = 0.001), while the 98 the dictionary flagged but the coder rejected give 0.948 (p = 0.88). The association sits in the religious content, not in the words. By type (Appendix Table B1), formulaic invocations carry the association (1.385, p = 0.001, n = 467). Identity claims point the same way on too few loans to tell (1.460, n = 34), and descriptions that report religious *practice* show no elevated default (0.988, n = 82). The split is exploratory and the identity-claims cell is small, but the pattern is in the direction Section 2 anticipates. The data also add a gradient. Replacing the indicator with the number of religious terms gives ORs of 1.14, 1.56 and 1.87 for one, two, and three or more terms (Appendix Table C5). The pattern is consistent with the sign of H2, but I did not specify it in advance.

**Table 8. Religious language and default: words or content**

| | OR | p-value |
|---|---:|---:|
| Religious language, coded religious (583 descriptions) | 1.335 | 0.001 |
| Dictionary false positives (98 descriptions) | 0.948 | 0.88 |
| N | 123,292 | |

*Notes.* Controls of Table 6, column (3), with the dictionary indicator replaced by two indicators: the 583 descriptions the codebook coding confirmed as religious and the 98 dictionary matches it rejected.

*Any rare words.* If the association reflected the rarity of a small word set rather than religion, random word sets of the same frequency should reproduce it. The fake-dictionary permutation puts the residualized effect of the actual dictionary at 0.035 against a permutation mean of −0.003 (standard deviation 0.014), and only one random word set in two hundred reaches that value (one-sided p = 0.005; Appendix Figure C1).

*Unobserved confounding.* The H2 column of Table 4 shows where the narrative result is fragile. Oster's δ is 9.7, so the point estimate is no more sensitive to proportional selection than H1's. But the robustness value is 0.0066. A confounder explaining 0.1 percent of the variance in both wording and default, about the explanatory power of employment length, would be enough to make the estimate insignificant. This is the sensitivity-analysis counterpart of the widening DML intervals: the coefficient is stable, the precision is not.

## 5.3 Two signals, not one

Section 2 treats affiliation and religious language as two channels rather than one, and the opposite signs of H1 and H2 already say they are not the same thing measured twice. Table 9 makes the point in one regression. Entered together on the description sample, religious language has an OR of 1.293 (p = 0.013) and affiliation, on the 372 affiliated borrowers who wrote a description, 0.672 (p = 0.041). The religious-language estimate is unchanged from Table 6 (1.281 alone).

**Table 9. Both signals in one regression (description sample)**

| | OR | p-value | N treated |
|---|---:|---:|---:|
| Religious language | 1.293 | 0.013 | 681 |
| Religious-institution affiliation | 0.672 | 0.041 | 372 |

*Notes.* Specification of Table 6, column (3). Twenty loans carry both indicators.

## 5.4 Mechanism: the pastor and the secretary

If the affiliation gap came from the vocation itself, from a pastor's vows or from a professional identity in which unpaid debt is a scandal, church secretaries and administrators should default like secretaries and administrators elsewhere. Table 10 splits the indicator by whether the title contains a clerical role word. The split is by keyword, not by a judgment of each role. The audit in Appendix Table B2 shows how close the two splits are: of 200 random affiliated titles, the LLM coder of Appendix B classed 146 as clerical and 48 as non-clerical staff, against the 80:20 keyword split. Misclassification of the few titles such as "Director of Music Ministry" that carry a clerical word in a staff role would make the two groups more alike, which works against finding a difference. Borrowers with a clerical role word have an OR of 0.686 (p < 0.001), and borrowers who name a religious employer without one 0.720 (p = 0.023) on 608 loans. Their raw default rate, 11.3 percent, is if anything lower than the clergy's 13.8, and a Wald test cannot distinguish the two coefficients (p = 0.77). The comparison holds the kind of community roughly fixed rather than the congregation itself, since only 583 of the 3,105 affiliated titles (497 distinct names) name a specific institution and recurring names such as "First Baptist Church" belong to many unrelated churches. What the pastor and the secretary share is not a vocation, an income level, or a professional code, but employment inside a congregation. Survey data show a parallel, since the financial risk aversion associated with church membership appears to stem from the social side of membership rather than from belief (Noussair et al., 2013). An exploratory split of the affiliation indicator in the same table puts titles marked senior, lead or executive at 0.459 and titles marked associate, youth or assistant at 0.636, against 0.751 for the remaining affiliated titles, church staff included.

The staff result also speaks to the job-stability objection more directly than the occupation controls do. A church secretary's pay and tenure look like an office worker's, and the advantage that teachers and government workers show, about 10 percent lower odds, is a third of what church staff show.

**Table 10. Clergy and church staff**

| | OR | p-value | N |
|---|---:|---:|---:|
| Clergy role | 0.686 | <0.001 | 2,497 |
| Church staff, non-clergy | 0.720 | 0.023 | 608 |
| Wald test of equal coefficients | | 0.77 | |
| Raw default rate, clergy / staff / other borrowers (%) | 13.8 / 11.3 / 20.0 | | |
| Exploratory split of the affiliation indicator: senior, lead or executive title | 0.459 | <0.001 | 509 |
| — associate, youth or assistant title | 0.636 | 0.050 | 235 |
| — other affiliated titles, church staff included | 0.751 | <0.001 | 2,361 |

*Notes.* Specification of Table 2, column (1), with the affiliation indicator replaced by two indicators (equation 2) or, in the exploratory rows, by three. Same sample, controls and clustering as Table 2. Raw default rates from Table 1. The exploratory split is a keyword rule on the job title: associate, assoc, youth, assistant or asst; otherwise senior, sr, lead or executive; otherwise other.

## 5.5 Mechanism: congregation density and labor-market shocks

*Congregation density.* Table 11 turns to local religious presence. Adding adherence rate and congregation density to the full specification leaves the affiliation OR at 0.686, so the individual association is not local religiosity in disguise. Local religiosity itself runs the other way. Within state, borrowers from more religious ZIP3 areas default slightly *more*, with ORs of 1.039 per standard deviation of adherence and 1.060 per standard deviation of congregation density. The evangelical share, estimated without state fixed effects, is unrelated to default (1.030, p = 0.15). But the individual association varies with local religiosity. The interaction of affiliation with congregation density has an OR of 0.836 per standard deviation (p = 0.003). By tercile of local adherence, the affiliation OR is 0.708 in the least religious third of ZIP areas, 0.830 in the middle, and 0.585 in the most religious (Appendix Table A2). That pattern is not monotonic. Across quintiles of congregation density it is closer to monotonic: the OR is about 0.85 in the two least dense quintiles and between 0.62 and 0.68 in the three densest (Figure 4, Appendix Table A3). The differential remains under 601 ZIP3 fixed effects, which absorb every time-invariant feature of the area, including density itself. The interaction then asks whether the within-area affiliation gap is larger in denser areas, and it is: the affiliation coefficient is −5.4 pp and the density interaction −2.2 pp per standard deviation (p = 0.027). If the signal reflected only a church employee's private character or the steadiness of a church paycheck, it is hard to see why it should depend on how many other churches stand nearby. Religious language shows no detectable interaction with local religiosity (1.075, p = 0.50), as one expects of a message whose meaning does not depend on who is listening (Figure 4).

**Table 11. Individual affiliation and local religiosity**

| | Main-effect OR | Interaction OR | p (interaction) | N |
|---|---:|---:|---:|---:|
| + adherence rate and congregation density (controls) | 0.686 | | | 253,038 |
| Adherence rate (per SD, main effect, within state) | 1.039 (p 0.007) | | | |
| Congregation density (per SD, main effect) | 1.060 (p 0.001) | | | |
| Affiliation × adherence | 0.688 | 0.892 | 0.078 | |
| Affiliation × congregation density | 0.642 | 0.836 | 0.003 | |
| Evangelical share (per SD, main effect, no state FE) | 1.030 (p 0.15) | | | |
| Affiliation × congregation density, ZIP3 FE (LPM) | −5.4 pp | −2.2 pp / SD | 0.027 | 146,248 |
| Religious language × adherence | 1.295 | 1.075 | 0.50 | 123,260 |

*Notes.* 2010 U.S. Religion Census county file merged to three-digit ZIP areas via the Census ZCTA–county relationship file, population-weighted (894 areas). Adherents per 1,000 residents and congregations per 10,000, standardized. ZIP3 fixed-effects (FE) row: linear probability model (LPM), all affiliated loans plus 150,000 randomly drawn other terminated loans (a draw that keeps the 601-fixed-effect model tractable), restricted to ZIP3 areas with at least 50 loans, standard errors (SE) clustered by ZIP3; SD = standard deviation.

![Figure 4. Heterogeneity by local religiosity. Panel A: affiliation OR by quintile of congregation density in the borrower's ZIP3 area, full controls and state fixed effects. Panel B: religious-language OR by quintile of the adherence rate, Table 6, column (3) specification. Bars are 95% confidence intervals.](fig4_density.png){width=6.3in}

*Labor-market shocks.* The job-stability account predicts that the affiliation advantage should widen when local unemployment rises over the life of the loan. It does not (interaction OR 0.975, p = 0.58; Appendix Table C6). The shock measure is the largest subsequent change in the local rate, which is negative for most loans in this period, so loans that faced a rise are few. Across terciles of that measure the affiliation OR is 0.588 where unemployment fell most, 0.763 in the middle and 0.721 where it fell least or rose: not the ordering a job-stability account predicts, and if anything the reverse. The gap for teachers and government employees, a positive control, does not widen either. The shocks of a period that was mostly a recovery are too small to reveal a job-stability mechanism for any occupation. The evidence supports a more limited statement: the affiliation gap does not visibly vary with shocks, while it does visibly vary with congregation density. Job tenure gives the stability account a partly favorable check. The gap is smaller among borrowers with ten or more years in their job (interaction 1.260, p = 0.038), as that account predicts, but the affiliation OR remains below one among them (0.795, p = 0.036). The density and shock interactions are unchanged when all three are estimated together (Appendix Table C4). Religious organizations also insure members' consumption against income shocks (Dehejia et al., 2007), as they did in the Indonesian crisis (Chen, 2010). Such insurance would cushion an affiliated borrower before default, although shared ties can spread default as well (Adbi et al., 2024).

## 5.6 Timing: the distress-marker objection

The distress-marker objection of Section 4.2 predicts early defaults among religious-language borrowers, and the timing runs the other way. A discrete-time hazard on loan-month panels puts the affiliation hazard ratio (HR) at 0.686, flat over the life of the loan. Religious language is unrelated to hazard in the first year (0.956, p = 0.85), and its association appears only later (1.274, p = 0.027). Figure 5 shows the same timing without a model: affiliated borrowers run below the comparison group from the first year, while the religious-language curve tracks its comparison group for a year and separates afterward. The default date is approximate, so I treat the timing evidence as suggestive.

![Figure 5. Cumulative default by months since origination, 36-month loans. Default is dated four months after the last payment. Comparison groups are reweighted to the treated group's grade × origination-year distribution. Panel A: 2,398 affiliated loans in the terminated sample; Panel B: 507 religious-language loans in the description sample.](fig5_cumdefault.png){width=6.3in}

# 6. Discussion

## 6.1 Two signals, one reading

The results sort into a simple pattern. A borrower whose job title places him or her in a religious institution defaults less than an observably identical borrower. A borrower who invokes faith in the loan request defaults more. Affiliation is a tie, not a message. The borrower reported a job, not a claim addressed to the lender, and the tie is visible to a congregation that can learn if the loan goes unpaid. What it tells the lender is that someone else is watching. Religious language is a message, not a tie. The borrower chose to address it to strangers deciding whether to lend, it costs nothing, and no one can check it. The borrowers who write it tend to be the ones in difficulty, and the ones with little hard information to offer instead. What matters is who observes the borrower and who chooses to speak, not the depth of anyone's faith. The same faith can enter a credit file as information or as persuasion.

The two results do not carry equal weight. The affiliation estimate survives every check in Section 5.1. Occupation controls, comparisons restricted to secure or to mission-driven jobs, entropy balancing, DML, a split by period and a second platform all leave it in place. Under Oster's proportional-selection assumption, an unobserved trait could account for the estimate only if it were several times as strong as all observed controls combined. The language estimate keeps its sign and roughly its size in every specification, and it comes from the descriptions a coder confirmed as religious, not from the dictionary matches the coder rejected (Table 8). But once the full text is represented, the interval widens enough to include zero, and a confounder no stronger than employment length would do the same. What H2 establishes is a positive association in the confirmatory specification. It does not establish an effect of religious wording separate from the text it arrives in. The timing of default fits this reading rather than its main rival. Religious language is not associated with a higher hazard in the first year, as it would be if the language marked distress at application. The positive association appears only after a year. The affiliation advantage, by contrast, is present from the first months and constant thereafter.

## 6.2 Community, not the job

The natural alternative reading of the affiliation result is that church jobs are steady. The evidence within the affiliated group is what argues against reading it that way alone. Three findings line up. Church secretaries and administrators, whose pay and tenure resemble those of office workers elsewhere, default as little as the clergy, and a Wald test cannot tell the two coefficients apart. The advantage grows where congregations are denser in the borrower's ZIP area, and the within-area gap is larger in denser areas once ZIP3 fixed effects are added. A steady paycheck would not produce that, because a paycheck does not depend on how many other churches stand nearby. And the advantage does not widen when local unemployment rises, which is where a job-stability account says it should.

The third finding is weaker than the first two. The period was mostly a recovery, the positive-control occupations did not respond either, and the smaller gap among long-tenure borrowers leaves job stability some role. Congregation density, for its part, does not measure monitoring or sanctions themselves. It measures a condition under which they should be stronger. Still, the pattern across the three findings is what community as collateral predicts and what job stability does not. It also reproduces, at the level of individuals, what group-lending studies find when they vary the group. Repeated contact within a group that observes its members lowers default (Feigenberg et al., 2013), and the group disciplines even when the lender has written no joint-liability contract (Giné and Karlan, 2014).

## 6.3 How much is it worth

Neither signal is priced, in the sense that neither moves the interest rate. Hertzberg et al. (2018) describe LendingClub's pricing as a rate menu fixed by sub-grade, term and amount at a given time, and the file is consistent with that. Within a sub-grade, term and month of origination the rate takes at most five distinct values, 95 percent of loans sit at the modal value, and the remainder reflect schedule changes within the month. The job title and the description have no room in that schedule. Against loans in the same sub-grade-year cell, affiliated borrowers defaulted at 13.3 rather than 17.4 percent and lost 5.5 rather than 7.7 cents per dollar funded. That is a gap of 2.2 cents over an average 41.5-month term, or an annualized net-loss gap of roughly 64 basis points relative to the cell. Loans with religious language went the other way: 20.0 against 15.9 percent default, 7.1 against 6.1 cents lost, or an annualized net-loss gap of about 28 basis points over a 42.1-month average term (Appendix Table C7). Loss is the realized shortfall on defaulted loans, one dollar minus total payments received per dollar funded, recoveries included, and zero for repaid loans. The benchmark weights sub-grade-year cells by the distribution of the flagged loans, and the annual figure divides the cumulative gap by the average contractual term. Adding term to the cell definition moves the two figures to 67 and 29 basis points. The signals flag a fraction of one percent of loans, so the gap is not a tradable strategy. It measures, in the units investors use, the difference in realized net losses that grade-based pricing did not reflect. On Prosper, where investors bid on rates, unverifiable disclosures earned lower rates (Michels, 2012) and text was priced, if not fully (Gao et al., 2023). In corporate debt, county religiosity earns a lower spread (Jiang et al., 2018). LendingClub's pricing used none of this, and where its terms drew out private information it was through the loan menu (Hertzberg et al., 2018). Nor did investors react to the language on their own account, as far as the file shows. It does not record how quickly a listing filled, and what it does record, the investor-funded share and the ratio of funded to requested amount, is unrelated to religious language (all p > 0.4; Appendix Table C7). On Kiva, where funding speed is observed, religious expression slows funding, less so among more religious lenders (Anglin et al., 2023).

## 6.4 Individual religion and local religion

The religiosity literature in finance is mostly about places, where a more religious surrounding is favorable for firms (He and Hu, 2016), credit unions (Davidson et al., 2026) and mortgages (Li and Ucar, 2022). My signals are measured on individual borrowers. In Section 5.5 the affiliation estimate does not move when local religiosity is controlled, and local religiosity itself is associated with slightly more default, not less. Those studies concern firms, institutions or mortgages, and even there the sign of an area's religious makeup is not fixed (Hasan et al., 2025). Whatever lies behind the affiliated borrower's lower default is a property of belonging to a religious institution, amplified by the density of such institutions rather than replaced by it.

## 6.5 Limits

This is an observational study of one platform's borrowers, most of whom are American and, where religion is visible, Christian. There is no instrument for working in a church, no natural experiment that moves people into or out of one, and no borrower identifier, so a within-borrower design is not available. The platform does not record age, education, marital status or household structure, on any of which church employees may differ. Nor does it record the longer planning horizon and greater thrift that religious households report (Renneboog and Spaenjers, 2012), which could lower default without any community watching. The affiliation indicator comes from a free-text job title and misses affiliated borrowers who described their job differently. If they resemble the ones I find, the omission biases the estimate toward zero, and otherwise the bias could run either way. The religious-language results describe borrowers who chose to write a description, about 27 percent of the 2008–2014 loans in the Appendix Table C2 sample, and say nothing about those who did not. Where a religious phrase stops being religious is judged differently by different readers, so I read the type breakdown for direction only. Religious language is also rare enough that the narrative estimate is imprecise in the strictest specifications.

# 7. Conclusion

In an online consumer-credit market, borrowers whose job titles place them in a religious institution default less than observably identical borrowers, and borrowers who profess faith in their loan request default more. The first association is large, stable over a decade and reproduced on a second platform; the second keeps its size once the full text is accounted for but can no longer be distinguished from zero. Neither is reflected in the platform's grade-based rates. The evidence is most consistent with religious community functioning as borrower-side social collateral, and religious language as a low-cost signal that is informative in spite of, not because of, what it says.

Two implications follow. The first concerns how a lender reads religion in a credit file. The same subject carries opposite information depending on whether it arrives as a tie or as a statement, so a model that treated religion as a single variable would average two signals of opposite sign. The second concerns where social collateral is found. Group-lending schemes build a community around the loan, whereas the borrowers I study reported theirs in a job title. Other affiliations a credit file records only in passing, such as a cooperative or a union local, are natural places to look for the same pattern. What a credit market can learn from religion is not what a borrower says about it but where the borrower stands within it.

# Funding

This work was supported by the Baekseok University Research Fund.

# Declaration of generative AI and AI-assisted technologies in the writing process

During the preparation of this work the author used Claude (Anthropic) in order to edit the English text, check the consistency of numbers between the text and the tables, and format the manuscript. After using this tool, the author reviewed and edited the content as needed and takes full responsibility for the content of the publication. The use of a large language model as a text coder in the research method is described in Section 3.2 and Appendix B.

# References

Adbi, A., Lee, M., & Singh, J. (2024). Community influence on microfinance loan defaults under crisis conditions: Evidence from Indian demonetization. *Strategic Management Journal*, 45(3), 535–563.

Agarwal, S., Chomsisengphet, S., & Zhang, Y. (2017). How does working in a finance profession affect mortgage delinquency? *Journal of Banking & Finance*, 78, 1–13.

Al-Azzam, M., Hill, R. C., & Sarangi, S. (2012). Repayment performance in group lending: Evidence from Jordan. *Journal of Development Economics*, 97(2), 404–414.

Anglin, A. H., Milanov, H., & Short, J. C. (2023). Religious expression and crowdfunded microfinance success: Insights from role congruity theory. *Journal of Business Ethics*, 185(2), 397–426.

Baele, L., Farooq, M., & Ongena, S. (2014). Of religion and redemption: Evidence from default on Islamic loans. *Journal of Banking & Finance*, 44, 141–159.

Bentzen, J. S. (2021). In crisis, we pray: Religiosity and the COVID-19 pandemic. *Journal of Economic Behavior & Organization*, 192, 541–583.

Besley, T., & Coate, S. (1995). Group lending, repayment incentives and social collateral. *Journal of Development Economics*, 46(1), 1–18.

Byrt, T., Bishop, J., & Carlin, J. B. (1993). Bias, prevalence and kappa. *Journal of Clinical Epidemiology*, 46, 423–429.

Caldieraro, F., Zhang, J. Z., Cunha, M., Jr., & Shulman, J. D. (2018). Strategic information transmission in peer-to-peer lending markets. *Journal of Marketing*, 82(2), 42–63.

Cameron, A. C., Gelbach, J. B., & Miller, D. L. (2008). Bootstrap-based improvements for inference with clustered errors. *The Review of Economics and Statistics*, 90(3), 414–427.

Chen, D. L. (2010). Club goods and group identity: Evidence from Islamic resurgence during the Indonesian financial crisis. *Journal of Political Economy*, 118(2), 300–354.

Chen, H., Huang, H. H., Lobo, G. J., & Wang, C. (2016). Religiosity and the cost of debt. *Journal of Banking & Finance*, 70, 70–85.

Chernozhukov, V., Chetverikov, D., Demirer, M., Duflo, E., Hansen, C., Newey, W., & Robins, J. (2018). Double/debiased machine learning for treatment and structural parameters. *The Econometrics Journal*, 21(1), C1–C68.

Cinelli, C., & Hazlett, C. (2020). Making sense of sensitivity: Extending omitted variable bias. *Journal of the Royal Statistical Society: Series B*, 82(1), 39–67.

Clark, B., Hasan, I., Lai, H., Li, F., & Siddique, A. (2021). Consumer defaults and social capital. *Journal of Financial Stability*, 53, 100821.

Clifton, T., Brewer, M., & Upenieks, L. (2023). Religious affiliation and debt among U.S. households. *Social Science Research*, 115, 102911.

Conklin, J. N., Diop, M., & Qiu, M. (2022). Religion and mortgage misrepresentation. *Journal of Business Ethics*, 179(1), 273–295.

Crawford, V. P., & Sobel, J. (1982). Strategic information transmission. *Econometrica*, 50(6), 1431–1451.

Croux, C., Jagtiani, J., Korivi, T., & Vulanovic, M. (2020). Important factors determining Fintech loan default: Evidence from a LendingClub consumer platform. *Journal of Economic Behavior & Organization*, 173, 270–296.

Davaadorj, Z., Enkhtaivan, B., & Lu, W. (2024). The role of job titles in online peer-to-peer lending: An empirical investigation on skilled borrowers. *Journal of Behavioral and Experimental Finance*, 41, 100890.

Davaadorj, Z., Enkhtaivan, B., & Lu, W. (2026). Character and creditworthiness: Unveiling the role of job titles in peer-to-peer lending. *Journal of Financial Research*, 49(3), 1205–1228.

Davidson, T., Ngo, T., & Wang, H. (2026). Credit union member benefits: Does local religiosity matter? *Journal of Financial Services Research*, 69(3), 181–217.

Dehejia, R., DeLeire, T., & Luttmer, E. F. P. (2007). Insuring consumption and happiness through religious organizations. *Journal of Public Economics*, 91(1–2), 259–279.

Deller, S. C., Conroy, T., & Markeson, B. (2018). Social capital, religion and small business activity. *Journal of Economic Behavior & Organization*, 155, 365–381.

Deng, J., Liu, Q., & Yan, S. (2025). Fostering social capital: The long-term effects of Protestant activities on corporate tax avoidance in modern China. *Journal of Economic Behavior & Organization*, 234, 107014.

Dorfleitner, G., Priberny, C., Schuster, S., Stoiber, J., Weber, M., de Castro, I., & Kammler, J. (2016). Description-text related soft information in peer-to-peer lending: Evidence from two leading European platforms. *Journal of Banking & Finance*, 64, 169–187.

Duarte, J., Siegel, S., & Young, L. (2012). Trust and credit: The role of appearance in peer-to-peer lending. *Review of Financial Studies*, 25(8), 2455–2484.

Farrell, J., & Rabin, M. (1996). Cheap talk. *Journal of Economic Perspectives*, 10(3), 103–118.

Feigenberg, B., Field, E., & Pande, R. (2013). The economic returns to social interaction: Experimental evidence from microfinance. *Review of Economic Studies*, 80(4), 1459–1483.

Freedman, S., & Jin, G. Z. (2017). The information value of online social networks: Lessons from peer-to-peer lending. *International Journal of Industrial Organization*, 51, 185–222.

Gao, Q., Lin, M., & Sias, R. (2023). Words matter: The role of readability, tone, and deception cues in online credit markets. *Journal of Financial and Quantitative Analysis*, 58(1), 1–28.

Ge, R., Feng, J., Gu, B., & Zhang, P. (2017). Predicting and deterring default with social media information in peer-to-peer lending. *Journal of Management Information Systems*, 34(2), 401–424.

Ghatak, M., & Guinnane, T. W. (1999). The economics of lending with joint liability: Theory and practice. *Journal of Development Economics*, 60(1), 195–228.

Giné, X., & Karlan, D. (2014). Group versus individual liability: Short and long term evidence from Philippine microcredit lending groups. *Journal of Development Economics*, 107, 65–83.

Grammich, C., Hadaway, K., Houseal, R., Jones, D. E., Krindatch, A., Stanley, R., & Taylor, R. H. (2012). *2010 U.S. Religion Census: Religious Congregations & Membership Study*. Association of Statisticians of American Religious Bodies.

Guiso, L., Sapienza, P., & Zingales, L. (2003). People's opium? Religion and economic attitudes. *Journal of Monetary Economics*, 50(1), 225–282.

Guiso, L., Sapienza, P., & Zingales, L. (2004). The role of social capital in financial development. *American Economic Review*, 94(3), 526–556.

Guiso, L., Sapienza, P., & Zingales, L. (2013). The determinants of attitudes toward strategic default on mortgages. *Journal of Finance*, 68(4), 1473–1515.

Hainmueller, J. (2012). Entropy balancing for causal effects: A multivariate reweighting method to produce balanced samples in observational studies. *Political Analysis*, 20(1), 25–46.

Hasan, I., He, Q., & Lu, H. (2022). Social capital, trusting, and trustworthiness: Evidence from peer-to-peer lending. *Journal of Financial and Quantitative Analysis*, 57(4), 1409–1453.

Hasan, I., Kiesel, K., & Noth, F. (2025). "And forgive us our debts": Christian moralities and over-indebtedness. *Journal of Financial Research*, 48(3), 1013–1031.

He, W., & Hu, M. R. (2016). Religion and bank loan terms. *Journal of Banking & Finance*, 64, 205–215.

Hertzberg, A., Liberman, A., & Paravisini, D. (2018). Screening on loan terms: Evidence from maturity choice in consumer credit. *Review of Financial Studies*, 31(9), 3532–3567.

Herzenstein, M., Sonenshein, S., & Dholakia, U. M. (2011). Tell me a good story and I may lend you money: The role of narratives in peer-to-peer lending decisions. *Journal of Marketing Research*, 48(SPL), S138–S149.

Hilary, G., & Hui, K. W. (2009). Does religion matter in corporate decision making in America? *Journal of Financial Economics*, 93(3), 455–473.

Iacus, S. M., King, G., & Porro, G. (2012). Causal inference without balance checking: Coarsened exact matching. *Political Analysis*, 20(1), 1–24.

Iannaccone, L. R. (1992). Sacrifice and stigma: Reducing free-riding in cults, communes, and other collectives. *Journal of Political Economy*, 100(2), 271–291.

Iannaccone, L. R. (1994). Why strict churches are strong. *American Journal of Sociology*, 99(5), 1180–1211.

Iannaccone, L. R. (1998). Introduction to the economics of religion. *Journal of Economic Literature*, 36(3), 1465–1495.

Iyer, R., Khwaja, A. I., Luttmer, E. F. P., & Shue, K. (2016). Screening peers softly: Inferring the quality of small borrowers. *Management Science*, 62(6), 1554–1577.

Iyer, S. (2016). The new economics of religion. *Journal of Economic Literature*, 54(2), 395–441.

Jiang, F., John, K., Li, C. W., & Qian, Y. (2018). Earthly reward to the religious: Religiosity and the costs of public and private debt. *Journal of Financial and Quantitative Analysis*, 53(5), 2131–2160.

Karlan, D. S. (2005). Using experimental economics to measure social capital and predict financial decisions. *American Economic Review*, 95(5), 1688–1699.

Karlan, D. S. (2007). Social connections and group banking. *The Economic Journal*, 117(517), F52–F84.

Karlan, D., Möbius, M., Rosenblat, T., & Szeidl, A. (2009). Trust and social collateral. *Quarterly Journal of Economics*, 124(3), 1307–1361.

Kartik, N. (2009). Strategic communication with lying costs. *Review of Economic Studies*, 76(4), 1359–1395.

Kirchmaier, I., Prüfer, J., & Trautmann, S. T. (2018). Religion, moral attitudes and economic behavior. *Journal of Economic Behavior & Organization*, 148, 282–300.

Kriebel, J., & Stitz, L. (2022). Credit default prediction from user-generated text in peer-to-peer lending using deep learning. *European Journal of Operational Research*, 302(1), 309–323.

Le, Q., & Mikolov, T. (2014). Distributed representations of sentences and documents. *Proceedings of the 31st International Conference on Machine Learning*, PMLR 32(2), 1188–1196.

Lei, L., Lu, W., Niu, G., & Zhou, Y. (2024). Religiosity and financial distress of the young. *Journal of Banking & Finance*, 168, 107276.

Li, L., & Ucar, E. (2022). Does religion affect mortgage delinquency? *International Real Estate Review*, 25(2), 237–265.

Lin, M., Prabhala, N. R., & Viswanathan, S. (2013). Judging borrowers by the company they keep: Friendship networks and information asymmetry in online peer-to-peer lending. *Management Science*, 59(1), 17–35.

Lu, H., Wang, B., Wang, H., & Zhao, T. (2020). Does social capital matter for peer-to-peer lending? Empirical evidence. *Pacific-Basin Finance Journal*, 61, 101338.

Lun, X., Meng, X., & Xu, J. (2024). Is cheap talk just empty words? The signalling value of voluntary promises for loan repayment. *Applied Economics Letters*, 31(17), 1737–1741.

Michels, J. (2012). Do unverifiable disclosures matter? Evidence from peer-to-peer lending. *The Accounting Review*, 87(4), 1385–1413.

Netzer, O., Lemaire, A., & Herzenstein, M. (2019). When words sweat: Identifying signals for loan default in the text of loan applications. *Journal of Marketing Research*, 56(6), 960–980.

Noussair, C. N., Trautmann, S. T., van de Kuilen, G., & Vellekoop, N. (2013). Risk aversion and religion. *Journal of Risk and Uncertainty*, 47(2), 165–183.

Nowak, A., Ross, A., & Yencha, C. (2018). Small business borrowing and peer-to-peer lending: Evidence from Lending Club. *Contemporary Economic Policy*, 36(2), 318–336.

Oster, E. (2019). Unobservable selection and coefficient stability: Theory and evidence. *Journal of Business & Economic Statistics*, 37(2), 187–204.

Prokhorenkova, L., Gusev, G., Vorobev, A., Dorogush, A. V., & Gulin, A. (2018). CatBoost: Unbiased boosting with categorical features. *Advances in Neural Information Processing Systems*, 31.

Putnam, R. D. (2000). *Bowling Alone: The Collapse and Revival of American Community*. Simon & Schuster.

Rajan, R. G., & Zingales, L. (1998). Financial dependence and growth. *American Economic Review*, 88(3), 559–586.

Renneboog, L., & Spaenjers, C. (2012). Religion, economic attitudes, and household finance. *Oxford Economic Papers*, 64(1), 103–127.

Sanz-Guerrero, M., & Arroyo, J. (2025). Credit risk meets large language models: Building a risk indicator from loan descriptions in P2P lending. *Inteligencia Artificial*, 28(75), 220–247.

Sosis, R., & Bressler, E. R. (2003). Cooperation and commune longevity: A test of the costly signaling theory of religion. *Cross-Cultural Research*, 37(2), 211–239.

Spence, M. (1973). Job market signaling. *Quarterly Journal of Economics*, 87(3), 355–374.

Stiglitz, J. E. (1990). Peer monitoring and credit markets. *World Bank Economic Review*, 4(3), 351–366.

Valencia Caicedo, F., Dohmen, T., & Pondorfer, A. (2023). Religion and cooperation across the globe. *Journal of Economic Behavior & Organization*, 215, 479–489.

Wang, C., Wang, J., Wu, C., & Zhang, Y. (2023). Voluntary disclosure in P2P lending: Information or hyperbole? *Pacific-Basin Finance Journal*, 79, 102024.

Webb, M. D. (2023). Reworking wild bootstrap-based inference for clustered errors. *Canadian Journal of Economics*, 56(3), 839–858.

\newpage

# Appendix

## Appendix A. Timing

**Appendix Table A1. Discrete-time hazard**

| | Loans | Loan-months | Events | HR (all) | HR ≤12 months | HR >12 months |
|---|---:|---:|---:|---:|---:|---:|
| Affiliation (all 3,105 affiliated loans) | 33,105 | 725,884 | 6,359 | 0.686 (p<0.001) | 0.693 (p<0.001) | 0.684 (p<0.001) |
| Religious language | 8,681 | 245,747 | 1,360 | 1.217 (p 0.055) | 0.956 (p 0.85) | 1.274 (p 0.027) |

*Notes.* Complementary log-log (cloglog) model on loan-month panels, with default dated four months after last payment (capped at term) and Fully Paid censored at last payment. The model includes a cubic in loan progress, year and grade FE, and credit and loan controls, with SE clustered by loan. Comparison groups subsampled (30,000 loans for affiliation, 8,000 for religious language).

**Appendix Table A2. Affiliation estimate by tercile of local religiosity**

| Adherence tercile of ZIP3 area | Affiliation OR | p-value | N affiliated |
|---|---:|---:|---:|
| Low | 0.708 | <0.01 | 890 |
| Middle | 0.830 | <0.01 | 974 |
| High | 0.585 | <0.01 | 1,241 |

*Notes.* Table 2 specification estimated separately within terciles of the 2010 adherence rate (Table 11 data).

**Appendix Table A3. Affiliation and religious language by quintile of local religiosity (Figure 4)**

| Quintile | Affiliation OR by congregation density (95% CI) | N affiliated | Religious-language OR by adherence (95% CI) | N religious language |
|---|---:|---:|---:|---:|
| 1 (lowest) | 0.847 (0.688–1.044) | 382 | 1.104 (0.734–1.662) | 163 |
| 2 | 0.847 (0.696–1.031) | 414 | 1.442 (0.835–2.491) | 115 |
| 3 | 0.624 (0.514–0.758) | 515 | 1.228 (0.861–1.753) | 152 |
| 4 | 0.679 (0.548–0.841) | 699 | 1.242 (0.854–1.806) | 142 |
| 5 (highest) | 0.618 (0.526–0.726) | 1,095 | 1.500 (1.095–2.053) | 109 |

*Notes.* Panel A of Figure 4: Table 2 specification estimated within quintiles of congregation density across ZIP3 areas. Panel B: Table 6, column (3) specification within quintiles of the adherence rate.

## Appendix B. Coding and measurement

*Codebook for religious-language descriptions.* Each flagged record receives one type and one frame. Type a, formulaic: religious words used as a greeting, closing or idiom that makes no claim about the writer ("Thank you and God bless", "God willing", "prayers answered"). Type b, identity or value claim: the writer asserts his or her own faith, religious identity or a religious value as a reason to trust him or her ("as a Christian I believe in paying my debts", "I have strong faith in God"). Type c, practice or expense: a concrete religious activity or outlay, such as tithes or offerings in a budget, church employment, a mission trip or seminary tuition. Type x, not religious: the matched word is used in a non-religious sense ("Lord & Taylor", "good faith", "heaven forbid"). When more than one type applies the coder assigns the strongest in the order c, then b, then a. The frame records what accompanies the religious content in the same description: religious content alone, a moral self-presentation (promises, honesty, responsibility), a hardship narrative (job loss, illness, divorce, medical bills), or both. Coders read each record without access to any automatic label. The three religious types follow the distinction in Section 2 between a costless invocation and a report of practice that ties the borrower to a community.

**Appendix Table B1. Language-model coding of religious-language descriptions**

| Type | N | Default rate (raw) | OR (full controls) | p-value |
|---|---:|---:|---:|---:|
| a. Formulaic ("God bless", "prayers answered") | 467 | 0.221 | 1.385 | 0.001 |
| b. Identity / value claim | 34 | 0.206 | 1.460 | 0.32 |
| c. Practice / expense (tithe, church employment, mission) | 82 | 0.146 | 0.988 | 0.97 |
| x. Non-religious match (dictionary false positive) | 98 | 0.143 | 0.948 | 0.88 |

*Notes.* Exploratory; not part of the confirmatory design. Coders: primary coding by a large language model (LLM) coder over all 820 flagged records (717 with description text, 103 title-only), using the codebook above as the prompt. The coder was Claude Fable 5.1 (Anthropic, model ID claude-fable-5-1), run as twelve parallel instances in the Claude application on 18 September 2026, each instance reading a disjoint share of the records so that every record received one label; the application does not expose a sampling temperature or other decoding settings, so the coding ran at its defaults. Agreement: independent recoding of a stratified 200-record sample by a second LLM coder (Claude Opus, Anthropic, same application, date and settings) gives κ = 0.86 for type (raw agreement 91%), 0.81 for religious vs non-religious, 0.73 for frame. A human coder (the author, who read the texts without the loan outcomes but was not blind to the hypotheses) coded the same 200 records and agrees with the primary coding at κ = 0.72 for type (raw 82%), 0.55 for religious vs non-religious (raw 85%, the low κ reflecting that 80% of the records are religious) and 0.48 for frame. The human coder reads 11 of the 40 model-coded false positives as religious and 20 of the 160 model-coded religious records as not. Because 80% of the sample is religious, the prevalence-adjusted κ for that binary is 0.69 (Byrt et al., 1993). The design note set κ of 0.7 as the bar for the coding. The four-way type clears it in both checks; the human coder's religious versus non-religious binary (0.55, 0.69 prevalence-adjusted) and the frame (0.48) do not. The frame enters no estimate, and the binary enters only Table 8, which should be read with that in mind. Most of the 31 disagreements sit at two boundaries, formulaic invocation against non-religious (17 records) and identity claim against non-religious (8 records). In the practice category the two agree on 36 of 40. Measurement completeness: a classifier trained with all explicit religious words masked (cross-validated area under the ROC curve 0.92) ranked the 122,611 unflagged descriptions. Because the masked classifier learns the gratitude and hardship style that accompanies religious language rather than religion itself, the ranking is a weak detector. The LLM coder read a stratified sample of it: 59 of the top 500 (0 religious), 58 of ranks 500–2,000 (0), 240 of ranks 2,000–10,000 (3) and 99 below rank 10,000 (0). Extrapolating the 2,000–10,000 stratum gives about 100 missed descriptions, and the sample below rank 10,000 bounds the miss rate there only at about 3 percent, so the upper bound is wide. A second search for implicit phrases ("godsend", "karma", "higher power") coded 11 of 77 matches as religious. Any missed religious descriptions sit in the comparison group and attenuate the H2 estimate toward zero.

**Appendix Table B2. Audit of the affiliation indicator (200 randomly drawn affiliated job titles)**

| Code | N | Examples |
|---|---:|---|
| A. Religious institution, clerical role | 146 | Pastor, Senior Pastor, Minister, Chaplain, Priest, Worship Leader |
| B. Religious institution, non-clerical staff | 48 | Director of Music Ministry, Parish Business Manager, "St. Thomas Episcopal Church", "Indianapolis Hebrew Congregation" |
| C. Not religious employment | 2 | "East Baton Rouge Parish Sheriff's Office", "Ouachita Parish Sheriff's Office" (Louisiana civil parishes) |
| D. Cannot classify from title | 4 | "Church and Stagg", "Pastor/Soccer Club Director", "Parish Manager" |

*Notes.* Codes assigned by the primary LLM coder of Appendix Table B1. Precision 97 percent (98 percent counting D as half). A rule targeting civil-parish titles (parish + sheriff, library, government, assessor, police jury, court, etc.) identifies 30 such loans in the terminated sample, all in Louisiana, with a raw default rate of 30 percent. Excluding them gives an affiliation OR of 0.683 (SE 0.041) in the Table 2, column (1) specification.

*Occupation indicators.* The eight stable-occupation indicators and the three neighboring occupation groups are keyword rules applied to the job title, in the same way as the affiliation rule. Teachers: teacher, professor, educator, instructor. Police: police, correction(s), sheriff, deputy, trooper. Firefighters: firefighter, fireman, fire dept. Military: army, navy, air force, marine corps, military, soldier. Government: government, federal, state of, city of, county (of), municipal. Nurses: nurse, RN, LPN. Postal: USPS, postal, post office. Transit: transit, MTA, bus driver, bus operator. Neighboring groups, each excluding affiliated titles: nonprofit and social service (non-profit, social work, social service, human services, case manager, caseworker, counselor, charity, foundation, community center or outreach, and named charities such as the YMCA, Salvation Army, Red Cross, United Way, Goodwill and Habitat for Humanity); education (teacher, professor, educator, school, principal, teaching, instructor, faculty); healthcare (nurse, RN, LPN, hospital, medical, health, physician, therapist, clinic).

**Appendix Table B3. Sample construction**

| Step | Loans |
|---|---:|
| LendingClub file, June 2007–December 2018 | 2,260,701 |
| Terminal status (Fully Paid, Charged Off, Default) | 1,345,350 |
| Non-missing DTI, FICO and interest rate (analysis sample) | 1,344,976 |
| Affiliation indicator, full file | 5,014 |
| Affiliation indicator, analysis sample (H1 treated): clerical role / church staff | 3,105: 2,497 / 608 |
| H1 estimation sample (treated plus random draw of 250,000) | 253,105 |
| Non-empty description, full file | 125,811 |
| Description sample (analysis sample with a description) | 123,292 |
| Religious-dictionary matches, full file: with description text / title only | 820: 717 / 103 |
| Religious-dictionary matches in the analysis sample | 784 |
| Religious-dictionary matches in the description sample (H2 treated) | 681 |
| Coded religious (formulaic 467, identity 34, practice 82) / not religious | 583 / 98 |

*Notes.* Counts from the public loan file after removing platform boilerplate from descriptions. The 103 title-only matches have a religious term in the loan title but no description text and therefore fall outside the description sample.

## Appendix C. Additional robustness

**Appendix Table C1. Covariate balance before and after entropy balancing (largest imbalances)**

| Covariate | SMD before | SMD after |
|---|---:|---:|
| Income verified | −0.175 | 0.000 |
| State: NY | −0.166 | 0.000 |
| State: AL | 0.139 | 0.000 |
| State: CA | −0.139 | 0.000 |
| State: NC | 0.132 | 0.000 |
| State: WA | −0.111 | 0.000 |
| Home: rent | −0.109 | 0.000 |
| Employment length < 1 year | −0.108 | 0.000 |
| Income source verified | 0.107 | 0.000 |
| Employment length 10+ years | 0.102 | 0.000 |
| Grade D | −0.102 | 0.000 |

*Notes.* Standardized mean differences (affiliated minus other) for the 76 covariate moments used in Table 2, column (5). The eleven shown are those exceeding 0.10 in absolute value before weighting. Maximum |SMD| 0.175 before, below 10⁻⁷ after. Effective control sample size after weighting 172,965.

**Appendix Table C2. Who wrote a description? Logit of a non-empty description, 2008–2014 terminated loans**

| | OR (per unit) | p-value | AME (per SD) |
|---|---:|---:|---:|
| Religious-institution affiliation | 1.017 | 0.81 | +0.2 pp |
| Interest rate | 1.096 | <0.001 | +6.1 pp |
| FICO | 0.999 | <0.001 | −0.5 pp |
| Log income | 0.998 | 0.89 | 0.0 pp |
| DTI | 1.000 | 0.79 | 0.0 pp |
| 60-month term | 0.958 | 0.039 | |
| Log amount | 1.249 | <0.001 | +2.2 pp |
| Grade B / C / D / E / F / G (vs A) | 0.63 / 0.38 / 0.26 / 0.18 / 0.15 / 0.16 | all <0.001 | |

*Notes.* All affiliated 2008–2014 terminated loans plus 150,000 randomly drawn others (N = 151,191, of which 27.3 percent have a description). Same controls and state fixed effects as Table 2, with SE clustered by state. ORs are per unit of the variable (one percentage point of rate, one FICO point, one log point of income or amount, one DTI point); AMEs are per standard deviation. Pseudo-R² 0.24, most of it from origination-year effects.

**Appendix Table C3. Alternative inference and samples for the two confirmatory estimates**

| Clustering | H1: affiliation, SE (p) | H2: religious language, SE (p) |
|---|---:|---:|
| State (51 clusters; reported) | 0.041 (<0.001) | 0.103 (0.016) |
| ZIP3 area (892 clusters) | 0.054 (<0.001) | 0.100 (0.013) |
| Month of origination (138 clusters) | 0.050 (<0.001) | 0.092 (0.007) |
| Heteroskedasticity-robust, no clustering | 0.054 (<0.001) | 0.101 (0.014) |
| Wild cluster bootstrap by state, linear probability model: p | <0.001 | 0.015 |
| 95% CI of the OR (state clusters) | 0.638–0.751 | 1.047–1.566 |
| H1 on all 1,344,976 terminated loans: OR (95% CI) | 0.694 (0.637–0.755) | |
| H1 with five further random comparison draws: OR range | 0.689–0.701 | |

*Notes.* Standard errors of the log-odds coefficient in the Table 2, column (1) and Table 6, column (3) specifications (coefficients −0.368 and +0.247). Wild cluster bootstrap: restricted (null imposed), Webb weights (Webb, 2023), 9,999 draws, on the linear probability analogue of each specification (51 state clusters for H1, 50 for H2, since one state has no description-sample loans). Random draws use seeds 2 to 6.

**Appendix Table C4. Competing explanations in one specification**

| | (1) Density | (2) Shock | (3) Tenure and verification | (4) All |
|---|---:|---:|---:|---:|
| Affiliation | 0.635 (<0.001) | 0.688 (<0.001) | 0.631 (<0.001) | 0.589 (<0.001) |
| Affiliation × congregation density (per SD) | 0.821 (0.002) | | | 0.830 (0.003) |
| Congregation density (per SD) | 1.059 (0.001) | | | 1.034 (0.040) |
| Affiliation × subsequent change in unemployment (per SD) | | 0.975 (0.58) | | 0.988 (0.80) |
| Affiliation × ten or more years in job | | | 1.260 (0.038) | 1.245 (0.048) |
| Affiliation × income verified | | | 0.998 (0.98) | 0.997 (0.98) |

*Notes.* Logit ORs, two-sided p in parentheses. Table 2 sample merged to ZIP3 unemployment and congregation data, N = 239,198 (2,973 affiliated), same controls as Table 2, SE clustered by state. Density standardized across ZIP3 areas as in Table 11; columns (1) and (4) also control for adherence, columns (2) and (4) for the unemployment rate at origination. The density interaction is 0.82 here rather than 0.84 in Table 11 because the sample is restricted to loans that merge to the unemployment data. Column (3): implied affiliation OR among borrowers with ten or more years in their job 0.795 (95% CI 0.642–0.985, p = 0.036; 1,119 affiliated). Predicted default from column (1) at one SD below and above mean density: affiliated 16.5 and 13.2 percent, others 19.9 and 21.6 percent.

**Appendix Table C5. Religious language: alternative text representations, repeated cross-fitting and term count**

| Specification | θ (AME) | p-value | Splits with p < 0.05 |
|---|---:|---:|---:|
| DML, six dictionaries | +0.033 | 0.027 | |
| + spaCy word vectors, 50 principal components (PCA-50) | +0.026 | 0.09 | |
| + spaCy word vectors, full 300-d | +0.023 | 0.14 | |
| + TF-IDF, 100 singular-value-decomposition (SVD) components | +0.028 | 0.059 | |
| + doc2vec | +0.024 | 0.11 | |
| Repeated cross-fitting (20 splits, median), dictionaries | +0.032 | 0.031 | 20/20 |
| Repeated cross-fitting, TF-IDF-SVD100 | +0.030 | 0.045 | 12/20 |
| Repeated cross-fitting, spaCy PCA-50 | +0.025 | 0.10 | 0/20 |
| Repeated cross-fitting, doc2vec | +0.024 | 0.11 | 0/20 |
| Religious-term count (Table 6, column (3) controls) | OR | p-value | |
| One term | 1.14 | 0.24 | |
| Two terms | 1.56 | 0.06 | |
| Three or more terms | 1.87 | 0.07 | |
| log(1 + count) | 1.37 | 0.006 | |

*Notes.* Description sample of Table 6. DML partially linear model with CatBoost nuisance functions and 5-fold cross-fitting, with doc2vec after Le and Mikolov (2014). The design note named a sentence-transformer model (all-MiniLM-L6-v2) for the text representation; its download was blocked in the computing environment, so the note's fallback, TF-IDF with SVD, was used and the spaCy word vectors and doc2vec were added; across-split SD of θ is 0.0013–0.0018 in every repeated-cross-fitting specification. Term-count rows are logit ORs with the Table 6, column (3) controls.

**Appendix Table C6. Affiliation and local unemployment shocks**

| | OR | p-value |
|---|---:|---:|
| Affiliation | 0.687 | <0.001 |
| Unemployment rate at origination (per SD) | 1.091 | 0.001 |
| Largest subsequent change in unemployment over loan life (per SD) | 1.028 | 0.001 |
| Affiliation × change | 0.975 | 0.58 |
| Affiliation × level | 0.959 | 0.44 |
| Affiliation by shock tercile (small / mid / large) | 0.588 / 0.763 / 0.721 | all <0.01 |
| Positive control: teacher × change; government × change | 1.057; 1.004 | 0.29; 0.93 |

*Notes.* BLS Local Area Unemployment Statistics (LAUS) county annual unemployment 2008–2018, ZIP3 population-weighted. "Change" = maximum rate in the years after origination within term, truncated at 2018, minus rate at origination (mean −0.62 pp, SD 0.55, so the measure is a maximum subsequent change and is negative for most loans); the period is mostly a recovery. Table 2 sample merged to ZIP3 unemployment, N = 239,198 (2,973 affiliated; 5,663 teachers and 2,202 government employees as positive control), same controls, SE clustered by state.

**Appendix Table C7. Pricing, investor response and prediction: the numbers behind Sections 4.4 and 6.3**

| | Affiliation | Religious language |
|---|---:|---:|
| Default rate, flagged loans / same sub-grade-year cells (%) | 13.3 / 17.4 | 20.0 / 15.9 |
| Net loss on defaulted loans per dollar funded, flagged / cells (cents) | 5.51 / 7.72 | 7.08 / 6.09 |
| Mean contractual term (months) | 41.5 | 42.1 |
| Annualized net-loss gap (basis points) | −64 | +28 |
| Investor-funded share, coefficient (p) | | −0.0009 (0.74) |
| Fully investor-funded, OR (p) | | 0.938 (0.53) |
| Funded / requested amount, coefficient (p) | | −0.0015 (0.50) |
| Cross-validated AUC without / with the indicator | 0.7150 / 0.7151 | 0.6958 / 0.6958 |
| Change in AUC (bootstrap 95% CI) | 0.00018 (0.00005 to 0.00029) | 0.00002 (−0.00010 to 0.00014) |
| Rate schedule: issue-month × sub-grade × term cells / loans at the cell's modal rate / most distinct rates in a cell | 7,642 / 94.7% / 5 | |

*Notes.* Rows 1–4: terminated loans, cells defined by sub-grade and origination year (254 cells for affiliation, 165 for religious language), cell values weighted by the flagged loans' distribution across cells; net loss = default × (1 − total payments received per dollar funded), so repaid loans count as zero; annualized gap = cumulative gap ÷ (mean contractual term of the flagged loans / 12), computed from unrounded values. With term added to the cell definition the gaps are −67 and +29 basis points; dividing by realized life to the last payment (23.3 and 28.2 months) instead of contractual term gives −114 and +42. Rows 5 and 7: OLS; row 6: logit; description sample (N = 123,292), Table 6, column (3) controls, SE clustered by state. Rows 8–9: five-fold cross-validated logit on the H1 sample (affiliation, N = 253,105) and the description sample (religious language, with the text dictionaries), with a 300-draw paired bootstrap of the out-of-fold predictions. Row 10: all 2,260,668 loans in the file with a rate, grouped by issue month, sub-grade and term; 99.94 percent of loans sit at one of the two most common rates of their cell. The by-year version is in the replication package (rate_schedule_by_year.csv).

![Appendix Figure C1. Fake-dictionary permutation. Distribution of the residualized linear probability coefficient on an indicator for 1,000 random sets of non-religious words matched to the religious dictionary's document frequency, Table 6, column (3) controls partialled out. The solid line marks the coefficient of the actual dictionary (0.035); the dotted line marks the permutation mean (−0.003, SD 0.014). Five of the 1,000 random sets reach the actual value (one-sided p = 0.005).](figC1_permutation.png){width=5in}
