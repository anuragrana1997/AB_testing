# A/B Testing and Hypothesis Testing Project

## Project Description

This project analyzes an A/B experiment conducted to compare an existing website experience with a new website experience.

- **Control group:** Users who experienced the existing website
- **Treatment group:** Users who experienced the new website
- **Control sample size:** 146,926 users
- **Treatment sample size:** 147,552 users
- **Total sample size:** 294,478 users

The main goal is to determine whether the treatment improves the conversion rate. Continuous metrics such as session duration, purchase amount, and another numerical feature are also analyzed to check whether the treatment affects user behavior and business performance.

## Statistical Tests Used

Two different hypothesis tests were used because the dataset contains both binary and continuous metrics.

- A **two-proportion z-test** was used for the binary conversion metric.
- **Welch's independent t-test** was used for continuous metrics.

The significance level for all tests was:

```text
alpha = 0.05
```

## Results

| Feature Tested | Test Type | Test Statistic | P-value | Difference | 95% Confidence Interval | Effect Size | Achieved Power | Decision |
|---|---|---:|---:|---:|---|---:|---:|---|
| Converted | Two-proportion z-test | 46.27734 | Approximately 0 | 0.06076 | [0.05820, 0.06333] | Cohen's h = 0.17141 | 1.00000 | Reject H0 |
| Session duration | Welch's t-test | -0.42335 | 0.67204 | -0.00309 | [-0.01739, 0.01121] | Cohen's d = -0.00156 | 0.07077 | Fail to reject H0 |
| `continuous_metric_2` | Welch's t-test | 1.16348 | 0.24463 | 0.00843 | [-0.00577, 0.02262] | Cohen's d = 0.00429 | 0.21377 | Fail to reject H0 |
| Purchase amount | Welch's t-test | 40.73823 | Approximately 0 | 2.31053 | [2.19937, 2.42169] | Cohen's d = 0.15009 | 1.00000 | Reject H0 |

A p-value displayed as `0.0` does not mean that the probability is exactly zero. It means that the p-value is extremely small and cannot be represented precisely with the available floating-point precision.

## Conversion-Rate Results

The control and treatment conversion rates were:

```text
Control conversion rate:   0.11873, or 11.87%
Treatment conversion rate: 0.17949, or 17.95%
Absolute difference:       0.06076, or 6.08 percentage points
```

The relative increase in conversion was approximately:

```text
(0.17949 - 0.11873) / 0.11873 = 51.18%
```

The treatment increased the conversion rate by approximately **6.08 percentage points**, which represents a relative improvement of approximately **51.18%** compared with the control group.

The z-score was 46.27734, which is much greater than the two-sided critical z-value of 1.96. The 95% confidence interval was entirely above zero.

Therefore, the null hypothesis of equal conversion rates was rejected.

## Why a Z-Test Was Used for `converted`

The `converted` feature is binary because each user has one of two possible outcomes:

```text
0 = Did not convert
1 = Converted
```

The analysis therefore compares two proportions: the control conversion rate and the treatment conversion rate.

A two-proportion z-test was appropriate because both groups were independent and had very large sample sizes. Each group also contained enough conversions and non-conversions for the normal approximation to be valid.

## Why Welch's T-Test Was Used

The remaining metrics are continuous numerical variables, so the analysis compares their average values between the control and treatment groups.

Welch's independent t-test was appropriate because:

- The control and treatment groups contained different users.
- The population standard deviations were unknown.
- The sample variances were not required to be equal.
- The group sample sizes were not exactly equal.

Welch's t-test is generally safer than the pooled Student's t-test because it does not assume equal population variances.

## Session-Duration Results

The session-duration results were:

```text
t-statistic:     -0.42335
Critical t:       1.95997
P-value:          0.67204
Mean difference: -0.00309
95% CI:          [-0.01739, 0.01121]
Cohen's d:       -0.00156
```

The absolute t-statistic was smaller than the critical t-value:

```text
|-0.42335| < 1.95997
```

