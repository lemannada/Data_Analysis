import matplotlib.pyplot as plt
import seaborn as sns
from data.data_preparation import prepare_data


def configure_styles():
    plt.style.use('seaborn-v0_8')
    sns.set_style("whitegrid")
    sns.set_palette("husl")


def create_main_visualizations1(df):
    plt.figure(figsize=(18, 12))

    # 1. Line Plot
    plt.subplot(2, 3, 1)
    plt.plot(df['Year'], df['Sales'], marker='o', label='Sales')
    plt.plot(df['Year'], df['Expenses'], marker='s', label='Expenses')
    plt.title('Sales and Expenses Over Years', fontweight='bold')
    plt.xlabel('Year')
    plt.ylabel('Amount ($)')
    plt.legend()
    plt.grid(True)

    # 2. Bar Plot
    plt.subplot(2, 3, 2)
    bars = plt.bar(df['Year'], df['Profit'], color=sns.color_palette()[2])
    plt.title('Profit by Year', fontweight='bold')
    plt.xlabel('Year')
    plt.ylabel('Profit ($)')
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2., height,
                 f'{height:.0f}',
                 ha='center', va='bottom')

    # 3. Pie Chart
    plt.subplot(2, 3, 3)
    region_sales = df.groupby('Region')['Sales'].sum()
    plt.pie(region_sales, labels=region_sales.index, autopct='%1.1f%%',
            colors=sns.color_palette('pastel'))
    plt.title('Sales Distribution by Region', fontweight='bold')

    plt.tight_layout()
    plt.show()
