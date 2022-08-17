# Keras를 모듈을 사용해 DeepLearning 모델 네트워크 구성 샘플
# 논리회로 분류

import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Activation

x = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([0,1,1,0]) # xor

model = Sequential()
model.add(Dense(units=5, input_dim=2, activation='relu'))   # 벡터곱 병렬 연산 - 완전연결층
model.add(Dense(units=5, activation='relu'))
model.add(Dense(units=1, activation='sigmoid'))

print(model.summary())
# 파라미터 수 = (입력 자료수 + 1) * 출력수  (2+1)*3  (3+1)*3 (3+1)*1

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001), loss='binary_crossentropy', metrics=['accuracy'])

history = model.fit(x, y, epochs=100, batch_size=1, verbose=2)
print(history.history['loss'])
print(history.history['accuracy'])
import matplotlib.pyplot as plt
plt.plot(history.history['loss'])
plt.xlabel('epochs')
plt.ylabel('loss')
plt.show()

plt.plot(history.history['accuracy'])
plt.xlabel('epochs')
plt.ylabel('loss')
plt.show()

print(model.weights)

print()
pred = (model.predict(x) > 0.5).astype('int32')
print('예측 결과 : ', pred.flatten())

















