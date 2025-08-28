# report_generator.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
import os

def generate_summary(df):
    top_company = df.loc[df["Revenue"].idxmax(), "Company"]
    worst_loss_reason = df["Loss_Reason"].value_counts().idxmax()

    summary = f"""
    <b>Key Highlights:</b><br/>
    • Top Revenue Company: {top_company}<br/>
    • Highest Risk Factor: {worst_loss_reason}<br/>
    • Total Revenue across all companies: {df['Revenue'].sum():,.0f}<br/>
    • Total Profit across all companies: {df['Profit'].sum():,.0f}<br/>
    • Total Lost Contracts: {df['Lost_Contracts'].sum()}<br/>
    """
    return summary

def generate_plots(df):
    if not os.path.exists("plots"):
        os.makedirs("plots")

    plt.figure(figsize=(6,4))
    sns.barplot(data=df, x="Company", y="Revenue", ci=None)
    plt.title("Revenue by Company")
    plt.tight_layout()
    plt.savefig("plots/revenue.png")
    plt.close()

    plt.figure(figsize=(6,4))
    sns.barplot(data=df, x="Company", y="Profit", ci=None, palette="viridis")
    plt.title("Profit by Company")
    plt.tight_layout()
    plt.savefig("plots/profit.png")
    plt.close()

    plt.figure(figsize=(6,4))
    sns.barplot(data=df, x="Company", y="Lost_Contracts", ci=None, palette="magma")
    plt.title("Lost Contracts by Company")
    plt.tight_layout()
    plt.savefig("plots/lost_contracts.png")
    plt.close()

def generate_pdf(filtered_df):
    generate_plots(filtered_df)

    doc = SimpleDocTemplate("IntelliRev_Report.pdf", pagesize=A4)
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="Heading", fontSize=14, leading=16, spaceAfter=10, textColor=colors.darkblue))

    elements = []

    elements.append(Paragraph("<b>IntelliRev: Revenue Intelligence Report</b>", styles["Title"]))
    elements.append(Spacer(1, 12))

    elements.append(Paragraph("Executive Summary", styles["Heading"]))
    elements.append(Paragraph(generate_summary(filtered_df), styles["Normal"]))
    elements.append(Spacer(1, 12))

    elements.append(Paragraph("Key Performance Indicators", styles["Heading"]))
    kpi_data = [["Company", "Revenue", "Profit", "Lost Contracts"]]
    for _, row in filtered_df.iterrows():
        kpi_data.append([row["Company"], row["Revenue"], row["Profit"], row["Lost_Contracts"]])

    table = Table(kpi_data, hAlign="LEFT")
    table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.lightblue),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ("GRID", (0,0), (-1,-1), 0.5, colors.grey),
    ]))
    elements.append(table)
    elements.append(Spacer(1, 12))

    elements.append(Paragraph("Visual Insights", styles["Heading"]))
    for plot_file in ["plots/revenue.png", "plots/profit.png", "plots/lost_contracts.png"]:
        elements.append(Image(plot_file, width=400, height=250))
        elements.append(Spacer(1, 12))

    doc.build(elements)

