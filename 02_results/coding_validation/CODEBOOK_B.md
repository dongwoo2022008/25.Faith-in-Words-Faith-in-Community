# Codebook B — does this loan description contain RELIGIOUS content by the borrower?
These texts were NOT caught by an explicit religious-word dictionary. Decide whether the borrower expresses religion in any form.
- r = religious: any reference to God/deity, prayer, faith in a religious sense, church/congregation/religious community, religious identity, scripture, religious practice or giving, religious phrasing ("the man upstairs", "higher power", "godsend", "miracle" used religiously, "keep us in your prayers", "praise Him", "walk by faith", "sunday school", "mission trip", "worship", other religions: mosque, synagogue, karma in religious sense, etc.).
- n = not religious: no religious content; secular gratitude, hardship, family, moral promises, "faith in me", "miracle" in secular sense, "god" not present, etc.
If r, also give type: a = formulaic phrase, b = identity/value claim, c = concrete practice or expense (same as Codebook A).
Output JSON lines: {"id": "...", "relig": "r|n", "type": "a|b|c|", "quote": "<=10 words of the religious phrase if r"}
Code every record. Read the text; do not guess from keywords.
