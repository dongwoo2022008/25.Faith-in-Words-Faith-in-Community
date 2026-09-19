# Faith in Words, Faith in Community
### Religious Affiliation, Religious Language, and Default in Online Consumer Credit

Working repository for the paper (target journal: *Journal of Economic Behavior & Organization*). Author: Dongwoo Kim, Division of Advanced IT, Baekseok University. Current manuscript: `01_manuscript/manuscript_v9_JEBO_2026-09-19.md` (draft v9, 19 September 2026, 25 pages in the Word/PDF build).

## Layout

| Folder | Contents |
|---|---|
| `01_manuscript/` | Manuscript v9 (Markdown source; the .docx/.pdf builds and the five 300-dpi figures live on the Google Drive copy), `previous_versions/` v1–v6 and section drafts, Zotero records for the paper (`.ris`, `.bib`) |
| `02_results/` | `tables_csv/` raw numbers behind the tables, `estimates_json/` output of each analysis step, `coding_validation/` LLM coding results, inter-AI reliability, human-coder validation sample, affiliation-indicator precision audit (200 titles), codebooks; `run_log_2026-09-18.md` (work log, rounds 1–10), methodology summary, paper summary for evaluation |
| `03_code/` | `analysis/` step scripts that produce every table and figure, `preprocessing_exploration/` raw data → pickles and early exploration, `manuscript_build/` Markdown → docx/pdf build and self-check scripts |
| `04_data/` | `raw/` LendingClub and Prosper loan data (not in the repository: see `raw/raw_data_location.md`), `external/` ARDA 2010 U.S. Religion Census (county), Census ZCTA–county relationship file, BLS LAUS county unemployment 2008–2018 |
| `05_literature/` | Literature notes, snowball citation-chain review, writing benchmark notes, Zotero RIS with the manuscript's 74 references (benchmark PDFs are on the Drive copy) |
| `06_planning_docs/` | Research question, work order, framing decision, first-pass analysis, progress notes |

## Reproduction

1. `03_code/preprocessing_exploration/lc_extract.py` → `lc_final.pkl` (terminated LendingClub loans, cleaned variables)
2. `03_code/analysis/step1.py` → `T.pkl` (terminal sample), `D.pkl` (description sample), religious indicators and text dictionaries
3. `step2.py` (H1 baseline, Table 2), `step3.py` (stable occupations and CEM, Table 2 Panel B), `step3b_fakedict.py` (placebo dictionaries), `step4*.py` (H2 double machine learning, Table 5 and Figure 3), `step5c.py` (entropy balancing), `step6.py` (discrete-time hazard, Appendix A1), `step7a.py` (Prosper replication, Table 4), `step7b.py` (investor response), `stepA_arda.py` and `stepU_unemp.py` (local religiosity and unemployment, Tables 7–8), `stepN_neighbor.py` (neighbor occupations), `stepID2.py` (Oster and Cinelli–Hazlett, Table 3), `stepG_extras.py` (selection into writing a description, alternative clustering, Appendix C), `stepH_precision.py` (indicator precision, Louisiana civil parishes), `stepF_figures.py` (Figures 2–5)
4. `03_code/manuscript_build/build_v9.py` → docx/pdf (pandoc, python-docx, LibreOffice)

Paths inside the scripts refer to the container they were run in (`/mnt/user-data/uploads/...`, `out/`); point them at `04_data/` before running. Random seeds are fixed in each script (`random_state=1`, `5`, etc.).

## What is not in the repository

Raw loan data (392 MB and 86 MB) exceed GitHub's file-size limit, and binary deliverables (docx, pdf, png, xlsx, zip) and the two large coding-result CSVs could not be pushed from the session that created this repository. All of them are in the Google Drive folder `논문.김동우/Under.writing/25.Faith in Words, Faith in Community`, which mirrors this layout with Korean folder names.
