import pandas as pd

# Load dataset
df = pd.read_csv("sales_data_sample.csv", encoding="utf-8")

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Basic info
print("\nDataset Info:")
print(df.info())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Basic statistics
print("\nSummary Statistics:")
print(df.describe())