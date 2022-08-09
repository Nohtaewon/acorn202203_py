
import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from xgboost import plot_importance
import matplotlib.pyplot as plt
df = pd.read_csv("../testdata/glass.csv")
print(df.head(3), df.shape) # (214, 10)
print(df.info())

X_features = df.iloc[:, :-1]
y_labels = df['Type']
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y_labels = le.fit_transform(y_labels)

X_train, X_test, y_train, y_test = train_test_split(X_features, y_labels, test_size=0.3, random_state=12)
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

# (171, 9) (43, 9) (171,) (43,)

model = xgb.XGBClassifier(booster='gbtree', max_depth=4, n_estimators=500).fit(X_train, y_train)

pred = model.predict(X_test)
print('예측값:', pred[:5])
print('실제값:', y_test[:5])

from sklearn import metrics
acc = metrics.accuracy_score(y_test, pred)
print('정확도:', acc)

fig, ax = plt.subplots(figsize=(10, 12))
plot_importance(model, ax=ax)
plt.show()








