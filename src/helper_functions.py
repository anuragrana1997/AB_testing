import pandas as pd
import os

file_name = "../output/hypothesis_test_results.csv"

def record_data_to_csv(results, feature, test, mode = "x"):
    new_result = pd.DataFrame([{
        "feature_tested": feature,
        "test_type": test,
        "p_value": results["p_value"],
        "mean_difference": results["mean_diff"],
        "ci_lower": results["ci_lower"],
        "ci_upper": results["ci_upper"],
        "alpha": 0.05,
        "decision": results["decision"]
    }])

    new_result.to_csv(
        file_name,
        mode=mode,                      
        header=not os.path.exists(file_name),
        index=False
    )