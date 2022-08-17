import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler    # 표준화 지원 클래스
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
df = pd.read_csv('testdata/student.csv', usecols=['국어', '영어', '수학'])
print(df.head(3))
print(df.corr())
print(df.columns)
model = smf.ols('수학~국어+영어', data=df).fit()
print(model.summary())

# kor_data = pd.DataFrame({'수학':[int(input('국어점수 : '))]})
# print('국어점수로 예측한 수학점수:', np.rint(model.predict(kor_data)))

# x=[1,2,3,4,5]
# y=[8,7,6,4,5]
# print(np.corrcoef(x, y)[0,1])

# data = pd.read_csv('testdata/titanic_data.csv', usecols=['Survived', 'Pclass', 'Sex', 'Age','Fare'])
# print(data.head(2), data.shape) # (891, 12)
# data.loc[data["Sex"] == "male","Sex"] = 0
# data.loc[data["Sex"] == "female", "Sex"] = 1
# print(data["Sex"].head(2))
# print(data.columns)
#
# feature = data[["Pclass", "Sex", "Fare"]]
# label = data["Survived"]
#
# x_train, x_test, y_train, y_test = train_test_split(feature, label, test_size = 0.3, random_state=12)
# print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)
#
# model = DecisionTreeClassifier()
# model.fit(x_train, y_train) 
# y_pred = model.predict(x_test)
# print('accuracy:', accuracy_score(y_test, y_pred))

# 코드 시작
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.model_selection import train_test_split
# import pandas as pd
# from sklearn.metrics import accuracy_score
#
# df = pd.read_csv("winequality-red.csv")
# df_x = df.drop(['quality'], axis=1)  # feature로 사용. quality를 제외한 나머지 열
# df_y = df['quality']  # label로 사용
# print(df_y.unique())  # [5 6 7 4 8 3]
# print(df_x.columns)
#
# x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size = 0.3, random_state=12)
# print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)
# model = RandomForestClassifier(criterion='entropy', n_estimators=500, random_state=1)
#
# print(model)
# model.fit(x_train, y_train)
# y_pred = model.predict(x_test)
# print('accuracy:', accuracy_score(y_test, y_pred))































