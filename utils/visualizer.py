import matplotlib.pyplot as plt
import seaborn as sns
import os

# Ensure plots folder exists
os.makedirs("plots", exist_ok=True)

# ==========================
#  BASIC VISUALIZATIONS
# ==========================
def plot_revenue_trend(df):
    plt.figure(figsize=(8, 5))
    sns.lineplot(data=df, x="Year", y="Revenue", hue="Company", marker="o")
    plt.title("Revenue Trend Over Years")
    plt.ylabel("Revenue")
    plt.tight_layout()
    filename = "plots/revenue_trend.png"
    plt.savefig(filename)
    plt.show(block=True)
    print(f"✅ Saved: {filename}")

def plot_profit_distribution(df):
    plt.figure(figsize=(8, 5))
    sns.barplot(data=df, x="Company", y="Profit", hue="Year")
    plt.title("Profit Distribution by Company & Year")
    plt.ylabel("Profit")
    plt.tight_layout()
    filename = "plots/profit_distribution.png"
    plt.savefig(filename)
    plt.show(block=True)
    print(f"✅ Saved: {filename}")

def plot_lost_contracts(df):
    plt.figure(figsize=(8, 5))
    sns.barplot(data=df, x="Company", y="Lost_Contracts", hue="Year")
    plt.title("Lost Contracts by Company & Year")
    plt.ylabel("Lost Contracts")
    plt.tight_layout()
    filename = "plots/lost_contracts.png"
    plt.savefig(filename)
    plt.show(block=True)
    print(f"✅ Saved: {filename}")

# ==========================
#  DEEP DIVE VISUALIZATIONS
# ==========================
def plot_industry_performance(df):
    plt.figure(figsize=(8, 5))
    summary = df.groupby("Industry")[["Revenue", "Profit", "Lost_Contracts"]].sum().reset_index()
    summary.set_index("Industry")[["Revenue", "Profit", "Lost_Contracts"]].plot(kind='bar')
    plt.title("Industry-wise Performance")
    plt.ylabel("Total Values")
    plt.tight_layout()
    filename = "plots/industry_performance.png"
    plt.savefig(filename)
    plt.show(block=True)
    print(f"✅ Saved: {filename}")

def plot_region_performance(df):
    plt.figure(figsize=(8, 5))
    summary = df.groupby("Region")[["Revenue", "Profit", "Lost_Contracts"]].sum().reset_index()
    summary.set_index("Region")[["Revenue", "Profit", "Lost_Contracts"]].plot(kind='bar')
    plt.title("Region-wise Performance")
    plt.ylabel("Total Values")
    plt.tight_layout()
    filename = "plots/region_performance.png"
    plt.savefig(filename)
    plt.show(block=True)
    print(f"✅ Saved: {filename}")

def plot_deal_size_trends(df):
    plt.figure(figsize=(8, 5))
    summary = df.groupby("Deal_Size")[["Revenue", "Profit", "Lost_Contracts"]].mean().reset_index()
    summary.set_index("Deal_Size")[["Revenue", "Profit", "Lost_Contracts"]].plot(kind='bar')
    plt.title("Deal Size Analysis (Avg Revenue, Profit, Lost Contracts)")
    plt.ylabel("Average Values")
    plt.tight_layout()
    filename = "plots/deal_size_analysis.png"
    plt.savefig(filename)
    plt.show(block=True)
    print(f"✅ Saved: {filename}")

def plot_loss_reasons(df):
    plt.figure(figsize=(8, 5))
    summary = df.groupby("Loss_Reason")["Lost_Contracts"].sum().reset_index()
    sns.barplot(data=summary, x="Loss_Reason", y="Lost_Contracts")
    plt.title("Loss Reasons Distribution")
    plt.ylabel("Total Lost Contracts")
    plt.tight_layout()
    filename = "plots/loss_reasons.png"
    plt.savefig(filename)
    plt.show(block=True)
    print(f"✅ Saved: {filename}")
