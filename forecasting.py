import pandas as pd
from prophet import Prophet

def prepare_data(df, company, metric="Revenue"):
    """Format data for Prophet"""
    filtered = df[df["Company"] == company]
    yearly = filtered.groupby("Year")[metric].sum().reset_index()
    yearly = yearly.rename(columns={"Year": "ds", metric: "y"})
    yearly["ds"] = pd.to_datetime(yearly["ds"], format="%Y")
    return yearly

def forecast(df, company, metric="Revenue", periods=3):
    """
    Forecast specified metric for a company using Prophet.
    
    Args:
        df (pd.DataFrame): input data with columns Company, Year, Revenue, Profit...
        company (str): company name to forecast
        metric (str): "Revenue" or "Profit"
        periods (int): number of years to forecast forward
    
    Returns:
        historical (pd.DataFrame): historical data used for forecasting
        predicted (pd.DataFrame): forecasted data with confidence intervals
    """
    data = prepare_data(df, company, metric)
    model = Prophet()
    model.fit(data)
    future = model.make_future_dataframe(periods=periods, freq='Y')
    forecast_df = model.predict(future)

    predicted = forecast_df[["ds", "yhat", "yhat_lower", "yhat_upper"]].tail(periods)
    historical = data

    return historical, predicted
