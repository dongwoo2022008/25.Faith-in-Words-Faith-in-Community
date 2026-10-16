# v19 수정내역 (2026-10-16) — 4차 검토(표 보강·B1 기술) 반영

기준: v18 → v19. apply_v19.py(13개 치환). 본문 12,270단어, 초록 249단어, 30쪽, selfcheck 통과. 10·29쪽 렌더링 확인. 지시대로 2차 코더 관련 항목(타사 모델 재코딩, Opus 버전)은 반영하지 않음.

## 재계산 (run_v19_extras.py → v19_extras.json, 재구축 T.pkl/D.pkl + 원자료 3개 열)
- Table 2 열 (4): step1 키워드 규칙으로 8개 안정 직업 지표를 다시 만들고 step3 사양으로 재추정. OR 0.6898(원 0.690 일치), SE 0.041, AME −4.9 pp → 빈칸 채움.
- Table 2 열 (5): step5c 엔트로피 균형화를 그대로 재현(76 모멘트, ESS 172,964.6, OR 0.6966·SE 0.0426 원 값과 일치). AME −4.3 pp → 빈칸 채움.
- C7 1–4행: 분실된 stepC 계산을 복원. 셀 부도율 0.17364·순손실 5.512/7.720이 저장값과 정확히 일치하는 정의를 확인: 순손실 = 부도 × (1 − 총상환/대출금), 즉 상환 완료 대출은 0; "mean loan life" 41.46/42.13은 실제로는 **평균 약정 기간**(36 + 24×60개월 비중). 원고의 정의 문장("one dollar minus total payments … nets out interest and recoveries", "average loan life")이 부정확했으므로 6.3절과 C7 행 이름·주석을 실제 정의대로 고침.
- 셀에 term 추가(sub-grade×year×term): −67/+29 bp(−64/+28에서 소폭 변화) → 6.3절과 C7 주석에 한 줄. 실현 기간(최종 납입까지 23.3/28.2개월)으로 나누면 −114/+42 bp → C7 주석에 병기.

## 표현·표기
- C7 AUC 변화 행을 5자리로 통일: 0.00018 (0.00005 to 0.00029) / 0.00002 (−0.00010 to 0.00014); 4.4절 "by 0.00018".
- C7 주석: 5·7행 OLS, 6행 로짓, 주 클러스터 SE 명시; 셀 수(254/165) 명시.
- B1 노트: 모델 ID claude-fable-5-1 병기; "12개 인스턴스가 서로 겹치지 않는 못을 읽어 각 레코드는 라벨 하나"(코딩결과_lc.csv 820행·고유 loan_id 820 확인); "no sampling temperature was set" → "the application does not expose a sampling temperature or other decoding settings, so the coding ran at its defaults".

## 반영하지 않음 / 저자 판단
- B2 감사의 C·D 6건을 저자가 눈으로 확인했다는 문장: 저자 확인 전에는 쓰지 않음.
- 투고본 docx의 "Draft v19" 날짜 줄 제거는 최종 제출 직전에.
