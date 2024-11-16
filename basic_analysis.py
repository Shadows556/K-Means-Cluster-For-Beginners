# 本文件用于基础的数据分析和提取：读取数据并将其中可以利用的数据进行规范化；将规范化的数据保存到xiaomi_kaggle_upload_cleaned.csv文件中；
# 从评分角度出发，绘制其与价格、电池容量、存储容量和内存的散点图，以展示它们之间的关系；检查是否可以找出一些聚类的特征；是否存在离群点。
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import MultipleLocator

# 读取数据
data = pd.read_csv('xiaomi_kaggle_upload.csv')

# 消除数据的单位并规范价格
data['price'] = data['price'].replace('[₹,]', '', regex=True).astype(float)

# 使用正则表达式提取电池容量
data['battery_capacity'] = data['battery'].str.extract(r'(\d+)\s*mAh').astype(float)

# 使用正则表达式提取存储容量
data['storage_capacity'] = data['storage_ram'].str.extract(r'Internal Storage(\d+)\s*GB').astype(float)

# 使用正则表达式提取内存
data['ram_capacity'] = data['storage_ram'].str.extract(r'RAM(\d+)\s*GB').astype(float)

# 在原始数据中，部分数据存储容量和内存标注存在数据方向的问题：
# 原本的数据应该为“Storage128 GBRAM4 GBMemory ”，部分数据出错，为“Storage4 GBRAM128 GBMemory ”。这部分数据较少，直接筛选掉。
# 筛选：在数据中存在存储容量需大于等于16，内存容量需小于等于16。
data = data[(data['storage_capacity'] >= 16) & (data['ram_capacity'] <= 16)]

# 保存处理后的数据
data.to_csv('xiaomi_kaggle_upload_cleaned.csv', index=False)

# 绘制散点图，展示ratings和price的关系
plt.figure(figsize=(10, 6))
plt.scatter(data['ratings'], data['price'], alpha=0.6, color='b', edgecolors='k')
plt.title('Ratings vs. Price')
plt.xlabel('Ratings')
plt.ylabel('Price')
plt.gca().yaxis.set_major_locator(MultipleLocator(3000))
plt.grid(True)
plt.show()

# 绘制散点图，展示ratings和电池容量的关系
plt.figure(figsize=(10, 6))
plt.scatter(data['ratings'], data['battery_capacity'], alpha=0.6, color='r', edgecolors='k')
plt.title('Ratings vs. Battery Capacity')
plt.xlabel('Ratings')
plt.ylabel('Battery Capacity (mAh)')
plt.grid(True)
plt.show()

# 绘制散点图，展示ratings和存储容量的关系
plt.figure(figsize=(10, 6))
plt.scatter(data['ratings'], data['storage_capacity'], alpha=0.6, color='g', edgecolors='k')
plt.title('Ratings vs. Storage Capacity')
plt.xlabel('Ratings')
plt.ylabel('Storage Capacity (GB)')
plt.grid(True)
plt.show()

# 绘制散点图，展示ratings和内存的关系
plt.figure(figsize=(10, 6))
plt.scatter(data['ratings'], data['ram_capacity'], alpha=0.6, color='m', edgecolors='k')
plt.title('Ratings vs. RAM Capacity')
plt.xlabel('Ratings')
plt.ylabel('RAM Capacity (GB)')
plt.grid(True)
plt.show()
