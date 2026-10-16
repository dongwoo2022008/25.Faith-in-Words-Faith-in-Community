# v23 수정내역 (2026-10-16) — 저자 교정 패스(v20 기준 33건) 병합

기준: v22 → v23. apply_v23.py(26개 치환). 30쪽, selfcheck 통과(세미콜론 3.61/1000어), 2·26쪽 렌더링 확인. 숫자 토큰 전수 대조: v22와 차이는 날짜 줄의 "22→23"과 교정안이 넣은 "Table 2" 참조, 그리고 2014 뒤의 쉼표가 마침표로 바뀜 것뿐.

## 교정안 33건의 처리
- 그대로 병합(21건): §1 "Such a group is a community", 로드맵 분할, §2.1 "a sanction the lender can rely on but cannot contract on", "the borrower's social contacts", "which holds that church jobs are simply stable"와 뒤 문장 분할, §2.2 cheap talk·"God bless" 문장 분할, §3.1 자료 출처·2014년 문장 분할, §3.2 사전 정의("Idiomatic uses … are excluded")·"Any that remain", §3.3 "Descriptions that contain it", §3.5 Prosper 분할, §4.1 "listed in the notes to Table 2"·클러스터링 문장 분할, §5.4 "The split is by keyword, not by a judgment of each role. The audit … how close the two splits are", "The staff result also speaks", §5.5 복음주의 비중 문장 분할, "rose: … and if anything the reverse", §5.6 "the timing evidence", §6.3 "28 basis points over a 42.1-month average term"("the other way" 중복 제거), §6.5 한계 문장 분할, B1 주석 "Coders:" / "Agreement:" 소제목.
- v22에서 이미 반영된 것(5건, 중복 적용 안 함): "Coarsened exact matching", "(0.88, and 0.92 per log point of length)", Table 11 헤더 "Main-effect OR", "how closely the community observes its members"(교정안의 "scale→rise"는 추가 반영), §1 "which, by a rule …, lowers the claim".
- 다르게 처리한 것(2건): §1 둘째 문단 첫 문장은 교정안대로 "The LendingClub file contains …"로 되돌림(바로 앞 문장이 Prosper라 이름이 필요; v22에서 "The same file"로 바꿨던 것을 철회). 두 문단의 LendingClub은 5회 → 3회. §2.1 "their employer … their reputation"은 교정안의 "the employer … a reputation … a professional reputation" 대신 v22의 복수 주어("Borrowers who work for a church are embedded …")를 유지.
- B 3건(사실관계): B1 설계 노트 범위, B2 "one in 450", B3 손실 표현은 v22에서 근거 확인 후 처리(B3는 "principal"이 아니라 "net"으로). 그림 4건도 v22에서 스크립트 수정 완료.
- 추가 1건: v22의 §4.1 설계 노트 문장이 56단어가 되어 교정 기준(35단어)에 걸리므로 두 문장으로 분할.

## 저자 확인 필요
- v22 수정내역의 목록과 같음(Prosper Kaggle 페이지, LICENSE, 이력 정리, 그림·PDF 릴리스 첨부, Zenodo DOI, 표지 주소·연구비, 투고 직전 "Draft v23" 날짜 줄 삭제).
