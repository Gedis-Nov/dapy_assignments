import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

tab = pd.read_csv('fcc-forum-pageviews.csv')

tab = tab[(tab['value'] >= tab['value'].quantile(0.025)) & (tab['value'] <= tab['value'].quantile(0.975))]

def draw_line_plot():
    fig = tab.plot(figsize=(25,10), kind='line', color='red', xlabel='Date', ylabel='Page Views', title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    res_tab = tab.resample('M').mean().reset_index()
    cols = ['Years', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    t_tab = pd.DataFrame({'Years':['2016', '2017', '2018', '2019']})
    for i in range(12):
        vval = []
        for j in range(4):
            y_tab = res_tab.loc[res_tab['date'].dt.year == (2016 + j)]
            mdat = y_tab.loc[y_tab['date'].dt.month == (i + 1), 'value']
            vval.append(mdat.values[0]) if len(mdat) != 0 else vval.append(float(0))
        t_tab[i] = vval
    t_tab.columns = cols

    pcols = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    fig = t_tab.plot(x='Years', y=pcols, kind='bar', ylabel='Average Page Views', figsize=(6,6))
    plt.legend(title='Months')
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    r_tab = tab.reset_index()
    r_tab['Year'] = r_tab['date'].dt.year
    r_tab['Month'] = r_tab['date'].dt.month_name().str[:3]

    fig, ax = plt.subplots(1, 2, figsize=(25,8))
    ax[0].set_title('Year-wise Box Plot (Trend)')
    ax[1].set_title('Month-wise Box Plot (Seasonality)')

    yr = sns.boxplot(x='Year', y='value', data=r_tab, palette='deep', flierprops={'marker': '*', 'markersize': 3}, ax=ax[0])
    yr.set_yticks(np.arange(0,220000,20000))
    mon = sns.boxplot(x='Month', y='value', data=r_tab, order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], palette='husl', flierprops={'marker': '*', 'markersize': 3}, ax=ax[1])
    mon.set_yticks(np.arange(0,220000,20000))

    fig.savefig('box_plot.png')
    return fig
