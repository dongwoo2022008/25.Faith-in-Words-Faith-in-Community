---
title: "Faith in Words, Faith in Community: Religious Affiliation, Religious Language, and Default in Online Consumer Credit"
author: "Dongwoo Kim, Division of Advanced IT, Baekseok University"
date: "Draft v12, September 2026 (JEBO version, condensed)"
---

**Abstract.** Religion enters a consumer-credit file in two ways: as an affiliation a borrower reports in a job title, and as language a borrower chooses to use in a loan request. Using 1.34 million terminated LendingClub loans issued between 2007 and 2018, I find that the two are associated with default in opposite directions. Borrowers whose job titles place them in religious institutions (pastors and ministers, but also church secretaries and administrators) default about five percentage points less than borrowers with the same credit score, income, debt burden, loan terms, state and origination year. The estimate changes little with controls for eight stable occupations, with matching to nonprofit, education and healthcare workers, who show no comparable advantage, and with entropy balancing and double machine learning. Its sign holds in a smaller Prosper sample. The gap is larger where local congregations are denser, including within ZIP areas, and shows no detectable response to local unemployment shocks, the response a job-stability account would predict. Borrowers who invoke faith in their loan description default about three percentage points more in the confirmatory specification. Once the full text is represented, the estimate keeps its size but is no longer distinguishable from zero, so religious wording cannot be separated from the rest of the text. Neither signal is reflected in the platform's grade-based rates. The pattern is consistent with religious community acting as borrower-side social collateral, and with religious language as a low-cost, unverifiable signal whose association with default works against its sender.

*Keywords:* religion, social capital, consumer credit, credit risk, online lending, text analysis, signaling.
*JEL:* D14, G21, G41, Z12.

# 1. Introduction

Borrowers on the early online lending platforms, then called peer-to-peer, were asked to say something about themselves, and LendingClub gave them a free-text box. Some wrote nothing, some wrote a paragraph about the debts they wanted to consolidate, and a small number wrote about God. "Thank you and God bless." "As a Christian I believe in paying my debts." "Monthly budget: tithe $529, rent $900…" These sentences are rare, 717 among 125,811 loan descriptions, and it is tempting to treat them as noise. Netzer, Lemaire and Herzenstein (2019) did not: in their study of Prosper applications, mentions of God were among the words that appeared more often in the text of borrowers who later defaulted.

I want to stay with it, because the same platform contains a second, quieter trace of religion that points the other way. LendingClub also asked borrowers for their job title, and about one in four hundred wrote "pastor," "minister," "chaplain," "church administrator," or "church secretary." I call a borrower affiliated when the job title places the job inside a religious institution in this way. Those borrowers default less: 13.3 percent against 20.0 percent in the raw data, and about five percentage points less after I condition on grade, FICO, income, debt-to-income, loan terms, state and year. Borrowers who talk about faith in their loan request go the other way, defaulting about three percentage points more than their scores predict. Same platform, same years, same controls, opposite signs. Neither difference is reflected in the interest rate, because LendingClub priced loans by grade, so investors earned more than the grade implied on loans to church employees and less on loans that invoked faith. I document both facts in LendingClub's public file of terminated loans, in which neither signal is a field, and replicate the first on Prosper.

This paper is about that contrast, and about what lies behind the second half of it. The question is whether the two traces religion leaves in a credit file carry the same information about repayment, and if they do not, what separates them. My claim is narrow. I do not argue that religion causes repayment, nor do I offer a religious credit score, since the signals are too rare to move a predictive model. What I argue is that religion reaches a credit market through two channels that carry different information. Faith that is *professed*, invoked in a request for money, looks like a low-cost signal: it costs nothing to write, cannot be verified, travels with hardship and appeals for help, and its association with default is consistent in sign but not strong. Faith as *belonging*, a job inside a congregation, looks like a commitment with a community attached, and its association with default is large, stable across a decade, present for the church secretary as much as for the pastor, and stronger where there are more churches nearby. The broader point concerns organization rather than piety: a congregation may enforce repayment through ties that the lender never sees and cannot contract on.

The evidence within the affiliated group is what moves the paper from a curiosity about words to a claim about mechanism. The obvious alternative reading of the clergy result is that pastors have steady jobs, but three findings push against reading it that way alone. Non-clergy church employees, whose pay and job security resemble those of secretaries and administrators anywhere, default as little as the clergy do. The affiliation gap grows where congregations are denser in the borrower's ZIP area, which job stability alone would not produce, even under ZIP-level fixed effects. And it shows no detectable change when local unemployment rises over the life of the loan. None of these is a natural experiment. Still, together they fit the pattern one would expect if a religious congregation works, for its members, the way the group in a group-lending scheme works for its borrowers (Besley and Coate, 1995; Karlan, 2007). That is a community that observes financial conduct and in which default has a cost beyond the credit file, and here it sits on the borrower's side of the transaction rather than the lender's.

![Figure 1. Two channels through which religion enters a consumer-credit file. Solid boxes: institutional affiliation revealed by the job title, its proposed mechanism, and the confirmatory test H1; dashed boxes: religious language volunteered in the loan description, its mechanism, and H2. Local congregation density (2010 U.S. Religion Census) moderates H1 only. Estimates from Tables 2, 5 and 7; pricing gap from Section 6.1.](fig1_channels.png){width=6.3in}

I should be direct about what the design can and cannot do. There is no instrument, and the public file has no borrower identifiers that would allow within-borrower comparison, so church employees may differ from other borrowers in ways I cannot observe. I report how strong an unobserved confounder would have to be to erase the estimate (Section 5.1), and I name, for each piece of evidence, what it rules out and what it does not. The narrative result I treat more guardedly still: it is estimated from 681 loans, and once the full text is represented it can no longer be distinguished from zero, which by a rule I set in advance lowers the claim.

The finding speaks to three literatures. The first is the work on religion, social capital and economic behavior. Religious belief is associated with trust, reciprocity and cooperation across countries (Guiso, Sapienza and Zingales, 2003; Valencia Caicedo, Dohmen and Pondorfer, 2023), counties with more congregations have more small business activity (Deller, Conroy and Markeson, 2018), and historical missionary activity left a lasting trace in local trust (Deng, Liu and Yan, 2025). That literature establishes that religion builds the kind of network group-lending theory needs, but it does not observe an individual's place in such a network alongside a debt with money at stake. Here both appear in the same loan record, and the form of religion associated with lower default is an affiliation with a community rather than a clerical vocation, since church secretaries show the same gap as pastors. What a borrower believes is not something the file records.

The second is the finance literature on religion and credit, which has identified religion mostly through the lending contract or the borrower's surroundings. Islamic loans default less than conventional loans to comparable borrowers (Baele, Farooq and Ongena, 2014), firms in more religious U.S. counties borrow at lower spreads and with fewer covenants (He and Hu, 2016; Chen, Huang, Lobo and Wang, 2016), credit unions there lend more cheaply and hold better loans (Davidson, Ngo and Wang, 2026), and county adherence predicts lower mortgage delinquency and less misrepresentation (Li and Ucar, 2022; Conklin, Diop and Qiu, 2022). At the individual level, religious affiliation is associated with the kinds of debt a household carries (Clifton, Brewer and Upenieks, 2023) and adolescent religiosity with less adult financial distress (Lei, Lu, Niu and Zhou, 2024), but neither observes a loan and its repayment. What this paper adds is that religion enters an individual credit file in two observable forms which carry opposite information about the repayment of the same kind of loan in the same market, and that the affiliation of the individual, not the religiosity of the place, is the one associated with lower default.

The third literature is the work on borrower-supplied information in online credit markets, where lenders infer creditworthiness from what lies outside the credit score (Iyer, Khwaja, Luttmer and Shue, 2016) and price soft information such as social-network ties, not always correctly (Freedman and Jin, 2017). What they read includes appearance (Duarte, Siegel and Young, 2012), verified friendships (Lin, Prabhala and Viswanathan, 2013) and the job title itself (Davaadorj, Enkhtaivan and Lu, 2024, 2026), and broad occupation classes predict LendingClub defaults beyond standard risk factors (Croux, Jagtiani, Korivi and Vulanovic, 2020). The affiliation I study is a community tie of a much thicker kind than a platform friendship, and I look at default rather than funding. The text of the request has been studied most (Herzenstein, Sonenshein and Dholakia, 2011; Michels, 2012; Dorfleitner et al., 2016; Nowak, Ross and Yencha, 2018; Netzer et al., 2019; Kriebel and Stitz, 2022; Gao, Lin and Sias, 2023; Sanz-Guerrero and Arroyo, 2025). That work has established that words predict default and that self-authored identity claims can raise funding while predicting worse repayment (Herzenstein et al., 2011), but it has taken less interest in which words carry information of their own. Religious language, it turns out, cannot be separated from the circumstances it travels with once the full text is represented.

