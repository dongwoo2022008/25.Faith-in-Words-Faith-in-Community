# 작업지시서 — LendingClub 신앙 신호 연구 (2026-09-17 기준)

이 문서는 이후 세션이 "진행"이라는 한마디로 이어받을 수 있도록 작성한 실행 지시서다. (2026-09-17 개정: 7-A Prosper 재현, 7-B 투자자 반응, 7-C 안정 직업군 통제 추가, 목표 저널 재조정.) 실행 순서: 1 → 2 → 3 → 7-C → 7-A → 4 → 5 → 7-B → 6 → 7 → 8. 각 단계는 입력·산출·합격 기준·판정 규칙을 갖는다. 단계 순서는 바꾸지 않으며, 한 단계의 산출물은 즉시 프로젝트("신앙과학문")와 폴더 `H:\내 드라이브\논문.김동우\data\P2P대출\신앙언어_검토`에 저장한 뒤 다음 단계로 넘어간다.

## 0. 동결 사항 (변경 금지)

- 연구질문 1개: 표현된 신앙(서술문 종교 언어)과 체화된 신앙(종교 직업)은 신용성과에 반대 방향의 정보를 담는가.
- 확인적 가설 2개만: H1 clergy OR < 1, H2 relig_lang OR > 1. Holm 보정. 이 밖의 검정은 모두 강건성 또는 탐색.
- 종속변수: 종결대출(Fully Paid / Charged Off / Default) 중 Charged Off·Default = 1. "Does not meet the credit policy" 건 제외.
- 처치 정의: clergy = emp_title에 pastor/minister/ministry/clergy/priest/chaplain/rabbi/missionar/reverend/evangelist/deacon/worship/imam/seminar 직무어, 또는 church/parish/diocese/congregation/synagogue/mosque 조직어(병원·학교·보험·은행 등 기관명 제외). relig_lang = 엄격 사전(God, Jesus/Christ, Christian, church, pray, bless, faith(종교 용법), the Lord, Bible, tithe, ministry/pastor/missionary, amen, 교단명; "faith in me", "good faith", "heaven forbid", "Lord & Taylor", "land lord" 제외).
- 통제: 등급, 발행연도, 금리, FICO, log 소득, DTI, 60개월, log 금액, 근속, 주거, 소득검증, 용도, 주 FE. H2 추가: log 서술길이 + 도덕·곤경·감사·가족·도움요청·사업 사전.
- 주장하지 않을 것: 인과 효과, 예측력 개선.

## 1. 자료·환경 준비

입력: `accepted_2007_to_2018Q4.csv.gz`(폴더 Lending Club), 작업 공간의 `lc_final.pkl`(종결대출 정리본), `lc_desc_sample.pkl`(서술 표본 123,292건), `lc_two_signal_analysis.py`.
할 일: 작업 공간이 초기화됐으면 원자료를 다시 옮겨 `lc_two_signal_analysis.py`의 전처리 부분으로 두 pkl을 재생성. CatBoost, DoubleML, sentence-transformers, R(fixest) 설치 확인.
합격: 종결대출 1,344,976건, clergy 3,105건, 서술 표본 123,292건, relig_lang 681건이 재현될 것. 숫자가 다르면 원인을 찾기 전까지 다음 단계로 가지 않는다.

## 2. 기준 모형 재추정 (표 2·3·4)

할 일: R `fixest::feglm`(logit) 또는 statsmodels BFGS로 H1·H2·동시투입 모형 재추정. 주 클러스터 SE. OR와 평균한계효과(AME) 병기. Holm 보정 p 산출.
H1 표본: clergy 전건 + 비clergy 무작위 250,000건(seed 1). 메모리 7GB 환경에서 전체 134만 건 주 FE 로짓은 실패함.
산출: `표2_H1.csv`, `표3_H2.csv`(사전 순차 투입 4열), `표4_동시투입.csv`, 수렴 로그.
합격: 수렴 경고 없음. 예비값(H1 OR 0.69, H2 OR 1.27–1.34)과 부호 일치, 크기 ±0.1 이내. 벗어나면 정의 차이를 찾아 기록.

## 3. 미관측 교란 민감도·플라시보 (표 5)

