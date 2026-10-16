# Raw data

The two raw loan files are not in the repository because of their size. Both are public Kaggle datasets; the author downloaded them in June 2026.

| File | Source | Size | Used by |
|---|---|---|---|
| accepted_2007_to_2018Q4.csv.gz | Kaggle, "All Lending Club loan data" (https://www.kaggle.com/datasets/wordsforthewise/lending-club), 2018Q4 release: 2,260,701 loans issued June 2007–December 2018 | 392 MB | 03_code/preprocessing_exploration/lc_extract.py, 03_code/analysis/rebuild_TD.py, verify_*.py |
| prosperLoanData.csv | Kaggle distribution of the Prosper loan file originally released with the Udacity data-analysis course: 113,937 listings, 2005–2014 [author: insert the Kaggle dataset page used] | 86 MB | 03_code/analysis/step7a.py |

The LendingClub data dictionary (LCDataDictionary.xlsx) ships with the Kaggle dataset and is not copied here. The external files used in Sections 3.4 and 5.5 (2010 U.S. Religion Census county file from the Association of Religion Data Archives, the Census Bureau's 2010 ZCTA–county relationship file, and BLS Local Area Unemployment Statistics county annual unemployment 2008–2018) are likewise public and are kept on the author's Drive copy of this package. No raw file is redistributed here; check each source's license before redistributing.
