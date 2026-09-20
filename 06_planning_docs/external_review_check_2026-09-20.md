# 외부 심사평(편집자용 종합 판정) 검토 — 원고 v10 대조 (2026-09-20)

심사평의 각 지적을 현재 v10 원고 원문, 추정 결과 JSON, 분석 코드와 대조했다.

## 총평
대체로 정확하고 유용한 심사평이다. "major revision에 가까운 reject 또는 major revision"이라는 판정은 앞선 JEBO 적합성 평가와 같은 결론이다. 다만 일부 지적은 이미 v10에 반영되어 있고, 일부는 원고 문장을 실제보다 강하게 읽었다.

## A. 맞는 지적 — 원고를 고쳤음 (텍스트 수준)
| 지적 | 확인 결과 | 조치 |
|---|---|---|
| Table 1 "1,341,87 / 1" 깨짐 | PDF에서 N 열이 좁아 마지막 자리가 줄바꿈됨(원본 md는 정상). 이전 육안 점검에서 놓침 | 빌드 스크립트에서 표 1의 N 열 폭 확대, 재확인 |
| 253,105 = 3,105 + 250,000인데 "full terminal sample"이라고 씀 | 5.1절 첫 문단이 "full terminal sample"로 되어 있어 표 주석과 모순 | "all 3,105 affiliated loans and a random draw of 250,000 other terminated loans"로 정정 |
| "same congregation/same churches" | 자료에 교회(고용주) 식별자가 없음. 4절 "staff of the same churches holds the community fixed"는 과장 | "holds the kind of community roughly fixed … the data do not identify individual congregations"로 수정. 2.3절에도 같은 한계 한 문장 |
| 인과로 읽히는 표현 | "A congregation can enforce repayment", "The protective form of religion" 확인 | "may enforce", "The form of religion associated with lower default"로 수정 |
| Table 7 ZIP3 FE N = 146,248 설명 없음 | 코드(stepID2.py) 확인: 소속 전부 + 비교군 150,000건 무작위, 대출 50건 이상 ZIP3만, ZIP3 군집 SE | 표 주석에 그대로 기재 |

## B. 맞는 지적 — 재분석이 필요 (자료는 세션에 있음, 실행 가능)
1. 표본 흐름표: 5,014(전체 파일) → 3,105(종결) / 717 사전 매칭 설명문 → 681(종결 설명문 표본) → 583(코딩 확인) / 820(코딩 대상 레코드, 제목만 103 포함). 부록 표 1개로 정리 가능.
2. 비교군 무작위 추출: 시드 여러 개 반복, 가능하면 전체 비교군(약 134만) 추정. 메모리 확인 필요.
3. 주 군집 51개: wild cluster bootstrap p값 추가.
4. 양측 p값과 95% 신뢰구간을 주 추정치에 병기.
5. Table 8의 affiliation 정규식을 Table 2와 동일하게 맞춰 재추정("differs trivially" 문장 제거).
6. Table 2 Panel A 열 (4)(0.686/0.720)과 stepID_identification.json의 within-institution 결과(0.675/0.679, n 2,363/768)가 서로 다른 정규식에서 나옴 — 심사평은 지적하지 않았지만 대조 중 발견. 하나의 정의로 통일 필요.
7. Louisiana civil-parish 30건 제외 결과를 부록 강건성 표에 한 줄로 추가(수치 0.683은 이미 본문에 있음).
8. 결과변수 정의별(Charged Off만 / 포함) 강건성: 선택.

## C. 이미 반영되었거나 정확하지 않은 지적
| 지적 | 실제 상태 |
|---|---|
| 초록이 "religious community acts as social collateral"로 단정 | 초록은 이미 "The pattern is consistent with religious community acting as borrower-side social collateral". 심사평이 권한 문장과 사실상 같음 |
| H2를 확정적 결과처럼 서술 | 초록·5.2절이 이미 "sign is stable … loses precision once the full text is conditioned on"으로 하향. 초록 H2 문장에 "in dictionary-controlled specifications" 정도를 더 넣을지는 선택 |
| "pre-specified" 표현 | v10 L4에서 이미 "confirmatory / specified before estimation"으로 교체, "pre-registered" 삭제. 남은 "I stated in advance"는 사실(2026-09-17 작업지시서에 판정 규칙이 있음). 공개 등록은 없으므로, 원하면 작업지시서를 보충자료로 첨부 |
| 2025–2026 최신 문헌 검증 | PDF 대조 감사(09-19)와 Sourcely(76편 전부 REAL, 09-20)로 완료 |
| 실업 충격 분석을 "기각"으로 해석 | 본문과 표 주석이 이미 "recovery period, adverse-shock variation is limited"와 양성 대조군 무반응을 명시 |
| 사람 코더 검증 | 타당한 지적이나 저자가 09-20에 보류 결정. 심사 요구 시 수행 |

## D. 저자 판단이 필요한 제안
- 제목 변경("Institutional Affiliation, Self-Authored Religious Language, and Default…"): 더 안전하지만 기억에 덜 남음. 현 제목 유지 + 본문 표현 절제를 권함.
- 기여를 "정체성 정보의 이질성"으로 재구성: 좋은 제안. 현재의 "조직으로서의 공동체" 프레임과 결합 가능(서론 기여문 한 문장 추가 수준).
- 메커니즘 대안가설 표(각 분석이 배제하는 설명/배제하지 못하는 설명): 4절 첫 문단이 이미 문장으로 하고 있으므로 표로 옮기면 심사자 요구를 선제 충족. 권장.

## 권장 순서
1) B의 재분석(표본 흐름표, 시드·전체 비교군, wild bootstrap, 양측 p·CI, 정규식 통일) → 2) 대안가설 표 → 3) 초록 H2 문장 미세 조정과 서론 기여문 한 문장.

## E. 대조 중 추가로 발견한 점 — 사전 판정 규칙(작업지시서 2026-09-17)과 원고의 불일치
심사평의 "확인적/탐색적 구분" 지적과 관련해, 작업지시서의 판정 규칙을 원고와 대조했다.
1. 작업지시서: "유형별 결과는 어떤 경우에도 본문 주장으로 올리지 않는다." 그런데 서론 셋째 문헌 문단은 "descriptions that report religious practice … behave like the affiliation signal"을 기여처럼 제시하고, 2.3절 명제 2와 5.2절도 이 셀을 이론이 지목한 셀로 강조한다. 규칙에 맞추려면 서론에서 이 문장을 "exploratory" 표시와 함께 낮추거나 삭제하고, 5.2절·부록 B1에서 탐색 결과로 명시해야 한다.
2. 작업지시서: "임베딩 포함 DML에서 H2 ATE의 95% CI가 0을 포함하면 '종교 언어는 텍스트 모형이 이미 담는 정보'로 결론짓고 H2 서술을 그렇게 고친다." 원고는 "부호는 일관되나 정밀도가 부족하다"로 서술해 규칙 문구보다 한 단계 약하게 하향했다(실행 로그 09-18에서 이렇게 결정). 심사평의 H2 지적은 이 차이를 겨냥한 것이다. 다만 점추정치는 전체 텍스트를 넣어도 최대 3분의 1만 줄었으므로 "텍스트가 이미 담은 정보"라고 단정하는 것은 오히려 증거와 맞지 않는다. 규칙의 취지를 살리면서 정확하게 쓰려면 초록·결론의 H2 문장을 "once the full text is represented, the association cannot be distinguished from information the text already carries, although its point estimate changes little" 쪽으로 옮기는 방안이 있다.
두 항목 모두 주장 강도를 바꾸는 저자 판단 사항이라 원고는 아직 고치지 않았다.
