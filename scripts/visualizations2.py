import matplotlib.pyplot as plt
import seaborn as sns
from data.data_preparation import prepare_data


def configure_styles():
    plt.style.use('seaborn-v0_8')
    sns.set_style("whitegrid")
    sns.set_palette("husl")


def create_main_visualizations2(df):
    plt.figure(figsize=(18, 12))

    # 4. Scatter Plot
    plt.subplot(2, 3, 1)
    sns.regplot(x='Sales', y='Expenses', data=df, ci=None)
    plt.title('Sales vs Expenses with Regression Line', fontweight='bold')
    plt.xlabel('Sales ($)')
    plt.ylabel('Expenses ($)')

    # 5. Box Plot
    plt.subplot(2, 3, 2)
    sns.boxplot(x='Product', y='Sales', data=df)
    plt.title('Sales Distribution by Product', fontweight='bold')
    plt.xlabel('Product')
    plt.ylabel('Sales ($)')

    # 6. Histogram
    plt.subplot(2, 3, 3)
    sns.histplot(df['Profit'], kde=True, bins=5, color=sns.color_palette()[4])
    plt.title('Profit Distribution', fontweight='bold')
    plt.xlabel('Profit ($)')
    plt.ylabel('Frequency')

    plt.tight_layout()
    plt.show()
