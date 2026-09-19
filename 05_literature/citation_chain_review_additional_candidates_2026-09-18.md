# 추가 인용 후보 — 참고문헌 32편의 인용 사슬 검토 (2026-09-18)

## 방법과 범위

원고 v2의 참고문헌 32편 중 방법론·자료 문헌 6편(Chernozhukov, Cinelli–Hazlett, Grammich, Hainmueller, Oster, Rajan–Zingales)을 제외한 26편에 대해 각 논문의 참고문헌 목록을 Crossref API·출판사 페이지·RePEc·arXiv로 수집했고(후방 추적), 핵심 3편(Baele 2014, He & Hu 2016, Netzer 2019)에 대해서는 이들을 인용한 2015–2026년 논문도 Semantic Scholar로 톥었다(전방 추적). 후보는 모두 출판사·DOI·RePEc 페이지에서 서지를 확인했고, 초록을 직접 읽지 못한 것은 표에 표시했다. 확인되지 않은 것은 마지막 절에 따로 둔다.

수집 범위: 26편 중 22편은 참고문헌 전체를 확보했다. 확보하지 못한 것은 Iannaccone 1992·1994(출판사가 참고문헌을 공개하지 않음), Guiso–Sapienza–Zingales 2004(Crossref 13건만; CEPR 판본 21건으로 보완), Spence·Crawford–Sobel·Farrell–Rabin(고전 이론 논문이라 참고문헌 대신 신용시장 적용 후속 문헌으로 대체)이다.

부수적으로 발견한 서지 오류 하나: Conklin, Diop & Qiu (2022)의 DOI는 10.1007/s10551-021-04831-2이다(04832-1은 다른 논문). 원고 참고문헌에는 DOI를 싣지 않으므로 수정할 것은 없으나 투고 시스템 입력 때 주의.

## 1순위 — 심사자가 없는 것을 알아챌 문헌 (원고에 반드시 반영 권고, 14편)

