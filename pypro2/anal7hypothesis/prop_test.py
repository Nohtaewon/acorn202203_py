# 비율 검정 : 집단의 비율이 특정값과 같은 지를 검증

# one-sample
# a 회사에서는 100명 중에 45명이 흡연을 하고 있다.
# 국가 통계를 보니 국민 흡연율은 35%라고 알려져 있다.
# a 회사의 흡연율이 국민 흡연율과 동일여부를 검정하시오

# 귀무 : a 회사의 흡연율이 국민 흡연율의 비율은 같다
# 대립 : a 회사의 흡연율이 국민 흡연율의 비율은 같지 않다.

import numpy as np
from statsmodels.stats.proportion import proportions_ztest

count = np.array([45])
nobs = np.array([100])
val = 0.35

z, p = proportions_ztest(count=count, nobs=nobs, value=val)
print(z, p)     # p-value : 0.04442318 < 0.05 이므로 귀무 기각.

print('----------------------------------------')
# two-sample
# a회사 직원 300명 중 100명이 햄버거를 먹었고, b회사 직원 400명중 170명이 햄버거를 먹었다.
# 두 집단의 햄버거를 먹는 비율은 동일한가?
# 귀무 : 비율이 같다.
# 대립 : 비율이 다르다.
count = np.array([100, 170])
nobs = np.array([300, 400])
z, p = proportions_ztest(count=count, nobs=nobs, value=0)
print(z, p)     # p-value : 0.013675 < 0.05 귀무기각

