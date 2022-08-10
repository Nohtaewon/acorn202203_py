# 세계적으로 유명한 정치인 일부 얼굴사진 데이터로 분류 작업 - SVM
# 5,749 명의 13,233개 사진을 가지고 있다

from sklearn.datasets import fetch_lfw_people
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.decomposition import PCA
from sklearn.pipeline import make_pipeline

faces = fetch_lfw_people(min_faces_per_person = 60, color = False)
# print(faces)
# print(faces.DESCR)

print(faces.data.shape) # (1348, 2914)
print(faces.data[0])
print(faces.target[0])
print(faces.target_names)
print(faces.images.shape)

plt.imshow(faces.images[0], cmap='bone')
plt.show()