| 문헌 | 실제 결과 | 넣을 곳과 문장 | 사슬 |
|---|---|---|---|
| Herzenstein, M., Sonenshein, S., & Dholakia, U. M. (2011). Tell me a good story and I may lend you money: The role of narratives in peer-to-peer lending decisions. *Journal of Marketing Research*, 48(SPL), S138–S149. doi:10.1509/jmkr.48.SPL.S138 | Prosper 서술문의 정체성 주장("trustworthy", "moral")이 많을수록 펀딩은 늘지만 상환은 나빠짐 | 2.2절·5.2절. 종교 언어 OR 1.28의 가장 가까운 선행 결과. "Unverifiable identity claims in Prosper narratives raise funding but predict worse repayment (Herzenstein et al., 2011)." | Netzer 2019; Sanz-Guerrero 2025 |
| Michels, J. (2012). Do unverifiable disclosures matter? Evidence from peer-to-peer lending. *The Accounting Review*, 87(4), 1385–1413. doi:10.2308/accr-50159 | Prosper에서 검증 불가 자발적 공시 1건당 금리 1.27%p 하락, 입찰 8% 증가 | 2.2절·6.1절. Prosper 투자자는 검증 불가 텍스트를 가격에 반영했는데 LendingClub은 그렇지 않았다는 대비. | Sanz-Guerrero 2025 |
| Iyer, R., Khwaja, A. I., Luttmer, E. F. P., & Shue, K. (2016). Screening peers softly: Inferring the quality of small borrowers. *Management Science*, 62(6), 1554–1577. doi:10.1287/mnsc.2015.2181 | Prosper 대출자들이 신용점수 밖의 연성 정보로 신용도를 추론 | 1절·2.2절. 직업란·서술문을 "연성 정보"로 자리매김하는 표준 인용. | 전방 탐색 |
| Lin, M., Prabhala, N. R., & Viswanathan, S. (2013). Judging borrowers by the company they keep: Friendship networks and information asymmetry in online peer-to-peer lending. *Management Science*, 59(1), 17–35. doi:10.1287/mnsc.1120.1560 | Prosper의 검증된 친구 관계가 펀딩↑·금리↓·사후 부도↓ | 1절·2.1절. 온라인 대출에서 "공동체 신호가 부도를 낮춘다"는 유일한 선행 결과. 소속(공동체) vs 언어(자기 주장) 대비의 출발점. | Nowak 2018 |
| Duarte, J., Siegel, S., & Young, L. (2012). Trust and credit: The role of appearance in peer-to-peer lending. *Review of Financial Studies*, 25(8), 2455–2484. doi:10.1093/rfs/hhs071 | 신뢰감 있는 외모의 Prosper 차입자는 펀딩·금리가 유리하고 실제 부도도 낮음 | 2.2절·6.1절. 정보가 있고 가격에도 반영된 연성 신호의 대조 사례. | He & Hu 2016 |
| Gao, Q., Lin, M., & Sias, R. (2023). Words matter: The role of readability, tone, and deception cues in online credit markets. *Journal of Financial and Quantitative Analysis*, 58(1), 1–28. doi:10.1017/S0022109022000850 | 읽기 쉽고 긍정적이며 기만 단서가 적은 서술문은 펀딩·부도 모두 유리하지만 투자자는 텍스트에 과소 반응 | 5.2절·6.1절. "텍스트는 정보가 있는데 가격에 덜 반영된다"는 우리 결과(연 28bp)와 같은 패턴. | 전방 탐색 |
| Davaadorj, Z., Enkhtaivan, B., & Lu, W. (2025). Character and creditworthiness: Unveiling the role of job titles in peer-to-peer lending. *Journal of Financial Research*, 49(3), 1205–1228. doi:10.1111/jfir.70016 | Prosper에서 신뢰도 높은 직업의 차입자가 펀딩 확률과 투자자 수익이 높음 — 직업란이 성격 정보를 담음 | 1절·3.2절·5.1절. 직업란을 신용 정보로 쓴 직접 선행. 반드시 인용하고 차이(우리는 종교 기관 소속, 부도 결과)를 명시. | 전방 탐색 |
| Hilary, G., & Hui, K. W. (2009). Does religion matter in corporate decision making in America? *Journal of Financial Economics*, 93(3), 455–473. doi:10.1016/j.jfineco.2008.10.001 | ARDA 카운티 종교성이 높을수록 기업 위험 노출·투자 낮음 | 3.4절·5.5절. ARDA 자료를 금융 연구에 쓴 표준 선행. 우리 출처 8편 중 6편이 인용 — 빠져 있으면 눈에 띄임. | Chen 2016; He & Hu; Davidson; Conklin; Clifton; Li & Ucar |
| Stiglitz, J. E. (1990). Peer monitoring and credit markets. *World Bank Economic Review*, 4(3), 351–366. doi:10.1093/wber/4.3.351 | 동료 감시가 위험을 공동 채무자에게 이전하면서 차입자 후생을 높임 | 2.1절. Besley–Coate 옆에 놓이는 "동료 감시"의 원전. | Besley & Coate; Karlan |
| Ghatak, M., & Guinnane, T. W. (1999). The economics of lending with joint liability: Theory and practice. *Journal of Development Economics*, 60(1), 195–228. doi:10.1016/S0304-3878(99)00041-3 | 연대 책임이 선별·감시·집행·감사의 네 문제를 푸는 경로를 정리 | 2.1절. 종교 공동체가 담보로 작동하는 경로를 네 가지로 나눠 말할 수 있게 해 줌 — 목사/비서·교회 밀도 결과가 어느 경로에 대응하는지 서술 가능. | Karlan |
| Clark, B., Hasan, I., Lai, H., Li, F., & Siddique, A. (2021). Consumer defaults and social capital. *Journal of Financial Stability*, 53, 100821. doi:10.1016/j.jfs.2020.100821 | 신용정보 계정 자료: 사회자본 높은 지역 차입자의 부도가 낮고, 전략적 모기지 부도에서 가장 큼 | 2.1절·5.5절. 소비자 신용에서 "부도의 사회적 비용"을 보인 가장 가까운 문헌. | Li & Ucar 2022 |
| Guiso, L., Sapienza, P., & Zingales, L. (2013). The determinants of attitudes toward strategic default on mortgages. *Journal of Finance*, 68(4), 1473–1515. doi:10.1111/jofi.12044 | 전략적 부도 의사는 도덕적 견해와 주변의 부도 관찰(사회적 전염)에 좌우됨 | 2.1절. 부도의 도덕 비용과 사회적 영향. GSZ 2003·2004는 있는데 이 논문이 없는 것은 어색함. | Baele 2014; Li & Ucar |
| Jiang, F., John, K., Li, C. W., & Qian, Y. (2018). Earthly reward to the religious: Religiosity and the costs of public and private debt. *Journal of Financial and Quantitative Analysis*, 53(5), 2131–2160. doi:10.1017/S002210901800039X | 종교성 높은 카운티 기업의 신용등급↑·부채 비용↓, 정보 비대칭·불황기에 더 강함 | 6.1절. 기업 부채시장은 종교성을 가격에 반영하는데 LendingClub은 소속을 반영하지 않았다는 대비. | Davidson; Conklin; Li & Ucar |
| Kirchmaier, I., Prüfer, J., & Trautmann, S. T. (2018). Religion, moral attitudes and economic behavior. *Journal of Economic Behavior & Organization*, 148, 282–300. doi:10.1016/j.jebo.2018.02.022 | 종교인은 비윤리 행동에 더 반대한다고 말하지만 관찰되지 않는 신뢰 게임에서는 배신율이 같음 | 2.2절·5.2절. "말해진 도덕"과 "관찰되지 않을 때의 행동"의 간극 — H2 해석의 이론적 근거. JEBO 게재. | Lei 2024; Valencia Caicedo 2023 |

