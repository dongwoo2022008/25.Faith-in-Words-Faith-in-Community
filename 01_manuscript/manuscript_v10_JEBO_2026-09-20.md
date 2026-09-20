---
title: "Faith in Words, Faith in Community: Religious Affiliation, Religious Language, and Default in Online Consumer Credit"
author: "Dongwoo Kim, Division of Advanced IT, Baekseok University"
date: "Draft v10, September 2026 (JEBO version)"
---

**Abstract.** Religion enters a consumer-credit file in two ways: as an affiliation a borrower reports in a job title, and as language a borrower chooses to use in a loan request. Using 1.34 million terminated LendingClub loans issued between 2007 and 2018, I show that the two carry opposite information about default. Borrowers employed by religious institutions (pastors and ministers, but also church secretaries and administrators) default about five percentage points less than borrowers with the same credit score, income, debt burden, loan terms, state and origination year. The estimate survives controls for eight other stable occupations and comparison with, and exact matching to, nonprofit, education and healthcare workers, who show no comparable advantage, and it also survives entropy balancing on 76 covariate moments, double machine learning, sensitivity analysis for unobserved confounding, and replication on Prosper. It is larger where local congregations are denser, holds within three-digit ZIP areas, and does not respond to local unemployment shocks. Borrowers who invoke faith in the text of their loan description default about three percentage points more. The sign is stable across every specification, but the estimate loses precision once the full text is conditioned on, and I report it as such. Neither signal is priced by the platform. The pattern is consistent with religious community acting as borrower-side social collateral, and with religious language as a low-cost, unverifiable signal whose information runs against the sender's intent.

*Keywords:* religion, social capital, consumer credit, credit risk, online lending, text analysis, signaling.
*JEL:* D14, G21, G41, Z12.

# 1. Introduction

Borrowers on the early online lending platforms, then called peer-to-peer, were asked to say something about themselves, and LendingClub gave them a free-text box. Some wrote nothing, some wrote a paragraph about credit cards, and a small number wrote about God. "Thank you and God bless." "As a Christian I believe in paying my debts." "Monthly budget: tithe $529, rent $900…" These sentences are rare (717 of them among 125,811 loan descriptions, almost all filed between 2008 and 2014), and it is tempting to treat them as noise. Netzer, Lemaire and Herzenstein (2019) did not. In their study of Prosper applications, mentions of God were among the words that appeared more often in the text of borrowers who later defaulted, but they reported it as one lexical signal among many and moved on.

I want to stay with it, because the same platform contains a second, quieter trace of religion that points the other way. LendingClub also asked borrowers for their job title, and about one in four hundred wrote "pastor," "minister," "chaplain," "church administrator," or "church secretary." Those borrowers default less: 13.3 percent against 20.0 percent in the raw data, and about five percentage points less after I condition on grade, FICO, income, debt-to-income, loan terms, state and year. The two facts sit uneasily together. Borrowers who talk about faith in their loan request default about three percentage points more than their scores predict, while borrowers whose working lives are embedded in a religious institution default about five points less. Same platform, same years, same controls, opposite signs. Neither difference is reflected in the interest rate, because LendingClub priced loans by grade, so investors earned more than the grade implied on loans to church employees and less on loans that invoked faith. I document both facts in LendingClub's full public file of terminated loans, which covers more than a decade of lending, and I replicate the first on Prosper. Neither signal is a field in that file. I build the affiliation indicator from free-text job titles and check its precision on a random sample, have every description the religious dictionary flags coded against a codebook, and link each borrower to local congregation density and unemployment through the three-digit ZIP code.

This paper is about that contrast, and about what lies behind the second half of it. My claim is narrow. I do not argue that religion causes repayment, nor do I offer a religious credit score, since the signals are too rare to move a predictive model and I show that they do not. What I argue is that religion reaches a credit market through two channels that carry different information, and that the gap between them is legible in ordinary loan data once one looks for it. Faith that is *professed*, invoked in a request for money, behaves like a low-cost signal: it costs nothing to write, cannot be verified, travels with hardship, gratitude and appeals for help, and its association with default is consistent in sign but not strong. Faith that is *belonged to* (a job inside a congregation) behaves like a commitment with a community attached. It is not something one adds to a loan request for effect, and its association with default is large, stable across a decade, present for the church secretary as much as for the pastor, stronger where there are more churches nearby, and reproduced on a second platform. The broader point concerns organization rather than piety. A congregation can enforce repayment through ties that the lender never sees and cannot contract on, and a national credit market registers that enforcement only when a borrower's job happens to name the community. Section 2 states the argument in a simple framework in which the two signals take opposite signs without any difference in belief between the borrowers who send them.

The evidence within the affiliated group is what moves the paper from a curiosity about words to a claim about mechanism. The obvious alternative reading of the clergy result is that pastors have steady jobs, but three findings push against reading it that way alone. First, non-clergy church employees, whose pay and job security resemble those of secretaries and administrators anywhere, default as little as the clergy do. Second, the affiliation effect grows where congregations are denser in the borrower's three-digit ZIP area, which job stability has no reason to do, and it does so even when every fixed characteristic of that area is absorbed by ZIP-level fixed effects. Finally, it does not change when local unemployment rises over the life of the loan. None of these is a natural experiment, and I do not present them as one. Still, together they are the pattern one would expect if a religious congregation works, for its members, the way the group in a group-lending scheme works for its borrowers (Besley and Coate, 1995; Karlan, 2007): a community that observes financial conduct and in which default has a cost beyond the credit file. Here the community sits on the borrower's side of the transaction rather than the lender's.

![Figure 1. Two channels through which religion enters a consumer-credit file. Solid boxes: institutional affiliation revealed by the job title, its proposed mechanism, and the confirmatory test H1; dashed boxes: religious language volunteered in the loan description, its proposed mechanism, and H2. Local congregation density (2010 U.S. Religion Census) enters as a moderator of H1 only. Odds ratios and marginal effects from Tables 2, 5 and 7; pricing gap from Section 6.1.](fig1_channels.png){width=6.3in}

