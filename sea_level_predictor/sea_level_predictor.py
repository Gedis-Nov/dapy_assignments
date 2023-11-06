import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():

    tab = pd.read_csv('epa-sea-level.csv')

    ext_yr1 = np.arange(1880, 2051, 1)
    ext_yr2 = np.arange(2000, 2051, 1)

    tab1 = tab[tab['Year'] >= 2000]
    res1 = linregress(tab['Year'], tab['CSIRO Adjusted Sea Level'])
    res2 = linregress(tab1['Year'], tab1['CSIRO Adjusted Sea Level'])

    lin1 = res1.slope * ext_yr1 + res1.intercept
    lin2 = res2.slope * ext_yr2 + res2.intercept

    fig = plt.figure(figsize=(14,7))
    plt.scatter(tab['Year'], tab['CSIRO Adjusted Sea Level'])
    plt.plot(ext_yr1, lin1, c='r')
    plt.plot(ext_yr2, lin2, c='g')
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')

    fig.savefig('scatter_plot.png')
    return fig.gca()
