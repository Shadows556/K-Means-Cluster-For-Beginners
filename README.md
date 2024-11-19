# K-Means-Cluster-For-Beginners

最近正在学习无监督机器学习中的聚类分析。感觉对于一些毫无头绪的数据来说，使用聚类分析可以很快速的得出一些思考的方向。所以非常认真的对待了这次的学习，
决定认真的完成这次作业，并将最后的结果上传至Github，用于记录自己在机器学习方面的收获。
如果能为其他同样正在学习类似话题和内容的数据分析者提供一点点帮助那就更好了！

K-means聚类：K-means聚类是一种常见且高效的无监督学习算法,用于将数据集分成K个簇(clusters)。每个簇都有一个质心(center)，质心是簇中所有点的平均值。
K-means算法的目标是最小化所有点到其所属簇质心的距离之和。

本项目基于Kaggle数据库中小米在印度的销售情况数据，完整进行一次最简单的K-means聚类分析并给出对应的结论。

## 一：整体思路

#### 1.数据清理

运行basic_analysis.py；该文件读取数据并将其中可以利用的数据进行规范化；将规范化的数据保存到xiaomi_kaggle_upload_cleaned.csv文件中；
同时该文件会输出从评分角度出发，其与价格、电池容量、存储容量和内存的散点图，以展示它们之间的关系；检查是否可以找出一些聚类的特征；是否存在离群点。

#### 2.标准化以及手肘法确定最佳簇数

运行cluster_number.py；该文件用于数据的标准化（Normalization），将标准化数据保存在xiaomi_kaggle_upload_scaled.csv，
被保存的数据会被用以手肘法以确定最佳簇数；

#### 3.使用K-means算法进行聚类分析，并绘制对应的散点图

运行k-means.py；该文件用于已经标准化的数据进行K-means聚类分析，并将聚类结果保存到文件，整理为可视化的形式输出。

## 二：结果呈现

#### 1.数据展示

###### 评分与价格（Rating vs. Price）
![Rating vs. Price](./outputs/Rating%20vs.%20Price.png)

###### 评分与电池容量（Ratings vs. Battery Capacity）
![Ratings vs. Battery Capacity](./outputs/Ratings%20vs.%20Battery%20Capacity.png)

###### 评分与RAM容量（Ratings vs. RAM Capacity）
![Ratings vs. RAM Capacity](./outputs/Ratings%20vs.%20RAM%20Capacity.png)

###### 评分与存储容量（Ratings vs. Storage Capacity）
![Ratings vs. Storage Capacity](./outputs/Ratings%20vs.%20Storage%20Capacity.png)

#### 2.标准化以及手肘法确定最佳簇数

###### 肘部法则（Elbow Method）
![Elbow Method for Optimal k](./outputs/Elbow%20Method%20for%20Optimal%20k(Rating&Price).png)

#### 3.聚类分析和其散点图

###### K-Means 聚类（K-Means Clustering）
![K-Means Clustering of Ratings and Price](./outputs/K-Means%20Clustering%20of%20Ratings%20and%20Price.png)

#### 4.一些尝试的结论分析

黄绿色簇（左下角）：评分较低（2.5 至 3.5），价格较低。这可能对应的是评价较差的低端或较老机型。

红色簇（右下部）：评分较高（4.0 至 4.25），价格中低。这些可能是性价比高、销量好的主流机型。

蓝色簇（右中部）：评分较高（4.0 至 4.5），价格中高。或许是配置更高的旗舰机型。

绿色簇（右上角）：评分较高（4.0 至 4.5），价格极高。这可能是高端市场中的奢侈型号或特殊版本。

可以看得出小米手机在印度市场的整体分布是较为符合第一直觉的；
低端老旧产品评分较低，高性价比的产品评分较高；高端机型在用户体验方面也较好，评分较高；

#### 5.相关说明

如果要尝试其他的分析，例如评分和电池/内存等，可以在clusters_number和k-means中进行修改；