# CNN(Convolution Neural Network) function API
# MNIST dataset으로 실습

import tensorflow as tf
import numpy as np
import sys
import matplotlib.pyplot as plt
from keras import models, layers

(x_train, y_train),(x_test, y_test) = tf.keras.datasets.mnist.load_data()
print(x_train.shape, y_train.shape, x_test.shape, y_test.shape)
# (60000, 28, 28) (60000,) (10000, 28, 28) (10000,)
print(x_train[0])
print(y_train[0])

# CNN은 channel을 사용하기 때문에 3차원 데이터를 4차원으로 변경
x_train = x_train.reshape((-1, 28, 28, 1))  # 흑백 이미지이므로 채널이 1
x_test = x_test.reshape((-1, 28, 28, 1))
print(x_train.ndim)
print(x_test.ndim)
# print(x_train[:1]) 4차원

x_train = x_train / 255.0
x_test = x_test / 255.0

# model : function API 사용
input_shape = (28,28,1)

img_input = layers.Input(shape=input_shape)

net = layers.Conv2D(filters=16, kernel_size=(3,3), strides=(1,1), activation='relu')(img_input)
net = layers.MaxPooling2D(pool_size=(2,2))(net)

net = layers.Conv2D(filters=32, kernel_size=3, strides=1, activation='relu')(net)
net = layers.MaxPooling2D(pool_size=(2,2))(net)

net = layers.Conv2D(filters=64, kernel_size=3, strides=1, activation='relu')(net)
net = layers.MaxPooling2D(pool_size=(2,2))(net)

net = layers.Flatten()(net)

net = layers.Dense(units=64, activation='relu')(net)
net = layers.Dropout(rate=0.2)(net)
net = layers.Dense(units=32, activation='relu')(net)
net = layers.Dropout(rate=0.2)(net)
outputs = layers.Dense(units=10, activation='softmax')(net)

model = tf.keras.Model(inputs = img_input, outputs = outputs)

print(model.summary())

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
# 조기종료
from keras.callbacks import EarlyStopping
es = EarlyStopping(monitor='val_loss', patience=3)

# 학습
history = model.fit(x_train, y_train, batch_size=128, epochs=100, verbose=2, 
                    validation_split=0.2, callbacks=[es])

# history를 저장하기
import pickle
history = history.history
with open('his_data.pickle', 'wb') as f:
    pickle.dump(history, f)

# 모델 평가
train_loss, train_acc = model.evaluate(x_train, y_train)
test_loss, test_acc = model.evaluate(x_test, y_test)
print('train loss, train acc : ', train_loss, train_acc)    # 둘의 차이가 크면 과적합
print('test_loss, test_acc : ', test_loss, test_acc)

# 이하 생략










