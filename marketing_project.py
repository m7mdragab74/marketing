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

#metrics
# CTR
df['CTR'] = df['Clicks'] / df['Impressions']

# Conversion Rate
df['Conversion_Rate'] = df['Conversions'] / df['Clicks']

# CPA (Cost per Acquisition)
df['CPA'] = df['Spend'] / df['Conversions']

# ROAS (Return on Ad Spend)
df['ROAS'] = df['Revenue'] / df['Spend']

#Profit / Profit Margin
df['Profit'] = df['Revenue'] - df['Spend']
df['Profit_Margin'] = df['Profit'] / df['Revenue']

print(df.head())