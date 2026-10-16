# v21 수정내역 (2026-10-16) — 저장소 감사 회신 반영

기준: v20 → v21. apply_v21.py(4개 치환). 30쪽, selfcheck 통과, 26·29쪽 렌더링 확인.

## 원고
- 부록 B1: 설계 노트의 κ 0.7 기준과 충족 여부 명시 — 유형 4분류는 두 검증 모두 충족(0.86, 0.72), 사람 코더의 종교/비종교 이분(0.55, PABAK 0.69)과 frame(0.48)은 미충족; frame은 어떤 추정에도 안 쓰이고 이분은 Table 8에만 들어감.
- 부록 C5 주석: 설계 노트가 지정한 sentence-transformer(all-MiniLM-L6-v2)의 다운로드가 차단되어 노트의 대체 조항대로 TF-IDF+SVD를 쓰고 spaCy 단어벡터·doc2vec을 추가했음을 기재(실행 로그 2026-09-18 근거).
- C7 주석: 상위 2개 금리 비중 99.95% → 99.94%. verify_rate_schedule.py를 5자리 출력으로 다시 돌린 결과 0.99942(이전 docstring의 99.95는 4자리 반올림 경계값).

## 저장소 (GitHub)
- README "Provenance" 정정: 첫 커밋 2026-09-19 05:28Z(KST 14:28), 설계 노트 커밋 a07732a 09:12Z(KST 18:12), 같은 날 201개 커밋; 프로젝트 문서 생성 시각 UTC·KST 병기; 실행 로그의 "작업지시서(2026-09-17 개정)" 참조 언급.
- 04_data/raw/raw_data_location.md: Kaggle URL(LendingClub: wordsforthewise/lending-club), Prosper는 Kaggle 배포본으로 수정하고 데이터셋 페이지는 저자 확인 [ ], LCDataDictionary 문구 삭제, H: 경로 삭제.
- 레코드 단위 LLM 코딩 결과 추가: coding_validation/llm_coding_lc_820.csv(loan_id, type, frame; frame 라벨 영문화). 정답키 폴더 _answer_key_do_not_open → coding_validation/validation_sample_LC_answer_key.csv로 이동(영문 라벨), kappa_after_human_coding.py를 LC 전용으로 수정.
- default_and_descriptions_by_year.csv: 보일러플레이트 제거 후 집계로 바꿔 125,811(2007–2014: 125,761)과 일치, 제거 전 수치(125,812) 열 병기; verify_vintage_default.py 갱신.
- rate_schedule_by_year.csv: 최빈 금리 비중(94.715%)·상위 2개 비중(99.942%) 열 추가; verify_rate_schedule.py 갱신.
- build_v16.py 추가. stepF_figures.json의 fig2_rows 라벨이 구버전임을 README에 명시. v11_축약내역(영문 condensation note와 중복) 삭제, v13_수정내역 → v13_change_notes_2026-10-01.md로 개명, fig_measurement_ko.py(논문 미사용 한국어 구조도) 삭제. CITATION.cff 추가.

## 저자 결정 필요
- LICENSE 선택(코드 MIT, 문서 CC BY 4.0 등) — Zenodo 릴리스에 필요.
- 그림 PNG 6개와 PDF를 GitHub 웹 UI로 업로드, 릴리스 태그·Zenodo DOI.
