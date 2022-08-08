# 분류모델 성능 평가용 : ROC curve 그리기
# 광고를 클릭('Clicked on Ad')할 가능성이 높은 사용자 분류.
# Age : 나이, Area Income : 지역수입, Daily Internet use:일별 인터넷 사용, 
# Clicked Ad : 광고 클릭 가능 여부 (0, 1)
# ROC 커브와 AUC 출력

from sklearn.linear_model import LogisticRegression
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn import metrics

data = pd.read_csv("../testdata/advertising2.csv")
# print(data.head(3))
# print(data.columns)
x = data[['Age', 'Area Income', 'Daily Internet Usage', 'Daily Time Spent on Site']]
y = data['Clicked on Ad']
x = x.values  
y = y.values   
print(x[:3], x.shape)
print(y[:3], y.shape)

model = LogisticRegression().fit(x,y)
y_hat = model.predict(x)
print('y_hat(분류 결과) : ', y_hat[:10])
print('실제값 : ', y[:10])

print(confusion_matrix(y, y_hat))

acc = (464+36)/100       # 정확도
recall = 464 / (464+36)    # 재현율 TPR
precision = 464 / (464+67) # 정밀도(특이도, specificity)
fallout = 67 / (67+464)    # 위양성율 FPR

fpr, tpr, thresholds = metrics.roc_curve(y, model.decision_function(x))
print('fpr:',fpr)
print('tpr:',tpr)
print('분류임계값:', thresholds)

plt.plot(fpr, tpr, 'o-', label='Logistic Regression')
plt.plot([0,1],[0,1], 'k--', label='classifier line(AUC:0.5)')
plt.plot([fallout], [recall], 'ro', ms=10)  # 위양성율, 재현율 값
plt.xlabel('fpr')
plt.ylabel('tpr')
plt.title('ROC curve')
plt.legend()
plt.show()

print('AUC:', metrics.auc(fpr, tpr))





