import numpy as np
import pandas as pd

class calc_demo_data:

    def __init__(self):
        tab = pd.read_csv('adult.data.csv')

#race_count
        self.race_count = tab['race'].value_counts()
#average_age_men
        q2 = tab.loc[tab['sex'] == 'Male', 'age']
        self.average_age_men = round(q2.sum() / len(q2), 1)
#percentage_bachelors
        self.percentage_bachelors = round(len(tab[tab['education'] == 'Bachelors']) / len(tab) * 100, 1)
#higher_education_rich
        all_adv_ed = tab.loc[((tab['education'] == 'Bachelors') | (tab['education'] == 'Masters') | (tab['education'] == 'Doctorate'))]
        q4 = tab.loc[((tab['education'] == 'Bachelors') | (tab['education'] == 'Masters') | (tab['education'] == 'Doctorate')) & (tab['salary'] == '>50K')]
        self.higher_education_rich = round(len(q4) / len(all_adv_ed) * 100, 1)
#lower_education_rich
        all_low_ed = tab.loc[~((tab['education'] == 'Bachelors') | (tab['education'] == 'Masters') | (tab['education'] == 'Doctorate'))]
        q5 = tab.loc[(~((tab['education'] == 'Bachelors') | (tab['education'] == 'Masters') | (tab['education'] == 'Doctorate'))) & (tab['salary'] == '>50K')]
        self.lower_education_rich = round(len(q5) / len(all_low_ed) * 100, 1)
#min_work_hours
        self.min_work_hours = tab['hours-per-week'].min()
#rich_percentage
        all_low = tab.loc[tab['hours-per-week'] == 1]
        self.rich_percentage = int(len(tab.loc[(tab['hours-per-week'] == 1) & (tab['salary'] == '>50K')]) / len(all_low) * 100)
#highest_earning_country
        q8 = tab.loc[tab['salary'] == '>50K', 'native-country'].value_counts()
        self.highest_earning_country = q8.index[0]
#highest_earning_country_percentage
        self.highest_earning_country_percentage = round(q8.max() / q8.sum() * 100, 1)
#top_IN_occupation
        self.top_IN_occupation = tab.loc[(tab['native-country'] == 'India') & (tab['salary'] == '>50K'), 'occupation'].value_counts().index[0]

    def __getitem__(self, key):
        return self.__dict__[key]
