import pandas as pd
import numpy as np

# Read dataset
df = pd.read_excel("marketing_dataset.xlsx", sheet_name="Campaigns")

#data exploration
df.head()
df.info()
df.isnull().sum()