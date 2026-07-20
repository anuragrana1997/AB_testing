import math
import numpy as np
from scipy.stats import ttest_ind, t as t_dist
from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize
import helper_functions

def t_statistics(df, feature):
    t_control_session = df[df["group"] == "control"][feature]
    t_treatment_session = df[df["group"] == "treatment"][feature]

    t_n1 = len(t_control_session)
    t_n2 = len(t_treatment_session)

    t_control_mean = sum(t_control_session) / t_n1
    t_treatment_mean = sum(t_treatment_session) / t_n2

    t_control_std = t_control_session.std()
    t_treatment_std = t_treatment_session.std()

    numerator = t_treatment_mean - t_control_mean
    denominator = math.sqrt(pow(t_treatment_std, 2)/t_n2 + pow(t_control_std, 2)/t_n1)

    t = numerator / denominator
    print("-------------------")
    print("t = ",t)

    t_stat, p_value = ttest_ind(t_treatment_session, t_control_session, equal_var=False)
    print("verify t = ", t_stat, "verify p = ", p_value)

    t_pooled_std = math.sqrt(((t_n1 - 1) * pow(t_control_std, 2) + (t_n2 - 1) * pow(t_treatment_std, 2)) / (t_n1 + t_n2 - 2))

    cohen_d = (t_treatment_mean - t_control_mean) / t_pooled_std
    achieved_power = NormalIndPower().power(
        effect_size=cohen_d,
        nobs1=t_n1,
        ratio=t_n2 / t_n1,
        alpha=0.05,
        alternative="two-sided"
    )
    print("Cohen's d:", cohen_d)
    print("Achieved power:", achieved_power)

    alpha = 0.05
    df = t_n1 + t_n2 - 2

    critical_t = t_dist.ppf(1 - alpha/2, df)
    print("critical T = ", critical_t)

    ci_lower = numerator - critical_t * denominator
    ci_upper = numerator + critical_t * denominator
    print("mean diff = ", numerator)
    print("CI lower and upper = ", ci_lower, ci_upper)

    results = {}
    results["p_value"] = p_value
    results["mean_diff"] = numerator
    results["ci_lower"] = ci_lower
    results["ci_upper"] = ci_upper
    if p_value < alpha:
        results["decision"] = "Reject null Hypothesis"
    else:
        results["decision"] = "Failed to reject null Hypothesis"

    helper_functions.record_data_to_csv(results, feature, "Welch's T-test", "a")