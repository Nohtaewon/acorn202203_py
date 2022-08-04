# [로지스틱 분류분석 문제1]
# 문1] 소득 수준에 따른 외식 성향을 나타내고 있다. 주말 저녁에 외식을 하면 1, 외식을 하지 않으면 0으로 처리되었다. 
# 다음 데이터에 대하여 소득 수준이 외식에 영향을 미치는지 로지스틱 회귀분석을 실시하라.
# 키보드로 소득 수준(양의 정수)을 입력하면 외식 여부 분류 결과 출력하라.
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
import statsmodels.formula.api as smf 

data = pd.read_csv("../testdata/ex.csv")
df=data.set_index('요일')
data2 = df.drop(['월', '화', '수', '목', '금'], axis=0)

# 분류 모델
formula = '외식유무 ~ 소득수준'
model = smf.logit(formula = formula, data=data2).fit()
print(model.summary())

print('예측값 :', np.rint(model.predict(data2)[:10].values))
print('실제값 :', data2['외식유무'][:10].values)
# 분류 정확도
pred = model.predict(data2)
print('정확도 :', accuracy_score(data2['외식유무'], np.around(pred)))  #  0.9047

new_input_data = pd.DataFrame({'소득수준':[int(input('소득수준 : '))]})
print('외식 유무 :', np.rint(model.predict(new_input_data)))
print('외식을 함' if np.rint(model.predict(new_input_data))[0] == 1 else '외식안함')


