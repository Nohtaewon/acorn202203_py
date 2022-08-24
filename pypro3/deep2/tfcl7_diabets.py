# 이항분류(sigmoid)는 다항분류(softmax)로 처리 가능

import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.utils.np_utils import to_categorical

dataset = np.loadtxt("../testdata/diabetes.csv", delimiter=",")

print(dataset.shape)
print(dataset[:1])
print(set(dataset[:, -1]))

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(dataset[:, 0:8], dataset[:, -1],
                                                    test_size=0.3, random_state=123)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)

# 이항 분류
model = Sequential()
model.add(Dense(64, input_dim=8, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])

model.fit(x_train, y_train, epochs=100, batch_size=32, verbose=0, validation_split=0.2)
scores = model.evaluate(x_test, y_test)
print('%s:%.2f%%'%(model.metrics_names[1], scores[1]*100))
print('%s:%.2f'%(model.metrics_names[0], scores[0]))

pred = model.predict([[-0.34, 0.487437, 0.180328, -0.292929, 0., 0.00149028, -0.53117, -0.03]])
print('예측결과:', pred, ' ', np.where(pred>0.5, 1, 0))

print('---' * 20)
# 다항 분류------------------------

# label을 원핫처리
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)
print(y_train[0])

model2 = Sequential()
model2.add(Dense(64, input_dim=8, activation='relu'))
model2.add(Dense(32, activation='relu'))
model2.add(Dense(1, activation='sigmoid'))

model2.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])

model2.fit(x_train, y_train, epochs=100, batch_size=32, verbose=0, validation_split=0.2)
scores = model2.evaluate(x_test, y_test)
print('%s:%.2f%%'%(model2.metrics_names[1], scores[1]*100))
print('%s:%.2f'%(model2.metrics_names[0], scores[0]))

pred = model2.predict([[-0.34, 0.487437, 0.180328, -0.292929, 0., 0.00149028, -0.53117, -0.03]])
print('예측결과:', pred, ' ', np.argmax(pred))
















