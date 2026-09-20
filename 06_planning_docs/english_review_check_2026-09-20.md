# 영문 표현 심사평 검토와 반영 결과 (2026-09-20)

심사평이 지적한 70개 표현을 원고 원문에서 하나씩 찾아 확인했다. 지적된 문구는 모두 실제로 원고에 있었다(정확한 인용). 판정 기준은 두 가지다. 주장 강도·측정 정의·통계 해석이 결과보다 강하면 고친다. 문장이 수사적이어도 뜻이 정확하면 저자 목소리로 두고 고치지 않는다(1인칭·사람이 쓴 톤 유지 원칙).

## 1. 반영한 것 (정확성 문제)
- 초록: "I show that the two carry opposite information" → "I find that the two are associated with default in opposite directions"; "Borrowers employed by religious institutions" → "Borrowers whose job titles place them in religious institutions"; "survives controls…" → "changes little with controls…"; "replication on Prosper" → "Its sign is reproduced in a smaller Prosper sample"; "does not respond to local unemployment shocks" → "shows no detectable response"; "Neither signal is priced" → "reflected in the platform's grade-based rates"; "whose information runs against the sender's intent" → "whose association with default runs opposite to the impression its sender seeks"; 마지막에 "The design is observational and does not identify either mechanism." 추가. H2 문장에 "in the confirmatory specification" 추가. 249단어.
- 서론: "Faith that is *belonged to*" → "Faith as *belonging*"(6.4의 "faith belonged to"도 함께); "behaves like" → "looks like"; "happens to name" → "names"; "affiliation effect grows" → "affiliation gap grows"; "does not change" → "shows no detectable change"; "they are the pattern" → "they fit the pattern"; "full public file" → "public file"; "reproduced on a second platform" → "reproduced in sign".
- 2절: "exactly this kind, and an unusually intense one" → "this kind, and often an intense one"; "are the members for whom the cost … is highest" → "should be".
- 4절: "rule out a misspecified functional form" → "guard against"; "tests the mechanism" → "asks whether the affiliation gap varies the way the mechanism predicts"; "memory constraint" → 계산상 이유 + 전체 표본·추가 추출 결과 참조; 교회 식별 불가 근거(기관명 606건, 반복 이름은 서로 다른 교회) 추가.
- 5절: "survives" → "remains"; "interval opens" → "confidence interval widens"; "The signal is in the religious content" → "The association sits in…"; "Table 7 turns to the community itself" → "local religious presence"; "there is no reason it should depend" → "it is hard to see why"; "What it can say" 문장을 제한된 서술로; "whatever protects" 2곳 → "whatever lowers … default"; "It is the congregation." → "What they share is employment inside a congregation."; "What the contrast makes clear" → "suggests".
- 6.1: "what the market left on the table" → "the difference in realized losses that grade-based pricing did not reflect".
- 6.4: 측정오차 방향 — "toward zero, not away from it" → 비차별적이면 0 쪽, 차별적이면 어느 방향이든 가능.
- 결론: "belong to a religious institution" → "whose job titles place them in"; "The first effect" → "association"; "insensitive to local unemployment" → "without a detectable response"; "Neither is priced" → "reflected in the platform's grade-based rates"; "most naturally read as" → "most consistent with".
- 커버레터: 같은 기준으로 5곳 수정, 1쪽 유지.

## 2. 반영하지 않은 것과 이유
- 제목 변경: 저자 판단 사항. 제목은 주장이 아니라 두 신호의 대비를 가리키고, 본문·초록이 인과 주장을 막고 있으므로 유지를 권함.
- "I want to stay with it", "quieter trace", "sit uneasily", "moves the paper", "push against", "clean account", "tells the same story", "barely moves", "the downgrade stands", "The cell is small", "the ledger" 문장: 뜻이 정확하고 결과보다 강하지 않음. 심사평 대안("This paper examines this pattern in greater detail" 등)은 정확성은 같고 전형적인 기계 문체라 저자 목소리 원칙과 충돌.
- "We assessed…"(1인칭 복수), "prespecified"(사전등록 오해 방지를 위해 v10에서 이미 제거한 표현), "This paper makes three contributions. First…" 형식: 단독 저자 원고와 이전 결정에 어긋남.
- "default less/more" → "lower/higher default odds" 일괄 교체: 본문에서 크기를 말할 때는 %p(평균 한계효과)라 "default less"가 정확함. 가설 문장은 이미 "(odds ratio below/above one)"으로 명시.
- "Lending Club"(참고문헌): Nowak, Ross & Yencha (2018) 논문 원제목의 표기라 바꾸지 않음.
- 권장 초록 전문 교체: H1 크기를 "odds 31% lower"로 쓰는 등 방향은 맞으나, "prespecified", 세미콜론 사용, 기계적 문장이 섞여 있어 원문을 고치는 방식으로 대체.

## 3. 같은 날 함께 반영한 재분석 결과(메커니즘 보완 권장안)
- 비교군 추출: 전체 1,344,976건 OR 0.694 (0.637–0.755), 추가 추출 5회 0.689–0.701. 원 추정 0.692 재현.
- wild cluster bootstrap(주 군집, Webb, 9,999회, 선형확률모형): H1 p < 0.001, H2 p = 0.015.
- 95% 신뢰구간·양측 p 병기: H1 0.638–0.751, H2 1.047–1.566 (p 0.016).
- 성직자=직원 Wald 검정 p = 0.77. 표 2 열(4)는 이미 표준 정의(step1)였음 — 다른 수치(0.675/0.679)는 원고에 쓰이지 않은 별도 파일.
- 표 8을 표 2와 같은 소속 정의로 재추정(N 239,198, 소속 2,973): 소속 0.687, 상호작용 0.975 (p 0.58), 수준 0.959 (p 0.44), 삼분위 0.588/0.763/0.721, 양성대조 교사 1.057 (p 0.29), 공무원 1.004 (p 0.93). "differs trivially" 주석 삭제.
- 부록 표 C4(경쟁 설명 동시 추정): 밀도 상호작용 0.83 (p 0.003), 충격 0.99 (p 0.80), 근속 10년 이상 상호작용 1.26 (p 0.038). 근속이 긴 차입자에서 격차가 작다는 것은 고용 안정성 설명이 예측하는 방향이라 원고에 그대로 쓰고, 6.4절의 "tenure도 배제" 서술을 삭제함. 다만 그 집단에서도 OR 0.80 (p 0.036)으로 격차가 남음.
- 부록 표 B3(표본 구성), 본문 표 9(결과별로 뒷받침하는 것과 확립하지 않는 것) 추가.
- 검증: 인용·참고문헌 변경 없음, 55단어 초과 문장 없음, 금지 표현 없음, 초록 249단어·대시 0·세미콜론 0, PDF 29쪽, 추가·수정 쪽 육안 확인.
