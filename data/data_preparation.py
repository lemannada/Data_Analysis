import pandas as pd
import numpy as np


def prepare_data():
    np.random.seed(42)
    data = {
        'Year': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019],
        'Sales': [100, 120, 90, 150, 200, 210, 180, 220, 250, 300],
        'Expenses': [80, 85, 95, 90, 110, 120, 115, 130, 140, 150],
        'Region': ['North', 'North', 'South', 'East', 'West', 'West',
                   'South', 'East', 'North', 'West'],
        'Product': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'B', 'A', 'C']
    }
    df = pd.DataFrame(data)

    # Calculate derived metrics
    df['Profit'] = df['Sales'] - df['Expenses']
    df['Growth_Rate'] = df['Sales'].pct_change() * 100

    return df