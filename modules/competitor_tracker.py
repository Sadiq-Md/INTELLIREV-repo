import pandas as pd
import plotly.express as px

def competitor_loss_comparison(df):
    """
    Create a Plotly bar chart comparing lost contracts by loss reason and company.
    
    Parameters:
        df (pd.DataFrame): Dataframe with columns ['Company', 'Loss_Reason', 'Lost_Contracts']
    
    Returns:
        fig (plotly.graph_objs._figure.Figure): Bar chart figure
    """
    comp_df = df.groupby(["Company", "Loss_Reason"]).agg(
        Lost_Contracts=("Lost_Contracts", "sum")
    ).reset_index()

    fig = px.bar(
        comp_df,
        x="Loss_Reason",
        y="Lost_Contracts",
        color="Company",
        barmode="group",
        title="Lost Contracts by Loss Reason - Competitor Comparison",
        labels={"Lost_Contracts": "Lost Contracts", "Loss_Reason": "Loss Reason"}
    )

    fig.update_layout(xaxis_tickangle=-45)
    return fig
