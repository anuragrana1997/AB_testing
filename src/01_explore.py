import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np
import t_test
import z_test
from scipy.stats import norm, ttest_ind, t as t_dist
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

''' Z-test '''
z_test.z_statistics(df, "converted")

''' T-test '''
t_test.t_statistics(df, "session_duration")
t_test.t_statistics(df, "pages_visited")
t_test.t_statistics(df, "purchase_amount")