import pandas as pd

df = pd.read_csv("AB Testing Data.csv")

''' data cleaning '''
df = df.drop_duplicates(subset = "user_id")
# print(df.isnull().sum())
df = df.dropna(
    subset=["group", "converted", "session_duration", "purchase_amount"]
)
df = df[df["session_duration"] >= 0]
df = df[df["purchase_amount"] >= 0]
df = df[df["converted"].isin([0, 1])]

user_group_count = df.groupby("user_id")["group"].nunique()
invalid_users = user_group_count[user_group_count > 1]
# print(invalid_users)

control_group = df[df["group"] == "control"]
treatment_group = df[df["group"] == "treatment"]

control_length = len(control_group)
treatment_length = len(treatment_group)

print(control_length)
print(treatment_length)

''' 
hypothesis 
1. Does the new website increase the conversion rate? — **Two-Proportion Z-Test**
2. Is the conversion-rate difference statistically significant? — **Two-Proportion Z-Test**
3. Does the new website increase average session duration? — **Welch’s Independent T-Test**
4. Is the session-duration difference statistically significant? — **Welch’s Independent T-Test**
5. Does the new website increase average revenue per user? — **Welch’s Independent T-Test**
6. Is the revenue difference statistically significant? — **Welch’s Independent T-Test**
7. How large is the difference between the groups? — **Effect-Size Analysis**
8. What is the likely range of the true difference? — **Confidence Interval**
9. Is the improvement practically meaningful? — **Effect-Size Analysis**
10. Is the sample size sufficient? — **Statistical Power Analysis**
11. Should the company launch the new website? — **Combined Statistical and Practical Significance Analysis**
'''
print(df.dtypes)