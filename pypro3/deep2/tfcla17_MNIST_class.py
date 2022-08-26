# CNN(Convolution Neural Network) : sub classing model 사용
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
x_train = x_train.reshape(-1, 28, 28, 1)  # 흑백 이미지이므로 채널이 1
x_test = x_test.reshape(-1, 28, 28, 1)
print(x_train.ndim)
print(x_test.ndim)
# print(x_train[:1]) 4차원

x_train = x_train / 255.0
x_test = x_test / 255.0

# model : sub classing model 사용
class MyModel(models.Model):
    def __init__(self):
        super(MyModel, self).__init__()
        self.conv1 = layers.Conv2D(filters=16, kernel_size=(3,3), activation='relu')
        self.conv2 = layers.Conv2D(filters=32, kernel_size=(3,3), activation='relu')
        self.conv3 = layers.Conv2D(filters=64, kernel_size=(3,3), activation='relu')
        self.pool = layers.MaxPooling2D(pool_size=(2,2))
        self.flatten = layers.Flatten()
        self.dropout = layers.Dropout(0.2)
        self.d1 = layers.Dense(units=64, activation='relu')
        self.d2 = layers.Dense(units=32, activation='relu')
        self.d3 = layers.Dense(units=10, activation='softmax')

    def call(self, x):
        x = self.conv1(x)
        x = self.pool(x)
        x = self.conv2(x)
        x = self.pool(x)
        x = self.conv3(x)
        x = self.pool(x)
        x = self.flatten(x)
        x = self.d1(x)
        x = self.dropout(x)
        x = self.d2(x)
        x = self.dropout(x)
        return self.d3(x)

model = MyModel()

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

history = model.fit(x_train, y_train, batch_size=128, epochs=5, verbose=2, 
                    validation_split=0.2)

# 모델 평가
train_loss, train_acc = model.evaluate(x_train, y_train)
test_loss, test_acc = model.evaluate(x_test, y_test)
print('train loss, train acc : ', train_loss, train_acc)    # 둘의 차이가 크면 과적합
print('test_loss, test_acc : ', test_loss, test_acc)  










