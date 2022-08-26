# CNN(Convolution Neural Network)
# 원래의 이미지(텍스트) 특징을 유지하며 크기를 줄이는 알고리즘
# Conv(특징추출) + Pooling(크기 축소) ... FCLayer(이미지를 1차원 만듦) == > Dense에게 전달

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
x_test = x_test.reshape((10000, 28, 28, 1))
print(x_train.ndim)
print(x_test.ndim)
# print(x_train[:1]) 4차원

x_train = x_train / 255.0
x_test = x_test / 255.0

# print(x_train[[[[0]]]])
# print(y_train[[0]])

"""
# model    Sequential API 적용 
input_shape = (28, 28, 1)
model = models.Sequential()
# CNN 구축
# Conv2D(필터수, 필터크기, 필터이동량, 패딩여부...)    padding='valid' 0으로 채우기X, 'same'은 0으로 채우기O
model.add(layers.Conv2D(filters=16, kernel_size=(3, 3), strides=(1, 1),
                        padding='valid', activation='relu', input_shape=input_shape))
model.add(layers.MaxPool2D(pool_size=(2, 2)))   # 이미지 크기 줄임
model.add(layers.Dropout(rate=0.2))

model.add(layers.Conv2D(filters=32, kernel_size=(3, 3), strides=(1, 1),
                        padding='valid', activation='relu'))
model.add(layers.MaxPool2D(pool_size=(2, 2)))   
model.add(layers.Dropout(rate=0.2))

model.add(layers.Conv2D(filters=64, kernel_size=(3, 3), strides=(1, 1),
                        padding='valid', activation='relu'))
model.add(layers.MaxPool2D(pool_size=(2, 2)))   
model.add(layers.Dropout(rate=0.2))

# FCLayer(Fully Connected Layer) : 이미지를 1차원으로 변경
model.add(layers.Flatten())

# Dense
model.add(layers.Dense(units=64, activation='relu'))
model.add(layers.Dropout(rate=0.2))
model.add(layers.Dense(units=32, activation='relu'))
model.add(layers.Dropout(rate=0.2))
model.add(layers.Dense(units=10, activation='softmax'))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

print(model.summary())

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

# 모델 저장
model.save('tf14.h5')

del model
"""
model2 = tf.keras.models.load_model('tf14.h5')

# predict
import numpy as np
print('예측값:', np.argmax(model2.predict(x_test[:1])))
print('예측값:', np.argmax(model2.predict(x_test[[0]])))
print('실제값:', y_test[0])

# 시각화 
import matplotlib.pyplot as plt
import pickle
with open('his_data.pickle', mode='rb') as obj:
    history = pickle.load(obj)
    
def plot_acc(title = None):
    plt.plot(history['accuracy'], label='accuracy')
    plt.plot(history['val_accuracy'], label='val_accuracy')
    plt.title(title)
    plt.xlabel('epochs')
    plt.legend()

plot_acc('acc')
plt.show()

def plot_loss(title = None):
    plt.plot(history['loss'], label='loss')
    plt.plot(history['val_loss'], label='val_loss')
    plt.title(title)
    plt.xlabel('epochs')
    plt.legend()

plot_loss('loss')
plt.show()

from keras.utils import plot_model
plot_model(model2, to_file='tf14cnn.png', show_shapes=True)


















