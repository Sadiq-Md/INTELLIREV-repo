# viz_test.py
import matplotlib
print("🔍 Current backend:", matplotlib.get_backend())

import pandas as pd
from data.data_test import load_data
from utils.visualizer import plot_revenue_trend, plot_profit_distribution, plot_lost_contracts

# Load dataset
df = load_data("data/company_data.csv")

# Call visualization functions
plot_revenue_trend(df)
plot_profit_distribution(df)
plot_lost_contracts(df)
