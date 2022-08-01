# 1
# import numpy as np
# data = np.array([[1,2,3,4],
#                         [5,6,7,8],
#                         [9,10,11,12],
#                         [13,14,15,16]])
# print(np.flip(data))
# 2
# import seaborn as sns
# titanic = sns.load_dataset('titanic')
# print(titanic.pivot_table(values=['survived'], index=['sex'], columns=['class']))
# from pandas import DataFrame
# frame = DataFrame({'bun':[1,2,3,4], 'irum':['aa','bb','cc','dd']}, index=['a','b', 'c','d'])
# print(frame.T)
# frame2= frame.drop('d')
# print(frame2)
# import pandas as pd
# df = pd.read_csv("testdata/ex.csv", names=['a','b','c','d'])
# print(df)
# import numpy as np
# x = np.array([1,2,3,4,5])
# y = np.arange(1, 4).reshape(3,1)
# print(x)
# print(y)
# print(x+y)
# from pandas import DataFrame
#
# data = {"a": [80, 90, 70, 30], "b": [90, 70, 60, 40], "c": [90, 60, 80, 70]}
# df =DataFrame(data)
# df.columns=['국어', '영어', '수학']
# print(df)
# print(df.수학)
# print(df.수학.std())
# print()
# print(df[['국어','영어']])

import scipy.stats as stats
from numpy import mean
# 귀무 : 포장지 색상에 따른 제품의 매출액에 차이가 존재하지 않는다.
# 대립 : 포장지 색상에 따른 제품의 매출액에 차이가 존재한다.

blue = [70, 68, 82, 78, 72, 68, 67, 68, 88, 60, 80]
red = [60, 65, 55, 58, 67, 59, 61, 68, 77, 66, 66]
print(mean(blue))   # 72.81818181818181
print(mean(red))    # 63.81818181818182
two_sample = stats.ttest_ind(blue, red)
print(two_sample)
# Ttest_indResult(statistic=2.9280203225212174, pvalue=0.008316545714784403)
# pvalue=0.00831 < 0.05 이므로 대립가설 채택














