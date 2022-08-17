# 단순선형회귀모델 작성 : 생성방법 3가지 경험하기
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras import optimizers
import numpy as np

# 공부에 투자한 시간에 따른 성적 결과 예측
x_data = np.array([1,2,3,4,5], dtype=np.float32)    # feature
y_data = np.array([11,32,53,64,70], dtype=np.float32)    # label
print(np.corrcoef(x_data, y_data))  # 0.9743547 이고 두 변수 간에는 인과관계가 있다고 가정

print('1) Sequential API 사용 : 가장 일반적이고 단순한 방법 ------------ ')
model = Sequential()
model.add(Dense(units=2, input_dim=1, activation='linear'))
model.add(Dense(units=1, activation='linear'))
print(model.summary())

opti = optimizers.Adam(learning_rate = 0.01)
model.compile(optimizer=opti, loss='mse', metrics=['mse'])   # mse : 평균제곱오차. 추측값에 대한 정확성을 측정하는 방법
history = model.fit(x=x_data, y=y_data, batch_size=1, epochs=100, verbose=0)

loss_metris = model.evaluate(x=x_data, y=y_data, batch_size=1, verbose=0)
print('loss_metris:', loss_metris)
from sklearn.metrics import r2_score
print('설명력:', r2_score(y_data, model.predict(x_data)))
print('실제값:', y_data)
print('예측값:', model.predict(x_data).flatten())

new_data = [1.5, 2.3, 5.8]
print('새 점수 예측 결과:', model.predict(new_data).flatten())

# 시각화
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')
plt.plot(x_data, model.predict(x_data), 'b', x_data, y_data, 'ko')
plt.xlabel('공부시간')
plt.ylabel('점수')
plt.show()

# 학습 도중에 발생된 변화량을 시각화
plt.plot(history.history['mse'], label='평균제곱오차')
plt.xlabel('학습횟수')
plt.ylabel('mse')
plt.show()

print('2) function API 사용 : 유연한 구조. 입력 데이터로부터 여러 층을 공유하거나 다양한 입출력 사용 가능 --- ')
from keras.layers import Input
from keras.models import Model

# 각 층을 일종의 함수로써 처리를 함 설계부분이 방법1과 다름
inputs = Input(shape = (1,))
# outputs = Dense(1, activation='linear')(inputs) # 이전 층 레이어를 다음 층 함수의 입력으로 사용
output1 = Dense(2, activation='linear')(inputs)
outputs = Dense(1, activation='linear')(output1)
model2 = Model(inputs, outputs)

# 이하는 방법1과 같음
print(model2.summary())

opti = optimizers.Adam(learning_rate = 0.01)
model2.compile(optimizer=opti, loss='mse', metrics=['mse'])   # mse : 평균제곱오차. 추측값에 대한 정확성을 측정하는 방법
history2 = model2.fit(x=x_data, y=y_data, batch_size=1, epochs=100, verbose=0)

loss_metris2 = model2.evaluate(x=x_data, y=y_data, batch_size=1, verbose=0)
print('loss_metris:', loss_metris2)
from sklearn.metrics import r2_score
print('설명력:', r2_score(y_data, model2.predict(x_data)))
print('실제값:', y_data)
print('예측값:', model2.predict(x_data).flatten())





















