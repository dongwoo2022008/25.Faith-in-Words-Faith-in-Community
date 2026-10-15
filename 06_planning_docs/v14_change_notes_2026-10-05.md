# v14 수정내역 (2026-10-05) — 3단계 교정 계획 2단계(지적 모드 검토) 반영

기준: v13 (2026-10-05 최종) → v14. 검토는 장 단위로 세 개의 독립 검토 에이전트가 "고쳐 쓰지 말고 의심 지점만 표로 내라"는 지시로 수행했고(지적 98건), 각 건을 원고·표·저장된 추정 결과 JSON·원자료에 대조해 채택 여부를 정했다. 내용·수치 변경 없음. 본문 11,520단어, 29쪽.

## 채택 74건 — 유형별

### 1. 사실 오류 교정 (원자료·결과 JSON으로 확인)
- 3.1 "an earlier and somewhat riskier slice" → "an earlier slice … with a lower default rate". Table 1이 보여주듯 설명문 표본 부도율은 15.3%로 전체 20.0%보다 낮다. 원자료 연도별 부도율도 2008–2014(0.13–0.18) < 2015–2016(0.20–0.23)로 확인.
- 4.2 *Early versus later borrowers* "and its default rates were higher (Section 3.1)" 삭제. 3.1에 그런 서술이 없고 자료도 반대.
- Appendix Table C2: OR 열은 변수 1단위당(금리 1%p, FICO 1점, 로그 1단위, DTI 1점), AME 열은 1SD당임을 stepG_extras.json으로 확인. 행 라벨 "(per SD)" 제거, 헤더를 "OR (per unit)" / "AME (per SD)"로, 노트에 단위 설명 추가.
- Appendix B1 노트: "The disagreements sit at two boundaries (17, 8)" → "Most of the 31 disagreements sit at two boundaries (17, 8). In the practice category the two agree on 36 of 40." 교차표로 17+8+6=31 확인.
- 5.5 "the evangelical share is unrelated to default"에 추정치 추가 "(1.030, p = 0.15), estimated without state fixed effects" (stepA_arda.json regional_evan_noStateFE).
- 5.3 "Neither estimate moves when the other is added" → "The religious-language estimate is unchanged from Table 6 (1.281 alone)". Table 9 수치(1.293/0.013, 0.672/0.041)는 step2_results.json과 일치 확인.
- 5.4 "only 606 affiliated titles name an institution" → "only 606 of the 3,105 affiliated titles name a specific institution".
- 5.4 탐색적 분할: 본문 "split of the clerical titles" → "split of the affiliation indicator"; 기타 행 2,355 = 3,105 − 497 − 253이므로 church staff 포함을 명시; "associate and youth" → "associate, youth and assistant".

### 2. 인과 어휘 → 연관 어휘 (저자 결과에 한정)
- 2.1, 4.2, 4.3, 5.2, 5.4, 5.5, 5.6의 "effect" 9곳 → gap / association / coefficient.

### 3. 약어·용어 정의 보강
- 정의 추가: ZCTA, BLS, LAUS, ROC, ATTE, TF-IDF, PCA, SVD, HR, cloglog, LLM, RV. "CV AUC" → "cross-validated area under the ROC curve".
- 3.1에 loan `title` 필드 추가, 3.2 "the title or text" → "the loan title or the description text".
- 5.2 "validated indicator" → "coded indicator"; "every linear placebo" → "both placebos (Table 8 and the random-word permutation below)".

### 4. 용어·표기 통일
- "job-security / income-stability account" → "job-stability account"; "terminal loans/sample" → "terminated"; "homeownership" → "home ownership"; "Table 6 column (3)" → "Table 6, column (3)"; "vs." → "vs"; "467 loans" → "n = 467"; "p<0.001" → "p < 0.001"; "ZIP-level" → "ZIP3".

### 5. 모호한 지시·수식 관계 해소, 6. 구두점·문장 분할
- 1장, 2.1, 4.2, 4.3, 4.4, 5.1, 5.2, 5.5, Appendix B 코드북의 모호한 "it"/비교 대상 정정; 쉼표 3곳; 40단어 초과 실문장 14개 분할; 중첩 괄호 해소.

## 기각 24건 — 이유
- 인용·단어 목록을 포함해 40단어를 넘는 문장: 인용·목록 제외 시 40 이하이므로 유지.
- 3.1 "2007 and 2014" vs 표 노트 "2008–2014": 전자는 원파일, 후자는 분석 표본 기준.
- Table 2 col (4) SE, ATTE vs DML, Table 4 H2 benchmark 공란: 원 결과 없음.
- 6.3 28bp: stepC_economic.json annualized_bp = 28.04 확인.
- 직렬 쉼표, "non-profit" 철자: 저널 교열 사항.

## 검증
- selfcheck: 금지어 0, em dash 0, 세미콜론 3.34/1000, 초록 247단어. 참고문헌 ↔ 본문 인용 교차 대조 일치. 29쪽 전체 육안 검사.
