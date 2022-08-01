import numpy as np
import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import statsmodels.api as sm
# 귀무 : 기름의 종류에 따라 흡수하는 기름의 평균에 차이가 없다.
# 대립 : 기름의 종류에 따라 흡수하는 기름의 평균에 차이가 있다.
data = pd.read_csv("anova4quiz.txt", sep=' ')
data.columns=['종류', '양']
data=data.fillna(data['양'].mean())

oil1=data[data['종류']==1]
oil2=data[data['종류']==2]
oil3=data[data['종류']==3]
oil4=data[data['종류']==4]

print(stats.ks_2samp(oil1['양'], oil2['양'])) # pvalue=0.9307359307359307

print("정규성 검정 : ", stats.shapiro(oil1['양'])) #0.8680403232574463  정규성 만족
print("정규성 검정 : ", stats.shapiro(oil2['양']))
print("정규성 검정 : ", stats.shapiro(oil3['양']))
print("정규성 검정 : ", stats.shapiro(oil4['양']))
print()
print('등분산성 확인 :', stats.levene(oil1['양'], oil2['양'], oil3['양'], oil4['양']).pvalue) #0.32689 등분산성 만족
print()

print('방법 1')
f_sta, p_val = stats.f_oneway(oil1['양'], oil2['양'], oil3['양'], oil4['양'])
print("p-value : {}".format(p_val))    
# 해석 : p-value : 0.84824 > 0.05이므로 귀무가설 채택 

print()
print('방법 2')
lmodel = ols('양 ~ C(종류)', data).fit()
print(anova_lm(lmodel)) 
