import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def contract_loss_summary(df):
    if "Loss_Reason" not in df.columns:
        print("⚠ No 'Loss_Reason' column found in dataset.")
        return
    
    summary = df.groupby(["Company", "Loss_Reason"]).size().reset_index(name="Count")
    print("\n📉 Contract Loss Breakdown by Reason:")
    print(summary)
    return summary

def plot_loss_reasons(df):
    if "Loss_Reason" not in df.columns:
        return
    
    plt.figure(figsize=(8,6))
    sns.countplot(data=df, x="Loss_Reason", hue="Company")
    plt.title("Lost Contracts Breakdown by Reason")
    plt.xticks(rotation=30)
    plt.show()
