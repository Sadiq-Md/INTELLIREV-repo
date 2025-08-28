# models/analysis.py
import pandas as pd

def revenue_growth(df):
    """Calculate year-over-year revenue growth by company"""
    growth = df.groupby("Company")["Revenue"].pct_change().fillna(0) * 100
    df["Revenue_Growth(%)"] = growth
    return df

def avg_profit_margin(df):
    """Calculate average profit margin by company"""
    df["Profit_Margin(%)"] = (df["Profit"] / df["Revenue"]) * 100
    return df

def contract_loss_ratio(df):
    """Contracts lost relative to revenue"""
    df["Loss_Ratio"] = df["Lost_Contracts"] / df["Revenue"]
    return df

def run_full_analysis(df):
    """Run all models on dataset"""
    df = revenue_growth(df)
    df = avg_profit_margin(df)
    df = contract_loss_ratio(df)
    return df
