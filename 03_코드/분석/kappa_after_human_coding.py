# 사람 코더가 '사람코더_검증표본_300건.xlsx'를 채운 뒤 실행: python kappa_after_human_coding.py
import pandas as pd
from sklearn.metrics import cohen_kappa_score
for sheet,key,idc in [("LC_200","검증표본_LC_정답키.csv","loan_id"),("PF_100","검증표본_PF_정답키.csv","listing_id")]:
    h=pd.read_excel("사람코더_검증표본_300건.xlsx",sheet_name=sheet); k=pd.read_csv(key)
    h[idc]=h[idc].astype(str); k[idc]=k[idc].astype(str); m=k.merge(h[[idc,'type','frame']],on=idc,suffixes=('_ai','_human')).dropna(subset=['type_human'])
    print(sheet, "n coded", len(m), "kappa type", round(cohen_kappa_score(m.type_ai,m.type_human),3), "kappa frame", round(cohen_kappa_score(m.frame_ai,m.frame_human.fillna('종교')),3))
    print(pd.crosstab(m.type_ai,m.type_human))
