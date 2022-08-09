# Titanic dataset으로 LogisticRegression, DecisionTreeClassifier, RandomForestClassifier
# 세개의 모델 성능 비교
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/titanic_data.csv")
print(df.head(2), df.shape)
print(df.columns)
df.drop(columns=['PassengerId', 'Name', 'Ticket'], inplace=True)
print(df.head(2), df.shape)

print(df.info())
print(df.isnull().sum())

# null 처리
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Cabin'].fillna('N', inplace=True)    # 방 호수 N
df['Embarked'].fillna('N', inplace=True)    # 탑승지 N
print(df.isnull().sum())

print()
# object 타입인 Sex, Cabin, Embarked 열들의 상태를 분류해서 보기
print('Sex:', df['Sex'].value_counts())
print('Cabin:', df['Cabin'].value_counts())
print('Embarked:', df['Embarked'].value_counts())
df['Cabin'] = df['Cabin'].str[:1]   # Cabin 호수번호는 제외함
print(df.head(2))

print()
# 성별이 생존확률에 미친 영향
print(df.groupby(['Sex', 'Survived'])['Survived'].count())  # 0은 사망
print(233 / (81 + 233))     # 74.2%
print(109 / (109 + 468))    # 18.9%

# 시각화
# sns.barplot(x='Sex', y='Survived', data=df, ci=95)
# plt.show()

print()
# 문자열 데이터를 숫자형으로 변환
from sklearn import preprocessing

def label_encode(datas):
    cols = ['Cabin', 'Sex', 'Embarked']
    for c in cols:
        lab = preprocessing.LabelEncoder()
        lab = lab.fit(datas[c])
        datas[c] = lab.transform(datas[c])
    return datas 
    
df = label_encode(df)
print(df.head(3))
print(df['Cabin'].unique()) # [7 2 4 6 3 0 1 5 8]
print(df['Sex'].unique())   # [1 0]
print(df['Embarked'].unique())  # [3 0 2 1]

print()
from sklearn.model_selection import train_test_split
feature_df = df.drop(['Survived'], axis='columns') # axis=1
label_df = df['Survived']
print(label_df.head(2))

x_train, x_test, y_train, y_test = train_test_split(feature_df, label_df, test_size=0.2, random_state=1)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)
# (712, 8) (179, 8) (712,) (179,)

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

logmodel = LogisticRegression(solver = 'lbfgs', max_iter=500).fit(x_train, y_train)
decmodel = DecisionTreeClassifier().fit(x_train, y_train)
rfmodel = RandomForestClassifier().fit(x_train, y_train)

logpredict = logmodel.predict(x_test)
print('LogisticRegression acc:{0:.5f}'.format(accuracy_score(y_test, logpredict)))

decpredict = decmodel.predict(x_test)
print('DecisionTreeClassifier acc:{0:.5f}'.format(accuracy_score(y_test, decpredict)))
rfpredict = rfmodel.predict(x_test)
print('RandomForestClassifier acc:{0:.5f}'.format(accuracy_score(y_test, rfpredict)))