## 2순위 — 논거를 강화하는 문헌 (선택 반영, 16편)

| 문헌 | 실제 결과 | 넣을 곳 | 사슬 |
|---|---|---|---|
| Wang, C., Wang, J., Wu, C., & Zhang, Y. (2023). Voluntary disclosure in P2P lending: Information or hyperbole? *Pacific-Basin Finance Journal*, 79, 102024. doi:10.1016/j.pacfin.2023.102024 | 독특한 자기 서술은 펀딩을 높이지만 부도·금리도 높음 | 5.2절 — H2 부호의 선행 | Netzer 인용 문헌 |
| Lun, X., Meng, X., & Xu, J. (2024). Is cheap talk just empty words? The signalling value of voluntary promises for loan repayment. *Applied Economics Letters*, 31(17), 1737–1741. doi:10.1080/13504851.2023.2206608 | 자발적 상환 약속이 신규 차입자에서는 상환↑, 재차입자에서는 상환↓ | 2.2절 — cheap talk의 실증 검정 | Netzer 인용 문헌 |
| Hasan, I., Kiesel, K., & Noth, F. (2025). "And forgive us our debts": Christian moralities and over-indebtedness. *Journal of Financial Research*, 48(3), 1013–1031. doi:10.1111/jfir.12436 | 독일에서 가톨릭 우세 지역의 가계 과다부채가 낮음 | 5.5절 — 지역 종교 구성과 가계 부채 곤경 | Baele 인용 문헌 |
| Al-Azzam, M., Hill, R. C., & Sarangi, S. (2012). Repayment performance in group lending: Evidence from Jordan. *Journal of Development Economics*, 97(2), 404–414. doi:10.1016/j.jdeveco.2011.06.006 | 동료 감시·사회적 유대와 함께 차입자 종교성이 상환을 높임 | 2.1절 — 사회적 담보와 종교를 잇는 직접 증거 | Baele 2014 |
| Feigenberg, B., Field, E., & Pande, R. (2013). The economic returns to social interaction: Experimental evidence from microfinance. *Review of Economic Studies*, 80(4), 1459–1483. doi:10.1093/restud/rdt016 | 모임 빈도를 무작위로 늘리자 다음 대출 부도가 1/3로 감소 | 2.1절·5.3절 — 반복 대면 상호작용 자체가 부도를 낮춘다는 인과 증거 | Deng 2025 |
| Giné, X., & Karlan, D. (2014). Group versus individual liability. *Journal of Development Economics*, 107, 65–83. doi:10.1016/j.jdeveco.2013.11.003 | 연대 책임을 없애도(모임은 유지) 부도가 늘지 않음 | 2.1절·6.4절 — 대출자가 그룹 계약을 두지 않아도 공동체가 규율한다는 점, LendingClub 상황과 동일 | Karlan |
| Cassar, A., Crowley, L., & Wydick, B. (2007). The effect of social capital on group loan repayment. *Economic Journal*, 117(517), F85–F106. doi:10.1111/j.1468-0297.2007.02016.x | 구성원 간 개인적 신뢰가 일반화된 사회 신뢰보다 상환을 잘 예측 | 5.5절 — 개인 소속(밀도 높은 유대)은 작동하고 지역 종교성(일반화)은 작동하지 않는 이유 | Karlan |
| Karlan, D. S. (2005). Using experimental economics to measure social capital and predict financial decisions. *American Economic Review*, 95(5), 1688–1699. doi:10.1257/000282805775014407 | 신뢰 게임에서 "신뢰받을 만함"을 보인 사람이 부도가 낮음 | 2.1절 | Karlan 2007 |
| Iannaccone, L. R. (1998). Introduction to the economics of religion. *Journal of Economic Literature*, 36(3), 1465–1495. | 종교경제학 개관(클럽재 모형 포함) | 2.1절 — 1992·1994와 함께 표준 인용 | GSZ 2003 |
| Iyer, S. (2016). The new economics of religion. *Journal of Economic Literature*, 54(2), 395–441. doi:10.1257/jel.54.2.395 | 최신 종교경제학 서베이 | 1절·2.1절 | Valencia Caicedo; Lei; Clifton |
| Noussair, C. N., Trautmann, S. T., van de Kuilen, G., & Vellekoop, N. (2013). Risk aversion and religion. *Journal of Risk and Uncertainty*, 47(2), 165–183. doi:10.1007/s11166-013-9174-8 | 교회 소속의 위험회피 효과는 믿음이 아니라 사회적 참여에서 나옴 | 5.3절·6.4절 — "사회적, 교리 아님" 패턴이 목사/비서 결과와 일치; 위험 선호라는 대안 경로도 명시 | Lei; Conklin; Li & Ucar; Deller |
| Renneboog, L., & Spaenjers, C. (2012). Religion, economic attitudes, and household finance. *Oxford Economic Papers*, 64(1), 103–127. doi:10.1093/oep/gpr025 | 종교 가구는 신뢰·계획 시야·저축 성향이 높음 | 6.4절 — 공동체 감시와 무관한 개인 선호 경로(한계로 명시) | Lei; Clifton; Li & Ucar; Valencia Caicedo |
| Hertzberg, A., Liberman, A., & Paravisini, D. (2018). Screening on loan terms: Evidence from maturity choice in consumer credit. *Review of Financial Studies*, 31(9), 3532–3567. doi:10.1093/rfs/hhy024 | LendingClub 차입자의 만기 선택이 신용 파일 밖의 사적 정보를 드러냄 | 2.2절·6.1절 — 같은 플랫폼에서 차입자 선택이 정보를 담는다는 선행 | 전방 탐색 |
| Kartik, N. (2009). Strategic communication with lying costs. *Review of Economic Studies*, 76(4), 1359–1395. doi:10.1111/j.1467-937X.2009.00559.x | 거짓말에 작은 비용만 있어도 cheap talk이 부분적으로 정보를 가짐 | 2.2절 — 종교 언어가 정보를 가질 수 있는(그리고 그 방향이 발신자 의도와 다를 수 있는) 이론적 다리 | Crawford–Sobel 후속 |
| Dehejia, R., DeLeire, T., & Luttmer, E. F. P. (2007). Insuring consumption and happiness through religious organizations. *Journal of Public Economics*, 91(1–2), 259–279. doi:10.1016/j.jpubeco.2006.05.004 | 종교 조직 기여 가구는 소득 충격에 대해 소비를 보험함 | 5.4절 — 실업 충격 무반응의 해석(공동체 보험 경로) | Chen 2016 |
| Kriebel, J., & Stitz, L. (2022). Credit default prediction from user-generated text in peer-to-peer lending using deep learning. *European Journal of Operational Research*, 302(1), 309–323. doi:10.1016/j.ejor.2021.12.024 | LendingClub 짧은 서술문도 부도 예측을 개선; 단순 임베딩 평균이 BERT와 대등 | 3.3절·4절 — 텍스트 표현 통제의 근거이자 BERT 미적용에 대한 방어 | Netzer 인용 문헌; Sanz-Guerrero |

