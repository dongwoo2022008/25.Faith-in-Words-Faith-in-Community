# Faith in Words, Faith in Community
### Religious Affiliation, Religious Language, and Default in Online Consumer Credit

논문 작업 폴더. 대상 저널 JEBO (Journal of Economic Behavior & Organization). 최신 원고: `01_원고/원고_v7_JEBO_2026-09-19.docx` (2026-09-19, 25쪽).

## 폴더 구조

| 폴더 | 내용 |
|---|---|
| `01_원고/` | 최신 원고 v7 (docx/pdf/md), `figures/` 제출용 그림 5개 (300 dpi PNG), `이전버전/` v1–v6 및 절별 초안 |
| `02_결과/` | `표_csv/` 본문 표 원자료, `추정결과_json/` 각 step 스크립트 산출 JSON, `코딩_검증/` LLM 코딩 결과·AI간 신뢰도·사람코더 검증표본·소속지표 정밀도 감사(200건)·코드북, `실행결과_2026-09-18.md` 작업 로그(1차~10차), `방법론정리`, `논문요약_평가용` |
| `03_코드/` | `분석/` step1~stepU 분석 스크립트(표·그림 생성), `전처리_탐색/` 원데이터 → pkl 전처리 및 초기 탐색, `원고빌드/` 원고 md → docx/pdf 빌드·자체검증 |
| `04_데이터/` | `원데이터/` LendingClub accepted_2007_to_2018Q4.csv.gz, LCDataDictionary.xlsx, Prosper prosperLoanData.csv; `외부자료/` ARDA 2010 Religion Census(county), Census ZCTA–county 관계표, BLS LAUS county 실업률 2008–2018 |
| `05_문헌/` | 문헌메모, 눈덩이 인용사슬 검토(추가인용후보), 문체 벤치마크 논문 3편 PDF·벤치마크 메모 |
| `06_기획_진행문서/` | 연구질문 확정안, 작업지시서, 프레임 확정, 1차 분석결과, 진행상황 정리 |

## 재현 순서

1. `03_코드/전처리_탐색/lc_extract.py` → `lc_final.pkl` (LendingClub 원데이터에서 종결 대출 추출·변수 정리)
2. `03_코드/분석/step1.py` → `T.pkl`(종결 표본), `D.pkl`(설명문 표본), 종교 지표·텍스트 사전
3. `step2.py` (H1 기준모형, 표 2), `step3.py` (안정직업·CEM, 표 2 Panel B), `step3b_fakedict.py` (가짜 사전 플라시보), `step4*.py` (H2 DML, 표 5·그림 3), `step5c.py` (엔트로피 균형), `step6.py` (이산시간 해저드, 부록 A1), `step7a.py` (Prosper 복제, 표 4), `step7b.py` (투자자 반응), `stepA_arda.py`·`stepU_unemp.py` (지역 종교성·실업, 표 7·8), `stepN_neighbor.py` (인접 직업), `stepID2.py` (Oster·Cinelli–Hazlett, 표 3), `stepG_extras.py` (설명문 작성 선택·대안 클러스터링, 부록 C), `stepH_precision.py` (소속지표 정밀도·루이지애나 parish), `stepF_figures.py` (그림 2–5)
4. `03_코드/원고빌드/build_v7b.py` → docx/pdf (pandoc + python-docx + LibreOffice)

스크립트 안의 경로는 작업 당시 컨테이너 기준(`/mnt/user-data/uploads/...`, `out/`)이라 실행 전에 `04_데이터/` 경로로 바꿔야 한다. 난수 시드는 각 스크립트에 고정되어 있다(random_state=1, 5 등).

## GitHub
https://github.com/dongwoo2022008/25.Faith-in-Words-Faith-in-Community — 원데이터(`04_데이터/원데이터/`, 100 MB 초과)는 GitHub 용량 제한으로 제외하고 Google Drive 폴더에만 보관한다. 이 저장소에는 세션 제약으로 텍스트 파일(코드·JSON·CSV·md)만 올라가 있으며, docx/pdf/png/xlsx/zip 등 이진 파일은 Google Drive 폴더 `H:\내 드라이브\논문.김동우\Under.writing\25.Faith in Words, Faith in Community`에서 git push로 추가한다.
