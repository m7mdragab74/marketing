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
df['Impressions'] = df['Impressions'].fillna(df['Impressions'].median())
df['Impressions'] = df['Impressions'].astype(int)
df.drop_duplicates(inplace=True)
print(df.isnull().sum())

#data transformation
df['Campaign_Name'] = df['Campaign_Name'].str.strip().str.title()
df['Channel'] = df['Channel'].str.strip().str.title()
df['Device'] = df['Device'].str.strip().str.title()
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Month_Name'] = df['Date'].dt.strftime('%b')
df['Day'] = df['Date'].dt.day

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

df.to_excel("marketing_cleaned.xlsx", index=False)