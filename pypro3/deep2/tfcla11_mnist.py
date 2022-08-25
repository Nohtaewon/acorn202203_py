# 이미지 분류 : MNIST dataset
# MNIST는 숫자 0부터 9까지의 이미지로 구성된 손글씨 데이터셋입니다. 
# 이 데이터는 과거에 우체국에서 편지의 우편 번호를 인식하기 위해서 만들어진 훈련 데이터입니다. 
# 총 60,000개의 훈련 데이터와 레이블, 총 10,000개의 테스트 데이터와 레이블로 구성되어져 있습니다. 
# 레이블은 0부터 9까지 총 10개입니다. 
# 이 예제는 머신 러닝을 처음 배울 때 접하게 되는 가장 기본적인 예제이기도 합니다.

import tensorflow as tf
import numpy as np
import sys
import matplotlib.pyplot as plt

(x_train, y_train),(x_test, y_test) = tf.keras.datasets.mnist.load_data()
print(x_train.shape, y_train.shape, x_test.shape, y_test.shape)
# (60000, 28, 28) (60000,) (10000, 28, 28) (10000,)
# print(x_train[0])
# print(y_train[0])

# for i in x_train[1]:
#     for j in i:
#         sys.stdout.write('%s '%j)
#     sys.stdout.write('\n')
    
# import matplotlib.pyplot as plt
# plt.imshow(x_train[0], cmap='gray')
# plt.show()

x_train = x_train.reshape(60000, 784).astype('float32') # 28 * 28 => 784
x_test = x_test.reshape(10000, 784).astype('float32')
print(x_train[0])

x_train /= 255.0   # 정규화 : 선택적
x_test /= 255.0
print(x_train[0])

# label : one-hot
print(y_train[0])  # 5
y_train = tf.keras.utils.to_categorical(y_train, 10)
print(y_train[0])  # [0. 0. 0. 0. 0. 1. 0. 0. 0. 0.]
y_test = tf.keras.utils.to_categorical(y_test, 10)

print()
# train data의 일부를 validation data로 사용
x_val = x_train[50000:60000]  # 1000개는 validation으로 사용. (선택적)
y_val = y_train[50000:60000]
x_train = x_train[0:50000]
y_train = y_train[0:50000]
print(x_val.shape, x_train.shape)   # (10000, 784) (50000, 784)

print()
# model
from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten, Dropout

model = Sequential()

# model.add(Dense(units=128, input_shape=(784, )))
# # model.add(Flatten(input_shape=(28,28)))   # reshape을 안 한 경우  (바로 위의 코드와 같은 의미)
# # model.add(Dense())                        # 따로 reshape을 해주지 않았다면 이와 같이 해줄 수 있다.
# model.add(Activation('relu'))
# model.add(Dropout(rate=0.2))   # 과적합 방지용
#
# model.add(Dense(units=64))
# model.add(Activation('relu'))
# model.add(Dropout(rate=0.2))
#
# model.add(Dense(units=10))
# model.add(Activation('softmax'))


model.add(Dense(units=128, input_shape=(784,), activation='relu'))
# model.add(Flatten(input_shape=(28,28)))   # reshape을 안 한 경우
model.add(Dropout(rate=0.2))
model.add(Dense(units=64, activation='relu'))
model.add(Dropout(rate=0.2))
model.add(Dense(units=10, activation='softmax'))    # 위 주석 처리한 코드와 결과. 속도는 느리지만 간략하게 쓸 수 있다.

print(model.summary())

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

history = model.fit(x=x_train, y=y_train, epochs=10, batch_size=128, 
                    validation_data=(x_val, y_val), verbose=2)

# 시각화 

plt.plot(history.history['loss'], label='loss')
plt.plot(history.history['val_loss'], label='val_loss')
plt.xlabel('epochs')
plt.legend()
plt.show()

plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label='val_accuracy')
plt.xlabel('epochs')
plt.legend()
plt.show()

score = model.evaluate(x_test, y_test, batch_size=128, verbose=0)
print('loss : ', score[0])
print('accuracy : ', score[1])

# 모델 저장 
model.save('tf11.hdf5')
del model

# 모델 읽기
mymodel = tf.keras.models.load_model('tf11.hdf5')

# 예측용 이미지 먼저 보기
print(x_test[:1], x_test[:1].shape)
plt.imshow(x_test[:1].reshape(28, 28), cmap='Greys')
plt.show()

# 예측
pred = mymodel.predict(x_test[:1])
print('pred : ', pred)
import numpy as np
print('예측값 : ', np.argmax(pred, 1))  # (pred)확률값을 가장 큰 지점의 index 값을 불러오는 것.
print('실제값 : ', y_test[:1])
print('실제값 : ', np.argmax(y_test[:1],1))



# 내가 그린 숫자 이미지 분류 모델로 판정하기











