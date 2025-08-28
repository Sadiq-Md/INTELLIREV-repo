import pandas as pd

def generate_consultant_suggestion(df: pd.DataFrame) -> str:
    suggestions = []

    if "Loss_Reason" in df.columns and not df["Loss_Reason"].isna().all():
        max_loss_reason = df["Loss_Reason"].value_counts().idxmax()
        suggestions.append(f"- 🚫 Most frequent loss reason: **{max_loss_reason}**")

    if "Company" in df.columns and "Profit_Margin" in df.columns:
        try:
            avg_margin = df.groupby("Company")["Profit_Margin"].mean()
            min_margin_company = avg_margin.idxmin()
            min_margin_value = avg_margin.min()
            suggestions.append(f"- 📉 Lowest avg margin: **{min_margin_company}** ({min_margin_value:.2f}%)")
        except:
            suggestions.append("- ⚠️ Margin data couldn't be processed.")

    if not suggestions:
        return "🤖 No actionable insights available due to insufficient data."

    return "🤖 Based on current trends:\n" + "\n".join(suggestions) + "\n\n💡 Recommendation: Review pricing, delivery quality, and customer retention strategy."
