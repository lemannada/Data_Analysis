import pandas as pd
from scipy import stats


def perform_analysis(df):
    print("\n=== Statistical Summary ===")
    print(df.describe())

    print("\n=== Correlation Matrix ===")
    print(df[['Sales', 'Expenses', 'Profit']].corr())

    print("\n=== Growth Rate Analysis ===")
    print(f"Average Growth Rate: {df['Growth_Rate'].mean():.2f}%")
    print(f"Maximum Growth Rate: {df['Growth_Rate'].max():.2f}% in {df.loc[df['Growth_Rate'].idxmax(), 'Year']}")
    print(f"Minimum Growth Rate: {df['Growth_Rate'].min():.2f}% in {df.loc[df['Growth_Rate'].idxmin(), 'Year']}")

    print("\n=== ANOVA Test (Product Sales Differences) ===")
    product_groups = [df[df['Product'] == prod]['Sales'] for prod in df['Product'].unique()]
    f_val, p_val = stats.f_oneway(*product_groups)
    print(f"F-value: {f_val:.2f}, p-value: {p_val:.4f}")
    print("Significant difference between products" if p_val < 0.05 else "No significant difference between products")