# v20 수정내역 (2026-10-16) — v18 PDF 검토 회신 반영

기준: v19 → v20. apply_v20.py(2개 치환) + Figure 1 재생성. 본문 12,361단어(선언문 포함), 초록 249단어, 30쪽, selfcheck 통과. 20쪽(선언문)·Figure 1 렌더링 확인.

## 반영
- Figure 1 H1 결과 상자 "unresponsive to local unemployment" → "no detectable response to local unemployment"(초록·5.5절과 일치). fig_framework_v20.py, Figure1_channels.png 재생성, docx/pdf 재빌드.
- 생성형 AI 선언: Elsevier 지침대로 원고 본문 References 바로 앞에 "Declaration of generative AI and AI-assisted technologies in the writing process" 절로 삽입(Claude(Anthropic), 영문 교정·수치 대조·서식; 방법론의 LLM 코더는 3.2절·부록 B에 별도 기술). 투고서류_v20의 선언문 항목은 이 절을 가리키도록 수정.
- 데이터 가용성 진술(투고서류_v20): 원자료 미재배포·재구축 스크립트 명시, 저장소 내용(코드·추정치·코드북·검증 표본·편집 이력·설계 노트) 열거, 레코드 단위 코딩 출력과 그림은 Drive 사본·아카이브 릴리스에 포함 예정, Kaggle 라이선스 확인 [ ].
- 설계 노트 날짜 근거: README에 "Provenance of the design note" 절 추가 — 저장소 git 이력은 10월이라 날짜 근거가 못 되고, 프로젝트 문서 서버 생성 시각 2026-09-17T23:37:48Z(UTC)와 Drive 버전 기록이 근거임을 명시; 9-05 탐색 분석 문서와 9-18 실행 로그 파일명 연결.
- 이전 회신에서 이미 v19에 반영된 항목(모델 ID, temperature 표현, 12개 인스턴스 분할, C7 5자리·term 셀·주석, Table 2 열 (4)(5)): 변경 없음.

## 반영하지 않음 / 저자 조치
- 2차 코더 Opus 버전·타사 모델 재코딩: 지시대로 보류.
- B2 C·D 6건 저자 육안 확인 문구: 저자 확인 후.
- 투고본 docx "Draft v20" 날짜 줄 제거, Zenodo DOI(투고 원고 버전과 일치하는 릴리스 태그), Kaggle 라이선스 확인.
