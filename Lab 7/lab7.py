import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import datasets
from sklearn.preprocessing import StandardScaler

# Load Iris dataset
iris = datasets.load_iris()
X = iris.data[:, :2]  # Use only the first two features for simplicity

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply kMeans with 2 clusters
kmeans_2 = KMeans(n_clusters=2, random_state=42)
kmeans_2.fit(X_scaled)
labels_2 = kmeans_2.predict(X_scaled)

# Apply kMeans with 3 clusters
kmeans_3 = KMeans(n_clusters=3, random_state=42)
kmeans_3.fit(X_scaled)
labels_3 = kmeans_3.predict(X_scaled)

# Plotting
fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# Plot for 2 clusters
axs[0].scatter(X_scaled[:, 0], X_scaled[:, 1], c=labels_2, cmap='viridis', marker='o')
axs[0].set_title(f'K-Means Clustering with 2 Clusters\nCompleted on 8th March 2024, Dikshith Reddy Macherla, 0789055')
axs[0].set_xlabel('Feature 1')
axs[0].set_ylabel('Feature 2')

# Plot for 3 clusters
axs[1].scatter(X_scaled[:, 0], X_scaled[:, 1], c=labels_3, cmap='viridis', marker='o')
axs[1].set_title(f'K-Means Clustering with 3 Clusters\nCompleted on 8th March 2024, Dikshith Reddy Macherla, 0789055')
axs[1].set_xlabel('Feature 1')
axs[1].set_ylabel('Feature 2')

plt.tight_layout()
plt.show()
