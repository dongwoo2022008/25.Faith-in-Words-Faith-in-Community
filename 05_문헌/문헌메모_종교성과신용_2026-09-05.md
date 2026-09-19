# 문헌 메모: 종교성·종교 언어와 신용 결과, Kiva 투자자 동기 (2026-09-05 웹 검색 기준)

검색으로 확인된 논문만 수록. 접근이 차단되어 초록을 확인하지 못한 항목은 "미확인"으로 표시.

## 1. 종교성 / 종교 직업과 대출 부도·신용 행동

**(가) 차입자 텍스트 사용.** Netzer, Lemaire & Herzenstein (2019, *Journal of Marketing Research*): Prosper 신청서 약 12만 건 텍스트마이닝, 부도 차입자가 가족·God·고난·도움 요청·단기 지향 단어를 더 많이 사용(보도 기준 God 언급 시 부도 확률 약 2.2배). 종교 언어는 여러 어휘 신호 중 하나로만 취급. Anglin, Milanov & Short (2023, *Journal of Business Ethics* 185): Kiva 차입자 설명문 253,130건에서 종교 표현이 펀딩 성공에 부정적(특히 여성), 대출자 종교성이 높을수록 완화. 상환/부도 미분석. Dorfleitner & Oswald (2016, *Review of Financial Economics*): Kiva 상환 결정요인(MFI 심사, 성별, 기간) — 종교·텍스트 변수 없음.

**(나) 지역 종교성.** Li & Ucar (2022, *International Real Estate Review*): 미국 2,220개 카운티 1999–2011, 종교 귀속률 1SD 증가 시 모기지 연체 약 9% 감소. Conklin, Diop & Qiu (2022, *JBE*): 카운티 종교성이 높을수록 감정가 과대평가·허위신고 감소, 부도 감소는 불명확. Baele, Farooq & Ongena (2014, *JBF* 44): 파키스탄 15만 건, 이슬람 대출 부도율이 일반의 절반 이하, 라마단·종교정당 득표율 높은 도시에서 더 낮음. Gyapong, Gyimah & Ahmed (2021, *RQFA*): 65개국 770개 MFI, 국가 종교성이 높을수록 대출손실 낮음 — 경로는 대출기관 위험회피. Yan & Yin (2021, EFMA WP): 중국 도시 종교시설 밀도가 가계 차입 의향을 높임. Cole, Filatova & Khaled (2023, SSRN 4447681): MFI 상환과 종교성 — 미확인.

**(다) 소속·직업.** "Religious affiliation and debt among U.S. households" (2023, *Social Science Research*) — 저자·결과 미확인. 성직자·목회자 차입자의 부도율을 직접 분석한 학술 논문은 검색에서 발견되지 않음.

**판단.** LendingClub/Prosper 서술문에서 종교 언어를 독립 범주로 다룬 논문 없음(Netzer는 부수적, Anglin은 Kiva 펀딩만). 종교 직업 차입자 부도율 연구 없음. 두 방향 모두 공백.

## 2. Kiva 투자자 동기·종교

Liu, Chen, Chen, Mei & Salib (2012, *WSDM*, "I Loan Because…"): Kiva loan_because 약 10만 건을 10개 범주로 코딩, "종교적 의무" 범주가 코더 일치도(0.89)·분류기 성능(F0.5 88%) 최고, 이 동기 투자자는 월 약 0.25건·$9 더 대출(모든 범주 중 최대). Atheists·Kiva Christians 팀이 총 대출액 1·2위. Chen, Chen, Liu & Mei (2015/2017, *Games and Economic Behavior*): 팀 경쟁이 대출 증가(세부 미확인). Chen et al. (2016, *PNAS*): 팀 추천 현장실험. Ge & Luo (2016, *Financial Innovation*): 라이벌 팀(Kiva Christians vs LGBT Kivan & Friends)이 상대 팀 지원 프로젝트를 회피. Sabzehzar, Hong & Santanam (ASU 2019 보도, 게재 여부 미확인): 대출자국–차입자국 종교적 거리 1SD 증가 시 거래 약 15건 감소.

**판단.** "Kiva 렌더 종교 서술 → 대출건수"는 Liu et al.(2012)과 겹침. 투자자–차입자 매칭(신앙 투자자가 고르는 차입자와 그 상환)으로 가야 신규성 확보.

## 3. 데이터 접근

- Kiva 공식 스냅샷: https://www.kiva.org/build/data-snapshots — lenders / loans / loans_lenders (CSV `http://s3.kiva.org/snapshots/kiva_ds_csv.zip`, JSON `kiva_ds_json.zip`). "비정기 생성" 공지, 최신 날짜 미표시. 이 환경에서 S3 다운로드 차단 → 실제 파일 존재 미확인.
- loans.csv 컬럼(GitHub 이용자 리포 기준, 34개, 140만+건): LOAN_ID, DESCRIPTION, DESCRIPTION_TRANSLATED, ORIGINAL_LANGUAGE, STATUS(fundraising/funded/in_repayment/paid/defaulted/refunded), COUNTRY_NAME, SECTOR_NAME, ACTIVITY_NAME, LOAN_USE, TAGS, BORROWER_GENDERS, NUM_LENDERS_TOTAL, POSTED_TIME 등. loans_lenders는 loan_id–lender_ids 매핑.
- Kaggle "Data Science for Good: Kiva Crowdfunding": 설명문·STATUS·대출자 ID 없음 → 부적합.
- LendingClub은 2014년 3월 이후 서술문 공개 제한 → 텍스트 표본 2007–2014 한정(이번 집계와 일치).

## References
1. Netzer, O., Lemaire, A., & Herzenstein, M. (2019). When Words Sweat. *Journal of Marketing Research*, 56(6), 960–980.
2. Anglin, A. H., Milanov, H., & Short, J. C. (2023). *Journal of Business Ethics*, 185.
3. Li, L., & Ucar, E. (2022). *International Real Estate Review*, 25(2).
4. Conklin, J., Diop, M., & Qiu, M. (2022). *Journal of Business Ethics*.
5. Baele, L., Farooq, M., & Ongena, S. (2014). *Journal of Banking & Finance*, 44, 141–159.
6. Gyapong, E., Gyimah, D., & Ahmed, A. (2021). *Review of Quantitative Finance and Accounting*.
7. Yan, A., & Yin, W. (2021). EFMA working paper.
8. Cole, R. A., Filatova, U., & Khaled, S. (2023). SSRN 4447681. (미확인)
9. Dorfleitner, G., & Oswald, E.-M. (2016). *Review of Financial Economics*, 30(1), 45–59.
10. Liu, Y., Chen, R., Chen, Y., Mei, Q., & Salib, S. (2012). I Loan Because… *WSDM'12*.
11. Chen, R., Chen, Y., Liu, Y., & Mei, Q. (2015/2017). *Games and Economic Behavior*.
12. Chen, R., et al. (2016). *PNAS*.
13. Ge, L., & Luo, X. (2016). *Financial Innovation*.
14. Sabzehzar, A., Hong, Y., & Santanam, R. (2019). ASU press release. (게재 여부 미확인)
15. Religious affiliation and debt among U.S. households (2023). *Social Science Research*. (미확인)
