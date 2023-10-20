import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

tab = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
bmi = tab['weight'] / np.square(tab['height'] / 100)
tab['overweight'] = (bmi > 25).astype('uint8')

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
tab['cholesterol'] = (tab['cholesterol'] != 1).astype('uint8')
tab['gluc'] = (tab['gluc'] != 1).astype('uint8')

def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    melt_tab = tab.melt(id_vars=['cardio'], value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    melt_tab = melt_tab.reset_index() \
                .groupby(['variable', 'cardio', 'value']) \
                .agg('count') \
                .rename(columns={'index': 'total'}) \
                .reset_index()

    # Draw the catplot with 'sns.catplot()'
    ax = sns.catplot(x='variable', col='cardio',  hue='value', kind='count', data=melt_tab)
    ax.set(ylabel='total')

    # Do not modify the next two lines
    ax.savefig('catplot.png')
    return ax

# Draw Heat Map
def draw_heat_map():
    # Clean the data
    heat_tab = tab[
        (tab['ap_lo'] <= tab['ap_hi'])
        & (tab['height'] >= tab['height'].quantile(0.025))
        & (tab['height'] <= tab['height'].quantile(0.975))
        & (tab['weight'] >= tab['weight'].quantile(0.025))
        & (tab['weight'] <= tab['weight'].quantile(0.975))]

    # Calculate the correlation matrix
    corr = heat_tab.corr()

    # Generate a mask for the upper triangle
    tri_mask = np.triu(np.ones_like(corr))

    # Set up the matplotlib figure
    fig = plt.figure(figsize=(12,6))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, mask=tri_mask, annot=True, fmt='.1f', center=0, vmin=0.5, vmax=0.5)

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
