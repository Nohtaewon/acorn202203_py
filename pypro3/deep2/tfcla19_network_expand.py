# 효울성 향상을 위한 네트워크 확장
# 개인이 연구에 의해 할 수 있는

import tensorflow as tf
from keras.datasets import fashion_mnist
from keras.utils import to_categorical
import numpy as np
import matplotlib.pyplot as plt
from keras import models, layers

(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
x_train = x_train.reshape(-1, 28, 28, 1).astype('float32') / 255
x_test = x_test.reshape(-1, 28, 28, 1).astype('float32') / 255

# 시각화
# plt.figure(figsize=(10, 10))
# for c in range(100):
#     plt.subplot(10, 10, c+1)
#     plt.axis('off')
#     plt.imshow(x_train[c].reshape(28, 28), cmap='gray')
# plt.show()

model = models.Sequential([
    layers.Conv2D(input_shape=(28, 28, 1), kernel_size=3, filters=16),
    layers.Conv2D(kernel_size=3, filters=32),
    layers.Conv2D(kernel_size=3, filters=64),
    layers.Flatten(),
    layers.Dense(units=128, activation='relu'),
    layers.Dense(units=128, activation='softmax')]
)

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
print(model.summary())

history = model.fit(x_train, y_train, batch_size=32, epochs=10, verbose=2, validation_split=0.25)

import matplotlib.pyplot as plt
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], 'b-', label='accuracy')
plt.plot(history.history['val_accuracy'], 'r--', label='val_accuracy')
plt.legend()
plt.show()

plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], 'b-', label='loss')
plt.plot(history.history['val_loss'], 'r--', label='val_loss')
plt.legend()
plt.show()

print('eval:', model.evaluate(x_test, y_test, verbose=0))















