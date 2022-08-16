# iris dataset으로 지도학습(KNN), 비지도학습(K-means) 비교 정리

from sklearn.datasets import load_iris
import numpy as np
from sklearn import metrics

iris_dataset = load_iris()
print(iris_dataset['data'][:3])
print(iris_dataset['feature_names'])
print(iris_dataset['target'][:3])
print(iris_dataset['target_names'])

# train / test
from sklearn.model_selection import train_test_split
train_x, test_x, train_y, test_y = train_test_split(iris_dataset['data'], iris_dataset['target'], test_size=0.25, random_state=42)
print(train_x.shape, test_x.shape, train_y.shape, test_y.shape)
print()

print('지도학습: k최근접 이웃 알고리즘으로 분류 모델 작성 : classfier')
from sklearn.neighbors import KNeighborsClassifier
# knnModel = KNeighborsClassifier(n_neighbors=1, weights='distance', metric='euclidean')
knnModel = KNeighborsClassifier(n_neighbors=3, weights='distance', metric='euclidean')
knnModel.fit(train_x, train_y)  # feature, label로 학습 (문제지와 답지가 있는 형태)

# 모델 성능 측정 후 예측
pred = knnModel.predict(test_x)
print(pred[:10])
print('분류 정확도:', np.mean(pred == test_y))
print('분류 정확도:', metrics.accuracy_score(test_y, pred))

# 새로운 값으로 예측
new_input = np.array([[6.1, 2.8, 4.7, 1.1]])
print('새로운 값 예측 결과 : ', knnModel.predict(new_input))
dist, index= knnModel.kneighbors(new_input)
print(dist, index)  # k가 1일 때 [[0.31622777]] [[71]]
# k가 3일 때 [[0.31622777 0.37416574 0.46904158]] [[71 82 31]]

print('비지도학습: K-means 이웃 알고리즘으로 분류 모델 작성 : cluster')
from sklearn.cluster import KMeans
kmeansModel = KMeans(n_clusters=3, init='k-means++', random_state=0)
kmeansModel.fit(train_x)    # label은 없음. (문제지만 있는 형태)
print(kmeansModel.labels_)  # [0 0 1 1 1 0 0 1 1 2 1 .....
print()
print('0 cluster: ', train_y[kmeansModel.labels_==0])
print('1 cluster: ', train_y[kmeansModel.labels_==1])
print('2 cluster: ', train_y[kmeansModel.labels_==2])
new_input = np.array([[6.1, 2.8, 4.7, 1.1]])
print('새로운 값 예측 결과 : ', kmeansModel.predict(new_input)) # [1] 군집으로 분류
print('군집모델 성능 파악')
pred_cluster = kmeansModel.predict(test_x)
print(pred_cluster)

np_arr = np.array(pred_cluster)
np_arr[np_arr == 0], np_arr[np_arr == 1], np_arr[np_arr == 2] = 3, 4, 5     # 임시 저장용
np_arr[np_arr == 3] = 0
np_arr[np_arr == 4] = 1
np_arr[np_arr == 5] = 2
print(np_arr)

pred_label = np_arr.tolist()
print(pred_label)
print('test acc:', np.mean(pred_label == test_y))














