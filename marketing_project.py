import pandas as pd
import numpy as np

# Read dataset
df = pd.read_excel("marketing_dataset.xlsx")

#data exploration
df.head()
df.info()
df.isnull().sum()

#data cleaning 
df['Region'] = df['Region'].fillna('Unknown')
df['Impressions'] = df['Impressions'].fillna(df['Impressions'].mean())
print(df.isnull().sum())