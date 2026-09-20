# 원고 v10 수정 내역 (2026-09-20)

v9 → v10. 모범 논문 3편(HLP 2023, Iyer et al. 2016, Netzer et al. 2019) 대비 구조 점검과 초견 심사자 관점 정독(cold read)을 거친 판본이다. 결과 수치·인용 목록·참고문헌은 바꾸지 않았다(아래 L7의 검정력 수치 2개만 예외).

## 1. 구조 (structure_comparison.md)
- 서론 ¶2에 가격·자료 문장 보강, 기여를 반복하던 ¶7 삭제(새 내용 한 가지는 문헌 문단으로 이동), ¶4 첫 문장 교체, 한계 문단 위치 조정, 로드맵을 실제 절 순서에 맞춤.
- 결론에 "Two implications follow…" 문단 추가(신용 파일에서 종교를 하나의 변수로 다루면 반대 부호 두 신호가 평균되는 문제, 협동조합·노조 지부 등 다른 소속으로의 확장).

## 2. 초견 정독 수정 22건 (coldread_issues.md)
용어 첫 정의(DTI, ZIP3, BLS, TF-IDF, AUC, CatBoost), 60단어 안팎 문장 분할, 지시어 모호성, "2008–2014" 표본 수 표현, "recovery sample" 표현 정정 등.

## 3. 저자 판단 항목(L1–L9) 처리 — 권장안 적용
| 항목 | 처리 |
|---|---|
| L1 "mostly proxies" | "partly proxies"로 수정. 텍스트 사전 통제 후 OR 1.27→1.28, DML 축소폭 최대 1/3이므로 "대부분"은 과장 |
| L2 "identifies the mechanism" | "tests the mechanism"으로 약화. 6.4절 "does not identify the mechanism causally"와 일치 |
| L3 "reader(s)" | 실행 로그 확인 결과 서술문 코딩·소속지표 정밀도 감사(200건)·마스킹 분류기 후보 판독 모두 LLM 코더가 수행. 본문 5곳, 표 5 열(6) 제목("Coder-validated"), 부록 표 B1 제목·열 이름을 language-model 코딩으로 수정 |
| L4 "pre-registered/pre-specified" | 등록기관 등록이 없으므로 "pre-registered test" 삭제, "pre-specified"는 "confirmatory" 또는 "specified before estimation/fixed in advance"로 바꿈. "did not pre-register"는 "did not specify as tests in advance"로 |
| L7 검정력 범위 | 본문 텍스트 조건 추정치는 +2.3~+3.0(+3.1 없음). step4e_aux.json의 SE 0.013845로 재계산: +3.0에서 검정력 = Φ(0.030/0.013845 − 1.645) = 0.70. "+2.3 to +3.1 … 50 and 72" → "+2.3 to +3.0 … 50 and 70" (기존 50%, 72%도 같은 식으로 재현됨) |
| L8 "the latest wave" | 2020 U.S. Religion Census가 존재하므로 "a wave"로 수정 |
| L5, L9 (문헌 문장 반복), L6 (삼분위 OR 반복, 부록 A 표 A2 위치) | 이번 판에서는 유지. 투고 전 분량 조정 때 정리 |

## 4. 인용 문장 표현 변경 6건 (changed_citation_sentences.md)
Oster/Cinelli("employment length"), Karlan 2005, Grammich(분할), Hainmueller/Chernozhukov, Chen 2010(뒷절), Cassar/Traunmüller(분할). 인용 내용은 3차 PDF 대조 판정과 일치 확인.

## 5. 검증
- 숫자 토큰: v9 대비 변화는 판 번호(9→10)와 L7의 3.1→3.0, 72→70뿐.
- 저자–연도 인용 다중집합: 변화 없음. 참고문헌 목록: 변화 없음.
- 부호 규칙: em dash 0.65/1000단어, 세미콜론 1.47/1000단어, 초록 233단어·대시 0·세미콜론 0, 55단어 초과 문장 없음.
- 빌드: docx·pdf 26쪽, 서론·표 5·결론 쪽 육안 확인.

