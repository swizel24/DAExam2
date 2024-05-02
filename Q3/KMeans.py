import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('Q3/Q3dataset.csv')

# Ensure the dataset is correctly loaded
print(data.head()) # This will print the first few rows of the dataset to verify it's loaded correctly

# Extracting features (attributes)
# If your dataset does not have a target column to exclude, simply use:
X = data.values

# Implementing K-means with k=3 clusters
kmeans = KMeans(n_clusters=2)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)

# Plotting the clusters
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, cmap='viridis')
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='red', marker='x')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('K-means Clustering')
plt.show()
