# 집단 간 차이분석: 평균 또는 비율 차이를 분석
# : 모집단에서 추출한 표본정보를 이용하여 모집단의 다양한 특성을 과학적으로 추론할 수 있다.
# * T-test와 ANOVA의 차이
# - 두 집단 이하의 변수에 대한 평균차이를 검정할 경우 T-test를 사용하여 검정통계량 T값을 구해 가설검정을 한다.
# - 세 집단 이상의 변수에 대한 평균차이를 검정할 경우에는 ANOVA를 이용하여 검정통계량 F값을 구해 가설검정을 한다

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 단일 표본 t검정 : one-sample t-test. 정규분포의 표본에 대해 기댓값을 조사하는 검정방법
# 실습1 : 어느 남성 집단의 평균 키 검정
# 귀무 : 어느 남성 집단의 평균 키는 175.0 이다.
# 대립 : 어느 남성 집단의 평균 키는 175.0이 아니다.
one_sample = [167.0, 182.7, 169.6, 176.8, 185.0]
print(np.array(one_sample).mean())  # 176.21999999999997

result = stats.ttest_1samp(one_sample, popmean=175.0)
print('검정통계량 t값 : %.3f, p-value : %.3f'%result)
# 해석 : p-value : 0.747 > 0.05 귀무가설 채택.
# 어느 남성 집단의 평균 키는 175.0 이다.

print()
print('참고 : 평균 키는 165.0이라고 한 경우-----')
result = stats.ttest_1samp(one_sample, popmean=165.0)
print('검정통계량 t값 : %.3f, p-value : %.3f'%result)
# 해석 : p-value : 0.033 < 0.05 귀무가설 기각. 대립가설 채택
# 어느 남성 집단의 평균 키는 175.0 이 아니다.
print("---------실습 예제 2 ----------------------------------")
# 실습 예제 2)
# A중학교 1학년 1반 학생들의 시험결과가 담긴 파일을 읽어 처리 (국어 점수 평균검정) 
# 귀무 : A중학교 1학년 1반 학생들의 국어 점수 평균은 80이다.
# 대립 : A중학교 1학년 1반 학생들의 국어 점수 평균은 80이 아니다.

data = pd.read_csv("testdata/student.csv")
print(data.head(3))
print(data.describe())
print(data['국어'].mean())    # 72.9

result2 = stats.ttest_1samp(data['국어'], popmean=80.0)
print('검정통계량 t값 : %.3f, p-value : %.3f'%result2)
# 해석 p-value : 0.199 > 0.05 귀무가설 채택.
# A중학교 1학년 1반 학생들의 국어 점수 평균은 80이다. 현재 수집된 데이터는 우연히 발생한 값이다.

print("---------실습 예제 3 ----------------------------------")
# 실습 예제3)
# 여아 신생아 몸무게의 평균 검정 수행 babyboom.csv
# 여아 신생아의 몸무게는 평균이 2800(g)으로 알려져 왔으나 이보다 더 크다는 주장이 나왔다.
# 표본으로 여아 18명을 뽑아 체중을 측정하였다고 할 때 새로운 주장이 맞는지 검정해 보자.
# gender : 1 이 여아 2 가 남아

data = pd.read_csv("testdata/babyboom.csv")
print(data.head(3), len(data))

fdata = data[data.gender == 1]
print(fdata, len(fdata))
print(np.mean(fdata.weight))    # 3132.44

# 정규성 검정 실시 (두 집단 이상일 때 주로 사용)
print(stats.shapiro(fdata.iloc[:, 2]))
# ShapiroResult(statistic=0.8702830076217651, pvalue=0.017984798178076744)
# 해석 : pvalue=0.01798 < 0.05 이므로 정규성 불만족

# histogram으로 정규분포 확인
sns.distplot(fdata.iloc[:, 2], kde=True)
plt.show()

stats.probplot(fdata.iloc[:, 2], plot=plt)
plt.show()

result3 = stats.ttest_1samp(fdata.weight, popmean=2800.0)
print('검정통계량 t값 : %.3f, p-value : %.3f'%result3)
# 해석 : p-value : 0.039 < 0.05 이므로 귀무가설 기각하고 대립가설 채택.
# 여아 신생아의 몸무게는 평균은 기존에 알려진 2800g 보다 증가하였다.

