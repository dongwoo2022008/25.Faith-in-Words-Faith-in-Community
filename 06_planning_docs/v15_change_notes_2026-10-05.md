# v15 수정내역 (2026-10-05) — 외부 검토 의견 반영

기준: v14 → v15. 외부 검토 의견(JEBO 지침 대조 + 수치·표·해석 검토)을 원고, 저장된 추정 결과 JSON(02_results/estimates_json), 원자료로 대조해 타당한 항목만 반영했다. 재분석 없음, 수치 변경 없음. 본문 11,758단어, 29쪽, selfcheck 통과(em dash 0, 세미콜론 3.46/1000).

## 반영 (30건)

### 사실 오류
- 5.1 "the later, lower-default years" → "the later years". 원자료 종료대출 부도율: 2008–2014 0.170, 2015–2018 0.215로 후기가 더 높음.
- Table 2 노트: DML 열의 −4.3 pp는 PLR 계수(θ = −0.0426), ATTE는 같은 실행의 별도 값(−0.042). 노트를 "the entry is the partially linear coefficient … The ATTE from the same run is −0.042"로 분리(step4_dml.json 확인).
- Appendix Table A1 행 라벨 "Affiliation (clergy definition)" → "Affiliation (all 3,105 affiliated loans)"; 노트에 대조군 부표본 크기(30,000 / 8,000) 추가(step6_hazard.json 확인).
- Table 7 노트: 길이 매칭은 복원 추출 5:1, N은 고유 대출 수(681 처리 + 2,891 대조)임을 명시(lc_two_signal_analysis_results.json H2_matched).
- Figure 2 캐프션: 신뢰구간을 "exact Wald p-value"에서 복원했다고 명시(fig2 스크립트 확인: 표시용 임계값이 아닌 JSON의 정확한 p 사용).
- Appendix B3: "— of which issued in 2007 | 0" 행 추가(85,132 + 167,973 = 253,105).
- 5.1 *Mission-driven jobs*: "the affiliation OR is 0.690, 0.679 and 0.747"의 집단 대응을 명시(stepN_neighbour.json: social work 0.690, healthcare 0.679, education 0.747).

### 해석 정정·완화
- 5.5, 6.2 ZIP3 FE 해석: 밀도는 ZIP3 고정값이므로 FE 하의 상호작용은 "ZIP 내부 소속 격차가 ZIP 간 밀도에 따라 더 큰가"를 추정. 5.5에 "including density itself, so the interaction asks whether the within-area affiliation gap is larger in denser areas" 추가; 6.2 "it grows within ZIP areas as well as across them" → "the within-area gap is larger in denser areas once ZIP3 fixed effects are added".
- 5.1 종료대출 선택: 2008–2014 열이 성숙 vintage 검사임을 명시 ("Every loan issued in those years had reached maturity by the 2018Q4 release, so keeping only terminated loans selects nothing there, whereas among 2015–2018 loans a terminated status can mean early repayment or early default"). 3.1에 자료 기준일(2018Q4 release) 추가.
- 5.4 키워드 분할 vs 역할: "Table 10 splits the indicator by whether the title contains a clerical role word. That is a keyword split, not a judgment of each role" + B2 감사(146/48 vs 80:20) 비교 + 오분류는 두 집단을 닮게 해 차이 발견에 불리하다는 문장 추가.
- 4.3: β₁ < β₂ 예측이 "성직자가 서약과 더 안정적 고용을 갖는다"는 추가 가정에 의존함을 명시.
- 5.2: "Religious wording cannot be separated…" → "The rich-text specifications do not estimate a distinct association for religious wording with enough precision to separate it from the rest of the text…".
- 6.1: "a congregation that will know" → "can learn"; hazard 문장을 연관 표현으로("Religious language is not associated with a higher hazard in the first year … The positive association appears only after a year"); Oster 문장에 "Under Oster's proportional-selection assumption" 추가.
- 6.3: "64 basis points a year of yield" → "an annualized realized net-loss gap of roughly 64 basis points"; 28bp도 같은 명명.
- 3.4, Appendix C6: 실업률 측정을 "largest subsequent change … truncated at 2018"으로 정확히 서술, C6 노트에 음수 가능성(대부분 음수) 명시.
- 1장: "The same platform contains" → "The LendingClub file contains"(앞 문장이 Prosper); "Same platform, same years, same controls" → "Same platform, same controls"(H2는 2008–2014 표본).
- 2.1: Deng et al. (2025) "local trust" → "local social capital"(논문 제목 기준).
- 3.3: "three times longer than the median" → "The median description that contains it is three times as long as the median other description".
- Table 3 제목·Appendix Table A2 제목의 "affiliation effect" → "affiliation estimate"; 5.1 "If the affiliation effect were" → "gap". 원고 내 "affiliation effect" 0건.
- Appendix B1 노트: 프롬프트·모델 식별자·설정이 재현 패키지에 있음을 명시.

## 반영하지 않음 (이유)
- "replace vs dictionaries + text 충돌": 원고는 대체가 아니라 추가로 서술하고 있음(JSON 키 DML_H2_dict_text). 충돌 없음.
- Table 2 (4) SE, (4)·(5) AME, Table 4 H2 벤치마크 공란: 원 결과에 값이 없어 재추정 없이는 채울 수 없음.
- "a church secretary has neither": Table 1(직원 소득 중앙값 53,000)로 뒷받침되므로 유지.
- Iyer (2016) / Iyer et al. (2016): 이미 구분됨.
- 부록 번호 A.1 형식, 직렬 쉼표: 저널 교열 사항.
- 성숙 vintage 재추정, 성직 재분류 민감도, 종교 단어 마스킹 DML: 기존 결과(Table 2 기간 분할, B2 감사)로 대응 가능하므로 보류. 심사 요구 시 수행.
- "default about five percentage points less" 등 문체 제안 일부: 경제학 관행상 문제 없음.

## 저자 확인 필요
- 부록 B1에 "prompt, model identifiers and settings are in the replication package"로 적었으므로, 1차·2차 LLM 코더의 모델명·버전과 프롬프트를 재현 패키지(코드 저장소)에 실제로 넣어야 함. 모델명은 원고에 기재하지 않았음(미확인 상태라 임의 기재하지 않음).
- 사전 지정 근거 문서(2026-09-17 연구질문확정안·방법론설계)를 저장소에 날짜와 함께 포함할지.

## 파일
01_원고/manuscript_v15.md, manuscript_v15_JEBO.docx, manuscript_v15_JEBO.pdf; 03_코드/원고빌드/build_v15.py, apply_v15.py(v14→v15 치환 목록).