Section 2 sets out the argument and the two hypotheses, Section 3 the data, and Section 4 the empirical approach. Section 5 presents the results, Section 6 discusses magnitude and limits, and Section 7 concludes.

# 2. Religious community, religious language, and repayment

## 2.1 Community as collateral

Group-lending theory gives a clean account of why belonging can substitute for collateral. When borrowers are jointly liable, their peers have a stake in repayment and a reason to monitor one another (Stiglitz, 1990). When they can also sanction one another socially, default costs the defaulter standing in the group, which the lender can rely on even though it cannot contract on it (Besley and Coate, 1995; Ghatak and Guinnane, 1999). Karlan, Möbius, Rosenblat and Szeidl (2009) give the idea its model: the trust a borrower can draw on is the value of the network ties a default would put at risk, largest in dense, closely knit communities. The microfinance evidence suggests the mechanism is real. Borrowers more socially connected to their quasi-randomly formed groups repay more (Karlan, 2007), and those who prove trustworthy in a trust game repay better (Karlan, 2005). More frequent meetings cut default by two thirds (Feigenberg, Field and Pande, 2013), removing joint liability while keeping the meetings does not raise default (Giné and Karlan, 2014), and more religiously observant groups repay more promptly (Al-Azzam, Hill and Sarangi, 2012).

The insight travels beyond microfinance. Households in high-social-capital Italian provinces use more formal credit, most strongly where courts are slow (Guiso, Sapienza and Zingales, 2004). U.S. borrowers in communities with more social capital default less, most markedly when default would be strategic (Clark, Hasan, Lai, Li and Siddique, 2021; Guiso, Sapienza and Zingales, 2013). The same holds inside marketplace lending (Hasan, He and Lu, 2022; Lu, Wang, Wang and Zhao, 2020), and making a borrower's default visible to his social contacts deters it (Ge, Feng, Gu and Zhang, 2017).

A religious congregation is a community of this kind, and often an intense one (Putnam, 2000): members meet weekly, know one another's families, and share explicit norms about money. The economics of religion treats the congregation as a club that produces goods its members cannot buy elsewhere (Iannaccone, 1998; Iyer, 2016), whose costly demands screen out the less committed and raise participation among those who remain (Iannaccone, 1992, 1994). Religious communes that imposed more such demands outlived those that imposed fewer, whereas secular communes did not (Sosis and Bressler, 2003). Believers also report more positive reciprocity, altruism and trust on validated preference measures (Valencia Caicedo, Dohmen and Pondorfer, 2023). What this literature lacks is a link between an individual's membership in such a community and a financial outcome with money at stake.

A borrower who works for a church is embedded in that community more deeply than an ordinary member, because their employer is the congregation and their reputation among its members is their professional reputation. If a congregation functions as a group in the group-lending sense, its employees should be the members for whom the cost of default is highest, whether pastor or secretary, and that cost should scale with how much observing the community does. I extend the logic of social collateral from groups a lender organizes to an affiliation a borrower reports, and since I do not observe the community's monitoring directly, what I can observe is whether the pattern of default matches what that logic predicts and fails to match what its rivals predict.

The mechanism predicts three further things that discriminate between it and the main rival account, that church jobs are simply stable. The social cost of default depends on how closely a community observes a member, not on the member's income shocks. So non-clergy church employees should show the effect as strongly as clergy, since the community is the same. The effect should be larger where congregations are denser, and it should not vary with local labor-market shocks. A job-stability account is silent on the first two and predicts the opposite of the third, because the value of a steady paycheck shows itself when other borrowers lose theirs, so the affiliation advantage should widen when local unemployment rises. I did not specify these three as tests in advance, and I report them as evidence on mechanism rather than as confirmatory results.

**H1.** Conditional on credit score, income, debt burden, loan terms, state and origination year, borrowers whose stated occupation places them in a religious institution default less (odds ratio below one).

## 2.2 Language as a low-cost signal

The description box gives borrowers a second channel, and signaling theory says what to expect from it. A message anyone can send at no cost, to an audience that would like to hear it, is cheap talk (Crawford and Sobel, 1982; Farrell and Rabin, 1996), and whether it carries information depends on who chooses to send it rather than on what it says. A costly signal is different, since it separates senders only when its cost differs across them (Spence, 1973). If misreporting carries even a small moral cost, such talk becomes partly informative (Kartik, 2009), and in online lending unverifiable disclosure relates non-monotonically to loan quality (Caldieraro, Zhang, Cunha and Shulman, 2018). Yet the information need not run the way the sender intends. Religious people state stricter moral attitudes than the non-religious yet betray trust just as often in an anonymous trust game (Kirchmaier, Prüfer and Trautmann, 2018), and in lending, unverifiable self-description and voluntary repayment promises raise funding while predicting worse repayment (Herzenstein et al., 2011; Wang, Wang, Wu and Zhang, 2023; Lun, Meng and Xu, 2024). "God bless" costs nothing to write, cannot be verified, and is addressed to strangers deciding whether to lend, and two mechanisms make its expected association with default positive. The first is selection: the borrowers who feel moved to invoke faith in a request for money are disproportionately those whose situation gives them reason to, as the rise of religious practice in crises suggests (Chen, 2010; Bentzen, 2021). The same descriptions thank the reader in advance, describe hardship, and ask for help at several times the base rate. The second is substitution: a borrower with strong verifiable facts to offer tends to offer them, so appeals to faith concentrate where such facts are thin.

Under either mechanism the test is not whether religious language correlates with default, which Netzer et al. (2019) already showed, but whether it does so *after* the length, tone, hardship and gratitude content it travels with are held fixed. That residual is what the low-cost-signal reading predicts should remain, and what a "religious language is just distress language" reading predicts should not.

**H2.** Conditional on the same credit and loan controls and on the length, moral, hardship, gratitude, family, appeal and business content of the description, borrowers who use religious language default more (odds ratio above one).

The two signals can therefore take opposite signs even if affiliated borrowers and borrowers who invoke faith hold the same beliefs, because what matters is who observes the borrower and who chooses to speak, not the depth of anyone's faith. The theory also predicts something inside the description that can be checked. Suppose what makes a religious signal informative is that it costs something and ties the borrower to a community. Then a description that reports religious *practice* should resemble the affiliation signal more than "God bless." Examples are a tithe line in a monthly budget, a job at a church, or a mission trip to be paid for. Because the coded types are few and were not part of the confirmatory design, Section 5.2 reports this comparison as exploratory.

# 3. Data

## 3.1 LendingClub

I use the public LendingClub loan-level file covering loans issued from June 2007 through December 2018 (2,260,701 loans). Each record carries the borrower's FICO range at origination, annual income, debt-to-income ratio (DTI), home ownership, employment length, income-verification status, state and three-digit ZIP code, and the loan's amount, term, interest rate, sub-grade, purpose and status. Two free-text fields matter here: the job title the borrower typed in (`emp_title`) and the loan description (`desc`), which investors could read while the loan was listed. LendingClub stopped showing descriptions in 2014, so of the 125,811 loans with any description text after I strip the platform's boilerplate, 125,761 were issued between 2007 and 2014. The median description is 24 words.

The outcome is default. I keep loans whose status is terminal (Fully Paid, Charged Off, or Default) and drop loans still current, in grace or late, and the small "does not meet credit policy" group. After removing records with missing DTI, FICO or rate, the analysis sample has 1,344,976 loans, 20.0 percent of which were charged off or defaulted. The description subsample has 123,292 loans (15.3 percent defaulted) and is an earlier and somewhat riskier slice of the platform's history, which is why every specification carries origination-year fixed effects. Writing a description was a choice, and Appendix Table C2 shows that origination year, grade and loan size predict it while affiliation does not (odds ratio 1.02, p = 0.81), so the narrative results describe borrowers who chose to write. Table 1 reports descriptive statistics.

