
import statsmodels.formula.api as smf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats
from statsmodels.stats.outliers_influence import variance_inflation_factor

data = pd.read_csv("testdata/Carseats.csv")
print(data.head(3))
print(data.info())
data=data.drop([data.columns[6], data.columns[9], data.columns[10]], axis=1)    # 범주형 빼기

print('상관계수')
print(data.corr())

# 다중선형회귀
model = smf.ols(formula = 'Sales ~ Income + Advertising + Price + Age', data = data).fit()
print(model.summary())
"""
# 모델 저장 후 읽기
joblib.dump(model, 'aaa.model')
del model
"""
import joblib
model=joblib.load('aaa.model')

# 잔차 구하기
fitted = model.predict(data.iloc[:, [0,2,3,5,6]])     # newspaper 제외하고 예측값 얻기
residual = data['Sales'] - fitted      # 잔차
print(residual)

print('선형성')
sns.regplot(fitted, residual, lowess = True, line_kws={'color':'red'})
plt.plot([fitted.min(), fitted.max()], [0,0],'--',color='grey')
plt.show() # 미흡하지만 선형성 만족

print('정규성 : Q-Q plot')

sr = scipy.stats.zscore(residual)   # 표본에 있는 z값을 계산함(확률분포)
(x, y), _ = scipy.stats.probplot(sr)
sns.scatterplot(x, y)
plt.plot([-3, 3], [-3, 3], '--', color='blue')
plt.show()

print('독립성 : 잔차가 자기상관(인접 관측치의 오차가 상관되어 있음)이 있는지 확인')
# Durbin-Watson:1.931 이므로 독립성은 만족

print('등분산성')
sns.regplot(fitted, np.sqrt(sr), lowess = True, line_kws={'color':'red'})
plt.show()

print('다중 공선성 ---')
vifdf = pd.DataFrame()
vifdf['vif_value'] = [variance_inflation_factor(data.iloc[:, [0,2,3,5,6]].values, i) 
                      for i in range(data.iloc[:, [0,2,3,5,6]].shape[1])]
print(vifdf)

print('새로운 값으로 예측')
new_df = pd.DataFrame({'Income':[35, 62],'Advertising':[6, 3],
                       'Price':[100, 60],'Age':[33, 40]})
new_pred = model.predict(new_df)
print('예측 결과 : ', new_pred.values)








