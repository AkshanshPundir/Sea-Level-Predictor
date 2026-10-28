import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', alpha=0.7)
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred = pd.Series([i for i in range(df['Year'].min(), 2050)])
    y_pred = res.slope * x_pred + res.intercept
    ax.plot(x_pred, y_pred, 'r', label='Best Fit Line (All Data)')
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_pred_recent = pd.Series([i for i in range(2000, 2050)])
    y_pred_recent = res_recent.slope * x_pred_recent + res_recent.intercept
    ax.plot(x_pred_recent, y_pred_recent, 'green', label='Best Fit Line (2000-Present)')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    fig.savefig('sea_level_plot.png')
    return plt.gca()