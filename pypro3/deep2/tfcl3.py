# kaggle의 red&white wine dataset 사용

from keras.models import Sequential
from keras.layers import Dense, BatchNormalization
from keras.callbacks import EarlyStopping, ModelCheckpoint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

wdf = pd.read_csv("../testdata/wine.csv", header=None)
print(wdf.head(2))
print(wdf.info())
print(wdf.iloc[:, 12].unique()) # [1:white 0:red]
print(len(wdf[wdf.iloc[:, 12] == 0]))   # red:4898
print(len(wdf[wdf.iloc[:, 12] == 1]))   # white:1599
dataset = wdf.values
print(dataset[:2], type(dataset))
x = dataset[:, 0:12]
y = dataset[:, -1]
print(x[:2])
print(y[:2])

# train/test split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3,random_state=12)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)

# model
model = Sequential()
model.add(Dense(32, input_dim=12, activation='relu', kernel_initializer="he_normal"))
model.add(BatchNormalization()) # 배치 정규화 : 역전파 도중 발생하는 기울기 소실, 폭주 문제 등을 해결해줌
model.add(Dense(16,activation='relu'))
model.add(BatchNormalization())
model.add(Dense(8,activation='relu'))
model.add(BatchNormalization())
model.add(Dense(1,activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

print(model.summary())

loss, acc = model.evaluate(x_train, y_train, batch_size=32, verbose=0)
print('훈련 전 모델 정확도: {:5.2f}%'.format(100*acc))
print('훈련 전 모델 loss: {:5.2f}'.format(loss))

loss, acc = model.evaluate(x_train, y_train, batch_size=32, verbose=0)
print('훈련 후 모델 정확도: {:5.2f}%'.format(100*acc))
print('훈련 후 모델 loss: {:5.2f}'.format(loss))

# 학습 도중 모델 저장 및 조기 종료
import os 
model_dir='./model_sav/'
if not os.path.exists(model_dir):
    os.mkdir(model_dir)

modelPath = "model_{epoch:02d}.hdf5"
chkpoint = ModelCheckpoint(filepath=model_dir+modelPath, monitor='val_loss', mode='auto',
                           verbose=0, save_best_only=True)
es = EarlyStopping(monitor='val_loss', mode='auto', patience=5)


history = model.fit(x_train, y_train, epochs=10000, batch_size=64, 
                    validation_split=0.2, verbose=2, callbacks=[chkpoint, es])

loss, acc = model.evaluate(x_train, y_train, batch_size=32, verbose=0)

print('훈련 후 모델 정확도: {:5.2f}%'.format(100*acc))
print('훈련 후 모델 loss: {:5.2f}'.format(loss))

vloss = history.history['val_loss']
loss=history.history['loss']
vacc=history.history['val_accuracy']
acc=history.history['accuracy']

# 시각화
epoch_len = np.arange(len(acc))

plt.plot(epoch_len, vloss, c='red', label="val_loss")
plt.plot(epoch_len, loss, c='blue', label="loss")
plt.xlabel('epochs')
plt.ylabel('loss')
plt.legend(loc='best')
plt.show()

plt.plot(epoch_len, vacc, c='red', label="val_accuracy")
plt.plot(epoch_len, acc, c='blue', label="accuracy")
plt.xlabel('epochs')
plt.ylabel('acc')
plt.legend(loc='best')
plt.show()

del model

# 새로운 값으로 예측
from keras.models import load_model
model2 = load_model(model_dir+"model_01.hdf5")
new_data = x_test[:5, :]
pred = model2.predict(new_data)
print('pred:',np.where(pred>0.5, 1, 0).flatten())






















