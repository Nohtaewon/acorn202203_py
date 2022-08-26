# 이미지 보강 : 여러장의 이미지가 필요할 때 기존 이미지를 사용해 비슷한 유형의 이미지를 생성

import tensorflow as tf
from keras.datasets import fashion_mnist
from keras.utils import to_categorical
import numpy as np
import matplotlib.pyplot as plt
from keras import models, layers

np.random.seed(0)
tf.random.set_seed(3)

(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
x_train = x_train.reshape(-1, 28, 28, 1).astype('float32') / 255
x_test = x_test.reshape(-1, 28, 28, 1).astype('float32') / 255
print(x_train[:1])
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)
print(y_train[:1])
"""
# 시각화
plt.figure(figsize=(10, 10))
for c in range(100):
    plt.subplot(10, 10, c+1)
    plt.axis('off')
    plt.imshow(x_train[c].reshape(28, 28), cmap='gray')
plt.show()

# 이미지 보강
from keras.preprocessing.image import ImageDataGenerator
img_gen = ImageDataGenerator(
    rotation_range=10,
    zoom_range=0.1,
    shear_range=0.5,
    width_shift_range=0.1,
    height_shift_range=0.1,
    horizontal_flip=-True,
    vertical_flip=True
)

augment_size = 100
x_augment = img_gen.flow(np.tile(x_train[0].reshape(28*28), 100).reshape(-1, 28, 28, 1),
                         np.zeros(augment_size), batch_size=augment_size,
                         shuffle=False).next()[0]
                         
print(x_augment.shape)
print(x_augment)    

plt.figure(figsize=(10,10)
for c in range(100):
    plt.subplot(10, 10, c+1)
    plt.axis('off')
    plt.imshow(x_augment[c].reshape(28, 28),cmap='gray')
plt.show()                     
"""
from keras.preprocessing.image import ImageDataGenerator
# train image를 6만 -> 9만으로 증강
img_gen = ImageDataGenerator(
    rotation_range=10,
    zoom_range=0.1,
    shear_range=0.5,
    width_shift_range=0.1,
    height_shift_range=0.1,
    horizontal_flip=-True,
    vertical_flip=True  # 숫자 데이터 같은 경우는 상하 좌우 전환은 안하는 것이 좋을 듯
)
augment_size = 30000
randidx = np.random.randint(x_train.shape[0], size=augment_size)    # 인덱스로 사용할 난수 얻기

x_augment = x_train[randidx].copy() # 복사본 3만개 샘플링 준비
y_augment = y_train[randidx].copy()

x_augment = img_gen.flow(x_augment,
                         np.zeros(augment_size), batch_size=augment_size,
                         shuffle=False).next()[0]
# 원래 데이터에 보강 이미지 추가
x_train = np.concatenate((x_train, x_augment))
y_train = np.concatenate((y_train, y_augment))                       
print(x_train.shape)
print(y_train.shape)





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

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

print(model.summary())

# 조기종료
from keras.callbacks import EarlyStopping
es = EarlyStopping(monitor='val_loss', patience=3)

# 학습
history = model.fit(x_train, y_train, batch_size=128, epochs=100, verbose=2, 
                    validation_split=0.2, callbacks=[es])

# 모델 평가
train_loss, train_acc = model.evaluate(x_train, y_train)
test_loss, test_acc = model.evaluate(x_test, y_test)
print('train loss, train acc : ', train_loss, train_acc)    # 둘의 차이가 크면 과적합
print('test_loss, test_acc : ', test_loss, test_acc)
