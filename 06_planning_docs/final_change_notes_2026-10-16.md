# 최종본 정리 (2026-10-16) — v21 → v22 → v23 → 최종본(manuscript)

## 버전 흐름
- v21: 저장소 감사 회신(B1 κ 기준, C5 임베딩 대체, 99.94%). README 출처 정정, 레코드 단위 코딩 CSV 추가.
- v22: 6차 검토 회신. Table 1 반올림 4곳(703.9, 14,827, 0.570, 0.113), 기관명 583, Table 10 탐색 행 재추정(509/235/2,361; OR 0.459/0.636/0.751, run_v22_hierarchy.py), Table 3 셀 수 삭제, Table 5 주석, §4.1 설계 노트 범위, one in 450, CEM, Main-effect OR, realized net losses, 그림 1·4·5·C1 수정. make_table1.py → descriptive_statistics.json/CSV. README C6 매핑 수정, stepU/stepID/lc_two_signal _note.
- v23: 저자 교정 패스(v20 기준 33건) 병합, 숫자 변경 없음. §1 "The LendingClub file" 유지, §2.1 복수 주어 유지.
- 최종본(manuscript.md/.docx/.pdf, apply_final.py 치환 3건): "Draft" 날짜 줄 → "October 2026"; Funding 절("This work was supported by the Baekseok University Research Fund.") 참고문헌 앞에 추가; §5.4 "only 583 of the 3,105 affiliated titles (497 distinct names) name a specific institution" — Table 8·B3의 "583 coded religious"와 같은 숫자라 복사 오류로 오해받지 않도록 고유 이름 수(descriptive_statistics.json의 distinct_strings 497)를 병기. build_final.py가 docx 바닥글 가운데에 PAGE 필드(쪽 번호)를 넣음. 30쪽, selfcheck 통과.
- 파일명: 저장소의 논문 파일에서 "JEBO"를 제거(다른 저널 투고 가능성). manuscript_JEBO.md → manuscript.md, cover_letter_JEBO_draft.md → cover_letter_draft_v10.md, JEBO_presubmission_checklist → presubmission_checklist_2026-10-05.md, previous_versions/manuscript_vN_JEBO_날짜.md → manuscript_vN_날짜.md. 빌드 스크립트·README·투고 서류의 참조도 같이 수정.

## 투고 패키지(2026-10-16 완성본, 자리표시 없음)
- manuscript.pdf/.docx/.md, title_page.docx(주소: Room 1120, Main Building, Baekseok University, Cheonan, Republic of Korea), highlights.docx, declarations.docx(연구비 과제번호 없음, 데이터 가용성은 GitHub 저장소 링크), figure_captions.docx, cover_letter.docx(날짜 2026년 10월 16일), submission_documents.md/.docx(전체), figures/ 6장(600 dpi). make_package.py가 submission_documents_final.md를 파일별로 분리해 docx로 만든다.

## 위치
- GitHub: 01_manuscript/manuscript.md(최종), submission_documents_final.md, cover_letter_draft_v10.md, apply_v22/v23/final.py, build_v22/v23/final.py, make_package.py, make_table1.py, run_v22_hierarchy.py, v22 그림 스크립트, descriptive_statistics.json/CSV, v22_hierarchy.json, CITATION.cff 1.0.
- Drive 01_원고: manuscript_final.md/.docx/.pdf, 투고패키지_final/(zip, 파일별 docx, figures), v21–v23 md/docx/pdf. 03_코드, 02_결과, 06_기획_진행문서에 스크립트·JSON·수정내역 동기화.

## 저자 확인 완료
- Davidson et al. (2026) 쪽수 181–217: Crossref DOI 10.1007/s10693-025-00451-3로 확인. 연구비 문구, 표지 주소, 커버레터 날짜, 데이터 가용성(GitHub만) 반영.

## 저자만 할 수 있는 것
- git filter-repo 이력 정리(옛 커밋 933714b, 99203f1 등에서 삭제 파일이 내려받아짐) → 정리 뒤 README의 두 SHA 갱신, 태그·릴리스(그림 PNG·PDF 첨부). LICENSE 선택. raw_data_location.md의 Prosper Kaggle 페이지 확인.
