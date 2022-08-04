import pandas as pd
import numpy as np
from sklearn.linear_model import  LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

data = pd.read_csv('testdata/Consumo_cerveja.csv')
data= data.dropna()
data['Temperatura Media (C)'] = data['Temperatura Media (C)'].str.replace(",",".")
data['Precipitacao (mm)'] = data['Precipitacao (mm)'].str.replace(",",".")

print(data.head(3))

x = data[['Temperatura Media (C)', 'Precipitacao (mm)']]
print(x[:3], x.shape)

y = data['Consumo de cerveja (litros)'].values
print(y[:3], y.shape)

lmodel = LinearRegression().fit(x,y)
print('회귀계수(slope) : ', lmodel.coef_)
print('회귀계수(intercept) : ', lmodel.intercept_)

pred = lmodel.predict(x)
print('예측값:', np.round(pred[:10], 1))
print('실제값:', y[:10])

print('결정계수(설명력, r2_score) :', r2_score(y, pred))

# 새로운 값으로 예측
new_x = [[11, 0]]
new_pred = lmodel.predict(new_x)
print('%s 평균기온과 %s 강수인 경우 맥주소비량은 약 %s 입니다.'%(new_x[0][0], new_x[0][1] ,new_pred[0]))

