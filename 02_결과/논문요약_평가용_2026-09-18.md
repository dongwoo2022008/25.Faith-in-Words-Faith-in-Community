---
title: "논문 요약 (평가용)"
subtitle: "Faith in Words, Faith in Community: Religious Affiliation, Religious Language, and Default in Online Consumer Credit"
date: "2026-09-18 · 김동우 (백석대학교 첨단IT학부)"
---

# 1. 한 문단 요약

온라인 무담보 대출시장(LendingClub, 2007–2018, 종결대출 134만 건)에서 차입자의 종교는 두 가지 서로 다른 형태로 관측된다. 직업란에 드러나는 **종교 기관 소속**(목사·전도사·교회 직원, 3,131건)과 대출 설명문에 쓰인 **종교 언어**("God bless", "as a Christian I pay my debts", 681건)이다. 같은 신용점수·소득·부채·대출조건·주·연도 아래서 전자는 부도 확률이 약 5%p 낮고(OR 0.67), 후자는 약 3%p 높다(OR 1.28). 소속 효과는 목사와 교회 비서에게 똑같이 나타나고, 교회가 많은 지역에서 더 크며, 지역 노동시장 충격에는 반응하지 않고, Prosper에서 재현된다. 종교 언어 효과는 방향이 일관되나 텍스트 전체를 조건화하면 정밀도가 부족하다. 두 신호 모두 플랫폼 가격에 반영되어 있지 않다.

**영문 초록(초안).** Religion enters a consumer-credit file in two ways: as an affiliation a borrower reports in a job title, and as language a borrower chooses to use in a loan request. Using 1.34 million terminated LendingClub loans (2007–2018), I show that the two carry opposite information about default. Borrowers employed by religious institutions — pastors, ministers, and church staff alike — default about five percentage points less than observably identical borrowers, an effect that survives stable-occupation controls, entropy balancing, double machine learning, sensitivity analysis, and replication on Prosper, and that is larger where congregations are denser but unresponsive to local unemployment shocks. Borrowers who invoke faith in their loan description default about three percentage points more; the sign is stable across every specification but the estimate is imprecise once the full text is conditioned on. Neither signal is priced. The evidence is consistent with religious community as a form of borrower-side social collateral, and with religious language as cheap talk.

# 2. 연구질문과 기여

**연구질문(단일).** 차입자의 종교는 소속의 형태와 표현의 형태에서 신용성과에 대해 서로 반대 방향의 정보를 담는가?

**기여 세 가지.**

1. 종교가 대출 파일에 들어오는 두 경로를 구분하고, 같은 자료·같은 통제 아래 두 경로가 반대 부호임을 보인다. 선행연구(Netzer, Lemaire & Herzenstein 2019, JMR)는 종교 언어를 부도 관련 어휘 중 하나로만 다뤘고, 종교 소속을 개인 수준에서 관측한 신용 연구는 확인되지 않는다.
2. 종교성과 금융 문헌은 거의 전부 카운티·국가 단위(Li & Ucar 2022; Conklin, Diop & Qiu 2022; Baele, Farooq & Ongena 2014)이다. 여기서는 개인 수준 신호가 지역 종교성을 통제해도 그대로이고, 지역 종교성 자체는 이 시장에서 보호 효과가 없으며, 개인 소속 효과가 지역 교회 밀도에 비례한다는 것을 보인다. 개인–지역 상호작용은 이 문헌에 없는 결과다.
3. 기제를 세 방향에서 좁힌다. 비성직 교회 직원이 성직자와 같은 효과를 보이므로 소명·서약이 아니라 공동체 소속이 신호이고, 교회 밀도 조절과 실업 충격 무반응은 "소득 안정"보다 "공동체 관찰·평판"과 일치한다. 이는 관계금융·그룹 대출의 사회적 담보 논리를 차입자 측 공동체로 옮긴 것이다.

**이론적 위치.** 첫째 축은 종교 공동체의 사회적 자본(Putnam 2000; Guiso, Sapienza & Zingales 2003, 2006; Iannaccone 1992)과 공동체 대출의 사회적 담보(Besley & Coate 1995; Karlan 2007). 둘째 축은 신호 이론에서 검증 가능·비용 있는 신호(소속)와 검증 불가·무비용 신호(언어)의 구분(Spence 1973; Farrell & Rabin 1996). [서지 원문 확인 필요]

# 3. 자료

- LendingClub 공개 파일 2,260,701건 → 종결대출(Fully Paid / Charged Off / Default) 1,344,976건, 부도율 20.0%. 서술문은 2014년 이후 폐지되어 서술 표본은 2008–2014, 123,292건(부도율 15.3%).
- 종교 기관 소속: 직업란 정규식(성직 역할어 + 종교 조직어, 병원·학교·보험·은행명 제외). 5,014건, 종결 3,131건(성직 2,363 + 교회 직원 768).
- 종교 언어: 명시 사전 + 관용 표현 제외 규칙. 717건, 종결 681건. 두 독립 LLM 코더가 코드북으로 전건 코딩(관용구 467 / 정체성 34 / 실천·지출 82 / 오탐 98), 층화 200건 κ 0.86.
- 외부 결합: ARDA 2010 종교 센서스(카운티 신자율·교회 수), Census ZCTA–카운티 관계표, BLS 카운티 실업률 2008–2018. ZIP3 인구가중, 결합률 99.97%.
- Prosper 공개 파일: 종결 50,270건, 직업 코드 Clergy/Religious 141건.

