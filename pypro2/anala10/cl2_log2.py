# 날씨 정보로 다음날 비가 올지 예측하는 분류 모델
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import statsmodels.api as sm
import statsmodels.formula.api as smf 

data = pd.read_csv("../testdata/weather.csv")
print(data.head(2), data.shape)     # (366, 12)

data2 = pd.DataFrame()
data2 = data.drop(['Date', 'RainToday'], axis=1)
data2['RainTomorrow'] = data2['RainTomorrow'].map({'Yes':1, 'No':0})
print(data2.head(2), data2.shape)   # (366, 10)
print(data2.RainTomorrow.unique())

print()
# 분류모델의 overfitting(과적합) 방지를 목적으로 train(학습용)/test(검정용) dataset을 작성
train, test = train_test_split(data2, test_size=0.3, random_state = 42)
print(train.shape, test.shape)  # (256, 10) (110, 10)

# 분류 모델
# my_formula = 'RainTomorrow ~ ........'
my_formula = 'RainTomorrow ~'+'+'.join(train.columns.difference(['RainTomorrow']))
print(my_formula)
model = smf.glm(formula = my_formula, data=train, family=sm.families.Binomial()).fit()

print(model.summary())

print('예측값 :', np.rint(model.predict(test)[:10].values))
print('실제값 :', test['RainTomorrow'][:10].values)

# 분류 정확도
# conf_mat = model.pred_table()   # glm()은 지원하지 않음
# print('confusion matrix : \n', conf_mat)
pred = model.predict(test)
print('정확도 :', accuracy_score(test['RainTomorrow'], np.around(pred)))    # 정확도: 0.872727

print()
model2 = smf.logit(formula = my_formula, data=train).fit()
conf_mat = model2.pred_table()
print('confusion matrix : \n', conf_mat)

print('정확도 :', (conf_mat[0][0] + conf_mat[1][1] )/ len(train))   # 정확도 : 0.87109375