## 3순위 — 특정 문장에 쓸 수 있는 문헌 (12편)

| 문헌 | 넣을 곳 |
|---|---|
| Dorfleitner, G., et al. (2016). Description-text related soft information in peer-to-peer lending. *JBF*, 64, 169–187. doi:10.1016/j.jbankfin.2015.11.009 — 텍스트는 펀딩에 영향, 부도 예측력은 약함 | 5.2절 |
| Demiroglu, C., Ozbas, O., Silva, R. C., & Ulu, M. F. (2021). Do physiological and spiritual factors affect economic decisions? *Journal of Finance*, 76(5), 2481–2523. doi:10.1111/jofi.13032 — 라마단 중 실행 대출은 부도 15%↑인데 스프레드는 낮음 | 6.1절 — 종교 요인의 비반영 가격 |
| Rama, A., Jiang, C., Johan, S., Liu, H., & Mai, Y. (2022). Religious and social narratives and crowdfunding success. *JIFMIM*, 80, 101595. doi:10.1016/j.intfin.2022.101595 — 종교 정체성 서술이 후원자를 늘림 | 6.3절 |
| Lim, C., & Putnam, R. D. (2010). Religion, social networks, and life satisfaction. *ASR*, 75(6), 914–933. doi:10.1177/0003122410386686 — 효과는 교회 내 친구 관계를 통함 | 2.1절·5.3절 |
| Traunmüller, R. (2011). Moral communities? *European Sociological Review*, 27(3), 346–363. doi:10.1093/esr/jcq011 — 개인 출석은 신뢰를 높이나 지역 종교성은 맥락 효과 없음 | 5.5절 — 개인 vs 지역 설계의 평행 사례 |
| Wuthnow, R. (2002). Religious involvement and status-bridging social capital. *JSSR*, 41(4), 669–684. doi:10.1111/1468-5906.00153 — 지도적 역할이 네트워크 연결을 예측 | 5.3절 위계 결과 |
| Jiang, D., & Lim, S. S. (2018). Trust and household debt. *Review of Finance*, 22(2), 783–812. doi:10.1093/rof/rfw055 — 신뢰 높은 개인의 가계 부채 부도 낮음 | 2.1절 |
| Kuhnen, C. M., & Melzer, B. T. (2018). Noncognitive abilities and financial delinquency. *Journal of Finance*, 73(6), 2837–2869. doi:10.1111/jofi.12724 — 자기효능감이 충격 후 연체를 낮춤 | 6.4절 — 미관측 특성 대안 |
| Maturana, G., & Nickerson, J. (2019). Teachers teaching teachers. *RFS*, 32(10), 3920–3957. doi:10.1093/rfs/hhy136 — 직장 동료 효과가 금융 결정을 바꿈 | 5.3절 — 직장을 공동체로 보는 관점 |
| Cwynar, A., Potocki, T., Białowolski, P., & Węziak-Białowolska, D. (2024). Religious service attendance and consumer financial outcomes. *Economics and Business Review*, 10(4), 101–128. doi:10.18559/ebr.2024.4.1225 — 출석이 저축↑·부채↓, 사회적 접촉이 매개 | 2.1절 |
| Gyapong, E., Gyimah, D., & Ahmed, A. (2021). Religiosity, borrower gender and loan losses in microfinance institutions. *RQFA*, 57(2), 657–692. doi:10.1007/s11156-021-00958-5 — 종교성의 손실 감소는 대출자 위험회피 경로 | 5.5절·6.4절 — 지역 종교성 효과가 대출자 쪽일 수 있음 |
| Benjamin, D. J., Choi, J. J., & Fisher, G. (2016). Religious identity and economic behavior. *REStat*, 98(4), 617–637. doi:10.1162/REST_a_00586 — 종교 정체성 점화의 효과는 교파별로 상이하고 크지 않음 | 2.2절 |

