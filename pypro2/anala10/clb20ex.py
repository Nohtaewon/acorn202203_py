from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import pandas as pd

df = pd.read_csv("../testdata/Heart.csv")
print(df.head(3), df.shape) # (303, 15)
print(df.info())
print(df.columns)
print(df.isnull().sum())

x = df.drop(['Unnamed: 0', 'ChestPain', 'Thal', 'AHD'], axis=1)
x['Ca'].fillna(x['Ca'].mean(), inplace=True)
y = df['AHD']

print(x[:3].values)
print(y[:3].values)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)
# (212, 11) (91, 11) (212,) (91,)
print()

# model
model = svm.SVC(C=0.1).fit(x_train, y_train)
print(model)

pred = model.predict(x_test)
print('예측값:', pred[:10])
print('실제값:', y_test[:10].values)

# acc
acc_score = metrics.accuracy_score(y_test, pred)
print('정확도:', acc_score)

print()
# 교차 검증 모델
from sklearn import model_selection
cross_vali = model_selection.cross_val_score(model, x, y, cv=3)
print('각각의 검증 정확도 :', cross_vali)
print('평균 검증 정확도 :', cross_vali.mean())










