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
df['Month_Number'] = df['Date'].dt.month
df['Month_Name'] = df['Date'].dt.strftime('%b')
df['Day'] = df['Date'].dt.day

#metrics
# CTR
df['CTR'] = np.where(df['Impressions'] > 0, df['Clicks'] / df['Impressions'], 0)

# Conversion Rate
df['Conversion_Rate'] = np.where(df['Clicks'] > 0, df['Conversions'] / df['Clicks'], 0)

# CPA (Cost per Acquisition)
df['CPA'] = np.where(df['Conversions'] > 0, df['Spend'] / df['Conversions'], 0)

# ROAS (Return on Ad Spend)
df['ROAS'] = np.where(df['Spend'] > 0, df['Revenue'] / df['Spend'], 0)

#Profit / Profit Margin
df['Profit'] = df['Revenue'] - df['Spend']
df['Profit_Margin'] = np.where(df['Revenue'] > 0, df['Profit'] / df['Revenue'], 0)

print(df.head())

df.to_excel("marketing_cleaned.xlsx", index=False)