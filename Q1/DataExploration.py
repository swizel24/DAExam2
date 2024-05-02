import pandas as pd
import numpy as np

# Generating sample data
np.random.seed(0)
data = {
    'empID': range(1, 21),
    'emp_ct': np.random.choice(["teaching","non-teaching","miscellaneous"], size=20),
    'emp_designation': np.random.choice(["faculty","peon","sweeper"], size=20),
    'emp_dept': np.random.choice(["cs","elec","chem","phy","math"], size=20),
    'emp_sal': np.random.randint(5000, 100000, size=20),
    'emp_ser_years': np.random.randint(0,10,size=20),
    'emp_ser_type': np.random.choice(["permanent","not"],size=20),
    'emp_phd_stat': np.random.choice(["ongoing","withdrawn","completed","nil"], size=20)
}

# Creating DataFrame
df = pd.DataFrame(data)

# Saving DataFrame to CSV
df.to_csv('Q1/sample_data.csv', index=False)




#########################################################################################
# Reading the CSV file
df = pd.read_csv('Q1/sample_data.csv')

# Displaying the first few rows
print("Head:")
print(df.head())

# Displaying the last few rows
print("\nTail:")
print(df.tail())

# Getting basic information about the DataFrame
print("\nInfo:")
print(df.info())

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Mean
print("\nMean:")
print(df.mean(numeric_only=True))

# Median
print("\nMedian:")
print(df.median(numeric_only=True))

# Mode
print("\nMode:")
print(df.mode(numeric_only=True))

# Standard deviation
print("\nStandard Deviation:")
print(df.std(numeric_only=True))

# Count
print("\nCount:")
print(df.count())

# Shape
print("\nShape:")
print(df.shape)

# Data types
print("\nData Types:")
print(df.dtypes)

# Checking for missing values
print("\nNull Values:")
print(df.isnull().sum())

# Inserting a new row
new_row = {'ID': 21, 'Age': 30, 'Income': 60000, 'Height': 170, 'Weight': 75}
df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
print("\nAfter inserting a new row:")
print(df.tail())

# Deleting a row (let's delete the last row)
df.drop(df.index[-1], inplace=True)
print("\nAfter deleting the last row:")
print(df.tail())

# Inserting a new column
new_column = pd.Series(['Male'] * len(df), name='Gender')
df = pd.concat([df, new_column], axis=1)
print("\nAfter inserting a new column 'Gender':")
print(df.head())

# Deleting a column
df.drop('Gender', axis=1, inplace=True)
print("\nAfter deleting 'Gender' column:")
print(df.head())
