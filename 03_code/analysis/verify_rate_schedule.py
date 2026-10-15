"""Check used in Section 6.3: LendingClub's interest rate is a schedule over sub-grade, term and date.
Reads the raw LendingClub file in chunks and tabulates distinct rates within
issue month x sub-grade x term cells. Output: 02_results/tables_csv/rate_schedule_by_year.csv
Run: python verify_rate_schedule.py <path to accepted_2007_to_2018Q4.csv.gz> <output csv>
Result on the 2018Q4 file (2,260,668 loans with a rate): 94.7 percent of loans sit at the modal rate of
their cell, 99.95 percent at one of the two most common rates, at most five distinct rates per cell.
"""
import sys, collections, pandas as pd
f, out = sys.argv[1], sys.argv[2]
cnt = collections.Counter()
for ch in pd.read_csv(f, usecols=["issue_d","sub_grade","int_rate","term"], chunksize=200000, low_memory=False, dtype=str):
    ch = ch.dropna(subset=["issue_d","sub_grade","int_rate"])
    ch["r"] = ch["int_rate"].str.strip().str.rstrip("%").astype(float)
    for k, v in ch.groupby(["issue_d","sub_grade","term","r"]).size().items(): cnt[k] += v
d = pd.DataFrame([(k[0],k[1],k[2],k[3],v) for k,v in cnt.items()], columns=["issue_d","sg","term","r","n"])
d["ym"] = pd.to_datetime(d.issue_d, format="%b-%Y"); d["year"] = d.ym.dt.year
N = d.n.sum()
g = d.groupby(["ym","sg","term"])
s = g.agg(nu=("r","nunique"), n=("n","sum")).reset_index(); s["year"] = s.ym.dt.year
top = g.n.max().sum(); top2 = g.n.apply(lambda x: x.sort_values(ascending=False).head(2).sum()).sum()
summary = s.groupby("year").apply(lambda x: pd.Series({"cells": len(x), "single_rate_cell_share": (x.nu==1).mean(),
          "loan_share_in_single_rate_cells": x.loc[x.nu==1,"n"].sum()/x.n.sum(), "max_distinct_rates": x.nu.max()}))
summary.loc["all"] = [len(s), (s.nu==1).mean(), s.loc[s.nu==1,"n"].sum()/N, s.nu.max()]
summary.to_csv(out)
print("loans", N, "| share at modal rate of cell", round(top/N,4), "| share at top-2 rates", round(top2/N,4))
print(summary)
