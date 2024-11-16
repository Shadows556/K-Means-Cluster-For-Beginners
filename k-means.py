import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans

# 读取数据
data = pd.read_csv('xiaomi_kaggle_upload_scaled.csv')
data_for_plot = pd.read_csv('xiaomi_kaggle_upload_cleaned.csv')

# scaled_features = data[['ratings', 'price', 'battery_capacity', 'storage_capacity', 'ram_capacity']]
scaled_features = data[['ratings', 'price']]

# 选择K为4进行聚类
optimal_k = 4
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
clusters = kmeans.fit_predict(scaled_features)

# 将簇分配添加到数据集中
data.loc[scaled_features.index, 'cluster'] = clusters

# 绘制聚类结果
plt.figure(figsize=(10, 6))
colors = ['r', 'g', 'b', 'y']
for cluster in range(optimal_k):
    cluster_data = data[data['cluster'] == cluster]
    plt.scatter(cluster_data['ratings'], cluster_data['price'], alpha=0.6, edgecolors='k', color=colors[cluster])
plt.title('K-Means Clustering of Ratings and Price')
plt.xlabel('Ratings')
plt.ylabel('Price')
plt.grid(True)
plt.show()

# 将聚类结果保存到文件
data.to_csv('xiaomi_kaggle_upload_clustered.csv', index=False)
