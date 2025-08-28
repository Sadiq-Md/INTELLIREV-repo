import pandas as pd
from utils.visualizer import plot_revenue_trend, plot_profit_distribution, plot_lost_contracts
from analyzer import (
    revenue_summary,
    profit_margin,
    top_loss_analysis,
    industry_analysis,
    region_analysis,
    deal_size_analysis
)
from optimizer import company_kpis, risk_rank, suggest_strategy
from utils.loss_autopsy import contract_loss_summary, plot_loss_reasons

# Load your company data
df = pd.read_csv("data/company_data.csv")

# Call visualization functions
plot_revenue_trend(df)
plot_profit_distribution(df)
plot_lost_contracts(df)

# Summaries & Analysis
revenue_summary(df)
df = profit_margin(df)
top_loss_analysis(df)

print("\n====== KPI SUMMARY ======")
print(company_kpis(df))

print("\n====== RISK RANK ======")
print(risk_rank(df)[["Company","Risk_Score","Total_Lost_Contracts","Avg_Profit_Margin"]])

suggest_strategy(df)

# Loss Analysis
loss_summary = contract_loss_summary(df)
plot_loss_reasons(df)

# Deep Dive Insights
industry_analysis(df)
region_analysis(df)
deal_size_analysis(df)
