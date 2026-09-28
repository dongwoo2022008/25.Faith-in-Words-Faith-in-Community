# Codebook: religious expression in LendingClub loan descriptions

This is the codebook reported in Appendix B of "Faith in Words, Faith in Community". It is the English-only version of the working codebook used for the September 2026 coding (`work/coding/CODEBOOK.md`), which also carried Korean examples for a Popfunding sample that the paper does not use. Definitions, examples, the precedence rule and the blinding rule are unchanged.

For each flagged record, assign exactly one TYPE and one FRAME.

## TYPE: what kind of religious expression is it?

- **a, formulaic.** Religious words used as a greeting, closing or idiom that makes no claim about the writer. Examples: "Thank you and God bless", "God willing", "prayers answered", a title such as "God is good".
- **b, identity or value claim.** The writer asserts his or her own faith, religious identity, or a religious or moral value as a reason to trust them. Examples: "as a Christian I believe in paying my debts", "I have strong faith in God".
- **c, practice or expense.** A concrete religious activity or outlay: tithes or offerings in a budget, church employment, a mission trip, seminary tuition, a church building project, pastor as occupation.
- **x, not religious.** The matched word is used in a non-religious sense. Examples: "Lord & Taylor", "landlord", "heaven forbid", "good faith". A mention of someone else's religion (a wedding officiant, a relative's church) is x unless the writer's own faith or practice is involved.

If more than one type applies, choose the strongest in the order c > b > a (practice beats identity, identity beats formula).

## FRAME: what accompanies the religious content in the same description?

- **religious only.** No moral self-presentation and no hardship narrative.
- **moral.** Accompanied by honesty, promise, responsibility or reliability claims ("I always pay on time", "I promise", "I take my obligations seriously").
- **hardship.** Accompanied by a hardship narrative (job loss, illness, divorce, medical bills, arrears).
- **moral/hardship.** Both.

Code FRAME independently of TYPE.

## Procedure

Output one JSON object per record: `{"id": "...", "type": "a|b|c|x", "frame": "religious|moral|hardship|moral/hardship", "note": "<=12 words, optional"}`. Code every record. Do not skip. Do not look at, or infer from, any prior automatic label.
