# 나이브베이즈 분류기로 비 여부 분류 모델
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn import metrics

df = pd.read_csv("../testdata/weather.csv")
print(df.head(2))
print(df.columns)

x = df[['MinTemp', 'MaxTemp', 'Rainfall']]
label = df['RainTomorrow'].map({'Yes':1, 'No':0})
print(x[:5])
print(label[:5])

x_train, x_test, y_train, y_test = train_test_split(x, label, random_state = 1)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)

gmodel=GaussianNB().fit(x_train, y_train)

pred = gmodel.predict(x_test)
print('예측값:', pred[:10])
print('실제값:', y_test[:10].values)

# k-fold 교차검증
from sklearn import model_selection
cross_val = model_selection.cross_val_score(gmodel, x, label, cv=7)
print(cross_val)
print(cross_val.mean())     # 0.7437

# acc
acc = sum(y_test == pred) / len(pred)
print('분류 정확도:', acc)
print('분류 정확도:', accuracy_score(y_test, pred))

print()
# 새로운 값으로 분류 예측
# print(x_test[:3])
import numpy as np
new_weather = np.array([[0, 16, 10], [10, 36, 0],[10, 36, 40]])
print(gmodel.predict(new_weather))

















