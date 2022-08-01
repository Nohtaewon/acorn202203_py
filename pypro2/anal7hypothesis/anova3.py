# 어느 음식점이 대상 : 최고 온도에 따른 매출의 평균 차이 검정

# 귀무 : 온도에 따른 매출액에 차이가 없다.
# 대립 : 온도에 따른 매출액에 차이가 있다.

import numpy as np
import scipy.stats as stats
import pandas as pd

# 매출 데이터 읽기
sales_data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/tsales.csv",
                         dtype={'YMD':'object'})   # int type ==> object type 으로 변환해 읽기
print(sales_data.head(3))
print(sales_data.info())
print()
# 날씨 데이터 읽기
wt_data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/tweather.csv")
print(wt_data.head(3))

print()
# wt_data의 날짜를 2018-06-01 ==> 20180601로 변환. 병합(merge)을 위함
wt_data.tm = wt_data.tm.map(lambda x:x.replace('-',''))
print(wt_data.head(3))
# print(wt_data.info())
print()
frame = sales_data.merge(wt_data, how='left', left_on='YMD', right_on='tm')
print(frame.head(3))
print(frame.columns)
# 'YMD', 'AMT', 'CNT', 'stnId', 'tm', 'avgTa', 'minTa', 'maxTa', 'sumRn', 'maxWs', 'avgWs', 'ddMes'

data = frame.iloc[:, [0,1,7,8]]  # 'YMD', 'AMT', 'maxTa', 'sumRn'
print(data.head(3))

print(data.maxTa.describe())

import matplotlib.pyplot as plt
# plt.boxplot(data.maxTa)
# plt.show()

# 온도(연속형)를 임의로 추움, 보통, 더움 ( 0, 1, 2 )으로 (세 구간)나누기(범주형) (null 값 제외)
# 결측치 확인
print(data.isnull().sum())

data['Ta_gubun'] = pd.cut(data.maxTa, bins=[-5, 8, 24, 37], labels=[0,1,2])
data = data[data.Ta_gubun.notna()]
print(data.head(3), '', data.Ta_gubun.unique())

print(data.corr())  # 상관관계 확인

# 등분산성 확인
x1 = np.array(data[data.Ta_gubun == 0].AMT)
x2 = np.array(data[data.Ta_gubun == 1].AMT)
x3 = np.array(data[data.Ta_gubun == 2].AMT)
print(x1[:3])
print(stats.levene(x1, x2, x3).pvalue)  # 0.03900239 < 0.05 이므로 만족하지 않다.
# 정규성 확인
print(stats.ks_2samp(x1, x2).pvalue)    # 정규성 만족못함
print(stats.ks_2samp(x1, x3).pvalue)
print(stats.ks_2samp(x2, x3).pvalue)

# 온도별 매출액 평균
spp = data.loc[:, ['AMT', 'Ta_gubun']]
# 과학적 표기법 대신 소수점 5자링까지 나타낸다
pd.options.display.float_format='{:.3f}'.format
print(pd.pivot_table(spp, index=['Ta_gubun'], aggfunc='mean'))
# 0        1032362.319
# 1         818106.870
# 2         553710.938
# 다시 원래대로 옵션을 변경하고 싶을 때
pd.reset_option('display.float_format')

sp = np.array(spp)
print(sp[:2])
group1 = sp[sp[:,1]==0, 0]
group2 = sp[sp[:,1]==1, 0]
group3 = sp[sp[:,1]==2, 0]

# plt.boxplot([group1, group2, group3])
# plt.show()

# ANOVA 검정 수행
print(stats.f_oneway(group1, group2, group3))
# F_onewayResult(statistic=99.1908012029983, pvalue=2.360737101089604e-34)
# 해석 : pvalue=2.360737101089604e-34 < 0.05 이므로 귀무가설 기각 대립가설 채택
# 온도에 따른 매출액에 차이가 있다.

print()
print(stats.kruskal( group1, group2, group3 )) # 정규성 X 이므로
# KruskalResult(statistic=132.7022591443371, pvalue=1.5278142583114522e-29)
print()
# pip install pingouin
from pingouin import welch_anova
print(welch_anova(dv='AMT', between='Ta_gubun', data=data)) # 등분산성 X 이므로
#      Source  ddof1     ddof2           F         p-unc       np2
# 0  Ta_gubun      2  189.6514  122.221242  7.907874e-35  0.379038

# 사후검정
from statsmodels.stats.multicomp import pairwise_tukeyhsd
posthoc = pairwise_tukeyhsd(spp['AMT'], spp['Ta_gubun'], alpha=0.05)
print(posthoc)

posthoc.plot_simultaneous()
plt.show()

