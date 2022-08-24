# 영화 리뷰 데이터로 이진 분류
# IMDB : train-25000, test-25000 개로 구성
from keras.datasets import imdb

(train_data, train_label), (test_data, test_label) = imdb.load_data(num_words=10000)
print(type(train_data), train_data.shape)
print(type(test_data), test_data.shape)
print(train_data)   # 모든 단어에 대해 인덱싱(고유 번호)을 해서 단어 사전을 만듦
print(train_label)

# 참고로 원래 영문으로 변환
word_index = imdb.get_word_index()
# print(word_index)   # {'fawn': 34701, 'tsukino': 52006
# print(word_index.items())
reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])
# print(reverse_word_index)    {34701: 'fawn', 52006: 'tsukino'.....
print(reverse_word_index.get(train_data[0][0])) # the
decode_review = ' '.join([reverse_word_index.get(i) for i in train_data[0]])
print(decode_review)

print('--------------------------------------------')

# 데이터 준비 : list를 벡터화
import numpy as np

def vector_seq(datas, dim=10000):
    results = np.zeros((len(datas), dim))
    # print(results)
    for i, seq in enumerate(datas):
        results[i, seq] = 1.
    return results
    
x_train = vector_seq(train_data)
print(x_train, x_train.shape)   # (25000, 10000)
x_test = vector_seq(test_data)
print(x_test, x_test.shape)
y_train = train_label   # train_label.astype('float32') 해도되고...
y_test = test_label

print()
# model
from keras import models, layers, regularizers
model = models.Sequential()
model.add(layers.Dense(16, activation='relu', input_shape=(10000,)
                       , kernel_regularizer=regularizers.l2(0.001)))
# l2 규제 : 가중치 행렬의 모든 값을 제곱하고 0.001을 곱해 model 신경망의 전체 손실을 조정함. 패널티를 추가
model.add(layers.Dropout(rate=0.3))
# Drop out 이란 과적합 방지를 위해 네트워크의 유닛의 일부만 동작하고 일부는 동작하지 않도록 하는 방법이다.
model.add(layers.Dense(16, activation='relu'))
model.add(layers.Dropout(rate=0.3))
model.add(layers.Dense(1, activation='sigmoid'))
                       
model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['acc'])

# 훈련시 validation data를 준비
x_val = x_train[:10000]
partial_x_train = x_train[10000:]
print(len(partial_x_train), len(x_val)) # 15000 10000

y_val = y_train[:10000]
partial_y_train = y_train[10000:]
print(len(partial_y_train), len(y_val)) # 15000 10000
# history = model.fit(x_train, y_train, ...)
history = model.fit(partial_x_train, partial_y_train, epochs=30, batch_size=512,
                    validation_data=(x_val, y_val), verbose=2)

print('evaluate:', model.evaluate(x_test, y_test, batch_size=512, verbose=0))

# 시각화
import matplotlib.pyplot as plt
history_dict = history.history
print(history_dict.keys())

loss = history_dict['loss']
val_loss = history_dict['val_loss']
epochs = range(1, len(loss)+1)

plt.plot(epochs, loss, 'bo', label='train loss')
plt.plot(epochs, val_loss, 'r', label='validation loss')
plt.xlabel('epochs')
plt.ylabel('loss')
plt.legend()
plt.show()

acc = history_dict['acc']
val_acc = history_dict['val_acc']
epochs = range(1, len(acc)+1)

plt.plot(epochs, acc, 'bo', label='train acc')
plt.plot(epochs, val_acc, 'r', label='validation acc')
plt.xlabel('epochs')
plt.ylabel('acc')
plt.legend()
plt.show()

pred = model.predict(x_test[:5])
print('예측값:', np.where(pred > 0.5, 1, 0).flatten())
print('실제값:', y_test[:5])


# 과적합 방지 방법 - 최적화와 일반화(모델의 포용성)
# 모델의 파라미터 조정 units=?
# 가중치 규제 regularizers
# Dropout 추가
# BatchNormalization 추가
# train / test split
# k-fold
# 훈련 데이터를 줄이기




