서지는 확인했으나 초록을 직접 읽지 못한 것(인용 전 초록 확인 필요): Li, Ucar & Yavas (2022) JREFE 64(3), 379–403; Adhikari & Agrawal (2016) JCF 38, 272–293; Keys (2018) REStat 100(3), 405–415; Rupasingha, Goetz & Freshwater (2006) J. Socio-Economics 35(1), 83–101; Keister (2003) Social Forces 82(1), 175–207; Galen (2012) Psychological Bulletin 138(5), 876–906.

## 미확인 — 인용 불가

Gao & Lin, "Lemon or cherry? The value of texts in debt crowdfunding" (UCSC CAFIN WP, 2015; SSRN 2446114) — 널리 인용되는 워킹페이퍼이나 게재본 미확인. Cong, Guo, Zhao & Zhou (2024) "Writing quality and soft information in the GenAI age" (SSRN 4959535) — 존재는 확인, 초록 페이지 접근 불가. Khan (2010) 예금자 행동 WP, Ostergaard–Schindele–Vale (2013) mimeo, Bai et al. (2020) SSRN — Baele·Conklin이 인용한 미게재 원고.

## 권고

1순위 14편은 전부 넣을 것을 권한다. 그중 원고 논리에 실제로 변화를 주는 것은 넷이다. Davaadorj 외 (2025)는 "직업란을 신용 정보로 쓴 선행이 없다"는 인상을 줄 수 없게 하므로 1절과 3.2절에서 차이를 명시해야 한다. Herzenstein 외 (2011)와 Michels (2012)는 H2가 Netzer 한 편이 아니라 "검증 불가 자기 서술" 문헌 전체와 대화하게 만든다. Lin 외 (2013)는 온라인 대출에서 공동체 신호가 부도를 낮춘 유일한 선행이라 H1의 자리를 정해 준다. 나머지 열 편은 문헌 절의 빈자리(동료 감시 원전, ARDA 표준 인용, 소비자 부도와 사회자본, 기업 부채의 종교성 가격 반영)를 메운다.

