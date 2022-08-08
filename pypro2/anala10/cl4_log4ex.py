# [로지스틱 분류분석 문제2] 
# 게임, TV 시청 데이터로 안경 착용 유무를 분류하시오.
# 안경 : 값0(착용X), 값1(착용O)
# 예제 파일 : https://github.com/pykwon  ==>  bodycheck.csv
# 새로운 데이터(키보드로 입력)로 분류 확인. 스케일링X
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

data = pd.read_csv("../testdata/bodycheck.csv")
print(data)
x = data[['게임', 'TV시청']]
y = data['안경유무']
x = x.values   # 2차원 배열
y = y.values   # 1차원 배열
print(x[:3])
print(y[:3], set(y))

# train / test 분리
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state=0)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)

model =LogisticRegression(C = 0.1,  random_state=0)

print(model)
model.fit(x_train, y_train)
# 분류 예측
y_pred = model.predict(x_test)  # test dataset 으로 모델 검정
print('예측값 : ', y_pred)
print('실제값 : ', y_test)
print('총 갯수:%d, 오류수:%d'%(len(y_test), (y_test != y_pred).sum()))

print('분류 정확도 확인')
print('accuracy:', accuracy_score(y_test, y_pred))

new_input_data = pd.DataFrame({'게임':[int(input('게임 : '))], 'TV시청':[int(input('TV시청 : '))]})

print('안경 유무 :', np.rint(model.predict(new_input_data)))
print('안경씀' if np.rint(model.predict(new_input_data))[0] == 1 else '안경안씀')









