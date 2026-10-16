# Human-coder agreement for the 200-record LendingClub validation sample. Run after the human coder has filled the
# validation workbook (Drive copy, sheet LC_200; frame labels there are Korean: 종교=religious, 도덕=moral, 곤경=hardship): python kappa_after_human_coding.py
# The primary LLM labels for the same records are 02_results/coding_validation/validation_sample_LC_answer_key.csv.
import pandas as pd
from sklearn.metrics import cohen_kappa_score
h=pd.read_excel("사람코더_검증표본_300건.xlsx",sheet_name="LC_200"); k=pd.read_csv("validation_sample_LC_answer_key.csv")
h['loan_id']=h['loan_id'].astype(str); k['loan_id']=k['loan_id'].astype(str)
m=k.merge(h[['loan_id','type','frame']],on='loan_id',suffixes=('_ai','_human')).dropna(subset=['type_human'])
print("LC_200 n coded", len(m), "kappa type", round(cohen_kappa_score(m.type_ai,m.type_human),3),
      "kappa religious vs not", round(cohen_kappa_score(m.type_ai!='x', m.type_human!='x'),3),
      "kappa frame", round(cohen_kappa_score(m.frame_ai,m.frame_human.fillna('religious')),3))
print(pd.crosstab(m.type_ai,m.type_human))
