# 문제4) testdata/HR_comma_sep.csv 파일을 이용하여 salary를 예측하는 분류 모델을 작성한다.
# * 변수 종류 *
# satisfaction_level : 직무 만족도
# last_eval‎uation : 마지막 평가점수
# number_project : 진행 프로젝트 수
# average_monthly_hours : 월평균 근무시간
# time_spend_company : 근속년수
# work_accident : 사건사고 여부(0: 없음, 1: 있음)
# left : 이직 여부(0: 잔류, 1: 이직)
# promotion_last_5years: 최근 5년간 승진여부(0: 승진 x, 1: 승진)
# sales : 부서
# salary : 임금 수준 (low, medium, high)
# 조건 : Randomforest 클래스로 중요 변수를 찾고, Keras 지원 딥러닝 모델을 사용하시오.
# Randomforest 모델과 Keras 지원 모델을 작성한 후 분류 정확도를 비교하시오.
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
import numpy as np
from sklearn.preprocessing import OneHotEncoder, StandardScaler

data = pd.read_csv("../testdata/HR_comma_sep.csv")
# print(data.head(3))
# print(data.columns)
# print(data.shape)   # (14999, 10)
# print(data.isnull().sum())
x_data = data.values[:, 0:8]
y_data = data['salary'].values
data['salary']=data['salary'].apply(lambda x:0 if x == 'low' else (1 if x == 'medium' else 2))
print(x_data[:5])
print(y_data[:5])
print()
train_x, test_x, train_y, test_y = train_test_split(x_data, y_data, random_state = 12, test_size=0.3)
print(train_x.shape, test_x.shape, train_y.shape, test_y.shape) # (10499, 9) (4500, 9) (10499,) (4500,)

# model
model = RandomForestClassifier(criterion='entropy', n_estimators = 100)
model = model.fit(train_x, train_y)

# pred
pred = model.predict(test_x)
print('예측값 : ', pred[:10])
print('실제값 : ', np.array(test_y[:10]))

# 분류 정확도
print('acc:', sum(test_y == pred) / len(test_y))
from sklearn.metrics import accuracy_score
print('acc:', accuracy_score(test_y, pred))

# 교차검증 모델
cross_vali = cross_val_score(model, x_data, y_data, cv = 5)
print(cross_vali, '평균:', np.round(np.mean(cross_vali), 3))

print()
# feature로 사용할 중요 변수 확인
print('특성(변수) 중요도 :\n{}'.format(model.feature_importances_))    # 근속년수


print(y_data.shape) # (14999,)
onehot = OneHotEncoder(categories='auto')
y = onehot.fit_transform(y_data[:, np.newaxis]).toarray()
print(y.shape)  # (14999, 3)
scaler = StandardScaler()
x_scale = scaler.fit_transform(x_data)
print(x_scale[:2])

# train/test split
x_train, x_test, y_train, y_test = train_test_split(x_scale, y, test_size=0.3, random_state=1)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)
# (10499, 8) (4500, 8) (10499, 3) (4500, 3)

N_FEATURES = x_train.shape[1]   
N_CLASSES = y_train.shape[1]

# model
from keras.models import Sequential
from keras.layers import Dense

# 노드(뉴런)의 갯수를 변경해 가며 모델 작성 함수
def create_custom_model_func(input_dim, output_dim, out_nodes, n, model_name='mode'):
    # print(input_dim, output_dim, out_nodes, n, model_name)
    def create_model():
        model = Sequential(name=model_name)
        for _ in range(n):
            model.add(Dense(units=out_nodes, input_dim=input_dim, activation='relu'))
        
        model.add(Dense(units=output_dim, activation='softmax'))
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])
        return model
    return create_model
   
models = [create_custom_model_func(N_FEATURES, N_CLASSES, 10, n, 'model_{}'.format(n)) for n in range(1,4)]
print(len(models))

for cre_model in models:
    print('---')
    cre_model().summary()

print()
history_dict = {}

for cre_model in models:
    model = cre_model()
    print('모델명:', model.name)
    historys = model.fit(x_train, y_train, batch_size=5, epochs=50, verbose=0, 
                         validation_split=0.3)
    scores = model.evaluate(x_test, y_test, verbose=0)
    print('test loss : ', scores[0])
    print('test acc : ', scores[1])
    history_dict[model.name] = [historys, model]
    
print(history_dict)