할 일:
(a) Oster(2019) δ: R `robomit` 또는 Stata `psacalc`, R²max = 1.3×R²(통제 모형). H1·H2 각각.
(b) Cinelli & Hazlett(2020) RV: R `sensemakr`, 벤치마크 공변량 = emp_length, verification_status.
(c) 직업 플라시보: teacher·police·nurse 동시 투입(예비: 0.90/0.89/1.04) — 재추정.
(d) 가짜 사전 플라시보: 서술 표본에서 신앙 사전과 출현 빈도(0.57%)·평균 서술길이 분포가 같은 무작위 단어 집합 1,000개를 만들어 H2 모형 반복, 실제 OR 1.28의 순열 p.
산출: `표5_민감도.csv`, `그림1_가짜사전분포.png`.
판정: (d)에서 순열 p ≥ 0.05이면 H2는 "우연 수준"으로 격하하고 논문은 H1 중심으로 재구성한다. (a)(b)에서 δ < 1 또는 RV < 0.01이면 H1의 해석을 "소속 신호"에서 "직업 특성"으로 낮춘다.

## 4. 이중 기계학습 DML (표 6)

할 일: DoubleML PLR/IRM. 처치 clergy(H1), relig_lang(H2). 뉴이선스 = CatBoost(iterations 500, depth 6), 5-fold cross-fitting, seed 고정.
H2 뉴이선스에 텍스트 임베딩 추가: `sentence-transformers/all-MiniLM-L6-v2`로 서술문 임베딩(384차원) → PCA 50차원. 모델 다운로드가 막히면 TF-IDF 5,000차원 + TruncatedSVD 100차원으로 대체하고 그 사실을 기록.
산출: `표6_DML.csv`(ATE, SE, CI; 임베딩 포함/미포함 2열).
판정: 임베딩 포함 DML에서 H2 ATE의 95% CI가 0을 포함하면 "종교 언어는 텍스트 모형이 이미 담는 정보"로 결론짓고 논문의 H2 서술을 그렇게 고친다. 이 결과는 숨기지 않는다.

## 5. 엔트로피 균형화 (표 5 보조)

할 일: H1에 `ebal`(R) 또는 `empirical_calibration`(Python)으로 FICO·소득·DTI·금액·금리·등급·연도·주 분포의 1·2차 모멘트 일치 후 가중 로짓. H2는 등급×연도 내 길이 1:5 매칭(기존)에 사전 점수 추가한 다차원 매칭.
산출: 균형표(표준화 차이 < 0.1 확인), 가중 추정치.

## 6. 이산시간 hazard (부록 A)

할 일: 부도 시점 = last_pymnt_d + 4개월(LendingClub 120일 연체 후 charge-off 관행에 근거한 근사, 자료 절에 명시). 대출–월 패널, cloglog, 기저 = 회차 진행률 3차 다항 + 연도 FE, 통제 동일. 두 처치의 hazard ratio를 1년 이내/이후로 분리.
판정: 결과가 표 2·3과 방향이 다르거나 약하면 부록으로 내린다.

## 7. 유형 코딩·이질성 (부록 B)

할 일: `신앙표현_수동코딩시트.xlsx` LC_820 시트를 2인 독립 코딩(type: 관용구/정체성/실천/오탐, frame: 종교/도덕/곤경). κ 산출, κ < 0.7이면 코딩 기준을 재정의하고 재코딩. 유형별 OR은 탐색 표로만. causal forest(`grf`)로 clergy CATE를 등급·소득·Bible Belt에 걸쳐 탐색.
판정: 유형별 결과는 어떤 경우에도 본문 주장으로 올리지 않는다.

## 7-A. 교차 플랫폼 재현 — Prosper (표 7) [2026-09-17 추가]

입력: `Prosper/prosperLoanData.csv/prosperLoanData.csv`(113,937건, 2005–2014). Occupation 코드 Clergy 196건, Religious 124건. 자유서술 텍스트는 없으므로 H1만 재현.
할 일: 종결대출(Completed / Chargedoff / Defaulted) 표본에서 clergy_prosper = Occupation ∈ {Clergy, Religious}. 로짓, 통제 = ProsperRating(또는 CreditGrade), 발행연도, BorrowerRate, CreditScore 범위 중앙값, StatedMonthlyIncome(log), DebtToIncomeRatio, Term, LoanOriginalAmount(log), EmploymentStatus, IsBorrowerHomeowner, IncomeVerifiable, BorrowerState FE. 플라시보 직업(Teacher, Police Officer/Correction Officer, Nurse (RN)) 동시 투입.
산출: `표7_Prosper_H1.csv`.
판정: OR < 1이고 p < 0.10이면 "두 플랫폼 재현"으로 본문에 넣는다. 부호가 반대이거나 p > 0.10이면 표본 320건의 검정력 한계를 명시하고 부록으로 내리되 결과는 반드시 보고한다. 2007–2008년 Prosper 1기(경매 방식)와 2009년 이후 2기가 섞여 있으므로 시기 더미 필수.

## 7-B. 투자자 반응 (표 8) [2026-09-17 추가]

