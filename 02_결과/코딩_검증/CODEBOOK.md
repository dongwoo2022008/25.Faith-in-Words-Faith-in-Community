# Codebook — religious expression in loan descriptions

For EACH record, assign exactly one TYPE and one FRAME.

TYPE (what kind of religious expression is it?)
- a = 관용구 formulaic: religious words used as a closing/greeting/idiom with no claim about the writer ("Thank you and God bless", "God willing", "prayers answered", "기도합니다", "축복"). Includes a title like "God is good".
- b = 정체성/가치 identity-or-value claim: writer asserts their own faith, religious identity, or a religious/moral value as a reason to trust them ("as a Christian I believe in paying my debts", "I have strong faith in God", "저는 신앙인으로서", "하나님만 믿고", "믿는 사람으로서").
- c = 실천/지출 practice-or-expense: concrete religious activity or money — tithes/offerings in a budget, church employment, mission trip, seminary tuition, church building, pastor as occupation, "십일조 15만원", "교회 사역", "목회자입니다".
- x = 비종교 not religious: the matched word is used non-religiously ("Lord & Taylor", "land lord", "heaven forbid", "good faith", "신부님" in a wedding context = still religious? no → 'b'/'c' only if it's the writer's religion; a wedding officiant mention is x; "불교정" typo, "선불교통", "신불자").
If several apply, choose the STRONGEST in the order c > b > a (practice beats identity beats formula).

FRAME (what accompanies the religious content in the SAME description?)
- 종교 = religious content only, no moral self-presentation and no hardship narrative
- 도덕 = accompanied by honesty/promise/responsibility/reliability claims ("I always pay on time", "I promise", "성실히", "책임", "정직")
- 곤경 = accompanied by hardship narrative (job loss, illness, divorce, medical bills, 실직, 병원, 수술, 이혼, 연체, 신용불량)
- 도덕/곤경 = both
Code FRAME independently of TYPE.

Output: one JSON object per line: {"id": "...", "type": "a|b|c|x", "frame": "종교|도덕|곤경|도덕/곤경", "note": "<=12 words optional"}. Code every record. Do not skip. Do not look at or infer from any prior automatic labels.
