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

# plt.imshow(faces.images[0], cmap='bone')
# plt.show()

fig, ax = plt.subplots(3, 5)
# print(fig)
# print(ax.flat, len(ax.flat))

# for i, axi in enumerate(ax.flat):
#     axi.imshow(faces.images[i], cmap='bone')
#     axi.set(xticks=[], yticks=[], xlabel=faces.target_names[faces.target[i]])
#
# plt.show()

# 이미지 차원 축소 : PCA
m_pca = PCA(n_components = 150, whiten=True, random_state=0)
x_low = m_pca.fit_transform(faces.data)
print(x_low[0], x_low.shape)   # (1348, 150)

m_svc = SVC(C=1)

# 모델 설계
model = make_pipeline(m_pca, m_svc)     # 선처리기와 분류기를 묶어서 실행
print(model)

# train / test 
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(faces.data, faces.target, random_state = 1)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)
# (1011, 2914) (337, 2914) (1011,) (337,)

model.fit(x_train, y_train)

pred=model.predict(x_test)
print('예측값:', pred[:10])
print('실제값:', y_test[:10])

from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
mat = confusion_matrix(y_test, pred)
print('confusion_matrix:\n', mat)
print('acc:', accuracy_score(y_test, pred))
print('report:\n', classification_report(y_test, pred, target_names=faces.target_names))


# 분류 결과를 시각화
fig, ax = plt.subplots(4, 6)

for i, axi in enumerate(ax.flat):
    axi.imshow(x_test[i].reshape(62, 47), cmap='bone')
    axi.set(xticks=[], yticks=[])
    axi.set_ylabel(faces.target_names[pred[i]].split()[-1], 
                   color='black' if pred[i] == y_test[i] else 'red')
    fig.suptitle('pred result', size=14)

plt.show()

# 오지 행렬 시각화
import seaborn as sns
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False,
            xticklabels = faces.target_names, yticklabels=faces.target_names)

plt.xlabel('true(real) label')
plt.ylabel('pred(real) label')
plt.show()