## 6. 추가 수정 (2026-09-20)
- 초록 "who show no such advantage" → "who show no comparable advantage". 교육 종사자는 일반 차입자 대비 OR 0.945(p<0.001)로 작은 이점이 있으므로(표 2 Panel B) "그런 이점이 없다"는 과장. 초록 233단어 유지.

## 7. JEBO 적합성 보강 (2026-09-20, 평가 보고서의 조치 2·3·4)
- 조치 2 (JEBO 선례 인용): Croux, Jagtiani, Korivi & Vulanovic (2020, JEBO 173, 270–296)을 서론 셋째 문헌 문단과 5.1절 직업 문단에 추가. 필라델피아 연준 WP 20-15 원문으로 확인(ISCO-08 10개 직업군, 전문직 부도 낮음, 단순노무·판매·기능직 높음). Bentzen (2021, JEBO 192, 541–583)을 2.3절에 추가(코로나 초기 기도 검색 30% 증가, RePEc 초록 확인). 참고문헌 76편.
- 조치 3 (이론 틀): 2.3절 "A simple framework" 신설. 명제 1(사회적 제재 S → 부도 감소, 밀도에 따라 커짐, 소득 충격과 무관; 안정 직업 경쟁가설과의 차이), 명제 2(검증 불가 메시지의 자기선택 → 양의 부도 연관, 텍스트 통제 후 잔차; 실천형 메시지는 S를 일부 가짐). 수식 대신 기호를 쓴 서술형.
- 조치 4 (포지셔닝): 서론 셋째 문단 끝에 "organization rather than piety" 논지 3문장 추가, 로드맵 수정. JEBO 커버레터 초안(cover_letter_JEBO) 작성, 확인 필요 항목은 [ ]로 표시.
- 검증: 55단어 초과 문장 없음, 금지 표현 없음, 새 인용 2편 본문↔참고문헌 대조 완료, 초록 233단어, 본문 12,857단어, PDF 27쪽, 2.3절·서론 쪽 육안 확인.

## 8. 보류 결정 (2026-09-20)
- 사람 코더 검증(직업명 200건 감사, 설명문 100건 표본, 부록 B 한계 문장 추가) 모두 보류. 저자가 추후 진행 여부 판단. 검증 파일은 02_결과/코딩_검증/사람코더_검증표본_300건.xlsx에 준비되어 있음. 심사에서 요구가 나오면 수정 단계에서 수행.

## 9. 측정 구축 강조 (2026-09-20)
- 서론 둘째 문단 끝에 2문장 추가: 두 신호 모두 원자료의 변수가 아니며, 직업명 자유기술에서 소속 지표를 구축·정밀도 점검, 사전이 잡은 설명문 전부를 코드북으로 코딩, 3자리 우편번호로 지역 회중 밀도·실업과 연결했다는 점. (자료 독자성 약점 보완 목적, 새 수치·인용 없음)
- 커버레터: 같은 취지 1문장 추가, 중복 문장 2개 축약, 여백 조정으로 1쪽에 맞춤.
- 검증: 금지 표현 없음, 초록 233단어, 본문 12,908단어, PDF 27쪽, 1–2쪽과 커버레터 육안 확인.

## 10. 외부 심사평 대조 후 수정 (2026-09-20)
- 표 1 N 열 폭 확대(PDF에서 1,341,871이 줄바꿈되던 문제), 5.1절 "full terminal sample" → 실제 표본(소속 3,105 + 무작위 250,000)으로 정정, "same churches/same congregation" 과장 수정(교회 식별 불가 명시), "can enforce" → "may enforce", "protective form" → "form … associated with lower default", 표 7 주석에 ZIP3 FE 표본(비교군 150,000, ZIP3당 50건 이상, ZIP3 군집) 명시.
- 상세 검토: 06_기획_진행문서/외부심사평_검토_2026-09-20.md
