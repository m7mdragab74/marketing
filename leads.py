import pandas as pd
import numpy as np

# Read dataset
df = pd.read_excel("marketing_dataset.xlsx", sheet_name="Leads")

#data exploration
df.head()
df.info()
df.isnull().sum()

#data cleaning
df['Status'] = df['Status'].fillna('Unknown')
print(df.isnull().sum())

df.to_excel("Leads.xlsx", index=False)