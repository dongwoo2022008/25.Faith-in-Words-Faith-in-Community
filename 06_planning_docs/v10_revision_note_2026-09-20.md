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