**Table 1. Descriptive statistics by group**

| Group | N | Default rate | FICO (mean) | Income (median, $) | DTI | Rate (%) | Amount ($) | 60-month | Grade A–B |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Religious-institution affiliation | 3,105 | 0.133 | 704.0 | 60,000 | 19.0 | 12.28 | 14,826 | 0.228 | 0.571 |
| — clergy role | 2,497 | 0.138 | 702.9 | 62,400 | 19.3 | 12.12 | 15,259 | 0.233 | 0.565 |
| — church staff (non-clergy) | 608 | 0.114 | 708.3 | 53,000 | 17.5 | 12.92 | 13,050 | 0.207 | 0.594 |
| All other borrowers | 1,341,871 | 0.200 | 698.2 | 65,000 | 18.3 | 13.24 | 14,418 | 0.241 | 0.466 |
| All terminated loans | 1,344,976 | 0.200 | 698.2 | 65,000 | 18.3 | 13.24 | 14,419 | 0.241 | 0.467 |
| Religious language (description sample) | 681 | 0.200 | 704.9 | 55,000 | 16.0 | 13.44 | 13,460 | 0.256 | 0.502 |
| Other descriptions | 122,611 | 0.153 | 703.7 | 62,000 | 16.3 | 13.42 | 13,982 | 0.232 | 0.535 |
| All descriptions | 123,292 | 0.153 | 703.7 | 62,000 | 16.3 | 13.42 | 13,979 | 0.232 | 0.535 |

*Notes.* Terminated LendingClub loans issued 2007–2018. Default rate is the share of loans charged off or in default. FICO is the mean of the midpoint of the borrower's FICO range at origination. Income is the median self-reported annual income. DTI is the mean debt-to-income ratio in percent. Rate is the mean interest rate and Amount the mean loan amount. 60-month is the share of loans with a 60-month rather than 36-month term, and Grade A–B is the share of loans in LendingClub's two highest grades. Description sample: loans with non-empty borrower text after removing platform boilerplate, issued 2008–2014. Religious-language vs other descriptions: mean words 116 vs 36; share with moral language 0.19 vs 0.06, hardship 0.15 vs 0.07, gratitude 0.56 vs 0.14, family 0.33 vs 0.07, appeal for help 0.15 vs 0.04, business 0.16 vs 0.07.

## 3.2 Two religious indicators

*Religious-institution affiliation.* I flag a borrower as affiliated when the job title contains a clerical role word (pastor, minister, ministry, clergy, priest, chaplain, rabbi, missionary, reverend, evangelist, deacon, worship, imam, seminary) or a religious-organization word (church, parish, diocese, congregation, synagogue, mosque) that is not part of a hospital, school, insurer or bank name. This yields 5,014 loans in the full file and 3,105 in the terminal sample, of which 2,497 carry a clerical role word and 608 name a religious organization without one. I do not distinguish denominations, and the list is dominated by Christian titles because the borrowers are. An audit of 200 randomly drawn titles (Appendix Table B2) puts the rule's precision at 97 percent. The only clear errors are Louisiana civil parishes, and dropping them barely moves the estimate, so I report what the rule fixed in advance produces.

*Religious language.* I flag a description as containing religious language when the title or text matches a dictionary of religious terms (God, Jesus, Christ, Christian, church, pray/prayer, bless/blessed/blessing, faith in its religious sense, the Lord, Bible/scripture, tithe, ministry/pastor/missionary, amen, and denominational names), after excluding idiomatic uses ("good faith," "heaven forbid," "Lord & Taylor"). The dictionary flags 681 of the 123,292 descriptions in the terminal description sample (0.55 percent), and Appendix Table B3 traces the count from the full file. Because a dictionary cannot read context, every flagged description was also coded by a language model against a short codebook (Appendix B), which confirms 583 as religious and separates formulaic uses such as "Thank you and God bless" from identity claims and from concrete religious practice or expense. Appendix B reports agreement with a second model (κ = 0.86) and a human coder (κ = 0.72 on the four-way type, lower on the religious/non-religious boundary), and a search for religious content the dictionary misses, which amounts to a few dozen descriptions in the whole file. The confirmatory test uses the dictionary indicator, because that is what I specified before estimation. The coded indicator enters only as a robustness check, with the 98 rejected matches as a placebo, and the type breakdown is exploratory. The two indicators rarely coincide: in the description sample, 372 loans are affiliated and 681 carry religious language, and 20 are both.

## 3.3 Text controls

Religious language does not appear in a vacuum. Descriptions that contain it are three times longer than the median (68 versus 23 words) and far more likely to thank the reader (56 versus 14 percent), mention family (33 versus 7), describe hardship (15 versus 7), ask for help (15 versus 4) or make moral claims about reliability (19 versus 6). I therefore build six dictionary indicators (moral self-presentation, hardship, gratitude, family, appeal for help, and business purpose) and the log of description length, and include them in every narrative specification. Moral language is associated with lower default (odds ratio 0.88), hardship, gratitude and appeals with higher (1.17, 1.12, 1.12), and length with lower (0.92 per log point). In the double machine learning specifications a flexible learner also uses a 300-dimensional pretrained word-vector representation of each description, following Kriebel and Stitz (2022).

## 3.4 Local religiosity and local labor markets

To separate individual affiliation from the religiosity of the place a borrower lives in, I use the 2010 U.S. Religion Census county file (Grammich et al., 2012), the source behind the religiosity measures used in corporate finance since Hilary and Hui (2009), linked to three-digit ZIP areas (ZIP3) through the Census ZCTA–county relationship file with population weights. This gives adherents per thousand residents and congregations per ten thousand for 894 areas covering 99.97 percent of loans. For labor-market shocks I merge BLS county unemployment rates for 2008–2018 the same way and compute, for each loan, the rate at issue and the largest rise over the loan's term.

## 3.5 Prosper

To replicate the occupational result I use the public Prosper file (113,937 listings, 2005–2014), which has no free text but has an occupation code with the categories "Clergy" and "Religious." Among the 50,270 terminated loans with complete covariates, 141 fall in those categories, and the controls parallel LendingClub's.

# 4. Empirical approach

H1 and H2 are the only confirmatory tests. I test each one-sided, with a Holm correction across the pair, and I stated in advance what a failure would mean. Without H2 the paper would be a study of affiliation with expressed faith as a null result, and without H1 surviving stable-occupation controls the affiliation effect would have to be read as a secure job. H1 survived everything and H2 survived its confirmatory test but not a stricter one I had also set out in advance, and I report both outcomes as the rules required.

The confirmatory specification is a logit of default on the religious indicator and the credit and loan variables described above, with origination-year, grade, purpose, employment-length, homeownership, verification and state fixed effects, and standard errors clustered by state. H1 is estimated on all 3,105 affiliated loans together with a random draw of 250,000 other terminated loans (the draw is computational, not part of the design), and H2 on the full description sample with the six text dictionaries and log length added. Clustering by ZIP3 area or by month instead changes the standard errors but not what I conclude, and because 51 state clusters are few I also report wild cluster bootstrap p-values (Appendix Table C3). Both hypotheses are one-sided with a Holm correction across the pair, and I report odds ratios and average marginal effects.

Everything that follows the two tests answers a specific objection, and I say for each what it rules out and what it does not. Against the objection that church employees simply have secure jobs, I add eight stable-occupation indicators and compare affiliated borrowers with those in nonprofit and social-service work, education or healthcare, directly and within coarsened-exact-matching cells. Against the objection that affiliated borrowers differ on observables in ways a logit handles poorly, I reweight the comparison group by entropy balancing (Hainmueller, 2012) and estimate a partially linear double machine learning model (Chernozhukov et al., 2018). These guard against a misspecified functional form but not against unobserved confounding, against which I have no instrument, so I report Oster's (2019) δ and the Cinelli–Hazlett (2020) robustness value. For mechanism I compare clergy with non-clergy church staff, interact affiliation with local congregation density under state and then ZIP3 fixed effects, in the manner of Rajan and Zingales (1998), and interact it with local unemployment shocks and job tenure, with teachers and government employees as a positive control.

Against the objection that religious language proxies for length or tone, I match each flagged description to its five nearest neighbors in length within grade-year cells, and I replace the dictionary controls with a pretrained text representation inside the double machine learning model. Against the objection that any rare word set would do, I draw 1,000 random sets of non-religious words matched to the dictionary's document frequency and re-estimate the residualized effect for each. And against the objection that one platform is one platform, I estimate H1 on Prosper.

