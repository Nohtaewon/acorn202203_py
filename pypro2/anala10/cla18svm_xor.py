# SVM으로 논리 연산

x_data = [
    [0,0,0],
    [0,1,1],
    [1,0,1],
    [1,1,0]
]

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn import svm, metrics

feature = []
label = []

for row in x_data:
    p = row[0]
    q = row[1]
    r = row[2]
    feature.append([p, q])
    label.append(r)
    
print(feature)
print(label)

# model1 
# model = LogisticRegression()
model = svm.SVC()
model.fit(feature, label)

pred = model.predict(feature)
print('예측값:', pred)
print('실제값:', label)

# 정확도
acc = metrics.accuracy_score(label, pred)
print('정확도:', acc)
print('report: \n', metrics.classification_report(label, pred))

