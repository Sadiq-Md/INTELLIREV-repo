import pandas as pd

# ==========================
#  BASIC ANALYSIS
# ==========================
def revenue_summary(df):
    print("\n====== REVENUE SUMMARY ======")
    revenue = df.groupby("Company")["Revenue"].sum().reset_index()
    print(revenue)
    return revenue

def profit_margin(df):
    print("\n====== PROFIT MARGIN ======")
    # Avoid division by zero
    df["Profit_Margin"] = (df["Profit"] / df["Revenue"]).replace([float("inf"), -float("inf")], 0).fillna(0) * 100
    margin = df.groupby("Company")["Profit_Margin"].mean().reset_index()
    print(margin)
    return df   # return df with new Profit_Margin column

def top_loss_analysis(df):
    print("\n====== TOP LOSS ANALYSIS ======")
    loss_summary = df.groupby("Loss_Reason")["Lost_Contracts"].sum().reset_index().sort_values(by="Lost_Contracts", ascending=False)
    print(loss_summary)
    return loss_summary

def industry_analysis(df):
    print("\n📊 INDUSTRY-WISE ANALYSIS")
    industry_summary = df.groupby("Industry")[["Revenue", "Profit", "Lost_Contracts"]].sum().reset_index()
    print(industry_summary)
    return industry_summary

def region_analysis(df):
    print("\n🌍 REGION-WISE ANALYSIS")
    region_summary = df.groupby("Region")[["Revenue", "Profit", "Lost_Contracts"]].sum().reset_index()
    print(region_summary)
    return region_summary

def deal_size_analysis(df):
    print("\n💼 DEAL SIZE IMPACT")
    deal_summary = df.groupby("Deal_Size")[["Revenue", "Profit", "Lost_Contracts"]].mean().reset_index()
    print(deal_summary)
    return deal_summary