A word on what I do not do. I do not estimate a prediction model, since adding either indicator to a cross-validated logit moves the area under the ROC curve by less than 0.0001, and indicators that flag a quarter of one percent of borrowers cannot improve aggregate prediction. Nor do I fit a structural or mediation model, because the mediators of interest are not observed at the individual level.

# 5. Results

## 5.1 Affiliation (H1)

Table 2 reports the affiliation estimates. Column (1) of Panel A gives the confirmatory specification: an odds ratio of 0.69 (95 percent confidence interval 0.64 to 0.75), an average marginal effect of −4.8 percentage points against a base default rate of 20 percent, or about a quarter of the base rate. Split by period, the estimate is 0.61 for loans issued in 2008–2014 and 0.74 for 2015–2018, smaller in the later, lower-default years but not fading, so the finding is not a property of the platform's early, self-selected borrowers. The one-sided Holm-adjusted p-value is below 10⁻¹⁸ and the wild cluster bootstrap p-value below 0.001. Using all 1.34 million terminated loans instead of the random draw gives 0.694, and five further draws give 0.689 to 0.701 (Appendix Table C3).

**Table 2. Religious-institution affiliation and default (H1)**

*Panel A. Confirmatory estimates and robustness*

| | (1) All years | (2) 2008–2014 | (3) 2015–2018 | (4) Clergy vs staff | (5) + 8 stable occupations | (6) Entropy-balanced | (7) DML-PLR |
|---|---:|---:|---:|---:|---:|---:|---:|
| Affiliation (OR) | 0.692 | 0.607 | 0.743 | | 0.690 | 0.697 | −0.043 (AME) |
| SE (log-odds) | 0.041 | 0.087 | 0.060 | | | 0.043 | 0.006 |
| p | <0.001 | <0.001 | <0.001 | | <0.001 | <0.001 | <0.001 |
| Clergy role (OR) | | | | 0.686 (p<0.001) | | | |
| Church staff, non-clergy (OR) | | | | 0.720 (p=0.023) | | | |
| AME | −4.8 pp | −5.6 pp | −4.2 pp | | | | |
| N | 253,105 | 85,132 | 167,973 | 253,105 | 253,105 | 253,105 | 253,105 |

*Notes.* Logit, default on affiliation and controls: grade, origination year, interest rate, FICO midpoint, log income, DTI, 60-month term, log amount, employment length, home ownership, income verification, purpose, state fixed effects. SE clustered by state. Sample = all affiliated terminated loans plus 250,000 randomly drawn other terminated loans (3,105 affiliated: 2,497 clerical, 608 church staff). Column (5) adds indicators for teachers, police/corrections, firefighters, military, government, nurses, postal and transit workers (ORs 0.91, 0.93, 0.64, 0.93, 0.90, 1.06, 1.20, 1.10). Column (6): weights equate 76 covariate moments (Appendix Table C1). Column (7): DoubleML partially-linear, CatBoost nuisance, 5-fold cross-fitting, ATTE −0.042 (p<0.001). Column (1): 95% CI 0.638–0.751, one-sided Holm-adjusted p < 10⁻¹⁸. Column (4): Wald test of equal coefficients p = 0.77. Panel B: same controls; nearest occupations from job titles; coarsened exact matching on grade, year, FICO band, income, employment length, homeownership and term.


*Panel B. Occupation-selection tests*

| | OR | p | N (affiliated / comparison) |
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
| CEM within the eight stable occupations | 0.741 | <0.001 | 3,008 / 58,032 (1,746 cells) |
| Clergy hierarchy (exploratory): senior / lead / executive pastor | 0.452 | <0.001 | 497 |
| — associate / youth / assistant pastor | 0.696 | 0.08 | 253 |
| — other affiliated | 0.743 | <0.001 | 2,355 |

The stable-employment objection is the first thing to settle, and column 5 adds the eight occupation indicators. Teachers (0.91), government employees (0.90) and police (0.93) default modestly less than other borrowers and firefighters markedly less (0.64), but the affiliation coefficient does not move (0.69), and restricting the comparison group to the 118,022 borrowers in those stable jobs still leaves affiliated borrowers defaulting less (0.73). Entropy balancing tells the same story from the other side: after reweighting on 76 moments the comparison default rate falls from 20.1 to 17.5 percent, affiliated borrowers remain at 13.3, and the weighted odds ratio is 0.70. The double machine learning estimate is −4.3 percentage points (standard error 0.6). Table 3 gives the sensitivity analysis: Oster's δ is 6.5, so unobserved selection would have to be six and a half times as strong as selection on observables to explain the estimate away, and the robustness value of 0.015 is about twelve times the explanatory power of employment length.

**Table 3. Sensitivity to unobserved confounding**

| | H1 (affiliation) | H2 (religious language) |
|---|---:|---:|
| β uncontrolled / controlled (LPM) | −0.067 / −0.045 | +0.047 / +0.035 |
| R² uncontrolled / controlled | 0.000 / 0.094 | 0.000 / 0.065 |
| Oster δ (R²max = 1.3 R²) | 6.5 | 9.7 |
| β* at δ = 1 | −0.038 | +0.031 |
| Robustness value RV (q=1) | 0.015 | 0.0066 |
| RV at α = 0.05 | 0.011 | 0.0010 |
| Benchmark partial R²: employment length / verification | 0.00125 / 0.00027 | |

Panel B takes the objection one step further. If the affiliation effect were a property of mission-driven, modestly paid service work, borrowers in the jobs nearest to church work should show it too, and comparing affiliated borrowers with those jobs alone should shrink it. Neither happens. Social workers, case managers and counselors (11,592 loans) default no less than other borrowers (1.02), nor do healthcare workers (1.02), while education workers default modestly less (0.94). With each group as the only comparison the affiliation odds ratio is 0.69, 0.68 and 0.75, and exact matching gives 0.70 against those neighbors and 0.74 against the eight stable occupations. Whatever the affiliation captures is not shared by the jobs that most resemble it in pay, tenure or purpose. Occupation has carried default information before, for finance professionals (Agarwal, Chomsisengphet and Zhang, 2017) and for professional and skilled job titles (Croux et al., 2020; Davaadorj et al., 2024), but there the natural reading is expertise or earning power, and a church secretary has neither. Figure 2 collects the affiliation estimates with the Prosper replication, where every interval lies below one.

![Figure 2. Religious-institution affiliation and default across specifications. Odds ratios with 95% confidence intervals (log scale) from Table 2, Panels A and B, and Table 4. Intervals for estimates reported with p-values only are recovered from the p-value.](fig2_forest.png){width=6.3in}

Prosper replicates the affiliation result (Table 4). The 141 clergy and religious-occupation borrowers default at 22.7 percent against 30.5 percent, and with the full set of controls the odds ratio is 0.68 (p = 0.037), while the placebo occupations on Prosper (teachers, police, nurses) are all indistinguishable from one.

**Table 4. Prosper replication of H1**

| | OR | p | N |
|---|---:|---:|---:|
| Clergy / Religious occupation | 0.684 | 0.037 | 141 |
| Placebo: Teacher | 1.073 | 0.28 | 1,571 |
| Placebo: Police / corrections | 1.008 | 0.93 | 663 |
| Placebo: Nurse (RN) | 0.965 | 0.71 | 794 |

*Notes.* 50,270 terminated Prosper loans, 2005–2014. Controls: Prosper rating or pre-2009 credit grade, origination year, borrower rate, credit-score midpoint, log stated monthly income, DTI, term, log amount, employment status, homeownership, income verifiability, state FE. Raw default: 22.7% vs 30.5%.

## 5.2 Religious language (H2)

Table 5 builds the narrative estimate one control set at a time. With credit and loan controls only, religious language carries an odds ratio of 1.27 (p = 0.018). Adding log length moves it to 1.34, because long descriptions default less and religious descriptions are long. Adding the six text dictionaries (column 3, the specification fixed before estimation) brings it back to 1.28 (p = 0.016), an average marginal effect of +3.2 percentage points against a base rate of 15 percent. Replacing log length with length deciles changes nothing, and in the length-matched sample the odds ratio is 1.34 (p = 0.012). The fake-dictionary permutation puts the residualized effect of the actual dictionary at 0.035 against a permutation mean of −0.003 (SD 0.014), and one random word set in two hundred does as well (one-sided p = 0.005).

