# K-means로 군집이 어려운 경우 DBSCAN을 사용
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
from sklearn.datasets import make_moons
from sklearn.cluster import KMeans, DBSCAN

# sample data
x, _ = make_moons(n_samples=200, noise=0.05, random_state=0)
print(x)

plt.scatter(x[:, 0], x[:, 1])
plt.show()

print('KMeans로 군집화 ----')
km = KMeans(n_clusters = 2, random_state=0).fit(x)
pred1 = km.fit_predict(x)

def plotResult(x, pr):
    plt.scatter(x[pr==0, 0], x[pr==0, 1], c='blue', marker='o', s=40, label='cluster1')
    plt.scatter(x[pr==1, 0], x[pr==1, 1], c='red', marker='s', s=40, label='cluster2')
    plt.legend()
    plt.show()

plotResult(x, pred1)
print()
# K-Means로 클러스터링이 안된 경우 DBSCAN을 사용
dm = DBSCAN(eps=0.2, min_samples=5, metric='euclidean') # 샘플간 최대거리, 점에 대한 이웃 샘플수
pred2 = dm.fit_predict(x)
plotResult(x, pred2)

