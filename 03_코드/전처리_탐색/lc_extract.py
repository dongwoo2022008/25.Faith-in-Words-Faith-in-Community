import pandas as pd, re, time
f="/mnt/user-data/uploads/Lending Club/accepted_2007_to_2018Q4.csv.gz"
cols=['id','loan_amnt','funded_amnt','funded_amnt_inv','term','int_rate','grade','sub_grade','emp_title','emp_length','home_ownership','annual_inc','verification_status','issue_d','loan_status','desc','purpose','title','addr_state','dti','fico_range_low','fico_range_high','application_type']
t=time.time(); parts=[]
for ch in pd.read_csv(f, usecols=cols, chunksize=250000, low_memory=False):
    parts.append(ch)
df=pd.concat(parts, ignore_index=True)
print("rows",len(df), "sec",round(time.time()-t))
df=df[df['id'].notna()]
df.to_pickle("lc_small.pkl")
print("rows after id filter",len(df))