**Table 5. Religious language and default (H2)**

| | (1) Credit controls | (2) + log length | (3) + text dictionaries | (4) + length deciles | (5) Length-matched | (6) Coder-validated | (7) DML + dict. | (8) DML + dict. + text |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Religious language (OR) | 1.265 | 1.338 | 1.281 | 1.274 | 1.344 | 1.335 | +0.033 (θ) | +0.026 (θ) |
| SE | 0.100 | 0.098 | 0.103 | 0.101 | | | 0.015 | 0.015 |
| p | 0.018 | 0.003 | 0.016 | 0.016 | 0.012 | 0.001 | 0.027 | 0.091 |
| AME | +3.1 pp | +3.8 pp | +3.2 pp | +3.1 pp | | | | |
| Dictionary false positives (OR) | | | | | | 0.948 (p=0.88) | | |
| N | 123,292 | 123,292 | 123,292 | 123,292 | 3,572 | 123,292 | 123,292 | 123,292 |

*Notes.* Same controls as Table 2 plus, from column (2), log description length and, from column (3), six text indicators (moral, hardship, gratitude, family, appeal, business; ORs 0.88, 1.17, 1.12, 1.07, 1.12, 1.08). Column (5): each flagged loan matched to five nearest in length within grade×year. Column (6): the 583 descriptions coded religious, with the 98 non-religious matches entered separately. Columns (7)–(8): DoubleML-PLR, CatBoost; column (8) adds 300-d word vectors (PCA-50); alternative representations, repeated cross-fitting and term counts in Appendix Table C5. Column (3): 95% CI 1.047–1.566, two-sided p 0.016, one-sided Holm-adjusted p 0.008, wild cluster bootstrap p 0.015; minimum detectable effect at 80% power 3.4 pp. Fake-dictionary permutation (1,000 word sets of matched frequency): actual 0.035 vs mean −0.003 (SD 0.014), one-sided p 0.005.

The language-model coding sharpens this. Flagging only the 583 descriptions confirmed as religious gives an odds ratio of 1.34 (p = 0.001), while the 98 the dictionary flagged but the coder rejected give 0.95 (p = 0.88): the association sits in the religious content, not in the words. By type (Appendix Table B1), formulaic invocations carry the effect (1.39, p = 0.001, 467 loans), identity claims point the same way on too few loans to tell (1.46, n = 34), and descriptions that report religious *practice* show no elevated default (0.99, n = 82). The split is exploratory and the cell is small, but the pattern is in the direction Section 2 anticipates.

The double machine learning estimates are where the narrative result shows its limits. With the six dictionaries as controls the partially linear estimate is +3.3 points (p = 0.027), and +3.6 on the validated indicator (p = 0.028). Once the learner is also given a representation of the text itself, the point estimate barely moves but the interval widens. It is +2.8 with a TF-IDF factorization (p = 0.059), +2.6 with pretrained word vectors reduced to 50 components (p = 0.09), +2.3 with the full 300 dimensions (p = 0.14) and +2.4 with a document-embedding model (p = 0.11). The sign never changes and the coefficient shrinks by at most a third, but 681 treated loans cannot pin down a three-point effect once several hundred text features are conditioned on. I set out in advance that a confidence interval covering zero in this specification would lead me to lower the claim, and I do: religious wording cannot be separated from the information the rest of the text already carries, although the point estimate gives no sign that the text absorbs it. H2 passes its confirmatory test and every linear placebo, but I present it as an association whose sign is consistent, not as a result on the same footing as H1 (Figure 3).

![Figure 3. Religious language and default: double machine learning estimates by text representation. Partially linear DoubleML with CatBoost nuisance functions, 5-fold cross-fitting; "20 splits" aggregates twenty repeated sample splits by the median. Bars are 95% confidence intervals.](fig3_dml.png){width=6.3in}

Two further checks put the imprecision in its place. The estimate does not depend on the sample split, since twenty repetitions of the cross-fitting give a median of +3.2 points with the dictionary controls, significant in every split, and +3.0 with the TF-IDF representation, significant in twelve of twenty. And the imprecision is what the sample size implies: with 681 treated loans the smallest effect a one-sided test detects with 80 percent power is 3.4 points, and more religious descriptions than exist would be needed to do better. The data still add a gradient, since replacing the indicator with the number of religious terms gives odds ratios of 1.14, 1.56 and 1.87 for one, two, and three or more terms (Appendix Table C5), a pattern consistent with the sign of H2 that I did not specify in advance.

Table 6 puts both indicators in the same regression, where religious language has an odds ratio of 1.29 (p = 0.013) and affiliation, on the 372 affiliated borrowers in the description sample, 0.67 (p = 0.041). Neither estimate moves when the other is added.

**Table 6. Both signals in one regression (description sample)**

| | OR | p | N treated |
|---|---:|---:|---:|
| Religious language | 1.293 | 0.013 | 681 |
| Religious-institution affiliation | 0.672 | 0.041 | 372 |

*Notes.* Specification of Table 5 column (3). 20 loans carry both indicators.

## 5.3 Mechanism: the pastor and the secretary

If the affiliation effect came from the vocation, a pastor's vows or a professional identity in which unpaid debt is a scandal, church secretaries and administrators should default like secretaries and administrators elsewhere. Column 4 of Table 2 splits the indicator. Borrowers with a clerical role word have an odds ratio of 0.69 (p < 0.001), and borrowers who name a religious employer without one 0.72 (p = 0.023) on 608 loans. Their raw default rate, 11.4 percent, is if anything lower than the clergy's 13.8, and a Wald test cannot distinguish the two coefficients (p = 0.77). The comparison holds the kind of community roughly fixed rather than the congregation itself, since only 606 affiliated titles name an institution and recurring names such as "First Baptist Church" belong to many unrelated churches. What the pastor and the secretary share is not a vocation, an income level, or a professional code, but employment inside a congregation. Survey data show a parallel, since the financial risk aversion associated with church membership appears to stem from the social side of membership rather than from belief (Noussair, Trautmann, van de Kuilen and Vellekoop, 2013).

This also speaks to the job-stability objection more directly than the occupation controls do, because a church secretary's pay and tenure look like an office worker's, and the advantage that teachers and government workers show, about 10 percent lower odds, is a third of what church staff show.

## 5.4 Mechanism: congregation density and labor-market shocks

Table 7 turns to local religious presence. Adding adherence rate and congregation density to the full specification leaves the affiliation odds ratio at 0.686, so the individual effect is not local religiosity in disguise. But it varies with it. The interaction of affiliation with congregation density has an odds ratio of 0.84 per standard deviation (p = 0.003), and by tercile of local adherence the affiliation odds ratio is 0.71 in the least religious third of ZIP areas, 0.83 in the middle, and 0.58 in the most religious. The differential remains under 601 ZIP3 fixed effects, which absorb every time-invariant feature of the area: the affiliation coefficient is −5.4 points and the density interaction −2.2 points per standard deviation (p = 0.027). If the signal reflected only a church employee's private character or the steadiness of a church paycheck, it is hard to see why it should depend on how many other churches stand nearby. Religious language shows no interaction with local religiosity (1.07, p = 0.50), as one expects of a message whose meaning does not depend on who is listening (Figure 4).

**Table 7. Individual affiliation and local religiosity**

| | Affiliation OR | Interaction OR | p (interaction) | N |
|---|---:|---:|---:|---:|
| + adherence rate and congregation density (controls) | 0.686 | | | 253,038 |
| Adherence rate (per SD, main effect, within state) | 1.039 (p 0.007) | | | |
| Congregation density (per SD, main effect) | 1.060 (p 0.001) | | | |
| Affiliation × adherence | 0.688 | 0.892 | 0.078 | |
| Affiliation × congregation density | 0.642 | 0.836 | 0.003 | |
| Affiliation × congregation density, ZIP3 FE (LPM) | −5.4 pp | −2.2 pp / SD | 0.027 | 146,248 |
| Religious language × adherence | 1.295 | 1.075 | 0.50 | 123,260 |

