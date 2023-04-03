import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('data.csv')

# Replace null values with 0
df = df.fillna(0)

# Split data by product and location
grouped = df.groupby(['product', 'location'])

# Calculate the average and median for each group
avg = grouped.mean()
median = grouped.median()

# Create a bar chart for each group
for name, group in grouped:
    plt.bar(avg.loc[name].index, avg.loc[name].values)
    plt.title(f'Average for {name}')
    plt.show()

    plt.bar(median.loc[name].index, median.loc[name].values)
    plt.title(f'Median for {name}')
    plt.show()