2순위는 2.1절 사회적 담보 문단과 5.5절 개인/지역 대비 문단을 두꺼게 하는 데 쓰인다. 특히 Cassar 외 (2007)와 Traunmüller (2011)는 "개인 소속은 작동하고 지역 종교성은 작동하지 않는다"는 결과에 평행 사례를 제공하므로 5.5절에 한 문장씩 넣을 가치가 있다. Kriebel & Stitz (2022)는 리뷰어의 BERT 요구에 대한 문헌상 답(단순 임베딩이 BERT와 대등)이 된다.

원고에 반영하면 참고문헌은 32편에서 46편(1순위만) 또는 62편(2순위까지)이 된다. JEBO 논문의 통상 범위 안이다.

---

## 2회차·3회차 — 포화 검정 (2026-09-19)

1회차에서 새로 찾은 핵심 6편(Herzenstein 2011, Michels 2012, Lin 2013, Davaadorj 2025, Clark 2021, Kirchmaier 2018)에 대해 전방·후방 추적을 한 번 더 했고(2회차: 인용 논문 약 1,970건, 참고문헌 약 330건 검토, Iyer 2016 JEL 서베이의 참고문헌 159건으로 시작 집합 독립성 점검), 거기서 나온 핵심 3편(Lu 2020, Agarwal 2017, Hasan–He–Lu 2022)과 Davaadorj 2024에 대해 3회차를 돌렸다(인용 122건, 참고문헌 156건).