The confidence interval also included zero. Therefore, the null hypothesis was not rejected.

There is no statistically significant difference in average session duration between the control and treatment groups. Cohen's d was almost zero, which means the practical effect was also negligible.

## Continuous Metric 2 Results

The results for `continuous_metric_2` were:

```text
t-statistic:      1.16348
Critical t:       1.95997
P-value:          0.24463
Mean difference:  0.00843
95% CI:          [-0.00577, 0.02262]
Cohen's d:        0.00429
```

The t-statistic was smaller than the critical t-value, and the confidence interval included zero.

Therefore, the null hypothesis was not rejected. There is no statistically significant difference between the control and treatment groups for this metric.

Cohen's d was close to zero, indicating that the practical difference was negligible.

## Purchase-Amount Results

The purchase-amount results were:

```text
t-statistic:      40.73823
Critical t:        1.95997
P-value:           Approximately 0
Mean difference:   2.31053
95% CI:           [2.19937, 2.42169]
Cohen's d:         0.15009
```

The t-statistic was much greater than the critical t-value:

```text
40.73823 > 1.95997
```

The confidence interval was entirely above zero. Therefore, the null hypothesis was rejected.

The treatment increased the average purchase amount by approximately **2.31 units**. Cohen's d indicates a small standardized effect, but the increase was estimated very precisely because of the large sample size.

## Statistical Power

The conversion-rate test and purchase-amount test both had achieved power close to 1.0.

This means that, assuming the observed effects represent the true effects, the available sample sizes were more than sufficient to detect them.

The session-duration test and `continuous_metric_2` test had low achieved power because their observed effect sizes were extremely close to zero.

However, low post-experiment power should not automatically be interpreted as evidence that more data is required. The confidence intervals and effect sizes show that the observed differences for these metrics were very small.

## Final Recommendation

### Recommendation: Ship the treatment

The treatment should be shipped because it produced a large and statistically significant improvement in the primary conversion metric.

The conversion rate increased from **11.87% to 17.95%**, representing:

- An absolute increase of approximately **6.08 percentage points**
- A relative increase of approximately **51.18%**

The treatment also increased the average purchase amount by approximately **2.31 units**.

No statistically significant negative effect was found for session duration or the other continuous metric. Their effect sizes were also close to zero.

The treatment should therefore be deployed, provided that:

- Experiment assignment was properly randomized.
- Users did not appear in both groups.
- Tracking and conversion logging were accurate.
- The treatment did not introduce technical, legal, or operational problems.
- The experiment duration covered normal variations in traffic and user behavior.

## Business Impact

The treatment produced approximately 6,076 additional conversions for every 100,000 users:

```text
100,000 × 0.06076 = 6,076 additional conversions
```

For one million users, the estimated increase would be approximately:

```text
1,000,000 × 0.06076 = 60,763 additional conversions
```

Therefore, if one million users experience the treatment under similar conditions, the business may receive approximately **60,763 additional conversions** compared with the control experience.

The treatment also increased the average purchase amount by approximately 2.31 units.

A general estimate of incremental revenue can be calculated using:

```text
Incremental revenue =
Additional conversions × Average revenue per conversion
```

The purchase-amount improvement can also be incorporated into the estimate:

```text
Estimated purchase-value increase =
Expected number of purchases × 2.31053
```

The actual financial impact depends on:

- The currency used for purchase amount
- The number of users receiving the treatment
- The percentage of conversions that become completed purchases
- Refunds and cancellations
- Customer acquisition costs
- Development and maintenance costs
- Whether the experimental effect remains stable after deployment

## Overall Conclusion

The experiment provides strong statistical evidence that the treatment improves both conversion rate and average purchase amount.

The treatment did not produce meaningful changes in session duration or the other tested continuous metric.

Based on the statistical results and the expected business impact, the treatment is recommended for deployment. Conversion quality, retention, refunds, customer satisfaction, and long-term revenue should continue to be monitored after launch.
