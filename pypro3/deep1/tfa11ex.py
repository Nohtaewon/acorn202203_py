# 문제2)
# https://github.com/pykwon/python/tree/master/data
# 자전거 공유 시스템 분석용 데이터 train.csv를 이용하여 대여횟수에 영향을 주는 변수들을 골라 다중선형회귀분석 모델을 작성하시오.
# 모델 학습시에 발생하는 loss를 시각화하고 설명력을 출력하시오.
# 새로운 데이터를 input 함수를 사용해 키보드로 입력하여 대한 대여횟수 예측결과를 콘솔로 출력하시오.
from keras.models import Sequential
from keras.layers import Dense
from sklearn.preprocessing import MinMaxScaler, minmax_scale, StandardScaler, RobustScaler
import pandas as pd
import numpy as np

data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/master/data/train.csv")
del data['datetime']
print(data.head(2))
print(data.columns)

fdata = data[['temp','humidity','casual','registered']]
ldata = data[['count']]
print(fdata.head(2))
print(ldata.head(2))

fedata = minmax_scale(fdata, axis=0, copy=True)  # 행기준, 원본 데이터는 보존
print(fdata.head(2))
print(fedata[:2], len(fedata))

# train / test
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(fedata, ldata, shuffle=True,
                                                    test_size=0.3, random_state=123)
print(x_train[:2], x_train.shape)  # (7620, 3)
print(y_train[:2], y_train.shape)  # (7620, 1)

model = Sequential()
model.add(Dense(20, input_dim=3, activation='linear'))
model.add(Dense(10, activation='linear'))
model.add(Dense(1, activation='linear'))

model.compile(optimizer='adam', loss='mse', metrics = ['mse'])
print(model.summary())

history = model.fit(x_train, y_train, epochs=100, 
                    batch_size = 32, verbose=2, 
                    validation_split=0.2)

# 모델 평가 score 보기
loss = model.evaluate(x_test, y_test)   # test data 사용
print('loss : ', loss)
print('loss : ', loss[0])

# history 값 확인
print('history : ', history.history)
print(history.history['loss'])
print(history.history['mse'])
print(history.history['val_loss'])
print(history.history['val_mse'])

# loss 시각화
import matplotlib.pyplot as plt
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.show()

from sklearn.metrics import r2_score
print('r2_score : ', r2_score(y_test, model.predict(x_test)))

# predict
pred = model.predict(x_test[:3])
print('예측값 : ', pred.flatten())
print('실제값 : ', y_test[:3].values.flatten())

new_input = pd.DataFrame({'temp':[int(input('temp : '))], 'humidity':[int(input('humidity : '))]})
print('새로운 대여 예측값: ', model.predict(new_input).flatten())






