# 本文件用于数据的标准化（Normalization），将标准化数据保存在xiaomi_kaggle_upload_scaled.csv，并使用手肘法确定最佳簇数；
# 输出的图像为手肘法的结果，用于确定最佳簇数。
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# 读取数据
data = pd.read_csv('xiaomi_kaggle_upload_cleaned.csv')

# 分簇的特征：评分、价格、电池容量、存储容量和内存
# 丢弃缺失值
# 如果要使用别的特征，修改下面features中的内容即可
features = data[['ratings', 'price']].dropna()
# features = data[['ratings', 'price', 'battery_capacity', 'storage_capacity', 'ram_capacity']].dropna()

# 标准化特征
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# 将标注化的数据保存到文件
pd.DataFrame(scaled_features, columns=features.columns).to_csv('xiaomi_kaggle_upload_scaled.csv', index=False)

# 手肘法确定最佳簇数
inertia = []
k_values = range(1, 11)
for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_features)
    inertia.append(kmeans.inertia_)

# 作图
plt.figure(figsize=(8, 5))
plt.plot(k_values, inertia, marker='o')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
plt.title('Elbow Method for Optimal k')
plt.show()
