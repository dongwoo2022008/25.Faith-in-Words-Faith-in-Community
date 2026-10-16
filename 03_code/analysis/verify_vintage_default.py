"""Check used in Sections 3.1 and 5.1: descriptions and raw default rates by issue year.
Output: 02_results/tables_csv/default_and_descriptions_by_year.csv
Run: python verify_vintage_default.py <path to accepted_2007_to_2018Q4.csv.gz> <output csv>
A description counts only if text remains after the platform boilerplate is removed, with the same
cleaning as rebuild_TD.py / step1 ("Borrower added on MM/DD/YY >" stamps and <br> tags), so the counts
match Section 3.1 and Appendix Table B3 (125,811 descriptions, 125,761 issued 2007-2014); the column
with_description_raw keeps the count before cleaning (one description is boilerplate only).
Result on the 2018Q4 file: default among terminated loans is 0.170 for 2008-2014 issues and 0.215 for
2015-2018 issues; descriptions exist for 2007-2016 issues (50 after 2014).
"""
import sys, re, pandas as pd
f, out = sys.argv[1], sys.argv[2]
def clean(s):
    if not isinstance(s, str): return ''
    s = re.sub(r'Borrower added on \d{2}/\d{2}/\d{2} >', ' ', s); s = re.sub(r'<br\s*/?>', ' ', s, flags=re.I)
    return re.sub(r'\s+', ' ', s).strip()
rows = []
for ch in pd.read_csv(f, usecols=["issue_d","desc","loan_status"], chunksize=300000, low_memory=False, dtype=str):
    ch = ch.dropna(subset=["issue_d"]); ch["yr"] = ch.issue_d.str[-4:]
    ch["hasdesc_raw"] = ch.desc.notna() & (ch.desc.str.strip().str.len() > 0)
    ch["hasdesc"] = ch.desc.map(clean).str.len() > 0
    ch["terminated"] = ch.loan_status.isin(["Fully Paid","Charged Off","Default"])
    ch["defaulted"] = ch.loan_status.isin(["Charged Off","Default"])
    rows.append(ch.groupby("yr").agg(loans=("yr","size"), with_description=("hasdesc","sum"), with_description_raw=("hasdesc_raw","sum"),
                terminated=("terminated","sum"), defaulted=("defaulted","sum")))
g = pd.concat(rows).groupby(level=0).sum()
g["default_rate_terminated"] = (g.defaulted / g.terminated).round(3)
g.to_csv(out); print(g); print("total with_description", int(g.with_description.sum()), "raw", int(g.with_description_raw.sum()))
