# 과적합 방지를 위해 k-fold(k겹 교차검증)
# 보스톤 집값 예측 희귀모델
from keras.datasets import boston_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import Dense, Input, Concatenate
from keras import models, layers
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score
import tensorflow as tf

# CRIM: 지역별 범죄 발생률
# ZN: 25,000평방피트를 초과하는 거주 지역의 비율
# NDUS: 비상업 지역 넓이 비율
# CHAS: 찰스강에 대한 더미 변수(강의 경계에 위치한 경우는 1, 아니면 0)
# NOX: 일산화질소 농도
# RM: 거주할 수 있는 방 개수
# AGE: 1940년 이전에 건축된 소유 주택의 비율
# DIS: 5개 주요 고용센터까지의 가중 거리
# RAD: 고속도로 접근 용이도
# TAX: 10,000달러당 재산세율
# PTRATIO: 지역의 교사와 학생 수 비율
# B: 지역의 흑인 거주 비율
# LSTAT: 하위 계층의 비율
# PRICE: 본인 소유의 주택 가격(중앙값) - 종속변수 (위의 건 독립변수)
(x_train, y_train), (x_test, y_test) = boston_housing.load_data()

print(x_train.shape, y_train.shape, x_test.shape, y_test.shape)
# (404, 13) (404,) (102, 13) (102,)

# feature 는 표준화 : (요소값-평균)/표준편차
# x_train = StandardScaler().fit_transform(x_train)
# print(x_train[:1])

# 직접 수식 사용
mean = x_train.mean(axis=0)
x_train -= mean
std = x_train.std(axis=0)
x_train /= std
print(x_train[:1])

x_test -= mean
x_test /= std 

# 모델 설계
def build_model():
    model = models.Sequential()
    model.add(layers.Dense(64, activation='relu', input_shape=(x_train.shape[1],)))
    model.add(layers.Dense(32, activation='relu'))
    model.add(layers.Dense(1))  # activation='linear' 생략
    
    model.compile(optimizer='adam', loss='mse', metrics=['mse'])
    return model

model=build_model()
print(model.summary())

# 학습
print('train dataset으로 학습. validation X')
# history = model.fit(x_train, y_train, epochs=50, batch_size=10, verbose=0)


print('train dataset으로 학습. validation O')

history = model.fit(x_train, y_train, epochs=50, batch_size=10, verbose=0,
                    validation_split=0.2, callbacks=[tf.keras.callbacks.EarlyStopping(patience=3, monitor='val_loss')])

mse_history = history.history['mse']
print('mse_history:',mse_history)
val_mse_history = history.history['val_mse']
print('val_mse_history:',val_mse_history)
print('val_mse_history mean:', np.mean(val_mse_history))


print('예측값:', np.squeeze(model.predict(x_test[:5])))
print('실제값:', y_test[:5])

print('r2_score:', r2_score(y_test, model.predict(x_test)))


plt.plot(mse_history, 'r', label='mse(loss)')
plt.plot(val_mse_history, 'b', label='val_mse')
plt.xlabel('epochs')
plt.legend()
plt.show()


# 모델 학습 도중 검증 : k-fold(데이터가 비교적 적을 경우 효과적)
k=4
var_sample = len(x_train)//k
print(var_sample)   # 404 개중 101
all_mse_hitory=[]

for i in range(k):
    print('processing fold:',i)
    # print(i*var_sample, ':', (i+1)*var_sample)  # 0:101, 101:202, 202:303, 303:404
    val_x=x_train[i*var_sample:(i+1)*var_sample]    # 검정데이터로 사용
    val_y=y_train[i*var_sample:(i+1)*var_sample]    # 검정데이터로 사용
    # print(val_x.shape, val_y.shape)

    # validation을 제외한 나머지는 train data로 사용
    # 0:101일때 [:0, 101:], 101:202dlfEo [:101, 202:]
    # print([x_train[:i * var_sample], x_train[(i+1)*var_sample:]])
    train_x = np.concatenate([x_train[:i * var_sample], x_train[(i+1)*var_sample:]], axis=0)
    train_y = np.concatenate([y_train[:i * var_sample], y_train[(i+1)*var_sample:]], axis=0)
    # print(train_x.shape)

    model2=build_model()
    history2 = model2.fit(train_x, train_y, epochs=50, batch_size=10, verbose=0,
                    validation_data=(val_x, val_y), callbacks=[tf.keras.callbacks.EarlyStopping(patience=3, monitor='val_loss')])

    mse_history2 = history2.history['mse']
    print('mse_history2:',mse_history2)
    all_mse_hitory.append(mse_history2)
    val_mse_history2 = history2.history['val_mse']

print('mse mean: ', np.mean(all_mse_hitory))
print('r2_score:', r2_score(y_test, model2.predict(x_test)))
plt.plot(mse_history2, 'r', label='mse(loss)')
plt.plot(val_mse_history2, 'b', label='val_mse')
plt.xlabel('epochs')
plt.legend()
plt.show()














