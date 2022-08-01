# 단순회귀분석 : ols()
import pandas as pd
import statsmodels.formula.api as smf
df = pd.read_csv('testdata/drinking_water.csv')
print(df.head(3))

# 상관관계 확인
print(df.corr())

# 적절성, 만족도 : 0.766853
# 위 두 변수는 인과관계가 있다 가정하고 회구분석을 수행. x : 적절성, y = 만족도

model=smf.ols(formula='만족도~적절성', data=df).fit()
print(model.summary())
# 수식 : y =0.7393 * x +0.7789
print(0.766853*0.766853)    # 0.588063523609 : 상관계수를 제곱한 값이 모델의 R-squared(결정계수, 설명력)가 됨
# 설명력 : 독립변수가 종속변수의 분산을 어느정도 설명하는 지를 알려줌.
# 선형회귀모델의 성능을 표현할 때 사용함. 절대적으로 신뢰하지는 않음. 15% 이상일 경우 모델을 사용함

print('회귀 계수(Intercept, slope) : ', model.params) 
print('결정 계수(R-squared) : ', model.rsquared)
print('p-value : ', model.pvalues)

# 결과 예측
print(df.적절성[:5].values)
new_df = pd.DataFrame({'적절성':[4, 3, 4, 2, 6]})
pred = model.predict(new_df)
print('예측결과 : ', pred)






