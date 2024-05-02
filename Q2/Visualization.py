import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generating sample data for df1
np.random.seed(0)
data1 = {
    'ID': range(1, 21),
    'Age': np.random.randint(18, 65, size=20),
    'Income': np.random.randint(20000, 100000, size=20),
    'Height': np.random.randint(150, 200, size=20),
    'Weight': np.random.randint(50, 100, size=20)
}

# Creating DataFrame df1
df1 = pd.DataFrame(data1)

# Generating sample data for df2
np.random.seed(1)
data2 = {
    'ID': range(21, 41),
    'Age': np.random.randint(18, 65, size=20),
    'Income': np.random.randint(20000, 100000, size=20),
    'Height': np.random.randint(150, 200, size=20),
    'Weight': np.random.randint(50, 100, size=20)
}

# Creating DataFrame df2
df2 = pd.DataFrame(data2)

# Concatenating df1 and df2
combined_df = pd.concat([df1, df2], ignore_index=True)

# Visualizations
# Heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(combined_df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()

# Histogram
plt.figure(figsize=(10, 6))
combined_df['Age'].hist(bins=10, color='skyblue', edgecolor='black', grid=False)
plt.tight_layout()
plt.title('Combined Age Distribution Histogram')
plt.show()

# Box plot
plt.figure(figsize=(10, 6))
sns.boxplot(data=combined_df, palette='Set2')
plt.title('Box Plot')
plt.show()

# Scatter plot
plt.figure(figsize=(10, 6))#size of graph(10*6 inches)
sns.scatterplot(data=combined_df, x='Age', y='Income', hue='Height', size='Weight', sizes=(20, 200))#sizes specifies min and max sizes of the points
plt.title('Scatter Plot')
plt.show()

# Pie chart
plt.figure(figsize=(8, 8))
combined_df['Age'].value_counts().plot.pie(autopct='%1.1f%%', startangle=140)
plt.title('Pie Chart of Age Distribution')
plt.ylabel('')
plt.show()

# Bar graph
plt.figure(figsize=(10, 6))
combined_df['Age'].value_counts().sort_index().plot(kind='bar', color='salmon')
plt.title('Bar Graph of Age Distribution')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()
