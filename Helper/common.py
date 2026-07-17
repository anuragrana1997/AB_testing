from statistics import NormalDist
import math

alpha = 0.05
power = 0.80
beta = 1 - power

expected_control_rate = 0.10
expected_treatment_rate = 0.12
minimum_detectable_effect = 0.02

average_rate = (expected_control_rate + expected_treatment_rate) / 2

z_alpha = NormalDist().inv_cdf(1 - alpha / 2)
z_beta = NormalDist().inv_cdf(1 - beta)

print(z_alpha)
print(z_beta)

''' to find the sample size when contemplating whether you have enough data or not, as we decided on allocation 50:50 and groups are independent control and treatment and outcome is binary '''

first_val = z_alpha * math.sqrt(2 * average_rate * (1 - average_rate))
second_val = z_beta * math.sqrt(expected_control_rate * (1 - expected_control_rate) + expected_treatment_rate * (1 - expected_treatment_rate))

dataset_count_required = pow((first_val + second_val), 2) / pow((expected_treatment_rate - expected_control_rate), 2)

print(dataset_count_required)

# since we have dataset greater that dataset_count_required, so good to go