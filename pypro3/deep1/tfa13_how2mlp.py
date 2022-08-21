# 회귀용 MLP 작성 : Sequential, Function api
# 캘리포니아 주택 가격 dataset 사용

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import Dense, Input, Concatenate
from keras import Model
import matplotlib.pyplot as plt

datas = fetch_california_housing()
print(datas.keys())
print(datas.data[:3])
print(datas.target[:3])
print(datas.feature_names)
print(datas.target_names)

# train / validation / test
print(datas.data.shape)     # (20640, 8)
x_train_all, x_test, y_train_all, y_test = train_test_split(datas.data, datas.target, random_state=12)
print(x_train_all.shape, x_test.shape, y_train_all.shape, y_test.shape)
# (15480, 8) (5160, 8) (15480,) (5160,)
x_train, x_valid, y_train, y_valid = train_test_split(x_train_all, y_train_all, random_state=12)
print(x_train.shape, x_valid.shape, y_train.shape, y_valid.shape)
# (11610, 8) (3870, 8) (11610,) (3870,)

# 표준화
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_valid = scaler.fit_transform(x_valid)
x_test = scaler.fit_transform(x_test)
print(x_test[:1])
print(scaler.inverse_transform(x_test[:1]))

print('----Sequential API로 단순한 형태의 MLP(deep learning network) 작성----')
model = Sequential()
model.add(Dense(units=30, activation='relu', input_shape=x_train.shape[1:]))
model.add(Dense(units=1))
model.compile(optimizer='adam', loss='mse', metrics=['mse'])
print(model.summary())
history = model.fit(x_train, y_train, epochs=20, validation_data=(x_valid, y_valid), verbose=2)
print('evaluate:', model.evaluate(x_test, y_test))

x_new = x_test[:3]
y_pred=model.predict(x_new)
print('예측값:', y_pred.ravel())
print('실제값:', y_test[:3])


plt.plot(range(1, 21), history.history['mse'], c='b', label='mse')
plt.plot(range(1, 21), history.history['val_mse'], c='r', label='val_mse')
plt.xlabel('epochs')
plt.ylabel('mse')
plt.legend()
plt.show()

print('----Function API로 복잡한 형태의 MLP(deep learning network) 유연하게 작성----')
input_ = Input(shape=x_train.shape[1:])
net1 = Dense(units=30, activation='relu')(input_)
net2 = Dense(units=30, activation='relu')(net1)
concat = Concatenate()([input_,net2])   # 마지막 은닉층의 출력과 입력을 연결
output = Dense(units=1)(concat)
model2 = Model(inputs=[input_], outputs=[output]) # 최종적으로 입력과 출력을 지정하여 케라스 모델 완성
model2.compile(optimizer='adam', loss='mse', metrics=['mse'])

history = model2.fit(x_train, y_train, epochs=20, validation_data=(x_valid, y_valid), verbose=2)
print('evaluate:', model2.evaluate(x_test, y_test))

x_new = x_test[:3]
y_pred2=model2.predict(x_new)
print('예측값:', y_pred2.ravel())
print('실제값:', y_test[:3])


plt.plot(range(1, 21), history.history['mse'], c='b', label='mse')
plt.plot(range(1, 21), history.history['val_mse'], c='r', label='val_mse')
plt.xlabel('epochs')
plt.ylabel('mse')
plt.legend()
plt.show()

print('----Function API: 일부 특성은 짧은 경로로 전달하고, 다른 특성은 깊은 경로로 전달하는 모델 작성--')

# 5개의 특성(0~4)은 짧은 경로로, 6개의 특성(2~7)은 깊은 경로로 보낸다고 가정
input_a = Input(shape=[5], name='wide_input')   # 층이 복잡할 땐 name을 주자
input_b = Input(shape=[6], name='deep_input')
net1 = Dense(units=30, activation='relu')(input_b)
net2 = Dense(units=30, activation='relu')(net1)
concat=Concatenate()([input_a, net2])
output = Dense(units=1, name='output')(concat)
model3 = Model(inputs=[input_a, input_b], outputs=[output])
model3.compile(optimizer='adam', loss='mse', metrics=['mse'])

# 입력데이터 모양
x_train_a, x_train_b = x_train[:, :5], x_train[:, 2:]
# print(x_train[:2])
# print(x_train_a[:2])
# print(x_train_b[:2])

x_valid_a, x_valid_b = x_valid[:, :5], x_valid[:, 2:]

x_test_a, x_test_b = x_test[:, :5], x_test[:, 2:]   # evluate용
x_new_a, x_new_b = x_test_a[:3], x_test_b[:3]   # predict용

history = model3.fit((x_train_a, x_train_b), y_train, epochs=20, validation_data=((x_valid_a, x_valid_b), y_valid), verbose=2)
print('evaluate:', model3.evaluate((x_test_a,x_test_b), y_test))


y_pred3=model3.predict((x_new_a, x_new_b))
print('예측값:', y_pred3.ravel())
print('실제값:', y_test[:3])


plt.plot(range(1, 21), history.history['mse'], c='b', label='mse')
plt.plot(range(1, 21), history.history['val_mse'], c='r', label='val_mse')
plt.xlabel('epochs')
plt.ylabel('mse')
plt.legend()
plt.show()


















