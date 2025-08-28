import pandas as pd

def calculate_revenue_leakage(actual: pd.DataFrame, forecasted: pd.DataFrame) -> float:
    actual_sum = actual["Revenue"].sum()
    forecast_sum = forecasted["Revenue"].sum()
    leakage = forecast_sum - actual_sum
    return leakage
