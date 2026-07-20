import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np
from scipy.stats import norm
from statsmodels.stats.proportion import (
    proportions_ztest,
    confint_proportions_2indep
)

df = pd.read_csv("../data/AB_testing.csv")
# print(df.info()) // check column type
# print(df.isna().sum()) // check missing values
# print(df["user_id"].duplicated().sum()) // check duplicate user ids
# print(pd.crosstab(df["group"], df["landing_page"])) // check crossovers
conversion_rate = df.groupby("group")["converted"].mean()

plt.figure(figsize = (6,4))
plt.bar(conversion_rate.index, conversion_rate.values)
plt.title("Conversion Rate by Group")
plt.xlabel("Group")
plt.ylabel("Conversion Rate")
plt.ylim(0, 1)
plt.savefig("../output/plots/conversion_rate_by_group.png")

df_control = df[df["group"] == "control"]
df_treatment = df[df["group"] == "treatment"]  
n1 = len(df_control)
n2 = len(df_treatment)
print("n1=", n1,"n2=", n2)

control_conversions = df_control[df_control["converted"] == 1]
treatment_conversions = df_treatment[df_treatment["converted"] == 1]
x1 = len(control_conversions)
x2 = len(treatment_conversions)
print("x1=", x1,"x2=", x2)

p1 = x1 / n1
p2 = x2 / n2

p_pool = (x1 + x2) / (n1 + n2)

standard_error = math.sqrt(p_pool * (1 - p_pool) * (1/n1 + 1/n2))

z_score = (p2 - p1) / standard_error
print("p_pool=", p_pool, "SE=", standard_error, "Z score=", z_score)

p_value = norm.sf(abs(z_score)) * 2
print(p_value)

val_1 = (p1 * (1 - p1)) / n1
val_2 = (p2 * (1 - p2)) / n2
unpooled_SE = math.sqrt(val_1 + val_2)

confidence_interval_plus = (p2 - p1) + 1.96 * unpooled_SE
confidence_interval_neg = (p2 - p1) - 1.96 * unpooled_SE

print(confidence_interval_plus, confidence_interval_neg)

z_score, p_value = proportions_ztest(
    count=np.array([x2, x1]),
    nobs=np.array([n2, n1]),
    value=0,
    alternative="two-sided"
)

ci_low, ci_high = confint_proportions_2indep(
    count1=x2,
    nobs1=n2,
    count2=x1,
    nobs2=n1,
    method="wald",
    compare="diff",
    alpha=0.05
)

print("Group 1 rate:", p1)
print("Group 2 rate:", p2)
print("Difference:", p2 - p1)
print("Z-score:", z_score)
print("P-value:", p_value)
print("95% CI:", (ci_low, ci_high))