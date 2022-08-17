# 문제1)
# http://www.randomservices.org/random/data/Galton.txt
# data를 이용해 아버지 키로 아들의 키를 예측하는 회귀분석 모델을 작성하시오.
# train / test 분리
# Sequential api와 function api 를 사용해 모델을 만들어 보시오.
# train과 test의 mse를 시각화 하시오
# 새로운 아버지 키에 대한 자료로 아들의 키를 예측하시오

from keras.models import Sequential
from keras.layers import Dense
from keras import optimizers
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_table("http://www.randomservices.org/random/data/Galton.txt", sep='\t', usecols=['Father', 'Gender', 'Height'])
data = df[df['Gender'] == 'M'].drop('Gender', axis=1)

x = data.Father
y = data.Height
print(data.head(3))
print(np.corrcoef(x, y))

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state=1)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)



print('1) Sequential API 사용 : 가장 일반적이고 단순한 방법 ------------ ')
model = Sequential()
model.add(Dense(units=5, input_dim=1, activation='linear'))
model.add(Dense(units=1, activation='linear'))
print(model.summary())

opti = optimizers.Adam(learning_rate = 0.001)
model.compile(optimizer=opti, loss='mse', metrics=['mse'])   # mse : 평균제곱오차. 추측값에 대한 정확성을 측정하는 방법

history = model.fit(x=x_train, y=y_train, batch_size=4, epochs=50, verbose=0)
loss_metris = model.evaluate(x=x_test, y=y_test, verbose=0)
print('loss_metris:', loss_metris)

print('실제값:', y_test[:5])
print('예측값:', model.predict(x_test).flatten()[:5])

new_data = [75, 70, 80]
print('아들 키 예측 결과:', model.predict(new_data).flatten())

# 시각화
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')

# 학습 도중에 발생된 변화량을 시각화
plt.plot(history.history['mse'], label='평균제곱오차')
plt.xlabel('학습횟수')
plt.show()



print('2) function API 사용 : 유연한 구조. 입력 데이터로부터 여러 층을 공유하거나 다양한 입출력 사용 가능 --- ')
from keras.layers import Input
from keras.models import Model

# 각 층을 일종의 함수로써 처리를 함 설계부분이 방법1과 다름
inputs = Input(shape = (1,))
# outputs = Dense(1, activation='linear')(inputs) # 이전 층 레이어를 다음 층 함수의 입력으로 사용
output1 = Dense(5, activation='linear')(inputs)
outputs = Dense(1, activation='linear')(output1)
model2 = Model(inputs, outputs)

# 이하는 방법1과 같음
print(model2.summary())

opti = optimizers.Adam(learning_rate = 0.01)
model2.compile(optimizer=opti, loss='mse', metrics=['mse'])   # mse : 평균제곱오차. 추측값에 대한 정확성을 측정하는 방법
history2 = model2.fit(x=x_train, y=y_train, batch_size=4, epochs=50, verbose=0)

loss_metris2 = model2.evaluate(x=x_test, y=y_test, verbose=0)
print('loss_metris:', loss_metris2)

print('실제값:', y_test[:5])
print('예측값:', model.predict(x_test).flatten()[:5])

new_data2 = [75, 70, 80]
print('아들 키 예측 결과:', model.predict(new_data2).flatten())



