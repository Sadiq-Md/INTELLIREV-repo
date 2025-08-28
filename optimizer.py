# optimizer.py
import pandas as pd

def ensure_profit_margin(df: pd.DataFrame) -> pd.DataFrame:
    if "Profit_Margin" not in df.columns and "Profit_Margin_%" not in df.columns:
        df = df.copy()
        df["Profit_Margin"] = (df["Profit"] / df["Revenue"]) * 100
    elif "Profit_Margin_%" in df.columns and "Profit_Margin" not in df.columns:
        df = df.copy()
        df["Profit_Margin"] = df["Profit_Margin_%"]
    return df

def company_kpis(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate core KPIs per company."""
    df = ensure_profit_margin(df)
    agg = df.groupby("Company").agg(
        Total_Revenue=("Revenue", "sum"),
        Avg_Profit_Margin=("Profit_Margin", "mean"),
        Total_Lost_Contracts=("Lost_Contracts", "sum")
    ).reset_index()
    return agg.sort_values("Total_Revenue", ascending=False)

def risk_rank(df: pd.DataFrame) -> pd.DataFrame:
    """Rank companies by risk (high losses + low margins)."""
    kpis = company_kpis(df).copy()
    # Normalize
    kpis["z_loss"] = (kpis["Total_Lost_Contracts"] - kpis["Total_Lost_Contracts"].min()) / (
        (kpis["Total_Lost_Contracts"].max() - kpis["Total_Lost_Contracts"].min()) or 1
    )
    kpis["z_margin"] = (kpis["Avg_Profit_Margin"] - kpis["Avg_Profit_Margin"].min()) / (
        (kpis["Avg_Profit_Margin"].max() - kpis["Avg_Profit_Margin"].min()) or 1
    )
    # Higher risk = more losses + lower margins
    kpis["Risk_Score"] = 0.6 * kpis["z_loss"] + 0.4 * (1 - kpis["z_margin"])
    return kpis.sort_values("Risk_Score", ascending=False)

def suggest_strategy(df: pd.DataFrame) -> None:
    """Print actionable suggestions from KPIs."""
    df = ensure_profit_margin(df)
    kpis = company_kpis(df)
    risks = risk_rank(df)

    worst_loss_co = kpis.sort_values("Total_Lost_Contracts", ascending=False)["Company"].iloc[0]
    worst_margin_co = kpis.sort_values("Avg_Profit_Margin")["Company"].iloc[0]
    best_margin_co  = kpis.sort_values("Avg_Profit_Margin", ascending=False)["Company"].iloc[0]

    print("\n🧠 IntelliRev Strategic Suggestions:")
    print(f"- 🔴 {worst_loss_co} is losing the most contracts → strengthen bid qualification,"
          f" improve client retention playbooks, and perform loss-postmortems.")
    print(f"- 🟠 {worst_margin_co} has the weakest profit margins → optimize delivery costs,"
          f" renegotiate low-margin accounts, and adjust pricing tiers.")
    print(f"- 🟢 {best_margin_co} leads on efficiency → reinvest into presales tooling,"
          f" solution accelerators, and high-ROI verticals.")

    print("\n⚠ Risk Ranking (higher = riskier):")
    print(risks[["Company", "Risk_Score", "Total_Lost_Contracts", "Avg_Profit_Margin"]]
          .round({"Risk_Score": 3, "Avg_Profit_Margin": 2}))
