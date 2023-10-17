import numpy as np
import pandas as pd

tab = pd.read_csv('adult.data.csv')
print('\n', tab.head(20, usecols=[0:]))
print(type(tab))

#QUESTION 01. How many people of each race are represented in this dataset?
#This should be a series with race names as the index labels. (race column)


#print('\n', tab.info())
