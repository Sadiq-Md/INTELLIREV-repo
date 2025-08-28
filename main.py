import pandas as pd
from utils.visualizer import plot_revenue_trend, plot_profit_distribution, plot_lost_contracts
from analyzer import revenue_summary, profit_margin, top_loss_analysis
from optimizer import company_kpis, risk_rank, suggest_strategy
from utils.loss_autopsy import contract_loss_summary, plot_loss_reasons

def main():
    # Load dataset
    df = pd.read_csv("data/company_data.csv")

    # Visualizations
    plot_revenue_trend(df)
    plot_profit_distribution(df)
    plot_lost_contracts(df)

    # Analysis
    revenue_summary(df)
    df = profit_margin(df)
    top_loss_analysis(df)

    # Optimizer
    print("\n====== KPI SUMMARY ======")
    print(company_kpis(df))

    print("\n====== RISK RANK ======")
    print(risk_rank(df)[["Company","Risk_Score","Total_Lost_Contracts","Avg_Profit_Margin"]])

    suggest_strategy(df)

    # Loss Autopsy
    print("\n====== CONTRACT LOSS SUMMARY ======")
    print(contract_loss_summary(df))
    plot_loss_reasons(df)

if __name__ == "__main__":
    main()
