# Cold read as a first-time JEBO referee (body text only; tables, notes, references and appendix excluded)

Status: **FIXED** = applied in v10 (meaning-preserving). **LEFT** = left for the author, with the reason.

## Fixed (22)

| # | Location | Snippet (v9) | Problem | Fix applied |
|---|---|---|---|---|
| 1 | §1 ¶1 | "125,811 loan descriptions filed between 2008 and 2014" | Doesn't match §3.1: 125,811 is the all-years total, and 125,761 fall in 2007–2014 | "…descriptions, almost all filed between 2008 and 2014" |
| 2 | §1 ¶3 to ¶4 | "That last set of facts is what moves the paper" | Unclear referent: literature sentences sit between the list and this sentence | Literature sentences moved to lit-3. Opener now reads "The evidence within the affiliated group…" |
| 3 | §1 ¶4 | "denser in the borrower's ZIP area" | "ZIP area" is undefined at first use (it means ZIP3) | "three-digit ZIP area" |
| 4 | §1 limits | "about twelve times as strong as employment tenure" | Term doesn't match Table 3 and §5.1 ("employment length") | "employment length". The 59-word sentence was also split |
| 5 | §1 ¶7 | "The paper therefore adds three things…" | Repeats the end of the preceding literature paragraph almost verbatim | Paragraph deleted. Its one new point moved to lit-1 |
| 6 | §1 roadmap | "the two main tests, the mechanism evidence, …, and the replication" | Order is wrong (Prosper is in §5.1). §5.6 timing and §6.3 investors are missing | Roadmap now matches the section order |
| 7 | §2.1 ¶1 | (≈480-word paragraph) | Too long to hold: microfinance evidence and consumer-credit evidence run together | Split at "The insight travels beyond microfinance." |
| 8 | §2.1 | "trustworthiness revealed in a trust game predicts repayment while trust revealed…" | Needs a second read (trustworthy vs trusting) | Rephrased. Logged in changed_citation_sentences.md |
| 9 | §2.2 | "Two facts about religious people bear on this." | Only the first fact is about religious people. The second is about lending | "Two findings bear on this, one about religious people and one about lending." |
| 10 | §2.2 | "two mechanisms make its expected sign positive" | "sign" of what? | "expected association with default positive" |
| 11 | §2.2 last ¶ | "If what makes a religious signal informative is… then…" (60 words) | Needs a second read | Split into two sentences |
| 12 | §2.2 end | "I test each one-sided with a Holm correction … and stated in advance" | Tense clash, run-on | Split into two sentences, "and I stated" |
| 13 | §3.1 | "debt-to-income ratio … missing DTI" | DTI is never defined | "debt-to-income ratio (DTI)" |
| 14 | §3.2 | "the 583 loans coded a, b or c" | The letters a/b/c are never defined in the text (only in Appendix B1) | "coded as formulaic, identity or practice" |
| 15 | §3.2 / §3.3 | "κ = 0.86"; "0.92 per log-word" | κ type unstated. "log-word" is an odd unit | "Cohen's κ"; "per log point of length" |
| 16 | §3.4 | "ZCTA-to-county relationship file … each ZIP3 area"; "BLS" | ZCTA, ZIP3 and BLS are undefined. The sentence runs to 59 words | Spelled out. Split into two sentences. Logged |
| 17 | §4 | "the controls listed above" | No controls are listed above (they first appear in the Table 2 notes) | "the credit and loan variables described in the data section" |
| 18 | §4 | "CatBoost nuisance functions"; "moves the AUC" | CatBoost and AUC are undefined | "CatBoost gradient-boosted trees as nuisance functions"; "area under the ROC curve (AUC)" |
| 19 | §5.1 | "Prosper replicates it (Table 4)." | "it" follows a paragraph on other occupations | "replicates the affiliation result" |
| 20 | §5.2 | "+2.8 with a 100-dimensional TF-IDF factorization…" (69 words) | TF-IDF undefined, and the list is too long for one sentence | Defined, and split into three sentences |
| 21 | §5.3 | "(about 10 percent) is a third of … (about 28 percent)" | Unclear whether these are odds or rates | "odds of default about 10 percent lower … about 28 percent lower" |
| 22 | §5.4 / §5.5 / §6.2 | "the opposite possibility also exists"; "I cannot explain it"; "the recovery sample is small" | Vague referent. "it" points to the evangelical null instead of the positive association. The recovery sample (268,599) is not small: the treated subsamples are | "shared ties can also spread default rather than absorb it"; "the positive association"; "the affiliated and religious-language recovery samples are small". The 64-word Cassar/Traunmüller sentence in §5.5 was also split |

## Left for the author (9)

| # | Location | Snippet (v10) | Problem | Suggested fix / reason left |
|---|---|---|---|---|
| L1 | §1 lit-3 | "Religious language, it turns out, mostly proxies" | Doesn't match the numbers. Text dictionaries leave the OR unchanged (1.27 to 1.28, Table 5 cols 1–3), and full-text DML shrinks the effect "by at most a third" (§5.2). "Mostly" implies more than half | "partly proxies". This changes the substantive claim, so it is not applied |
| L2 | §4 | "identifies the mechanism through heterogeneity in the manner of Rajan and Zingales (1998)" | Contradicts §6.4 ("does not identify the mechanism causally") | "tests the mechanism through heterogeneity". This weakens a claim, so it is not applied |
| L3 | §3.2, §5.2, Table 5 col 6, App. B | "coded by a reader", "reader coding", "readers rejected" | The coding was done by an LLM and checked by a second LLM (§3.2, B1 notes). "Reader" reads as human coders. The B2 audit coder is unspecified | Use "codebook-validated"/"LLM-coded" consistently, and state who coded B2. This touches table labels, which are frozen |
| L4 | §2.1, §3.2 vs elsewhere | "did not pre-register", "pre-registered test" vs "pre-specified" | Referees will ask for the registry, date and plan | Either cite the registration (registry, ID, date) or use "pre-specified" throughout |
| L5 | §5.5 | "Firms in more religious counties borrow at lower spreads (He and Hu, 2016; …)" | Repeats the intro lit-2 sentences almost word for word | Shorten one occurrence. Not applied because citation multisets are frozen |
| L6 | §5.5 | "0.71 … 0.83 … 0.58 (Appendix Table A2)" | Repeats the tercile ORs from §5.4. Table A2 sits under "Appendix A. Timing" | Keep the numbers in one place. Move A2 to Appendix C or retitle Appendix A (appendix is frozen) |
| L7 | §5.2 | "the +2.3 to +3.1 points estimated in the text-conditioned specifications" | The text-conditioned estimates reported are +2.3 to +3.0. +3.1 is the length-decile logit AME (col 4) | Check the upper bound of the power calculation. The number is not changed here |
| L8 | §3.4 | "the latest wave of the county membership surveys" | A 2020 U.S. Religion Census has been released, so "latest" is inaccurate | "the wave closest to the sample period". This is a factual claim tied to a citation, so it is left |
| L9 | §2.1 ¶3 | "Religious attitudes toward cooperation and thrift … (Guiso, Sapienza and Zingales, 2003)" | Repeats intro lit-1 (same two citations, same facts) | Shorten in one place. Frozen citation multiset |

**Counts:** 22 issues fixed, 9 left for the author (31 total).