*Notes.* 2010 U.S. Religion Census county file merged to three-digit ZIP areas via the Census ZCTA–county relationship file, population-weighted (894 areas). Adherents per 1,000 residents and congregations per 10,000, standardized. ZIP3 fixed-effects row: all affiliated loans plus 150,000 randomly drawn other terminated loans, restricted to ZIP3 areas with at least 50 loans, SE clustered by ZIP3.

![Figure 4. Heterogeneity by local religiosity. Panel A: affiliation odds ratio by quintile of congregation density in the borrower's ZIP3 area, full controls and state fixed effects. Panel B: religious-language odds ratio by quintile of the adherence rate, Table 5 column 3 specification. Bars are 95% confidence intervals.](fig4_density.png){width=6.3in}

Table 8 tests the income-stability alternative from the other side. Local unemployment is associated with default as expected, but the affiliation advantage does not widen when unemployment rises (interaction 0.98, p = 0.58) or when it is high (0.96, p = 0.44). I would not lean on this too hard. The sample period is mostly a recovery, and the same interaction for teachers and government employees as a positive control does not widen either (1.06 and 1.00, p = 0.29 and 0.93), so the shocks in these years are too small to reveal an income-stability mechanism for any occupation. The evidence supports a more limited statement: the affiliation gap does not visibly vary with shocks, while it does visibly vary with congregation density. Job tenure gives a partly favorable check on the stability account. The gap is smaller among borrowers with ten or more years in their job (interaction 1.26, p = 0.038), as that account predicts, but remains below one among them (0.80, p = 0.036). With the density, shock and tenure interactions estimated together (Appendix Table C4), the density interaction is 0.83 (p = 0.003) and the shock interaction 0.99 (p = 0.80). Religious organizations also insure members' consumption against income shocks (Dehejia, DeLeire and Luttmer, 2007), as they did in the Indonesian crisis (Chen, 2010), which would cushion an affiliated borrower before the loan, although shared ties can spread default as well (Adbi, Lee and Singh, 2024).

**Table 8. Affiliation and local unemployment shocks**

| | OR | p |
|---|---:|---:|
| Affiliation | 0.687 | <0.001 |
| Unemployment rate at origination (per SD) | 1.091 | 0.001 |
| Rise in unemployment over loan life (per SD) | 1.028 | 0.001 |
| Affiliation × rise | 0.975 | 0.58 |
| Affiliation × level | 0.959 | 0.44 |
| Affiliation by shock tercile (small / mid / large) | 0.588 / 0.763 / 0.721 | all <0.01 |
| Positive control: teacher × rise; government × rise | 1.057; 1.004 | 0.29; 0.93 |

*Notes.* BLS LAUS county annual unemployment 2008–2018, ZIP3 population-weighted. "Rise" = maximum rate in years after origination within term, minus rate at origination (mean −0.62 pp, SD 0.55); the period is mostly a recovery. Table 2 sample merged to ZIP3 unemployment, N = 239,198 (2,973 affiliated; 5,663 teachers and 2,202 government employees as positive control), same controls, SE clustered by state.

## 5.5 Individual religion and local religion

The religiosity literature in finance is almost entirely about places, where a more religious surrounding is favorable for firms (He and Hu, 2016), credit unions (Davidson, Ngo and Wang, 2026) and mortgages (Li and Ucar, 2022), so it is worth asking whether my signals are the same thing seen from closer up. They are not. Within state, borrowers from more religious ZIP3 areas default slightly *more* (Table 7), with odds ratios of 1.04 per standard deviation of adherence and 1.06 per standard deviation of congregation density, and the evangelical share is unrelated to default. I cannot explain the positive association and do not try to. Those studies concern firms, institutions or mortgages, within-state variation in religiosity is correlated with income and urbanicity in ways my controls may not fully absorb, and the sign of an area's religious makeup is not fixed even in that literature (Hasan, Kiesel and Noth, 2025). The split between an individual effect and a null regional one has parallels, since personal trust among group members matters for repayment where generalized trust does not (Cassar, Crowley and Wydick, 2007) and individual church attendance predicts trust while regional devoutness does not (Traunmüller, 2011). Whatever lowers the affiliated borrower's default is a property of belonging to a religious institution, amplified by the density of such institutions rather than replaced by it.

## 5.6 Timing (Appendix A)

A discrete-time hazard on loan-month panels puts the affiliation hazard ratio at 0.69 and flat over the life of the loan, while religious language has no effect on hazard in the first year (0.96, p = 0.85) and its effect appears only later (1.27, p = 0.027), the opposite of what a marker of immediate distress would show. Figure 5 shows the same timing without a model: affiliated borrowers run below the comparison group from the first year, while the religious-language curve tracks its comparison group for a year and separates afterward. The default date is approximate, so I treat this as suggestive.

![Figure 5. Cumulative default by months since origination, 36-month loans. Default is dated four months after the last payment. Comparison groups are reweighted to the treated group's grade × origination-year distribution. Panel A: 2,398 affiliated loans in the terminal sample; Panel B: 507 religious-language loans in the description sample.](fig5_cumdefault.png){width=6.3in}

# 6. Discussion

## 6.1 How much is it worth

Neither signal is priced, in the sense that neither moves the interest rate. LendingClub set rates by sub-grade and date, so two loans in the same sub-grade in the same month carried the same rate whatever the job title or the description said. Against loans in the same sub-grade-year cell, affiliated borrowers defaulted at 13.3 rather than 17.4 percent and lost 5.5 rather than 7.7 cents per dollar funded, a gap of 2.2 cents over an average 41-month life, or roughly 64 basis points a year of yield above the cell. Loans with religious language went the other way: 20.0 against 15.9 percent default, 7.1 against 6.1 cents lost, about 28 basis points a year below the cell. Loss is realized cash flow, one dollar minus total payments received per dollar funded, so it nets out interest and recoveries. The benchmark weights sub-grade-year cells by the distribution of the flagged loans, and the annual figure divides the cumulative gap by the average loan life. These are not large numbers, and I do not claim an investor could have traded on them, since the signals flag a fraction of one percent of loans, but they measure, in the units investors use, the difference in realized losses that grade-based pricing did not reflect. On Prosper, where investors bid on rates, unverifiable disclosures earned lower rates (Michels, 2012) and text was priced, if not fully (Gao, Lin and Sias, 2023). In corporate debt county religiosity earns a lower spread (Jiang, John, Li and Qian, 2018). LendingClub's pricing used none of this, and where its terms drew out private information it was through the loan menu (Hertzberg, Liberman and Paravisini, 2018).

## 6.2 After default

The same contrast appears, more faintly, after borrowers stop paying. Among the 268,599 charged-off loans, affiliated borrowers made at least one recovery payment 74.6 percent of the time against 68.7 percent for others and recovered 8.4 rather than 7.5 cents per dollar (0.9 cents with controls, p = 0.057), while borrowers who had used religious language recovered less (6.3 against 7.1 cents). This is a pattern, not a test, but it is what one would expect if belonging carries an obligation that outlasts the platform's collection efforts, and professing does not. The investor side cannot be examined here, since the file does not record how quickly a listing filled, and what it does record, the investor-funded share and the ratio of funded to requested amount, is unrelated to religious language (all p > 0.4). On Kiva, where funding speed is observed, religious expression slows funding, less so among more religious lenders (Anglin, Milanov and Short, 2023).

## 6.3 Limits

This is an observational study of one platform's borrowers, most of whom are American and, where religion is visible, Christian. There is no instrument for working in a church, no natural experiment that moves people into or out of one, and no borrower identifier, so a within-borrower design is not available. The platform does not record age, education, marital status or household structure, on any of which church employees may differ, nor the longer planning horizon and greater thrift that religious households report (Renneboog and Spaenjers, 2012), which could lower default without any community watching. The affiliation indicator comes from a free-text job title and certainly misses affiliated borrowers who described their job differently. If they resemble the ones I find the omission biases the estimate toward zero, and otherwise the bias could run either way. Where a religious phrase stops being religious is judged differently by different readers, so I read the type breakdown for direction only, and religious language is rare enough that the narrative estimate is imprecise in the strictest specifications. The mechanism evidence is consistent with a community-based account and difficult to reconcile with most of the labor-market accounts I can test, although the smaller gap among long-tenure borrowers leaves some room for job stability. Table 9 sets out, result by result, what the evidence supports and what it does not establish.

**Table 9. What the evidence supports and what it does not establish**

| Result | Supports | Does not establish |
|---|---|---|
| Affiliation OR 0.69, stable across adjustments (Tables 2–3) | Lower default conditional on observed characteristics | A causal effect of church employment |
| Clergy and staff alike (Wald p = 0.77) | The association is not specific to the clerical vocation | A within-congregation comparison (congregations are not identified) |
| Density interaction below one, also with ZIP3 fixed effects (Table 7) | A community-based account | Direct evidence of monitoring or sanctions |
| No differential response to unemployment shocks (Table 8) | No detectable shock absorption in a recovery period | Rejection of the income-stability account |
| Smaller gap at ten or more years' tenure (Appendix Table C4) | Some role for job stability | That stability explains the gap, which remains (OR 0.80) |
| Prosper OR 0.68 on 141 loans (Table 4) | The same sign on a second platform | External validity beyond these platforms |
| Religious language OR 1.28, not distinguishable from zero with full-text controls (Table 5) | A positive association in the confirmatory specification | An effect of religious wording separate from the text it travels with |
| Same default gaps within sub-grade-year cells (Section 6.1) | Grade-based rates did not reflect either indicator | A tradable strategy |

# 7. Conclusion

In an online consumer-credit market, borrowers whose job titles place them in a religious institution default less than observably identical borrowers, and borrowers who profess faith in their loan request default more. The first association is large, stable over a decade, present for church staff as much as for clergy, stronger where congregations are denser, without a detectable response to local unemployment, and reproduced in sign on a second platform. The second keeps its size once the full text is accounted for but can no longer be distinguished from zero. Neither is reflected in the platform's grade-based rates. The evidence is most consistent with religious community functioning as borrower-side social collateral, and religious language as a low-cost signal that is informative in spite of, not because of, what it says.

Two implications follow. The first concerns how a lender reads religion in a credit file: the same subject carries opposite information depending on whether it arrives as a tie or as a statement, so a model that treated religion as a single variable would average two signals of opposite sign. The second concerns where social collateral is found. Group-lending schemes build a community around the loan, whereas the borrowers I study reported theirs in a job title, and other affiliations a credit file records only in passing, such as a cooperative or a union local, are natural places to look for the same pattern. For lenders the practical content is modest, but the conceptual content is not: what a credit market can learn from religion is not what a borrower says about it but where the borrower stands within it.

# References

Adbi, A., Lee, M., & Singh, J. (2024). Community influence on microfinance loan defaults under crisis conditions: Evidence from Indian demonetization. *Strategic Management Journal*, 45(3), 535–563.

Agarwal, S., Chomsisengphet, S., & Zhang, Y. (2017). How does working in a finance profession affect mortgage delinquency? *Journal of Banking & Finance*, 78, 1–13.

Al-Azzam, M., Hill, R. C., & Sarangi, S. (2012). Repayment performance in group lending: Evidence from Jordan. *Journal of Development Economics*, 97(2), 404–414.

Anglin, A. H., Milanov, H., & Short, J. C. (2023). Religious expression and crowdfunded microfinance success: Insights from role congruity theory. *Journal of Business Ethics*, 185(2), 397–426.

Baele, L., Farooq, M., & Ongena, S. (2014). Of religion and redemption: Evidence from default on Islamic loans. *Journal of Banking & Finance*, 44, 141–159.

Bentzen, J. S. (2021). In crisis, we pray: Religiosity and the COVID-19 pandemic. *Journal of Economic Behavior & Organization*, 192, 541–583.

Besley, T., & Coate, S. (1995). Group lending, repayment incentives and social collateral. *Journal of Development Economics*, 46(1), 1–18.

Caldieraro, F., Zhang, J. Z., Cunha, M., Jr., & Shulman, J. D. (2018). Strategic information transmission in peer-to-peer lending markets. *Journal of Marketing*, 82(2), 42–63.

Cassar, A., Crowley, L., & Wydick, B. (2007). The effect of social capital on group loan repayment: Evidence from field experiments. *The Economic Journal*, 117(517), F85–F106.

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

Putnam, R. D. (2000). *Bowling Alone: The Collapse and Revival of American Community*. Simon & Schuster.

Rajan, R. G., & Zingales, L. (1998). Financial dependence and growth. *American Economic Review*, 88(3), 559–586.

Renneboog, L., & Spaenjers, C. (2012). Religion, economic attitudes, and household finance. *Oxford Economic Papers*, 64(1), 103–127.

Sanz-Guerrero, M., & Arroyo, J. (2025). Credit risk meets large language models: Building a risk indicator from loan descriptions in P2P lending. *Inteligencia Artificial*, 28(75), 220–247.

Sosis, R., & Bressler, E. R. (2003). Cooperation and commune longevity: A test of the costly signaling theory of religion. *Cross-Cultural Research*, 37(2), 211–239.

Spence, M. (1973). Job market signaling. *Quarterly Journal of Economics*, 87(3), 355–374.

Stiglitz, J. E. (1990). Peer monitoring and credit markets. *World Bank Economic Review*, 4(3), 351–366.

Traunmüller, R. (2011). Moral communities? Religion as a source of social trust in a multilevel analysis of 97 German regions. *European Sociological Review*, 27(3), 346–363.

Valencia Caicedo, F., Dohmen, T., & Pondorfer, A. (2023). Religion and cooperation across the globe. *Journal of Economic Behavior & Organization*, 215, 479–489.

Wang, C., Wang, J., Wu, C., & Zhang, Y. (2023). Voluntary disclosure in P2P lending: Information or hyperbole? *Pacific-Basin Finance Journal*, 79, 102024.

\newpage

# Appendix

## Appendix A. Timing

**Appendix Table A1. Discrete-time hazard**

| | Loans | Loan-months | Events | HR (all) | HR ≤12 months | HR >12 months |
|---|---:|---:|---:|---:|---:|---:|
| Affiliation (clergy definition) | 33,105 | 725,884 | 6,359 | 0.686 (p<0.001) | 0.693 (p<0.001) | 0.684 (p<0.001) |
| Religious language | 8,681 | 245,747 | 1,360 | 1.217 (p 0.055) | 0.956 (p 0.85) | 1.274 (p 0.027) |

*Notes.* cloglog on loan-month panels, with default dated four months after last payment (capped at term) and Fully Paid censored at last payment. The model includes a cubic in loan progress, year and grade FE, and credit and loan controls, with SE clustered by loan. Comparison groups subsampled.

**Appendix Table A2. Affiliation effect by tercile of local religiosity**

| Adherence tercile of ZIP3 area | Affiliation OR | p | N affiliated |
|---|---:|---:|---:|
| Low | 0.708 | <0.01 | 890 |
| Middle | 0.830 | <0.01 | 974 |
| High | 0.585 | <0.01 | 1,241 |

*Notes.* Table 2 specification estimated separately within terciles of the 2010 adherence rate (Table 7 data).

## Appendix B. Coding and measurement

*Codebook for religious-language descriptions.* Each flagged record receives one type and one frame. Type a, formulaic: religious words used as a greeting, closing or idiom that makes no claim about the writer ("Thank you and God bless", "God willing", "prayers answered"). Type b, identity or value claim: the writer asserts his or her own faith, religious identity or a religious value as a reason to trust them ("as a Christian I believe in paying my debts", "I have strong faith in God"). Type c, practice or expense: a concrete religious activity or outlay, such as tithes or offerings in a budget, church employment, a mission trip or seminary tuition. Type x, not religious: the matched word is used in a non-religious sense ("Lord & Taylor", "good faith", "heaven forbid"). When more than one type applies the coder assigns the strongest in the order c, then b, then a. The frame records what accompanies the religious content in the same description: religious content alone, a moral self-presentation (promises, honesty, responsibility), a hardship narrative (job loss, illness, divorce, medical bills), or both. Coders read each record without access to any automatic label. The three religious types follow the distinction in Section 2 between a costless invocation and a report of practice that ties the borrower to a community.

**Appendix Table B1. Language-model coding of religious-language descriptions**

| Type | N | Default rate (raw) | OR (full controls) | p |
|---|---:|---:|---:|---:|
| a. Formulaic ("God bless", "prayers answered") | 467 | 0.221 | 1.385 | 0.001 |
| b. Identity / value claim | 34 | 0.206 | 1.460 | 0.32 |
| c. Practice / expense (tithe, church employment, mission) | 82 | 0.146 | 0.988 | 0.97 |
| x. Non-religious match (dictionary false positive) | 98 | 0.143 | 0.948 | 0.88 |

*Notes.* Exploratory; not part of the confirmatory design. Primary coding by an LLM coder over all 820 flagged records (717 with description text, 103 title-only) against the codebook above. Independent recoding of a stratified 200-record sample by a second LLM coder of a different model family gives κ = 0.86 for type (raw agreement 91%), 0.81 for religious vs non-religious, 0.73 for frame. A human coder of the same 200 records agrees with the primary coding at κ = 0.72 for type (raw 82%), 0.55 for religious vs non-religious (raw 85%, the low κ reflecting that 80% of the records are religious) and 0.48 for frame; the human coder reads 11 of the 40 model-coded false positives as religious and 20 of the 160 model-coded religious records as not. Because 80% of the sample is religious, the prevalence-adjusted κ for that binary is 0.69. The disagreements sit at two boundaries, formulaic invocation against non-religious (17 records) and identity claim against non-religious (8 records), rather than in the practice category, where the two agree on 36 of 40. Measurement completeness: a classifier trained with all explicit religious words masked (CV AUC 0.92) ranked the 122,611 unflagged descriptions, and the LLM coder found 0 religious descriptions among 117 sampled from the top 2,000, 3 among 240 further down, and 11 among 77 implicit-phrase matches ("godsend", "karma", "higher power").

**Appendix Table B2. Audit of the affiliation indicator (200 randomly drawn affiliated job titles)**

| Code | N | Examples |
|---|---:|---|
| A. Religious institution, clerical role | 146 | Pastor, Senior Pastor, Minister, Chaplain, Priest, Worship Leader |
| B. Religious institution, non-clerical staff | 48 | Director of Music Ministry, Parish Business Manager, "St. Thomas Episcopal Church", "Indianapolis Hebrew Congregation" |
| C. Not religious employment | 2 | "East Baton Rouge Parish Sheriff's Office", "Ouachita Parish Sheriff's Office" (Louisiana civil parishes) |
| D. Cannot classify from title | 4 | "Church and Stagg", "Pastor/Soccer Club Director", "Parish Manager" |

*Notes.* Precision 97 percent (98 percent counting D as half). A rule targeting civil-parish titles (parish + sheriff, library, government, assessor, police jury, court, etc.) identifies 30 such loans in the terminal sample, all in Louisiana, with a raw default rate of 30 percent. Excluding them gives an affiliation odds ratio of 0.683 (SE 0.041) in the Table 2, column 1 specification.

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

*Notes.* Standardized mean differences (affiliated minus other) for the 76 covariate moments used in Table 2, column 6. The eleven shown are those exceeding 0.10 in absolute value before weighting. Maximum |SMD| 0.175 before, below 10⁻⁷ after. Effective control sample size after weighting 172,965.

**Appendix Table C2. Who wrote a description? Logit of a non-empty description, 2008–2014 terminal loans**

| | OR | p | AME |
|---|---:|---:|---:|
| Religious-institution affiliation | 1.017 | 0.81 | +0.2 pp |
| Interest rate (per SD) | 1.096 | <0.001 | +6.1 pp |
| FICO (per SD) | 0.999 | <0.001 | −0.5 pp |
| Log income (per SD) | 0.998 | 0.89 | 0.0 pp |
| DTI (per SD) | 1.000 | 0.79 | 0.0 pp |
| 60-month term | 0.958 | 0.039 | |
| Log amount (per SD) | 1.249 | <0.001 | +2.2 pp |
| Grade B / C / D / E / F / G (vs. A) | 0.63 / 0.38 / 0.26 / 0.18 / 0.15 / 0.16 | all <0.001 | |

*Notes.* All affiliated 2008–2014 terminal loans plus 150,000 randomly drawn others (N = 151,191, of which 27.3 percent have a description). Same controls and state fixed effects as Table 2, with SE clustered by state. Pseudo-R² 0.24, most of it from origination-year effects.

**Appendix Table C3. Alternative inference and samples for the two confirmatory estimates**

| Clustering | H1: affiliation, SE (p) | H2: religious language, SE (p) |
|---|---:|---:|
| State (51 clusters; reported) | 0.041 (<0.001) | 0.103 (0.016) |
| ZIP3 area (892 clusters) | 0.054 (<0.001) | 0.100 (0.013) |
| Month of origination (138 clusters) | 0.050 (<0.001) | 0.092 (0.007) |
| Heteroskedasticity-robust, no clustering | 0.054 (<0.001) | 0.101 (0.014) |
| Wild cluster bootstrap by state, linear probability model: p | <0.001 | 0.015 |
| 95% CI of the odds ratio (state clusters) | 0.638–0.751 | 1.047–1.566 |
| H1 on all 1,344,976 terminal loans: OR (95% CI) | 0.694 (0.637–0.755) | |
| H1 with five further random comparison draws: OR range | 0.689–0.701 | |

*Notes.* Standard errors of the log-odds coefficient in the Table 2, column 1 and Table 5, column 3 specifications (coefficients −0.368 and +0.247). Wild cluster bootstrap: restricted (null imposed), Webb weights, 9,999 draws, on the linear probability analogue of each specification (51 state clusters for H1, 50 for H2, since one state has no description-sample loans). Random draws use seeds 2 to 6.

**Appendix Table C4. Competing explanations in one specification**

| | (1) Density | (2) Shock | (3) Tenure and verification | (4) All |
|---|---:|---:|---:|---:|
| Affiliation | 0.635 (<0.001) | 0.688 (<0.001) | 0.631 (<0.001) | 0.589 (<0.001) |
| Affiliation × congregation density (per SD) | 0.821 (0.002) | | | 0.830 (0.003) |
| Congregation density (per SD) | 1.059 (0.001) | | | 1.034 (0.040) |
| Affiliation × rise in unemployment (per SD) | | 0.975 (0.58) | | 0.988 (0.80) |
| Affiliation × ten or more years in job | | | 1.260 (0.038) | 1.245 (0.048) |
| Affiliation × income verified | | | 0.998 (0.98) | 0.997 (0.98) |

*Notes.* Logit odds ratios, two-sided p in parentheses. Table 2 sample merged to ZIP3 unemployment and congregation data, N = 239,198 (2,973 affiliated), same controls as Table 2, SE clustered by state. Density standardized across ZIP3 areas as in Table 7; columns (1) and (4) also control for adherence, columns (2) and (4) for the unemployment rate at origination. The density interaction is 0.82 here rather than 0.84 in Table 7 because the sample is restricted to loans that merge to the unemployment data. Column (3): implied affiliation OR among borrowers with ten or more years in their job 0.795 (95% CI 0.642–0.985, p = 0.036; 1,119 affiliated). Predicted default from column (1) at one SD below and above mean density: affiliated 16.5 and 13.2 percent, others 19.9 and 21.6 percent.

**Appendix Table C5. Religious language: alternative text representations, repeated cross-fitting and term count**

| Specification | θ (AME) | p | Splits with p < 0.05 |
|---|---:|---:|---:|
| DoubleML-PLR, six dictionaries | +0.033 | 0.027 | |
| + spaCy word vectors, PCA-50 | +0.026 | 0.09 | |
| + spaCy word vectors, full 300-d | +0.023 | 0.14 | |
| + TF-IDF-SVD100 | +0.028 | 0.059 | |
| + doc2vec | +0.024 | 0.11 | |
| Repeated cross-fitting (20 splits, median), dictionaries | +0.032 | 0.031 | 20/20 |
| Repeated cross-fitting, TF-IDF-SVD100 | +0.030 | 0.045 | 12/20 |
| Repeated cross-fitting, spaCy PCA-50 | +0.025 | 0.10 | 0/20 |
| Repeated cross-fitting, doc2vec | +0.024 | 0.11 | 0/20 |
| Religious-term count (Table 5 column 3 controls) | OR | p | |
| One term | 1.14 | 0.24 | |
| Two terms | 1.56 | 0.06 | |
| Three or more terms | 1.87 | 0.07 | |
| log(1 + count) | 1.37 | 0.006 | |

*Notes.* Description sample of Table 5. DoubleML partially linear model with CatBoost nuisance functions and 5-fold cross-fitting; across-split SD of θ is 0.0013–0.0018 in every repeated-cross-fitting specification. Term-count rows are logit odds ratios with the Table 5 column (3) controls.
