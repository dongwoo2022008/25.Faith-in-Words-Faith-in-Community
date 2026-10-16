# v18 수정내역 (2026-10-16) — 3차 외부 검토(C7 대조·표현) 반영

기준: v17 → v18. apply_v18.py(24개 치환)로 재생성. 본문 12,247단어, 초록 249단어, 30쪽(C7에 2행 추가로 Figure C1이 30쪽으로 넘어감), selfcheck 통과. 29–30쪽 렌더링 육안 확인. 반영하지 않은 항목: LLM 코더·데이터 파일 관련 지적(v17에서 저자 확인으로 처리 완료, 지시대로 무시).

## 재계산 1건 (run_v18_auc.py, v18_auc.json)
- 소속 지표 AUC 변화의 부트스트랩 CI. 원 분석(lc_two_signal_analysis.py)과 같은 5-fold CV 로짓·같은 표본(253,105, seed 1)·같은 300회 짝 부트스트랩(seed 1). 원 값 0.71495 → 0.71513 정확히 재현. Δ 0.00018, 95% CI 0.00005–0.00029. C7에 "Change in AUC" 행 추가(종교 언어 0.00002, −0.0001~0.0001은 기존 값), 4.4절에 "by 0.0002" 추가.
- 같은 스크립트로 설명문 표본 발행연도 집계: 2007년 246건, 2015년 30건, 2016년 12건 → Table 1 주석 "all but 42 of them issued 2007–2014".

## C7 대조 결과 반영
- 6.3절 "41-month" → "41.5-month", "42-month" → "42.1-month"(표와 일치).
- C7 순손실을 소수 둘째 자리(5.51/7.72, 7.08/6.09; stepC_economic.json)로, 주석에 "computed from unrounded values" 명시 → 독자가 −64/+28 bp 재현 가능(2.207/41.46×12 = 63.9, 0.985/42.13×12 = 28.0).
- C7 주석 Rows 5–7 "2008–2014" 삭제(step7b는 설명문 표본 전체 123,292건을 씀; 라벨만 'all_2008_2014'), N 명시.
- C7에 금리표 행 추가: 7,642 셀 / 최빈 금리 비중 94.7% / 셀 내 최대 고유 금리 5 (verify_rate_schedule.py 기록, 2,260,668건); 주석에 상위 2개 금리 비중 99.95% 추가.
- Figure 1 확인: 하단 문구 "−64 bp and +28 bp" 일치.

## 표현 정정
- 5.1 "Loans issued through 2013 had all reached maturity … (10 … still open)" → "All but 10 of the loans issued through 2013 had reached maturity … (the 10 were among the 34,392 60-month loans issued in 2013)".
- 5.5 "closer to one" → "closer to monotonic"; "the reverse of the ordering" → "not the ordering a job-stability account predicts, if anything the reverse"; "shows no interaction" → "shows no detectable interaction (1.075, p = 0.50)".
- 4.1 "preceded the estimates reported here" → "preceded the confirmatory estimates reported here"; 탐색 1차 분석(9-05)에 두 추정치의 예비 버전이 있었음을 명시(1차분석결과_2026-09-05.md: H1 0.69, H2 1.27–1.34).
- 3.2 "the rule fixed in advance" → "the rule fixed in the design note"(작업지시서 2026-09-17 '동결 사항'에 키워드 목록 수록 확인).
- 5.4 B2 감사 주체: "a reader" → "the LLM coder of Appendix B"(실행결과_2026-09-18.md stepH: 무작위 200건 LLM 코딩); B2 주석에도 명시.
- 초록: "which a job-stability account would predict" → "the response a job-stability account would predict"(선행사 모호 제거). 249단어.
- 충격 변수 명칭 통일: 4.3 "unemployment rise" → "unemployment change"; C4·C6 행 "rise" → "(largest subsequent) change"; C6 주석 "Rise" → "Change". 5.5·6.2의 "when local unemployment rises"는 예측 서술이므로 유지.

## 파일
01_원고/manuscript_v18.md, manuscript_v18_JEBO.docx, manuscript_v18_JEBO.pdf; 03_코드/원고빌드/apply_v18.py, build_v18.py; 03_코드/분석/run_v18_auc.py; 02_결과/추정결과_json/v18_auc.json.