I should be direct about what the design can and cannot do. There is no instrument, and the public file has no borrower identifiers that would allow within-borrower comparison. Church employees differ from other borrowers in ways I cannot fully observe. I address this in two ways. I ask how strong an unobserved confounder would have to be, in the sense of Oster (2019) and Cinelli and Hazlett (2020), to erase the estimate (by Cinelli and Hazlett's measure, about twelve times as strong as employment length). I also name, for each piece of evidence, what it rules out and what it does not. I treat the narrative result more guardedly still. Its estimate is stable across length matching, a battery of text dictionaries, and a placebo against a thousand random word sets, and it passes the test I specified before estimation, with a Holm correction. Yet it is estimated from 681 loans, and once a flexible learner is given a representation of the full text the interval opens to include zero. I set out in advance that this would lead me to lower the claim, and I do.

The finding speaks to three literatures, and I should be precise about what each already knows. The first is the work on religion, social capital and economic behavior. Religious belief is associated with trust, reciprocity and cooperative attitudes in survey data across countries (Guiso, Sapienza and Zingales, 2003; Valencia Caicedo, Dohmen and Pondorfer, 2023). Deller, Conroy and Markeson (2018) find that U.S. counties with more religious congregations, which they treat as a source of social capital, have more small business activity, and Deng, Liu and Yan (2025) find that historical Protestant missionary activity in China left a lasting trace in local trust and trustworthiness. That literature establishes that religion builds the kind of network group-lending theory needs, but it does not observe an individual's place in such a network alongside a debt with money at stake. Here I observe both for the same borrower. The protective form of religion is an affiliation with a community, not a vocation or a belief, and its association with default grows as that community gets denser.

The second is the finance literature on religion and credit, which has identified religion mostly through the lending contract or the borrower's surroundings. For example, Baele, Farooq and Ongena (2014) find that Islamic loans default less than conventional loans to comparable borrowers. Firms in more religious U.S. counties borrow at lower spreads (He and Hu, 2016; Chen, Huang, Lobo and Wang, 2016) and with fewer covenants (He and Hu, 2016). Credit unions in more religious counties lend more cheaply and hold better loans (Davidson, Ngo and Wang, 2026), and county adherence predicts lower mortgage delinquency and less misrepresentation (Li and Ucar, 2022; Conklin, Diop and Qiu, 2022). At the individual level, religious affiliation is associated with the kinds of debt a household carries (Clifton, Brewer and Upenieks, 2023) and religiosity in adolescence with less financial distress in adulthood (Lei, Lu, Niu and Zhou, 2024), but neither study observes a loan and its repayment. What this paper adds is not that religion matters for credit, which is established. It is that religion enters an individual credit file in two observable forms (an institutional affiliation and a self-authored text) that carry opposite information about the repayment of the same kind of loan in the same market, and that the informative one is not the regional signal seen from closer up. Local religiosity does not protect borrowers here, while individual affiliation does, and the individual effect is amplified rather than explained by the local one.

The third literature is the work on borrower-supplied information in online credit markets. Iyer, Khwaja, Luttmer and Shue (2016) show that lenders there infer creditworthiness from what lies outside the credit score. Online lenders are known to read soft information, such as borrowers' social-network ties, and to price some of it, not always correctly (Freedman and Jin, 2017). What they read includes the borrower's appearance (Duarte, Siegel and Young, 2012), verified friendships (Lin, Prabhala and Viswanathan, 2013) and the job title itself (Davaadorj, Enkhtaivan and Lu, 2024, 2026). Some of these signals are associated with lower default, among them verified friendships on Prosper and trusted job titles, and broad occupation classes predict LendingClub defaults beyond standard risk factors (Croux, Jagtiani, Korivi and Vulanovic, 2020). The affiliation I study is a community tie of a much thicker kind than a platform friendship, and I look at default rather than funding. Within this literature, the text of the request has been studied most (Herzenstein, Sonenshein and Dholakia, 2011; Michels, 2012; Dorfleitner et al., 2016; Nowak, Ross and Yencha, 2018; Netzer et al., 2019; Kriebel and Stitz, 2022; Gao, Lin and Sias, 2023; Sanz-Guerrero and Arroyo, 2025). That work has established that words predict default (Netzer et al. list mentions of God among them) and that self-authored identity claims can raise funding while predicting worse repayment (Herzenstein et al., 2011). However, it has been less interested in which words carry information of their own rather than proxying for circumstances. Religious language, it turns out, partly proxies, and the part that does not is the part one would predict from theory, since descriptions that report religious *practice* rather than merely invoking faith behave like the affiliation signal.

The rest of the paper proceeds as follows. Section 2 sets out the argument, a simple framework and the two hypotheses, and Section 3 describes the data, the two religious indicators, the text controls, and the external data on local religiosity and labor markets. Section 4 explains the empirical approach, and Section 5 presents the results: the two main tests with the Prosper replication, the mechanism evidence, how individual and local religion compare, and the timing of default. Section 6 discusses economic magnitude, what happens after default, what investors did, and the limits of the evidence. Section 7 concludes.

# 2. Religious community, religious language, and repayment

## 2.1 Community as collateral

Group-lending theory gives a clean account of why belonging can substitute for collateral. When borrowers are jointly liable, their peers have a stake in repayment and a reason to monitor one another (Stiglitz, 1990). When they can also sanction one another socially, default imposes a cost on the defaulter's standing in the group that the lender can rely on even though it cannot contract on it (Besley and Coate, 1995). Ghatak and Guinnane (1999) set out the channels through which this works: who is admitted, how borrowers are monitored and their outcomes verified, and how default is sanctioned. Karlan, Möbius, Rosenblat and Szeidl (2009) give the idea its name and its model: the trust a borrower can draw on is the value of the network ties that a default would put at risk, and it is largest in dense, closely knit communities. Evidence from microfinance suggests the mechanism is real. Karlan (2007) finds that borrowers who are more socially connected to their group members repay more, and because the groups were formed quasi-randomly he attributes the effect to monitoring and enforcement rather than to selection. Among Peruvian group borrowers, those who were trustworthy in a trust game repay better, while those who were trusting in the same game have more repayment problems (Karlan, 2005), and Feigenberg, Field and Pande (2013) show that randomly more frequent group meetings cut default on the next loan by two thirds. In addition, Giné and Karlan (2014) find that removing joint liability while keeping the meetings does not raise default, which is to say the group disciplines even when the lender holds no contract with it. Al-Azzam, Hill and Sarangi (2012) find that Jordanian lending groups whose members are more religiously observant repay more promptly, alongside the effects of the group's social ties.

The insight travels beyond microfinance. Guiso, Sapienza and Zingales (2004) show that in Italian provinces with more social capital households use more formal credit and rely less on cash, and they read the result as trust substituting for legal enforcement, since the effect is strongest where courts are slow. In U.S. consumer credit, borrowers in communities with more social capital default less, most markedly when default would be strategic (Clark, Hasan, Lai, Li and Siddique, 2021), and whether borrowers are willing to default strategically depends on moral views and on knowing others who have done it (Guiso, Sapienza and Zingales, 2013). The same holds inside marketplace lending: borrowers from higher-social-capital regions default less on a Chinese platform (Hasan, He and Lu, 2022) and on LendingClub itself (Lu, Wang, Wang and Zhao, 2020), and making a borrower's default visible to his social contacts deters it (Ge, Feng, Gu and Zhang, 2017).

A religious congregation is a community of exactly this kind, and an unusually intense one (Putnam, 2000). Members meet weekly, know one another's families, and share explicit norms about money, since debt, stewardship and honesty are recurring subjects of religious teaching. The economics of religion has long treated the congregation as a club that produces goods its members cannot buy elsewhere (Iannaccone, 1998; Iyer, 2016). Iannaccone (1992) argued that the demands religious groups place on members, which look wasteful from outside, help the group overcome free riding: they screen out the less committed and, by making outside activities costlier, raise participation among those who remain. Strict churches are strong for the same reason, because their demands screen out members who lack commitment and stimulate participation among those who stay (Iannaccone, 1994). Sosis and Bressler (2003) found that religious communes imposing more costly demands on their members outlived those imposing fewer, although costly demands did not extend the life of secular communes. Religious attitudes toward cooperation and thrift show up in survey data across countries (Guiso, Sapienza and Zingales, 2003), and believers report more positive reciprocity, altruism and trust on experimentally validated preference measures (Valencia Caicedo, Dohmen and Pondorfer, 2023). However, this literature lacks a link between an individual's membership in such a community and an observable financial outcome with money at stake.

A borrower who works for a church is embedded in that community more deeply than an ordinary member, because their employer is the congregation and their reputation among its members is their professional reputation. If a congregation functions as a group in the group-lending sense, its employees are the members for whom the cost of default is highest, and that should be true whether the employee is the pastor or the secretary. It should also scale with how much observing the community does: denser networks of congregations mean more overlapping ties, more people who would hear of a default, and a higher cost of one. My account extends the logic of social collateral from groups a lender organizes to an affiliation a borrower reports, but it does not introduce a new mechanism, and I do not observe the community's monitoring directly. Instead, what I can observe is whether the pattern of default matches what that logic predicts and fails to match what its rivals predict.

**H1.** Conditional on credit score, income, debt burden, loan terms, state and origination year, borrowers whose stated occupation places them in a religious institution default less (odds ratio below one).

The mechanism predicts three further things that I did not specify as tests in advance but that discriminate between it and the main rival account, that church jobs are simply stable. First, non-clergy church employees should show the effect as strongly as clergy, since the community is the same. Second, the effect should be larger where congregations are denser. Third, the effect should not vary with local labor-market shocks, since how closely a community observes a member does not depend on the unemployment rate. An income-stability mechanism, by contrast, should show the affiliation advantage widening when local unemployment rises and other borrowers lose their jobs.

## 2.2 Language as a low-cost signal

The description box gives borrowers a second channel, and signaling theory says what to expect from it. A message is credible when sending it falsely is costly, or when the sender's interests happen to align with the receiver's. A message anyone can send at no cost, to an audience that would like to hear it, is cheap talk in the technical sense (Crawford and Sobel, 1982; Farrell and Rabin, 1996), and whether it carries information then depends on who chooses to send it rather than on what it says. A costly signal is different, since it separates senders only when its cost differs across them (Spence, 1973). If misreporting carries even a small moral cost to the sender, such talk becomes partly informative (Kartik, 2009), and in online lending markets unverifiable disclosure has been shown to relate non-monotonically to loan quality (Caldieraro, Zhang, Cunha and Shulman, 2018). Yet the information need not run the way the sender intends. Two findings bear on this, one about religious people and one about lending. Kirchmaier, Prüfer and Trautmann (2018) find in a representative Dutch sample that religious people state stricter moral attitudes toward economic behavior than the non-religious, yet betray trust just as often in an anonymous trust game. In lending, unverifiable self-description has been found to raise funding while predicting worse repayment (Herzenstein et al., 2011; Wang, Wang, Wu and Zhang, 2023), and voluntary repayment promises to predict better repayment among new borrowers and worse among returning ones (Lun, Meng and Xu, 2024). "God bless" costs nothing to write, cannot be verified, and is addressed to strangers who are deciding whether to lend, and two mechanisms make its expected association with default positive. The first is selection: the borrowers who feel moved to invoke faith in a request for money are disproportionately those whose situation gives them reason to, and the same descriptions thank the reader in advance, describe hardship, and ask for help at several times the base rate. The second is substitution: a borrower with strong verifiable facts to offer tends to offer them, so appeals to faith concentrate where such facts are thin.

Under either mechanism the test is not whether religious language correlates with default, which Netzer et al. (2019) already showed, but whether it does so *after* the length, tone, hardship and gratitude content it travels with are held fixed. That residual is what the low-cost-signal reading predicts should remain, and what a "religious language is just distress language" reading predicts should not.

**H2.** Conditional on the same credit and loan controls and on the length, moral, hardship, gratitude, family, appeal and business content of the description, borrowers who use religious language default more (odds ratio above one).

The theory also predicts something inside the description that can be checked. Suppose what makes a religious signal informative is that it costs something and ties the borrower to a community. Then a description that reports religious *practice* (a tithe line in a monthly budget, a job at a church, a mission trip to be paid for) should resemble the affiliation signal more than "God bless." Section 5.2 reports that it does.

## 2.3 A simple framework

The two hypotheses follow from one stylized setup, which I state to make the predictions and their rivals explicit rather than to offer a new model. A borrower with observable characteristics *X* has an unobserved repayment type *θ*. When a payment comes due, the borrower defaults if the net benefit of defaulting, which falls with *θ* and rises with an adverse income shock *ε*, exceeds the cost of default. That cost has two parts. The formal part (a damaged credit record, collection) is the same for every borrower with the same *X*, and the platform prices it through the grade. The social part, *S*, is what the borrower loses in the eyes of people who would learn of the default. Following Besley and Coate (1995) and Karlan et al. (2009), I let *S* rise with how embedded the borrower is in a community that observes financial conduct and with how dense that community's ties are. For most borrowers on a national platform *S* is close to zero, since nobody they know is watching the loan.

*Proposition 1.* Holding *X* fixed, a borrower with larger *S* defaults less often, and the difference grows with the density of the community behind *S*. Because *S* does not depend on *ε*, the difference need not widen when adverse income shocks become more common. Clergy and non-clergy staff of the same congregation are observed by the same community, so they should have similar *S*. A rival account in which a church job lowers the variance of *ε* predicts the same first statement but a different last one: the advantage of a stable job should grow when adverse shocks become more common, because that is when stability matters. H1 is the first statement, and the three further predictions in Section 2.1 are the rest.

*Proposition 2.* Before funding, the borrower may add a message *m* that no one can verify, such as "God bless," at a small personal cost *k*. Suppose investors respond to the message, raising the chance of funding by some Δ ≥ 0, or that the borrower believes they do. That increase is worth more to a borrower with fewer alternatives, that is, one with lower *θ* or a recent adverse shock, and the borrower sends *m* when Δ times that value exceeds *k*. Senders are then selected toward low *θ*, so, holding *X* fixed, borrowers who send *m* default more often. Controls *Z* for the content that travels with *m* (hardship, gratitude, appeals, length) absorb the part of that difference that *Z* reveals about *θ*, and a positive residual remains unless the text controls span *θ*. This residual is what H2 tests. The same selection arises without any response from investors if adversity itself prompts religious expression, as the rise of religious practice in crises suggests (Chen, 2010; Bentzen, 2021). A message that reports practice (a tithe in a budget, a job at a church) is different, because it describes conduct that places the borrower inside a community and so carries some of the *S* of Proposition 1.

The framework makes two points explicit. The two signals can take opposite signs even if affiliated borrowers and borrowers who invoke faith hold the same beliefs, because what matters is who observes the borrower and who chooses to speak. In addition, neither signal has to be priced for the propositions to hold, since the grade prices only what enters *X*.

H1 and H2 are the only confirmatory tests. I test each one-sided, with a Holm correction across the pair, and I stated in advance what a failure would mean. Without H2 the paper would be a study of affiliation with expressed faith as a null result, and without H1 surviving stable-occupation controls, the affiliation effect would have to be read as a secure job. As it happened, H1 survived everything and H2 survived its confirmatory test but not a stricter one I had also set out in advance. I report both outcomes as the rules required.

# 3. Data

## 3.1 LendingClub

I use the public LendingClub loan-level file covering loans issued from June 2007 through December 2018 (2,260,701 loans). Each record carries the borrower's FICO range at origination, annual income, debt-to-income ratio (DTI), home ownership, employment length, income-verification status, state and three-digit ZIP code, and the loan's amount, term, interest rate, sub-grade, purpose and status at the time of the data release. Two free-text fields matter here. The first is the job title the borrower typed in (`emp_title`), available throughout the sample, and the second is the loan description (`desc`), a free-text box that borrowers could fill in and that investors could read while the loan was listed. LendingClub stopped showing the description to investors in 2014 and the field is essentially empty afterward: of the 125,811 loans with any description text after I strip the platform's boilerplate, 125,761 were issued between 2007 and 2014. Descriptions were common in the early years (95–100 percent of loans in 2008–2009, 58–66 percent in 2010–2012) and fell to 36 percent in 2013 and 6.5 percent in 2014. The median description is 24 words.

The outcome is default. I keep loans whose status is terminal (Fully Paid, Charged Off, or Default) and drop loans still current, in grace or late, and the small "does not meet credit policy" group. After removing records with missing DTI, FICO or rate, the analysis sample has 1,344,976 loans, 20.0 percent of which were charged off or defaulted. The description subsample has 123,292 loans (15.3 percent defaulted) and is an earlier and somewhat riskier slice of the platform's history, which is why every specification carries origination-year fixed effects. Writing a description was a choice, and Appendix Table C2 reports what predicts it among 2008–2014 loans: the year of origination above all, then grade and loan size, while religious-institution affiliation is unrelated to it (odds ratio 1.02, p = 0.81). Thus the narrative results describe borrowers who chose to write, and I do not extrapolate them to those who did not. Table 1 reports descriptive statistics.

**Table 1. Descriptive statistics by group**

| Group | N | Default rate | FICO (mean) | Income (median, $) | DTI | Rate (%) | Amount ($) | 60-month | Grade A–B |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Religious-institution affiliation | 3,105 | 0.133 | 704.0 | 60,000 | 19.0 | 12.28 | 14,826 | 0.228 | 0.571 |
| — clergy role | 2,497 | 0.138 | 702.9 | 62,400 | 19.3 | 12.12 | 15,259 | 0.233 | 0.565 |
| — church staff (non-clergy) | 608 | 0.114 | 708.3 | 53,000 | 17.5 | 12.92 | 13,050 | 0.207 | 0.594 |
| All other borrowers | 1,341,871 | 0.200 | 698.2 | 65,000 | 18.3 | 13.24 | 14,418 | 0.241 | 0.466 |
| Religious language (description sample) | 681 | 0.200 | 704.9 | 55,000 | 16.0 | 13.44 | 13,460 | 0.256 | 0.502 |
| Other descriptions | 122,611 | 0.153 | 703.7 | 62,000 | 16.3 | 13.42 | 13,982 | 0.232 | 0.535 |

*Notes.* Terminated LendingClub loans issued 2007–2018 (Fully Paid, Charged Off, Default). Description sample: loans with non-empty borrower text after removing platform boilerplate, issued 2008–2014. Text features in the description sample, religious-language vs other: mean words 116 vs 36 (median 68 vs 23). The share containing moral language is 0.19 vs 0.06, hardship 0.15 vs 0.07, gratitude 0.56 vs 0.14, family 0.33 vs 0.07, appeal for help 0.15 vs 0.04, business 0.16 vs 0.07.

## 3.2 Two religious indicators

*Religious-institution affiliation.* I flag a borrower as affiliated when the job title contains a clerical role word (pastor, minister, ministry, clergy, priest, chaplain, rabbi, missionary, reverend, evangelist, deacon, worship, imam, seminary) or a religious-organization word (church, parish, diocese, congregation, synagogue, mosque) that is not part of a hospital, school, insurer or bank name. This yields 5,014 loans in the full file and 3,105 in the terminal sample. Of these, 2,497 carry a clerical role word (1,604 "pastor," 496 "senior pastor," 297 "minister," 211 "chaplain") and 608 name a religious organization without one ("First Baptist Church," "church administrator," "United Methodist Church," "parish administrator," "church secretary"). I make no attempt to distinguish denominations, and the list is dominated by Christian titles because the borrowers are. The split between role and staff underlies the within-institution comparison in Section 5.3. To check the indicator's precision I had 200 randomly drawn affiliated job titles coded by a large language model (Appendix Table B2): 146 are clerical roles, 48 are non-clerical church staff, 2 are not religious employment at all, and 4 cannot be classified from the title. The two clear errors share a cause. In Louisiana a "parish" is a county, so "Ouachita Parish Sheriff's Office" matches the organization word, and a targeted rule identifies 30 such civil-parish titles in the terminal sample. Dropping them moves the affiliation odds ratio from 0.692 to 0.683, and I keep them in the main sample so that the reported estimate is the one the rule fixed in advance produces.

*Religious language.* I flag a description as containing religious language when the title or text matches a dictionary of religious terms (God, Jesus, Christ, Christian, church, pray/prayer, bless/blessed/blessing, faith in its religious sense, the Lord, Bible/scripture, tithe, ministry/pastor/missionary, amen, and denominational names). I then exclude idiomatic uses that a first reading of the matches showed to be non-religious ("faith in me," "good faith," "heaven forbid," "Lord & Taylor," "land lord"). The dictionary flags 717 of the 125,811 descriptions (0.57 percent) and 681 loans in the terminal description sample. Because a dictionary cannot read context, every flagged description was then coded against a short codebook (Appendix B). The codebook distinguishes formulaic uses (467 loans, as in "Thank you and God bless"), identity or value claims (34, as in "as a Christian I believe in paying my debts"), concrete practice or expense (82, as with tithes in a budget, church employment, mission trips), and non-religious matches the exclusion rules had not caught (98). Coding was done by a large language model over all records and checked by an independent recoding of a stratified 200-record sample with a model of a different family, and the two agreed at Cohen's κ = 0.86 on the four-way type and 0.81 on religious versus not. I use the dictionary indicator for the confirmatory test, because that is what I specified before estimation, and the validated indicator (the 583 loans coded as formulaic, identity or practice) in robustness, where the 98 false positives serve as a placebo of their own.

One might worry that a dictionary misses religious content expressed without its keywords, such as "the man upstairs," "a higher power," or "keep us in your prayers." I checked. I trained a classifier on the 583 validated religious descriptions against 4,000 random unflagged ones, with every explicit religious word masked so the model could learn only from surrounding context, and scored the 122,611 unflagged descriptions. A large language model then coded stratified samples from the top of the ranking: none of 117 in the top 2,000 contained religious content, 3 of 240 further down did, and a supplementary list of implicit phrases found 11 more (mostly "godsend" and "karma"). Religious content the dictionary misses exists, but on the order of a few dozen descriptions in the whole file, so the 681 flagged loans are, for practical purposes, the population. Thus the narrative estimate in Section 5.2 is imprecise because few borrowers write this way, not because of how I found them.

The two indicators rarely coincide: in the description sample, 372 loans are affiliated and 681 carry religious language, and 20 are both.

## 3.3 Text controls

Religious language does not appear in a vacuum. Descriptions that contain it are three times longer than the median (68 versus 23 words) and far more likely to thank the reader (56 versus 14 percent), mention family (33 versus 7), describe hardship (15 versus 7), ask for help (15 versus 4) or make moral claims about reliability (19 versus 6). I therefore build six dictionary indicators (moral self-presentation, hardship, gratitude, family, appeal for help, and business purpose) and the log of description length, and include them in every narrative specification. Their coefficients are of independent interest: moral language is associated with lower default (odds ratio 0.88), hardship, gratitude and appeals with higher (1.17, 1.12, 1.12), and length itself with lower (0.92 per log point of length). In the double machine learning specifications I go further and let a flexible learner use a 300-dimensional pretrained word-vector representation of each description, so that anything the text says that a linear dictionary misses is still conditioned on. On this same platform, Kriebel and Stitz (2022) find that even short descriptions carry default information and that an average-embedding network predicts about as well as a transformer. That result motivates my use of averaged word vectors as one text representation.

## 3.4 Local religiosity and local labor markets

To separate individual affiliation from the religiosity of the place a borrower lives in, I use the 2010 U.S. Religion Census county file (Grammich et al., 2012), a wave of the county membership surveys behind the religiosity measures used in corporate finance since Hilary and Hui (2009). I link it to LendingClub's three-digit ZIP codes through the Census Bureau's relationship file between ZIP Code Tabulation Areas and counties, weighting counties by their number of residents within each three-digit ZIP area (ZIP3). This gives, for 894 areas covering 99.97 percent of loans, adherents per thousand residents and congregations per ten thousand. For labor-market shocks I merge county annual unemployment rates from the Bureau of Labor Statistics (BLS) Local Area Unemployment Statistics for 2008–2018 in the same way and compute, for each loan, the unemployment rate when the loan was issued and the largest rise in the rate over the loan's term.

## 3.5 Prosper

To replicate the occupational result I use the public Prosper file (113,937 listings, 2005–2014), which has no free text but has an occupation code with the categories "Clergy" and "Religious." Among the 50,270 terminated loans with complete covariates, 141 fall in those categories, and the controls parallel LendingClub's.

# 4. Empirical approach

The confirmatory specification is a logit of default on the religious indicator and the credit and loan variables described in the data section, with origination-year, grade, purpose, employment-length, homeownership, verification and state fixed effects, and standard errors clustered by state. H1 is estimated on all 3,105 affiliated loans together with a random draw of 250,000 other terminated loans (the draw is a memory constraint, not a design choice), and H2 on the full description sample with the six text dictionaries and log length added. Clustering by three-digit ZIP area or by month of origination instead of by state changes the standard errors but not what I conclude (Appendix Table C3), and Appendix Table C1 shows the covariate balance that entropy balancing achieves. Both hypotheses are one-sided, I apply a Holm correction across the pair, and I report odds ratios and average marginal effects.

Everything that follows the two tests is designed to answer a specific objection, and I want to be explicit about what each piece of evidence does and does not rule out. Against the objection that church employees simply have secure jobs, I add eight other stable-occupation indicators and compare the affiliation effect to theirs, which rules out a generic public-or-institutional-employment effect but not a feature peculiar to working for a church. The sharper version of that objection is that church employees resemble other mission-driven, modestly paid service workers rather than the average borrower. Against it, I compare them with borrowers whose job titles place them in nonprofit and social-service work, education, or healthcare, first with those jobs as the only comparison group and then within coarsened-exact-matching cells, and I ask whether those jobs show a default advantage of their own. Against the objection that affiliated borrowers differ on observables in ways a logit handles poorly, I use entropy balancing (Hainmueller, 2012) to reweight the comparison group so that 76 covariate moments match exactly, and a partially linear double machine learning model (Chernozhukov et al., 2018) with CatBoost gradient-boosted trees as nuisance functions and five-fold cross-fitting. These rule out a misspecified functional form but not unobserved confounding, against which I have no instrument, and I say so. I report Oster's (2019) δ and the Cinelli–Hazlett (2020) robustness value benchmarked against employment length, which state how strong a confounder would have to be. For mechanism, I use three designs. Comparing clergy with non-clergy staff of the same churches holds the community fixed and varies the vocation. An interaction of affiliation with local congregation density, estimated with state and then ZIP3 fixed effects, tests the mechanism through heterogeneity in the manner of Rajan and Zingales (1998): the main effect remains observational, but a differential that survives absorbing every fixed feature of the borrower's area is not a product of those features. Finally, an interaction with local unemployment shocks tests the income-stability alternative directly, with teachers and government employees as a positive control.

Against the objection that religious language proxies for length or tone, I match each flagged description to its five nearest neighbors in length within grade-year cells, and I replace the dictionary controls with the pretrained text representation inside the double machine learning model. Against the objection that any rare word set would do, I draw 1,000 random sets of non-religious words matched to the dictionary's document frequency and re-estimate the residualized effect for each. And against the objection that one platform is one platform, I estimate H1 on Prosper.

A word on what I do not do. I do not estimate a prediction model and claim that it predicts better, and when I checked, adding either indicator to a cross-validated logit moves the area under the ROC curve (AUC) by less than 0.0001. Indicators that flag a quarter of one percent of borrowers cannot improve aggregate prediction, and the paper should not be read as if they could. Nor do I fit a structural or mediation model, because the mediators of interest (community observation, reputational cost) are not observed at the individual level and a path diagram would add assumptions without adding identification.

# 5. Results

## 5.1 Affiliation (H1)

Table 2 reports the affiliation estimates. Column (1) of Panel A gives the confirmatory specification on the full terminal sample: the odds ratio is 0.69 (clustered standard error on the log-odds 0.041, p ≈ 7 × 10⁻¹⁹), an average marginal effect of −4.8 percentage points against a base default rate of 20 percent, or about a quarter of the base rate. Columns (2) and (3) split the sample by period: the estimate is 0.61 for loans issued in 2008–2014 and 0.74 for 2015–2018. The effect is smaller in the later, lower-default years but does not fade, which matters because it means the finding is not a property of the platform's early, self-selected borrowers. The one-sided Holm-adjusted p-value is below 10⁻¹⁸.

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

*Notes.* Logit, default on affiliation and controls: grade, origination year, interest rate, FICO midpoint, log income, DTI, 60-month term, log amount, employment length, home ownership, income verification, purpose, state fixed effects. SE clustered by state. Sample = all affiliated terminated loans plus 250,000 randomly drawn other terminated loans. Affiliation = job title contains a clerical role word or a religious-organization word not part of a hospital, school, insurer or bank name (3,105 loans, of which 2,497 have a clerical role word and 608 are church staff without one). Column (5) adds indicators for teachers, police/corrections, firefighters, military, government, nurses, postal and transit workers (their ORs: 0.91, 0.93, 0.64, 0.93, 0.90, 1.06, 1.20, 1.10). Column (6): weights equate 76 covariate moments between groups (max |SMD| 0.175 → 0.000). Column (7): DoubleML partially-linear, CatBoost nuisance, 5-fold cross-fitting. ATTE −0.042 (p<0.001). One-sided Holm-adjusted p for H1 < 10⁻¹⁸. Panel B: same controls as Panel A. Nearest occupations identified from job titles for social work (social worker, case manager, counselor and nonprofit/charity organizations), education (teacher, professor, school, instructor) and healthcare (nurse, hospital, medical, health, therapist, clinic). Coarsened exact matching cells: grade × year × 20-point FICO band × income quartile × employment length × homeownership × term (neighbor pool) or income decile × employment length × grade × year × term (stable occupations), with a weighted logit on matched cells. Hierarchy split over all 3,105 affiliated loans by title words.


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

The stable-employment objection is the first thing to settle, and column 5 adds the eight occupation indicators. Teachers (0.91), government employees (0.90) and police (0.93) do default modestly less than other borrowers, and firefighters markedly less (0.64, on 493 loans), but the affiliation coefficient does not move (0.69). When I restrict the comparison group to the 118,022 borrowers in those stable jobs, affiliated borrowers still default less (0.73, with raw rates of 13.3 versus 18.8 percent). Entropy balancing tells the same story from the other side: after reweighting so that the comparison group matches affiliated borrowers on every one of 76 moments, the comparison default rate falls from 20.1 to 17.5 percent, but affiliated borrowers remain at 13.3, and the weighted odds ratio is 0.70. The double machine learning estimate is −4.3 percentage points (standard error 0.6), and Table 3 gives the sensitivity analysis. Oster's δ is 6.5, so unobserved selection would have to be six and a half times as strong as selection on the observables to explain the estimate away. The robustness value is 0.015, meaning a confounder would need to explain 1.5 percent of the residual variance of both default and affiliation, which is about twelve times the explanatory power of employment length.

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

Panel B of Table 2 takes the objection one step further. If the affiliation effect were a property of mission-driven, modestly paid service work, borrowers in the jobs nearest to church work should show it too, and comparing affiliated borrowers with those jobs alone should shrink it. Neither happens. Social workers, case managers and counselors (11,592 loans) default no less than other borrowers (odds ratio 1.02), and neither do healthcare workers (1.02, on 76,981 loans), while teachers and other education workers default modestly less (0.94). With each of these groups as the only comparison, the affiliation odds ratio is 0.69, 0.68 and 0.75 respectively, and 0.71 against all three together. Matching affiliated borrowers exactly to those neighbors on grade, year, a 20-point FICO band, income quartile, employment length, homeownership and term (2,766 matched affiliated loans in 2,234 cells) gives 0.70, and a similar match to the eight stable occupations on income decile, employment length, grade, year and term gives 0.74 (3,008 matched). Whatever the affiliation captures, it is not shared by the jobs that most resemble it in pay, tenure or purpose. Figure 2 collects the affiliation estimates from Table 2, the neighbor-occupation comparisons and the Prosper replication in one plot, where every interval lies below one and the point estimates span 0.61 to 0.75.

![Figure 2. Religious-institution affiliation and default across specifications. Odds ratios with 95% confidence intervals (log scale) from Table 2, Panels A and B, and Table 4. Intervals for estimates reported with p-values only are recovered from the p-value.](fig2_forest.png){width=6.3in}

Occupation has been found to carry default information beyond observables before. Agarwal, Chomsisengphet and Zhang (2017) find that finance professionals are less often delinquent on their mortgages. On LendingClub, borrowers in professional occupations default less than those in elementary, sales and trade occupations (Croux et al., 2020), and skilled job titles default less and are priced accordingly (Davaadorj et al., 2024). However, in those cases the natural reading is expertise or earning power, and a church secretary has neither to point to.

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

Table 5 builds the narrative estimate one control set at a time, and with credit and loan controls only (column 1), religious language carries an odds ratio of 1.27 (p = 0.018). Adding log length (column 2) moves it to 1.34, because long descriptions default less and religious descriptions are long. Adding the six text dictionaries (column 3, the specification fixed before estimation) brings it back to 1.28 (p = 0.016), an average marginal effect of +3.2 percentage points against a base rate of 15 percent in the description sample. Replacing log length with length deciles (column 4) changes nothing, and the one-sided Holm-adjusted p-value for that specification is 0.008. In the length-matched sample (681 flagged loans and 2,891 neighbors averaging 114 words against 116) the odds ratio is 1.34 (p = 0.012). The fake-dictionary permutation puts the residualized linear effect of the actual dictionary at 0.035 against a permutation mean of −0.003 (SD 0.014), and one random word set in two hundred does as well (one-sided p = 0.005).

**Table 5. Religious language and default (H2)**

| | (1) Credit controls | (2) + log length | (3) + text dictionaries | (4) + length deciles | (5) Length-matched | (6) Coder-validated | (7) DML + dict. | (8) DML + dict. + text |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Religious language (OR) | 1.265 | 1.338 | 1.281 | 1.274 | 1.344 | 1.335 | +0.033 (θ) | +0.026 (θ) |
| SE | 0.100 | 0.098 | 0.103 | 0.101 | | | 0.015 | 0.015 |
| p | 0.018 | 0.003 | 0.016 | 0.016 | 0.012 | 0.001 | 0.027 | 0.091 |
| AME | +3.1 pp | +3.8 pp | +3.2 pp | +3.1 pp | | | | |
| Dictionary false positives (OR) | | | | | | 0.948 (p=0.88) | | |
| N | 123,292 | 123,292 | 123,292 | 123,292 | 3,572 | 123,292 | 123,292 | 123,292 |

*Notes.* Same controls as Table 2 plus, from column (2), log description length and, from column (3), six text indicators (moral, hardship, gratitude, family, appeal, business, with ORs 0.88, 1.17, 1.12, 1.07, 1.12, 1.08). Column (5): each flagged loan matched to five nearest in length within grade×year (mean 116 vs 114 words). Column (6): indicator restricted to the 583 descriptions coded religious by the language-model coder, with the 98 dictionary matches coded non-religious entered separately. Columns (7)–(8): DoubleML-PLR, CatBoost. Column (8) adds 300-d spaCy word vectors (PCA-50) to the nuisance. With the full 300 dimensions θ = +0.023 (p 0.14), with TF-IDF-SVD100 +0.028 (p 0.059), with doc2vec +0.024 (p 0.11). Repeated cross-fitting (20 sample splits, median aggregation): θ = +0.032 (p 0.031, p < 0.05 in 20/20 splits) with dictionaries, +0.030 (p 0.045, 12/20) with TF-IDF-SVD100, +0.025 (p 0.10, 0/20) with spaCy PCA-50 and +0.024 (p 0.11, 0/20) with doc2vec. Across-split SD of θ is 0.0013–0.0018 in every specification. Religious-term count in place of the indicator (column 3 controls): one term OR 1.14 (p 0.24), two 1.56 (p 0.06), three or more 1.87 (p 0.07), and log(1 + count) 1.37 (p 0.006). Power: with 681 treated loans and a 15.3 percent base rate, the one-sided 5 percent minimum detectable effect at 80 percent power is 3.4 pp. One-sided Holm-adjusted p for H2 (column 3) = 0.008. Fake-dictionary permutation (1,000 random non-religious word sets of matched frequency): actual residualized LPM coefficient 0.035 vs permutation mean −0.003 (SD 0.014), one-sided p = 0.005.

The language-model coding sharpens this. Flagging only the 583 descriptions confirmed as religious gives an odds ratio of 1.34 (p = 0.001), while the 98 descriptions the dictionary flagged but the coder rejected have an odds ratio of 0.95 (p = 0.88). The signal is in the religious content, not in the words. Broken down by type (Appendix Table B1), formulaic invocations such as "God bless" and "prayers answered" carry the effect (1.39, p = 0.001, 467 loans), and identity claims point the same way on too few loans to tell (1.46, n = 34). Descriptions that report religious *practice* (a tithe in the budget, church employment, a mission trip) show no elevated default at all (0.99, n = 82, with a raw rate of 14.6 percent, below the sample average). The cell is small, but it is the cell Section 2 singles out: where the narrative describes faith as something done inside a community rather than something said to a lender, it behaves like the affiliation signal.

The double machine learning estimates are where the narrative result shows its limits, and I report them in full. With the six dictionaries as controls the partially linear estimate is +3.3 points (p = 0.027), and +3.6 on the validated indicator (p = 0.028). However, once the learner is also given a representation of the text itself, the point estimate barely moves but the interval opens. The estimate is +2.8 with a 100-dimensional factorization of term frequency–inverse document frequency (TF-IDF) weights (p = 0.059) and +2.6 with 300-dimensional pretrained word vectors reduced to 50 components (p = 0.09, or 0.06–0.10 across seeds). It is +2.3 with the full 300 dimensions (p = 0.14) and +2.4 with a document-embedding model trained on the corpus (p = 0.11). The sign never changes and the coefficient shrinks by at most a third. Instead, what changes is that 681 treated loans cannot pin down a three-point effect once several hundred text features are conditioned on. I set out in advance that a confidence interval covering zero in this specification would lead me to lower the claim, and I do. The robustness value says the same thing in a different language: 0.0066 at the point estimate and 0.0010 at the 5 percent threshold, so a confounder as strong as employment length would move the estimate to the edge of significance. H2 passes its confirmatory test and every linear placebo, but I present it as a signal whose sign is consistent and whose magnitude is imprecisely estimated, not as a result on the same footing as H1.

Figure 3 plots the nine double machine learning estimates with their intervals: the point estimates move within a narrow band, and what separates the specifications is only whether the lower bound clears zero.

![Figure 3. Religious language and default: double machine learning estimates by text representation. Partially linear DoubleML with CatBoost nuisance functions, 5-fold cross-fitting; "20 splits" aggregates twenty repeated sample splits by the median. Bars are 95% confidence intervals.](fig3_dml.png){width=6.3in}

Two further checks put the imprecision in its place. First, the estimate does not depend on the sample split. Repeating the cross-fitting twenty times gives a median of +3.2 points (p = 0.031) with the dictionary controls, significant at 5 percent in all twenty splits, and +3.0 (p = 0.045) with the TF-IDF representation, significant in twelve of twenty. With the word-vector and document-embedding representations the medians are +2.5 and +2.4 (p = 0.10 and 0.11), significant in none. The spread of the estimate across splits is about 0.002 in every specification, an order of magnitude below its standard error, so the split contributes almost nothing to the imprecision and the downgrade stands. Second, the imprecision is what the sample size implies. With 681 treated loans and a base rate of 15 percent, the smallest effect a one-sided 5-percent test detects with 80 percent power is 3.4 points, and the power to detect the +2.3 to +3.0 points estimated in the text-conditioned specifications is between 50 and 70 percent. A more precise estimate would require more religious descriptions than exist, and the classifier screen of Appendix B found a few dozen outside the dictionary, not thousands. Still, the data can add a gradient. When I replace the indicator with the number of religious terms in the description, the odds ratio is 1.14 for one term (p = 0.24), 1.56 for two (p = 0.06) and 1.87 for three or more (p = 0.07). Within the 681 flagged descriptions more terms mean more default (p = 0.11), and the continuous log-count specification gives 1.37 (p = 0.006). None of this was specified in advance, and I report it as a pattern consistent with the sign of H2 rather than as a test.

Table 6 puts both indicators in the same regression, where religious language has an odds ratio of 1.29 (p = 0.013) and affiliation, on the 372 affiliated borrowers in the description sample, 0.67 (p = 0.041). Same loans, same controls, opposite signs. Neither estimate moves when the other is added.

**Table 6. Both signals in one regression (description sample)**

| | OR | p | N treated |
|---|---:|---:|---:|
| Religious language | 1.293 | 0.013 | 681 |
| Religious-institution affiliation | 0.672 | 0.041 | 372 |

*Notes.* Specification of Table 5 column (3). 20 loans carry both indicators.

## 5.3 Mechanism: the pastor and the secretary

If the affiliation effect came from the vocation (a pastor's vows, a professional identity in which unpaid debt is a scandal), church secretaries and administrators should default like secretaries and administrators elsewhere. Column 4 of Table 2 splits the indicator. Borrowers with a clerical role word have an odds ratio of 0.69 (p < 0.001), and borrowers who name a religious employer without one have an odds ratio of 0.72 (p = 0.023) on 608 loans. Their raw default rate, 11.4 percent, is if anything lower than the clergy's 13.8, and comparing the two groups directly within the affiliated sample shows that they do not differ. What the pastor and the secretary share is not a vocation, an income level (the staff earn less), or a professional code. It is the congregation. The pattern has a parallel in survey data, where Noussair, Trautmann, van de Kuilen and Vellekoop (2013) find that the financial risk aversion associated with church membership appears to stem from the social side of membership rather than from belief.

This also speaks to the job-stability objection more directly than the occupation controls of Section 5.1 do, because a church secretary's pay and tenure look like an office worker's, not like a public employee's. The modest default advantage that teachers and government workers show (odds of default about 10 percent lower) is a third of the advantage that church staff show (about 28 percent lower). Thus, whatever protects the church secretary is not the general stability of institutional jobs.

A last, exploratory split points the same way. Among clergy, senior, lead and executive pastors (497 loans) have an odds ratio of 0.45 (p < 0.001, raw default 8.7 percent), associate, youth and assistant pastors (253 loans) 0.70 (p = 0.08), and the remaining affiliated borrowers 0.74. Standing within the community and the cost of losing it move together — but so do seniority and income, and I cannot separate the two, so this is a pattern rather than a test.

## 5.4 Mechanism: congregation density and labor-market shocks

Table 7 turns to the community itself. When I add adherence rate and congregation density to the full specification, the affiliation odds ratio is 0.686, unchanged to the second decimal, so the individual effect is not local religiosity in disguise. But it varies with it. The interaction of affiliation with congregation density has an odds ratio of 0.84 per standard deviation (p = 0.003). By tercile of local adherence, the affiliation odds ratio is 0.71 in the least religious third of ZIP areas, 0.83 in the middle, and 0.58 in the most religious. The differential survives replacing state fixed effects with 601 ZIP3 fixed effects, which absorb every time-invariant feature of the borrower's area: in a linear probability model with those effects the affiliation coefficient is −5.4 points and the interaction with density is −2.2 points per standard deviation (p = 0.027). If the affiliation signal reflected only a church employee's private character or the steadiness of a church paycheck, there is no reason it should depend on how many other churches stand nearby. If part of it reflects the cost of default inside a community that observes financial conduct, it should. Religious language, by contrast, shows no interaction with local religiosity at all (1.07, p = 0.50), which is what one expects of a message whose meaning does not depend on who is listening. Figure 4 shows the two patterns by quintile. The affiliation odds ratio is 0.85 in the two least dense quintiles of ZIP areas and 0.62 to 0.68 in the three densest, a step rather than a smooth gradient, while the religious-language odds ratio moves between 1.10 and 1.50 across adherence quintiles with no ordering, and only the top quintile's interval excludes one.

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

*Notes.* 2010 U.S. Religion Census county file merged to three-digit ZIP areas via the Census ZCTA–county relationship file, population-weighted (894 areas). Adherents per 1,000 residents and congregations per 10,000, standardized.

![Figure 4. Heterogeneity by local religiosity. Panel A: affiliation odds ratio by quintile of congregation density in the borrower's ZIP3 area, from one logit with affiliation interacted with quintile indicators, full controls and state fixed effects. Panel B: religious-language odds ratio by quintile of the adherence rate, description-sample specification of Table 5, column 3. Bars are 95% confidence intervals; n is the number of treated loans in the quintile.](fig4_density.png){width=6.3in}

Table 8 tests the income-stability alternative from the other side. Local unemployment is associated with default as one would expect (a one-SD higher rate at origination with 9.5 percent higher odds, a one-SD larger rise over the loan's life with 3.2 percent higher odds). But the affiliation advantage does not widen when unemployment rises (interaction odds ratio 0.98, p = 0.69, indistinguishable from one) or when it is high (0.95, p = 0.38), and it is not monotone across shock terciles (0.58, 0.74, 0.70). I would not lean on this too hard. The sample period is mostly a recovery, the average "shock" is a fall in unemployment, and when I run the same interaction for teachers and government employees as a positive control, their advantage does not widen either (1.04 with p = 0.08 and 1.01 with p = 0.71). My reading is that the shocks in these years are too small to reveal an income-stability mechanism for any occupation, so the test cannot reject it. What it can say is that the affiliation effect is not visibly a shock-absorption effect, while it is visibly a community-density effect. One further reading is consistent with both facts: religious organizations insure their members' consumption against income shocks (Dehejia, DeLeire and Luttmer, 2007), so an affiliated borrower who loses income may be cushioned before the loan is, in which case local unemployment would not have to widen the gap. In the Indonesian financial crisis, households under distress intensified their religious participation and religious institutions helped smooth their consumption (Chen, 2010), but shared ties can also spread default rather than absorb it. In Indian microfinance after demonetization, defaults spread through borrowers' informal ties, and somewhat more strongly among borrowers of the same religion (Adbi, Lee and Singh, 2024), and this is another reason the shock interaction was worth testing and is worth reporting as flat.

**Table 8. Affiliation and local unemployment shocks**

| | OR | p |
|---|---:|---:|
| Affiliation | 0.667 | <0.001 |
| Unemployment rate at origination (per SD) | 1.095 | <0.001 |
| Rise in unemployment over loan life (per SD) | 1.032 | 0.001 |
| Affiliation × rise | 0.983 | 0.69 |
| Affiliation × level | 0.950 | 0.38 |
| Affiliation by shock tercile (small / mid / large) | 0.577 / 0.741 / 0.701 | all <0.001 |
| Positive control: teacher × rise; government × rise | 1.035; 1.009 | 0.08; 0.71 |

*Notes.* BLS LAUS county annual unemployment 2008–2018, ZIP3 population-weighted. "Rise" = maximum unemployment rate in years after origination within term, minus rate at origination (mean −0.62 pp, SD 0.55). The sample period is mostly a recovery, so adverse-shock variation is limited. N = 239,215 (2,997 affiliated after the merge). The affiliation regex here differs trivially from Table 2, which is why the main-effect OR is 0.667 rather than 0.692.

## 5.5 Individual religion and local religion

The religiosity literature in finance is almost entirely about places, and it is worth asking whether my signals are the same thing seen from closer up. They are not. In that literature a more religious surrounding is a favorable one. Firms in more religious counties borrow at lower spreads (He and Hu, 2016; Chen et al., 2016) and with fewer covenants (He and Hu, 2016), credit unions there lend more cheaply and hold better loans (Davidson, Ngo and Wang, 2026), and county adherence predicts lower mortgage delinquency (Li and Ucar, 2022). However, in this market local religiosity does nothing of the kind, and within state, borrowers from more religious ZIP3 areas default slightly *more* (Table 7), with odds ratios of 1.04 per standard deviation of adherence and 1.06 per standard deviation of congregation density. The evangelical share is unrelated to default. I cannot explain the positive association and do not try to. The settings differ, since those studies concern firms, institutions or mortgages and mine concerns individuals who sought unsecured credit online, and the within-state residual variation in religiosity is also correlated with income and urbanicity in ways that state fixed effects and my income control may not fully absorb. I flag it as a contrast with the county literature rather than as contradicting it. The sign of an area's religious makeup is not fixed even in that literature, since Hasan, Kiesel and Noth (2025) find less household over-indebtedness in German regions where Catholics outnumber Protestants. The split between an individual effect and a null regional one has parallels elsewhere. In repayment games played in South Africa and Armenia, Cassar, Crowley and Wydick (2007) find that personal trust among group members matters for repayment where generalized trust does not. In German regions, Traunmüller (2011) finds that individual church attendance predicts trust while regional devoutness shows no detectable contextual effect. What the contrast makes clear is that whatever protects the affiliated borrower is not a property of religious places. It is a property of belonging to a religious institution, and it is amplified by the density of such institutions rather than replaced by it: the affiliation odds ratio is 0.71 in the least religious tercile of areas, 0.83 in the middle and 0.58 in the most religious (Appendix Table A2). A religious environment, on this evidence, is not itself a borrower-level credit signal, but the value of an individual's affiliation depends on the community around it.

## 5.6 Timing (Appendix A)

A discrete-time hazard on loan-month panels, with default dated four months after the last payment, puts the affiliation hazard ratio at 0.69 and shows it flat over the life of the loan (0.69 in the first twelve months, 0.68 afterward). Religious language has no effect on hazard in the first year (0.96, p = 0.85) and its effect appears only later (1.27, p = 0.027). If religious language merely marked immediate distress one would expect the opposite, but I treat this as suggestive, since the default date is approximate and the comparison groups are subsampled. Figure 5 shows the same timing without a model. Among 36-month loans, cumulative default of affiliated borrowers runs below that of other borrowers from the first year (2.1 against 3.6 percent at twelve months, 9.5 against 14.1 at maturity). The curve for religious language, by contrast, tracks the comparison group for the first year (3.0 against 2.8 percent) and separates afterward (17.4 against 12.6 at maturity).

![Figure 5. Cumulative default by months since origination, 36-month loans. Default is dated four months after the last payment. Comparison groups are reweighted to the treated group's grade × origination-year distribution. Panel A: 2,398 affiliated loans in the terminal sample; Panel B: 507 religious-language loans in the description sample.](fig5_cumdefault.png){width=6.3in}

# 6. Discussion

## 6.1 How much is it worth

Neither signal is priced. LendingClub set interest rates by sub-grade and date, so two loans in the same sub-grade in the same month carried the same rate whatever the job title or the description said. Against loans in the same sub-grade-year cell, affiliated borrowers defaulted at 13.3 rather than 17.4 percent and lost 5.5 rather than 7.7 cents per dollar funded, a gap of 2.2 cents over an average 41-month life, or roughly 64 basis points a year of yield an investor holding those loans earned above the cell. Loans with religious language went the other way: 20.0 against 15.9 percent default, 7.1 against 6.1 cents lost, about 28 basis points a year below the cell. These are not large numbers, and I do not claim an investor could have traded on them, since the signals flag a fraction of one percent of loans. Still, they are the size of what the market left on the table, stated in the units the market uses, and that it was left there is itself informative. On Prosper, where investors bid on rates, unverifiable disclosures were associated with lower rates (Michels, 2012) and text was priced, if not fully (Gao, Lin and Sias, 2023), and in corporate debt a firm's county religiosity earns a lower spread (Jiang, John, Li and Qian, 2018). LendingClub's grade-based pricing used none of this. Where its terms did draw out private information, it was through the loan menu rather than the application: Hertzberg, Liberman and Paravisini (2018) find that borrowers with higher unobserved default risk select the higher-rate long-maturity loan.

## 6.2 After default

The same contrast appears, more faintly, in what borrowers do after they stop paying. Among the 268,599 charged-off loans, affiliated borrowers made at least one recovery payment 74.6 percent of the time against 68.7 percent for others, and recovered 8.4 rather than 7.5 cents per dollar, and with controls the recovery rates differ by 0.9 cents (p = 0.057). Borrowers who had used religious language recovered less (6.3 against 7.1 cents). I report this as a pattern, not a test, because the affiliated and religious-language recovery samples are small and I did not pre-specify the analysis. Yet it is what one would expect if belonging carries an obligation that outlasts the platform's collection efforts, and professing does not.

## 6.3 What investors did

LendingClub's public file does not record how quickly a listing filled or how many investors joined it, and by 2012 most loans were funded in full by design. What can be measured is the share of the loan funded by investors rather than the platform, whether it was fully investor-funded, and the ratio of funded to requested amount. None of these is associated with religious language once length and the text dictionaries are controlled (all p > 0.4). These data cannot answer the investor side of the question, and I leave it there. On Kiva, where funding speed is observed, Anglin, Milanov and Short (2023) find that religious expression in a request slows funding, particularly for women, and in an accompanying online experiment that the penalty is smaller among more religious lenders. Whether an audience wants to hear faith invoked therefore depends on who that audience is, and the LendingClub file does not say who its investors were.

## 6.4 Limits

This is an observational study of one platform's borrowers, most of whom are American and, where religion is visible, Christian. There is no instrument for working in a church and no natural experiment that moves people into or out of one, and the public file has no borrower identifier, so a within-borrower design that follows the same person across an occupational change is not available (the member identifier is empty for every loan). In addition, the platform does not record age, education, marital status or household structure, on any of which church employees may differ from other borrowers. Nor does it record the longer planning horizon and greater trust that religious households report, or the thrift reported by Catholic households in particular (Renneboog and Spaenjers, 2012), which could lower default without any community watching. The affiliation indicator comes from a free-text job title and certainly misses affiliated borrowers who described their job differently, which biases the estimate toward zero, not away from it. The description sample ends in 2014 because the platform stopped collecting descriptions, and religious language is rare enough that the narrative estimate is imprecise in the strictest specifications. The evidence on mechanism is consistent with a community-based account and difficult to reconcile with the observable labor-market accounts I can test — pay, tenure, the generic stability of institutional jobs, and the jobs nearest to church work — but it does not identify the mechanism causally. The labor-market test also has too little adverse variation in these years to settle the income-stability question. What the paper establishes is narrower than a mechanism: that two observable traces of religion carry opposite credit information, that the favorable one is tied to the community rather than the vocation and grows as the community becomes denser, and that the market did not price either.

A reader who comes to this from the study of religion rather than of credit may notice that the distinction the data draw — between faith professed and faith belonged to — is an old one in religious thought, and that the direction of the finding is the one that tradition would predict. I note it and leave it there; the data cannot speak to the theology, only to the ledger.

# 7. Conclusion

In an online consumer-credit market, borrowers who belong to a religious institution default less than observably identical borrowers, and borrowers who profess faith in their loan request default more. The first effect is large, stable over a decade, present for church staff as much as for clergy, stronger where congregations are denser, insensitive to local unemployment, and reproduced on a second platform. The second is consistent in sign but imprecisely estimated once the full text is accounted for. Neither is priced. The evidence is most naturally read as religious community functioning as borrower-side social collateral, and religious language as a low-cost signal that is informative in spite of, not because of, what it says.

Two implications follow. The first concerns how a lender reads religion in a credit file. The same subject carries opposite information depending on whether it arrives as a tie or as a statement, so a model that treated religion as a single variable would average two signals of opposite sign. The second concerns where social collateral is found. Group-lending schemes build a community around the loan, whereas the borrowers I study reported theirs in a job title. Other affiliations that a credit file records only in passing, such as a cooperative or a union local, are natural places to look for the same pattern. For lenders the practical content is modest — these are rare signals — but the conceptual content is not: what a credit market can learn from religion is not what a borrower says about it but where the borrower stands within it.

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

**Appendix Table B1. Language-model coding of religious-language descriptions**

| Type | N | Default rate (raw) | OR (full controls) | p |
|---|---:|---:|---:|---:|
| a. Formulaic ("God bless", "prayers answered") | 467 | 0.221 | 1.385 | 0.001 |
| b. Identity / value claim | 34 | 0.206 | 1.460 | 0.32 |
| c. Practice / expense (tithe, church employment, mission) | 82 | 0.146 | 0.988 | 0.97 |
| x. Non-religious match (dictionary false positive) | 98 | 0.143 | 0.948 | 0.88 |

*Notes.* Primary coding by an LLM coder over all 820 flagged records (717 with description text, 103 title-only) against the codebook in Appendix B2. Independent recoding of a stratified 200-record sample by a second LLM coder of a different model family gives κ = 0.86 for type (raw agreement 91%), 0.81 for religious vs non-religious, 0.73 for frame. Measurement completeness: a classifier trained with all explicit religious words masked (CV AUC 0.92) ranked the 122,611 unflagged descriptions, and the LLM coder found 0 religious descriptions among 117 sampled from the top 2,000, 3 among 240 further down, and 11 among 77 implicit-phrase matches ("godsend", "karma", "higher power").

**Appendix Table B2. Audit of the affiliation indicator (200 randomly drawn affiliated job titles)**

| Code | N | Examples |
|---|---:|---|
| A. Religious institution, clerical role | 146 | Pastor, Senior Pastor, Minister, Chaplain, Priest, Worship Leader |
| B. Religious institution, non-clerical staff | 48 | Director of Music Ministry, Parish Business Manager, "St. Thomas Episcopal Church", "Indianapolis Hebrew Congregation" |
| C. Not religious employment | 2 | "East Baton Rouge Parish Sheriff's Office", "Ouachita Parish Sheriff's Office" (Louisiana civil parishes) |
| D. Cannot classify from title | 4 | "Church and Stagg", "Pastor/Soccer Club Director", "Parish Manager" |

*Notes.* Precision 97 percent (98 percent counting D as half). A rule targeting civil-parish titles (parish + sheriff, library, government, assessor, police jury, court, etc.) identifies 30 such loans in the terminal sample, all in Louisiana, with a raw default rate of 30 percent. Excluding them gives an affiliation odds ratio of 0.683 (SE 0.041) in the Table 2, column 1 specification.

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

**Appendix Table C3. Alternative standard errors for the two confirmatory estimates**

| Clustering | H1: affiliation, SE (p) | H2: religious language, SE (p) |
|---|---:|---:|
| State (51 clusters; reported) | 0.041 (<0.001) | 0.103 (0.016) |
| ZIP3 area (892 clusters) | 0.054 (<0.001) | 0.100 (0.013) |
| Month of origination (138 clusters) | 0.050 (<0.001) | 0.092 (0.007) |
| Heteroskedasticity-robust, no clustering | 0.054 (<0.001) | 0.101 (0.014) |

*Notes.* Standard errors of the log-odds coefficient in the Table 2, column 1 and Table 5, column 3 specifications (coefficients −0.368 and +0.247).
