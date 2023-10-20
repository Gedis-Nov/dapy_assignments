import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

tab = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
tab['overweight'] = tab['weight'] / (tab['height'] / 100) **2
tab.loc[(tab['overweight'] <= 25), 'overweight'] = 0
tab.loc[(tab['overweight'] > 25), 'overweight'] = 1
tab['overweight'] = tab['overweight'].astype(int)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
tab.loc[tab['cholesterol'] == 1,'cholesterol'] = 0
tab.loc[tab['gluc'] == 1, 'gluc'] = 0
tab.loc[tab['cholesterol'] > 1,'cholesterol'] = 1
tab.loc[tab['gluc'] > 1, 'gluc'] = 1

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    q3 = tab.melt(id_vars='cardio',value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    #df_cat = None

    # Draw the catplot with 'sns.catplot()'
    ax1 = sns.catplot(col='cardio', x='variable', hue='value', kind='count', data=q3)
    ax1.set(ylabel='total')


    # Get the figure for the output
    print(ax)

    # Do not modify the next two lines
    ax1.savefig('catplot.png')
    return ax

# Draw Heat Map
def draw_heat_map():
    # Clean the data
    ctab = tab.copy()
    ctab = ctab[ctab['ap_lo'] <= ctab['ap_hi']]
    ctab = ctab[ctab['height'] >= ctab['height'].quantile(0.025)]
    ctab = ctab[ctab['height'] <= ctab['height'].quantile(0.975)]
    ctab = ctab[ctab['weight'] >= ctab['weight'].quantile(0.025)]
    ctab = ctab[ctab['weight'] <= ctab['weight'].quantile(0.975)]

    # Calculate the correlation matrix
    cor_ctab = ctab.corr()

    # Generate a mask for the upper triangle
    tri_mask = np.triu(np.ones_like(cor_ctab))

    # Set up the matplotlib figure

    # Draw the heatmap with 'sns.heatmap()'
    bx = sns.heatmap(cor_ctab, linewidths=0.5, mask=tri_mask, annot=True, annot_kws={'size':5})
    print(bx)

    # Do not modify the next two lines
    bx.savefig('heatmap.png')
    return bx
