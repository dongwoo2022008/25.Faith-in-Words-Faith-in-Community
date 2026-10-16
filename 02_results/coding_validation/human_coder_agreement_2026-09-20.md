# Human-coder validation (20 September 2026)

The author (one human coder) coded the 200-record LendingClub validation sample by the codebook and the result was compared with the primary LLM coding. (The same exercise was run on a 100-record sample from a Korean platform during the feasibility stage; that platform is not used in the paper and its records were removed from this repository.)

| Sample | n | Type (4 classes) κ | Raw agreement | Religious vs not κ | Raw agreement | Frame κ |
|---|---:|---:|---:|---:|---:|---:|
| LC_200 | 200 | 0.719 | 81.5% | 0.553 | 84.5% | 0.481 |

LC 200 cross-tabulation (rows LLM, columns human): a 88/2/1/9, b 2/10/0/8, c 0/1/36/3, x 8/0/3/29.
Religious vs not: LLM religious and human not religious 20 records; LLM not religious and human religious 11.

Reading
- Lower than LLM vs LLM (κ 0.86 / 0.81). Raw agreement on the religious/not binary is high (84.5%), but 80% of the sample is religious, so κ falls to 0.55 (prevalence-adjusted κ 0.69).
- Disagreements cluster at the boundaries (formulaic a vs not religious x; identity claim b vs formulaic a).
- Against the design note's κ ≥ 0.7 rule: met for the four-class type (0.86 LLM–LLM, 0.72 human–LLM); not met for the human–LLM religious/not binary (0.55; 0.69 prevalence-adjusted) or for frame (0.48). Frame enters no estimate; the binary enters Table 8, which Appendix B1 reports with this caveat.

Manuscript
- Section 3.2 reports both the second-LLM check and the human check as robustness checks, not as a better measurement; the type breakdown is treated as the most uncertain result.
- Appendix Table B1 notes carry the human κ values and the disagreement counts (11, 20).
- The confirmatory test uses the dictionary indicator fixed in the design note, so the main results do not depend on the coding.