결과: 2회차 핵심 신규 9편, 3회차 핵심 신규 1편(Karlan, Möbius, Rosenblat & Szeidl 2009 — "social collateral"이라는 용어의 원전, 1·2회차에서 Karlan 2005·2007에 가려 누락). 3회차에서 심사자가 요구할 만한 문헌이 한 편으로 떨어졌으므로 **포화로 판정하고 탐색을 종료**한다. 종교×소비자 신용 축은 2회차에서 이미 포화였고, 남은 신규 문헌은 전부 인접 축(P2P의 지역 사회자본, 직업 정보, 검증 불가 공시 이론)에서 나왔다.

### 2·3회차 핵심 신규 — 원고 v4에 반영 (10편)

| 문헌 | 실제 결과 | 넣은 곳 | 사슬 |
|---|---|---|---|
| Karlan, D., Möbius, M., Rosenblat, T., & Szeidl, A. (2009). Trust and social collateral. *QJE*, 124(3), 1307–1361. doi:10.1162/qjec.2009.124.3.1307 | 네트워크 유대의 가치가 비공식 대출의 "사회적 담보"; 밀도 높고 동질적인 공동체에서 신뢰가 큼 | 2.1 — 용어의 원전이자 교회 밀도 예측의 모형 | Davaadorj 2024 후방 |
| Hasan, I., He, Q., & Lu, H. (2022). Social capital, trusting, and trustworthiness: Evidence from peer-to-peer lending. *JFQA*, 57(4), 1409–1453. doi:10.1017/S0022109021000259 | 중국 P2P에서 사회자본 높은 지역 차입자의 펀딩↑·부도↓ | 2.1 | Lin 2013·Herzenstein 2011 전방 |
| Lu, H., Wang, B., Wang, H., & Zhao, T. (2020). Does social capital matter for peer-to-peer lending? *PBFJ*, 61, 101338. doi:10.1016/j.pacfin.2020.101338 | LendingClub 2008–2018: 사회자본 높은 주의 차입자 부도↓ | 2.1 (5.5 지역 종교성 결과의 직접 비교 대상) | Davaadorj 2025 후방 |
| Ge, R., Feng, J., Gu, B., & Zhang, P. (2017). Predicting and deterring default with social media information in peer-to-peer lending. *JMIS*, 34(2), 401–424. doi:10.1080/07421222.2017.1334472 | 부도를 사회적 접촉에 노출시키면 부도가 줄어듦(사회적 낙인) | 2.1 | Lin 2013 전방 |
| Davaadorj, Z., Enkhtaivan, B., & Lu, W. (2024). The role of job titles in online peer-to-peer lending. *JBEF*, 41, 100890. doi:10.1016/j.jbef.2024.100890 | LendingClub 16만 건: 숙련 직함이 금리↓·부도↓ | 서론·5.1 — 같은 저자 2025 JFR과 짝 | Davaadorj 2025 후방·전방 |
| Agarwal, S., Chomsisengphet, S., & Zhang, Y. (2017). How does working in a finance profession affect mortgage delinquency? *JBF*, 78, 1–13. doi:10.1016/j.jbankfin.2017.01.019 | 금융 종사자의 모기지 연체가 관측 변수 통제 후에도 낮음 | 5.1 — H1과 가장 가까운 설계(직업→부도) | Davaadorj 2025 후방 |
| Freedman, S., & Jin, G. Z. (2017). The information value of online social networks. *IJIO*, 51, 185–222. doi:10.1016/j.ijindorg.2016.09.002 | Prosper의 사회적 유대가 펀딩·금리엔 유리하나 부도는 오히려 높음 — 대출자의 오독 | 서론 — 연성 신호가 반대 방향으로 잘못 가격될 수 있음 | Michels·Davaadorj 후방 |
| Caldieraro, F., Zhang, J. Z., Cunha, M., Jr., & Shulman, J. D. (2018). Strategic information transmission in peer-to-peer lending markets. *Journal of Marketing*, 82(2), 42–63. doi:10.1509/jm.16.0113 | 검증 불가 정보 전달과 대출 질의 관계가 비단조 | 2.2 | Lin·Michels 전방 |
| Chen, D. L. (2010). Club goods and group identity. *JPE*, 118(2), 300–354. doi:10.1086/652462 | 경제 위기 때 종교 강도↑, 종교 기관이 사후 보험 역할 | 5.4 — 실업 충격 무반응의 해석 | Iyer 2016 후방 |
| Adbi, A., Lee, M., & Singh, J. (2024). Community influence on microfinance loan defaults under crisis conditions. *SMJ*, 45(3), 535–563. doi:10.1002/smj.3558 | 인도 화폐개혁 때 부도가 종교적 유대를 따라 확산 | 5.4 — 종교 유대의 반대 방향 가능성 | Lin 2013 전방 |

