# data/data_test.py
import pandas as pd

def load_data():
    """Loads company data from CSV"""
    df = pd.read_csv("data/company_data.csv")
    return df

if __name__ == "__main__":
    df = load_data()
    print("Company Data Preview:")
    print(df.head())

    print("\n📈 Summary Statistics:")
    print(df.describe())

    print("\n🏢 Companies in dataset:")
    print(df["Company"].unique())
