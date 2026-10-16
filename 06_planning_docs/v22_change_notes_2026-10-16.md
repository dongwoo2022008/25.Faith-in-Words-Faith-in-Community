# v22 수정내역 (2026-10-16) — 6차 검토 회신 반영

기준: v21 → v22. apply_v22.py(21개 치환). 30쪽, selfcheck 통과, 16·17쪽(Table 10·11, Figure 4) 렌더링 확인. 모든 수치는 재구축 T.pkl/D.pkl(rebuild_TD.py)과 저장된 JSON으로 재확인.

## 검토 결과의 처리
- 125,811 / 125,812: 저장소의 default_and_descriptions_by_year.csv는 이미 v21 작업(커밋 933714b)에서 보일러플레이트 제거 후 집계로 바뀌어 합계 125,811(2007–2014: 125,761)이고, 제거 전 수치 125,812는 별도 열(with_description_raw)로 병기되어 있음. 검토자가 본 것은 그 이전 파일. 원고 수정 없음.
- 추적되지 않던 기술통계: make_table1.py(03_code/analysis)를 추가해 descriptive_statistics.json·descriptive_statistics_table1.csv 산출. Table 1 전 열, 3.3절 중앙값 68/23·평균 116/36·사전 비율 6쌍, 3.2절 5,014·784·372·681·20, 5.4절 기관명 건수, Table 11 N, Table 5 원 부도율 22.7/30.5를 담음.
  - 그 결과 Table 1 반올림 4곳 정정: 소속 FICO 704.0 → 703.9(703.947), 금액 14,826 → 14,827(14,826.76), A–B 비율 0.571 → 0.570(0.5704), 교회 직원 부도율 0.114 → 0.113(69/608 = 0.1135). 5.4절 본문과 Table 10의 11.4 → 11.3.
  - Table 11 N(253,038 / 123,260): 재구성은 253,040 / 123,261(ZCTA–county 파일의 894개 ZIP3 기준). 원 추정 표본의 N을 유지하고 JSON에 차이를 기록.
  - 기관명 건수 606: 당시 규칙이 남아 있지 않아 재현 불가. 규칙을 문서화한 재구성(조직어 + 일반어가 아닌 토큰 1개 이상)은 583건(고유 문자열 497, 반복 46)이므로 원고를 583으로 바꿈. 반복 이름 상위는 동일(first baptist church 18, united methodist church 8).
  - Table 10 탐색 행(497/253/2,355, OR 0.452/0.696/0.743): 분실된 스크립트의 결과. 단어 목록 조합을 모두 시도해도 건수가 재현되지 않아(가장 가까운 것 509/235) run_v22_hierarchy.py로 규칙을 명시해 재추정: associate/assoc/youth/assistant/asst 우선, 그다음 senior/sr/lead/executive, 나머지 — 509건 OR 0.459(p < 0.001), 235건 0.636(p 0.050), 2,361건 0.751(p < 0.001). 본문 문장·표·주석을 새 수치로 교체. 결론(지위가 높을수록 효과가 큼, 탐색)은 유지.
  - Table 3 Panel A CEM 행의 "(1,746 cells)"는 실행 로그에만 있어 삭제(매칭 건수 3,008/58,032는 stepR_review_extras.json에 있음). Panel B의 2,234셀은 stepN_neighbour.json에 있어 유지.
- README C6 매핑: C6 → stepR2a.py의 T8 블록으로 수정. stepU_unemp.json에는 superseded 주석(_note) 추가(소속 0.667, 3분위 0.577/0.741/0.701, 교사×변화 1.035는 다른 지표·표본의 이전 실행).
- stepID_identification.json의 within_institution(2,363/768)에 옛 분류 규칙임을 알리는 _note 추가; paper_summary·methodology_summary의 3,131건은 README의 02_results 항목에 같은 취지의 설명을 적음(두 문서는 9월 18일 스냅샷으로 그대로 둠).
- lc_two_signal_analysis_results.json의 _note: "2026-09-17" → 9월 5일 실행(원본 lc_results.json 저장 시각 2026-09-05 08:43 UTC, 내용 동일, 9월 5일 문서의 수치)으로 정정.
- Table 5 주석: 성직 OR 0.684는 플라시보 없는 모형, 플라시보 3행은 4개 직업 동시 투입 모형(그 모형의 성직 OR 0.686, p 0.039)에서 왔음을 명시(step7a_prosper.json).

## 본문 정정·교정
- 4.1절: 설계 노트에 인접 직업군 비교와 기간 분할이 없음을 확인(작업지시서 2026-09-17 전문 대조). "most of the robustness checks of Section 4.2 … the split by period is not in the note, and the neighbor-occupation comparison was added after the confirmatory estimates"로 수정. 9월 5일 문서에 기간 분할·플라시보·길이 매칭·AUC가 있음을 확인해 "preliminary versions of both estimates and several of the checks"로 수정.
- 1절: "about one in four hundred" → "roughly one in 450"(3,105/1,344,976 = 1/433, 5,014/2,260,701 = 1/451). 둘째 문단의 LendingClub 반복 5회 → 2회("The same file", "The platform also asked", "because loans were priced by grade"; 원고 전체 17 → 14회). "which, by a rule … were run, lowers the claim" 쉼표.
- 2.1절: "how closely the community observes its members"; 단수 대명사 혼용을 피하려 주어를 복수로("Borrowers who work for a church are embedded …").
- 3.3절: "(0.88, and 0.92 per log point of length)".
- 5.1절: "Exact matching" → "Coarsened exact matching".
- Table 11 헤더 "Affiliation OR" → "Main-effect OR"(종교 언어 행 포함).
- 6.3절: "realized losses" → "realized net losses". 검토 제안은 "principal losses"였으나 손실 정의(1 − 총수취액/실행액, 이자·회수 포함)는 원금 손실이 아니라 순손실이므로 본문의 "net-loss gap" 용어와 맞춤.
- 참고문헌: Davidson et al. (2026) 쪽수 181–217은 여전히 미확인 [저자 확인].

## 그림
- Figure 1(fig_framework_v22.py): 인용문 "as a Christian I believe in paying my debts"로 본문과 일치.
- Figure 4(fig4_density_v22.py): n 라벨을 각 패널 하단 한 줄로 이동, x축 여백 확대 — 축·눈금과 겹침 해소.
- Figure 5(fig5_cumdefault_v22.py): 패널 A 제목 "terminated sample", y축 상단 여유를 두어 범례가 곡선과 겹치지 않게. 재구축 자료로 재생성(n 2,398 / 507 동일).
- Figure C1(figC1_permutation_v22.py): 라벨의 하이픈을 마이너스(U+2212)로. 분포 파일(fake_dict_dist.npy)은 보존되지 않았으나 step3b_fakedict.py를 재구축 D.pkl에 seed 42로 다시 돌려 정확히 재현(평균 −0.00260, SD 0.01411, p 0.005, 평균 1,059.9건).

## 저자 확인 필요
- Davidson et al. (2026) 쪽수. Prosper Kaggle 데이터셋 페이지(raw_data_location.md). LICENSE, 이력 정리(git filter-repo), 그림 PNG·PDF 릴리스 첨부, Zenodo DOI, 표지의 주소·연구비, 투고 직전 "Draft v22" 날짜 줄 삭제.