### 2·3회차 주변 신규 — 미반영 (후보 보존)

Xu & Chau (2018) JMIS 35(1) 53–85 (대출자–차입자 소통은 펀딩만 움직임); Goel & Ren (2026) JCF 96, 102915 (씨족 문화와 P2P 부도); Lu, Lu, Wang & Wu (2021) POM 30(8) 2564–2585 (사회적 통지 RCT); Baek 외 (2021) Managerial Finance 47(3); Davaadorj 외 (2025) AEL 고용정보 공시(초록 미확인); Diao 외 (2026) FRL 88; Gaganis 외 (2023) AOR; von Bieberstein 외 (2020) FBR; Levy & Razin (2012) AEJ Micro 4(3) 121–151; Hasan, Hoi, Wu & Zhang (2017) JFQA 52(3); Scheve & Stasavage (2006) QJPS; Goodstein 외 (2017) JFI 30; Weaver & Agle (2002) AMR; Bertrand 외 (2010) QJE 125(1); Larrimore 외 (2011); Stocken (2000) RAND; Hungerman (2005) JPubE; Gross & Souleles (2002) RFS; Richardson & McBride (2009) JEBO; Liu 외 (2020) EJOR 281(2) 428–438; Kaakeh & Parker (2025) JBF 177, 107472 (LendingClub 주 부패와 부도 — 5.5절에 넣을 만함, 선택); Duong 외 (2024) JFR 47(3); Wang, Ye & Liao (2024) JBR 171; Li & Hu (2022) IRF; Wei & Lin (2017) Mgmt Sci 63(12); Becchetti & Conzo (2011) JPubE; Cavoli 외 (2025) JIFMIM 105. 미게재: Chen & Lian (2025) SSRN 5407298.

### 최종 집계

원고 v4 참고문헌 74편(v1 32 → v2 32 → v3 64 → v4 74). 세 회차에 걸쳐 검토한 참고문헌 약 1,100건, 인용 논문 약 2,100건. 남은 후보(3순위·주변)는 심사 대응용으로 이 문서에 보존.
