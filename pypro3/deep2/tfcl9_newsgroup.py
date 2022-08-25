# 로이터 뉴스 분류하기(Reuters News Classification)
# 케라스에서 제공하는 로이터 뉴스 데이터를 Dense을 이용하여 다항 분류를 진행해보겠습니다. 
# 로이터 뉴스 기사 데이터는 총 11,258개의 뉴스 기사가 46개의 뉴스 카테고리로 분류되는 뉴스 기사 데이터입니다.

from keras.datasets import reuters

(train_data, train_label), (test_data, test_label) = reuters.load_data(num_words=10000)
print(len(train_data), len(test_data))  # 8982 2246
print(train_data)
print(train_label, set(train_label), max(train_label)+1)

# 참고: 뉴스의 내용(문자열)을 확인 --------------
word_index = reuters.get_word_index()   # 단어와 정수인덱싱을 매핑한 dict를 반환 {'the':1...}
reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])
print(reverse_word_index)   # {10996: 'mdbl', 16260: 'fawc' ....
print(train_data[0])
decode_review = ' '.join([reverse_word_index.get(i) for i in train_data[0]])
print(decode_review)

# ---------------------------------------

# data 준비
import numpy as np
def vec_seq(sequences, dim=10000):
    results = np.zeros((len(sequences), dim))
    for i, seq in enumerate(sequences):
        results[i, seq] = 1.
    return results

x_train = vec_seq(train_data)
x_test = vec_seq(test_data)
print(x_train)  # [list([1, 2, 2, 8, 43, 10, 447, 5 ... => [[0. 1. 1. ... 0. 0. 0.] ....

# label : one-hot encoding
def one_hot_func(labels, dim=46):
    results = np.zeros((len(labels), dim))
    for i, seq in enumerate(labels):
        results[i, seq] = 1.
    return results

# one_hot_train_labels = one_hot_func(train_label)
# one_hot_test_labels = one_hot_func(test_label)
# print(one_hot_train_labels[0])

from keras.utils import to_categorical
one_hot_train_labels = to_categorical(train_label)
one_hot_test_labels = to_categorical(test_label)
print(one_hot_train_labels[0])

# model
from keras import models
from keras import layers
model = models.Sequential()
model.add(layers.Dense(units=64, activation='relu', input_shape=(10000,)))
model.add(layers.Dense(units=64, activation='relu'))
model.add(layers.Dense(units=46, activation='softmax'))

model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['acc'])
# 'categorical_crossentropy' : 모델이 예측한 확률분포와 실제값 확률분포의 거리를 계산. 두 분포 사이에 거리가 최소화되도록 함

# validation data를 만들 수도 있다. 그러나 생략...

history = model.fit(x_train, one_hot_train_labels, epochs=15, batch_size=128,
                    validation_split=0.2, verbose=2)

results = model.evaluate(x_test, one_hot_test_labels, batch_size=128, verbose=0)
print('evaluate:', results)

# 시각화
import matplotlib.pyplot as plt
loss = history.history['loss']
val_loss = history.history['val_loss']
epochs = range(1, len(loss)+1)

plt.plot(epochs, loss, 'bo', label='train loss')
plt.plot(epochs, val_loss, 'r', label='train val_loss')
plt.xlabel('epochs')
plt.legend()
plt.show()

# pred
pred = model.predict(x_test)
print('출력 확률분포의 합:', np.sum(pred[0]))
print('예측값:', np.argmax(pred[0]))
print('실제값:', test_label[0])