목적: 서술문 신앙 언어가 투자자를 더 끌었는지. 정보(부도↑)와 반대 방향의 설득(투자↑)이면 원래의 "information vs persuasion" 구도가 살아난다.
입력: 서술 표본(2008–2014)의 funded_amnt, funded_amnt_inv, loan_amnt, issue_d. LendingClub 원자료에 모집 소요 시간·투자자 수는 없음 — 미확인 상태로 두고, 있는 변수만 쓴다.
할 일: (a) 투자자 충족률 = funded_amnt_inv / funded_amnt, (b) 완전 충족 여부(= 1), (c) 신청액 대비 실행액 = funded_amnt / loan_amnt. 각각을 종속변수로 relig_lang + 통제(H2와 동일 + log 길이 + 사전) 회귀. 2012년 이후 기관투자자(whole loan) 비중 증가로 (a)가 왜곡되므로 initial_list_status(w/f)를 통제하고 2008–2012 하위표본을 주로 본다.
산출: `표8_투자자반응.csv`.
판정: relig_lang 계수가 양(+)이고 유의하면 논문에 "투자자는 종교 언어에 더 반응하나 그 언어는 부도와 양의 관계"라는 한 절을 추가한다. 무의미하면 "투자자 반응은 관측 한계로 검정 불가"로 자료 절에 한 줄 적고 끝낸다. 해석 시 funded_amnt는 플랫폼 정책이 개입하므로 (a)(b)를 우선한다.

## 7-C. 고용 안정 직업군 통제 (표 5 확장) [2026-09-17 추가]

목적: "성직자 효과 = 고용 안정성"이라는 첫 번째 반론을 정면 처리.
할 일: emp_title에서 고용 안정 직업군 더미 생성 — 교사·교수, 경찰·교정, 소방, 군인, 연방·주·시 공무원(government/federal/state of/city of/county), 간호사, 우체국(usps/postal), 공공 교통. 이 더미들을 H1 모형에 동시 투입한 뒤 clergy 계수의 잔차 효과를 보고. 추가로 "안정 직업군만의 하위표본" 안에서 clergy vs 나머지 안정 직업을 직접 비교.
산출: `표5b_안정직업통제.csv`.
판정: 안정 직업군 전체 통제 후 clergy OR가 0.85 이상으로 올라가면 논문 해석을 "종교적 소속의 신호"에서 "종교 직업 특유의 신호(안정 직업 일반과 구별됨)"로 낮춘다. 0.8 미만이 유지되면 현재 해석을 유지한다.

## 8. 원고 작성

순서: 서론·가설 → 자료·변수 → 결과(H1·H2·동시투입, Prosper 재현) → 강건성(민감도·플라시보·안정직업·DML·균형화) → 투자자 반응(7-B 결과에 따라 절 또는 한 줄) → 논의(부도 이후 회수 탐색 문단 포함, p=0.057 명시) → 결론.
톤: 사람이 쓴 글, 1인칭, 문장 길이 변화, 병렬 나열 최소화.
제목: *Faith in Words and Faith at Work: Two Religious Signals with Opposite Credit-Risk Content in Online Lending*.
목표 저널 순서(2026-09-17 냉정 평가 반영): 1순위 Journal of Business Ethics(종교·신호·윤리 주제 적합, 이론 절 강화 필요) 또는 International Review of Financial Analysis → 2순위 Journal of Behavioral and Experimental Finance, JFSR → 3순위 Applied Economics, Finance Research Letters(단문). JBF급은 식별 전략 부재로 목표에서 제외. 저널 요건(분량·형식)은 투고 직전에 원문 확인.
판본 분기: JBE 판본은 신호 이론 + 종교사회학 문헌으로 서론을 세우고 신앙융합 해석을 논의에 포함; 금융 저널 판본은 신학적 해석을 각주 수준으로 줄인다.
합격: 모든 표의 수치가 산출 파일과 대조 확인됨. 렌더링된 원고 전체 육안 검사.

## 9. 보고 규칙

- 각 단계 완료 시 프로젝트에 `P2P신앙언어_<단계명>_<날짜>.md`로 결과·판정을 저장하고, 폴더에 산출 파일을 저장한다.
- 예비값과 다른 결과가 나오면 감추지 않고 판정 규칙대로 논문 구조를 바꾼다.
- 미확인 사항(모델 다운로드 가능 여부, 저널 요건 등)은 "미확인"으로 표기하고 추정을 사실처럼 쓰지 않는다.

## 10. 미결·외부 확인 필요

- Kiva 공식 스냅샷 loans 파일 다운로드 가능 여부(후속 논문용) — 교수님 환경에서 확인.
- 2인 코딩의 두 번째 코더 지정.
- R 사용 가능 여부(없으면 Python으로 대체: sensemakr → 직접 구현, ebal → empirical_calibration, grf → econml CausalForest).
