from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
import pandas as pd

df = pd.read_csv("../testdata/patient.csv")
print(df.head(3))
print(df.columns)
print(df.shape) # (200, 11)
df_x = df[['AGE', 'SEX', 'RACE', 'SER', 'CAN', 'CRN', 'INF', 'CPR','HRA']] # feature
print(df_x[:3], df_x.shape)

df_y = df['STA']   # label
print(df_y[:3])

train_x, test_x, train_y, test_y = train_test_split(df_x, df_y, random_state = 12)  # test_size = 0.25
print(train_x.shape, test_x.shape, train_y.shape, test_y.shape) 

# model
model = RandomForestClassifier(criterion='entropy', n_estimators = 100)
model = model.fit(train_x, train_y)

# pred
import numpy as np
pred = model.predict(test_x)
print('예측값 : ', pred[:10])
print('실제값 : ', np.array(test_y[:10]))

# 분류 정확도
print('acc:', sum(test_y == pred) / len(test_y))
from sklearn.metrics import accuracy_score
print('acc:', accuracy_score(test_y, pred))

# 교차검증 모델
cross_vali = cross_val_score(model, df_x, df_y, cv = 5)
print(cross_vali, '평균:', np.round(np.mean(cross_vali), 3))

print()
# feature로 사용할 중요 변수 확인
import matplotlib.pyplot as plt
print('특성(변수) 중요도 :\n{}'.format(model.feature_importances_))

def plot_feature_importances(model):   # 특성 중요도 시각화
    n_features = df_x.shape[1]
    plt.barh(range(n_features), model.feature_importances_, align='center')
    plt.yticks(np.arange(n_features), df_x.columns)
    plt.xlabel("attr importances")
    plt.ylabel("attr")
    plt.ylim(-1, n_features)
    plt.show()

plot_feature_importances(model)






