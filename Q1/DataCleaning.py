import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv('Q1/sample_data.csv')

# Drop irrelevant columns (assuming 'empID' is irrelevant for analysis)
df.drop('empID', axis=1, inplace=True)

# Rename columns for clarity (if needed)
# Since the dataset does not include 'Age', 'Income', 'Height', and 'Weight', this step can be skipped or adjusted.
df.rename(columns={'emp_ct': 'Employee Category'}, inplace=True)

# Drop duplicate rows if any
df.drop_duplicates(inplace=True)

# Checking for null values after cleaning
print("Null Values after cleaning:")
print(df.isnull().sum())

# Replace null values with mean for numerical columns
df.fillna(df.mean(numeric_only=True), inplace=True)

# Displaying the cleaned DataFrame
print("\nCleaned DataFrame:")
print(df)

# Save the cleaned DataFrame to a CSV file
df.to_csv('Q1/cleaned_data.csv', index=False)