# 4. 방법 (요약)

확인적 검정은 둘뿐이다. 로짓(주 클러스터 SE), 통제 = 등급·연도·금리·FICO·소득·DTI·기간·금액·근속·주거·소득검증·용도·주 FE; 서술 모형은 log 길이와 도덕·곤경·감사·가족·도움요청·사업 사전 추가. H1 소속 OR < 1, H2 언어 OR > 1, 단측 Holm. 판정 규칙(H2 하향 조건, H1 격하 조건)은 결과 전에 문서화했다.

대안 설명 차단: 안정 직업군 8개 통제, 엔트로피 균형화(76 모멘트), DML(CatBoost, 5-fold; 텍스트 표현 TF-IDF·spaCy 300d·doc2vec 투입), 길이 매칭, 가짜 사전 순열 1,000회, Oster δ·Cinelli–Hazlett RV, Prosper 재현, 지역 종교성 통제, ΔAUC 확인.

기제: 성직 vs 교회 직원 동일 기관 대조, 소속 × 교회 밀도(주 FE·ZIP3 FE), 소속 × 실업 충격(양성 대조 병기), 언어의 무조절, 유형별 분해, 이산시간 hazard.

# 5. 핵심 결과

| | 소속(H1) | 종교 언어(H2) |
|---|---|---|
| 기준 로짓 | OR 0.67–0.69, p < 1e-18, AME −4.8%p | OR 1.28 (사전 포함), Holm p 0.008, AME +3.2%p |
| 기간 분할 | 2008–14 0.61 / 2015–18 0.74 | — (서술문은 2008–14만) |
| 동시 투입 | 0.67 | 1.29 |
| 안정 직업 8개 통제 | 0.69 (불변) | — |
| 엔트로피 균형화 | 0.70 | 길이 매칭 1.34 |
| DML(구조화/사전) | −4.3%p, p 2e-13 | +3.3%p, p 0.027 |
| DML + 텍스트 표현 | — | +2.3~+3.1%p, p 0.06–0.14 → **하향** |
| 가짜 사전 순열 | — | p 0.005 |
| Oster δ / RV | 6.5 / 근속의 12배 | 9.7 / 근속 수준(취약) |
| Prosper 재현 | 0.68, p 0.037 (플라시보 무의미) | 텍스트 없음 |
| 지역 종교성 통제 | 0.69 (불변) | 1.28 (불변) |

**기제.** 성직 0.675 vs 교회 직원 0.679(동일). 소속 × 교회 밀도 OR 0.84 (p 0.003; ZIP3 FE LPM −2.2%p/SD, p 0.027); 지역 종교성 삼분위별 소속 효과 0.71 / 0.83 / 0.58. 소속 × 실업 충격 0.98 (p 0.69; 교사·공무원 양성 대조도 무의미 → 검정력 한계). 종교 언어 × 지역 종교성 1.07 (p 0.50). 유형별: 관용구 1.39 (p 0.001), 실천·지출 0.99. Hazard: 소속 효과 기간 전체 균일, 언어 효과 12개월 이후에만.

**지역 종교성 자체.** 주 내에서 신자율·교회 밀도가 높을수록 부도 소폭 높음(OR 1.04–1.06/SD). 모기지 문헌(Li & Ucar 2022)과 반대 방향 — 설명 없이 대비로 보고.

**경제적 크기.** 같은 sub_grade×연도 대비 소속 대출 연 64bp 과대 가격, 종교 언어 대출 연 28bp 과소 가격. 예측력(ΔAUC ≈ 0.0001)은 개선되지 않으며 주장하지 않는다.

# 6. 주장하지 않는 것·한계

- 인과 효과: 외생적 변동이 없다(도구변수·자연실험 없음, 반복 차입자 패널은 member_id 결측으로 불가). 민감도·이질성·동일 기관 대조로 대체하며 각각의 한계를 명시한다.
- 예측력 개선: 두 신호는 표본의 0.2–0.6%에만 존재한다.
- H2: 방향은 일관되나 정밀도 부족. 사전 밖 종교 표현을 분류기로 탐색한 결과 수십 건 규모라 표본 확대 불가(모집단 크기의 문제).
- 소득 안정 기제를 기각하지는 못한다(양성 대조 무의미).
- 서술문 표본은 2008–2014에 한정.

# 7. 저널 적합성 (저자 추정)

JEBO(1순위) → JBE → JFSR/IRFA. JBF급은 식별 부재로 낮음. 신앙융합 해석("고백과 소속")은 논의 절 한 문단.

# 8. 평가자에게 묻고 싶은 점

1. "공동체 소속 → 낮은 부도"의 사회적 담보 해석이 관계금융 문헌과의 연결로 충분히 설득력 있는가, 아니면 고용 안정성 반론이 여전히 우세한가?
2. H2를 "방향 일관·정밀도 부족"으로 하향해 보고하는 것이 논문의 대비 구조를 약하게 하는가, 아니면 신뢰성을 높이는가?
3. 지역 종교성이 보호 효과가 없다는 결과를 본문에 둘 것인가, 부록으로 내릴 것인가?
4. 이 결과 조합으로 JEBO/JBE가 현실적인가, 아니면 JFSR/IRFA로 바로 가는 것이 나은가?
