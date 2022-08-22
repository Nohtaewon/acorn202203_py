# 문제2) 21세 이상의 피마 인디언 여성의 당뇨병 발병 여부에 대한 dataset을 이용하여 당뇨 판정을 위한 분류 모델을 작성한다.
# 피마 인디언 당뇨병 데이터는 아래와 같이 구성되어있다.
#   Pregnancies: 임신 횟수
#   Glucose: 포도당 부하 검사 수치
#   BloodPressure: 혈압(mm Hg)
#   SkinThickness: 팔 삼두근 뒤쪽의 피하지방 측정값(mm)
#   Insulin: 혈청 인슐린(mu U/ml)
#   BMI: 체질량지수(체중(kg)/키(m))^2
#   DiabetesPedigreeFunction: 당뇨 내력 가중치 값
#   Age: 나이
#   Outcome: 5년 이내 당뇨병 발생여부 - 클래스 결정 값(0 또는 1)
# 당뇨 판정 칼럼은 outcome 이다.   1 이면 당뇨 환자로 판정
# train / test 분류 실시
# 모델 작성은 Sequential API, Function API 두 가지를 사용한다.
# loss, accuracy에 대한 시각화도 실시한다.
from keras.models import Sequential
from keras.layers import Dense, BatchNormalization
from keras.callbacks import EarlyStopping, ModelCheckpoint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from keras import optimizers

df = pd.read_csv("../testdata/pima-indians-diabetes.data.csv", header=None)
print(df.head(2))
print(df[:2], type(df))
data = df.values
x = data[:, 0:8]
y = data[:, -1]
print(x[:2])
print(y[:2])

# train/test split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)


# 1) Sequential API
model = Sequential()
model.add(Dense(1, input_dim=x_train.shape[1], activation='sigmoid'))    # input_shape(1,)
opti = optimizers.Adam(learning_rate=0.1)
model.compile(optimizer=opti, loss='binary_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, batch_size=1, epochs=10, shuffle=False, verbose=1)
loss, acc = model.evaluate(x_train, y_train, batch_size=32, verbose=0)
print('훈련 전 모델 정확도: {:5.2f}%'.format(100*acc))
print('훈련 전 모델 loss: {:5.2f}'.format(loss))

# 2) function API
from keras.layers import Input
from keras.models import Model

inputs = Input(shape=(x_train.shape[1],))
outputs = Dense(1, activation='sigmoid')(inputs)
model2 = Model(inputs, outputs)

model2.compile(optimizer=opti, loss='binary_crossentropy', metrics=['accuracy'])
model2.fit(x_train, y_train, batch_size=1, epochs=10, shuffle=False, verbose=1)
loss, acc = model2.evaluate(x_train, y_train, batch_size=32, verbose=0)
print('훈련 전 모델 정확도: {:5.2f}%'.format(100*acc))
print('훈련 전 모델 loss: {:5.2f}'.format(loss))















