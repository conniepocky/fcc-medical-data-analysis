import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('data/medical_examination.csv')

# 2
df['overweight'] = df.apply(lambda x: 1 if x['weight'] / ((x['height'] / 100) ** 2) > 25 else 0, axis=1)

# 3 normalise data

df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x <= 1 else 1)
df["gluc"] = df["gluc"].apply(lambda x: 0 if x <= 1 else 1)

print(df.head())

# 4
def draw_cat_plot():

    # 5
    df_cat = df.melt(id_vars=['cardio'], value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke']) #melt converts from wide to long format, meaning it will have a column for each variable

    # 6 group by cardio

    df_cat["total"] = 1 # add a column to count how many instances of each variable there are
    df_cat = df_cat.groupby(["cardio", "variable", "value"], as_index=False).count() # group by cardio, variable and value and count the number of instances. e.g when therer is 6378 instances where cardio is 0 and active is 0

    fig = sns.catplot(data=df_cat, kind='bar', x='variable', y="total", hue='value', col='cardio')


    # 9
    fig.savefig('catplot.png')
    return fig