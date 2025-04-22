import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {'Year': [2010, 2011, 2012, 2013, 2014],
        'Sales': [100, 120, 90, 150, 200]}
df = pd.DataFrame(data)

# Plot
df.plot(x='Year', y='Sales', kind='line', title='Sales Over Years')
plt.show()
