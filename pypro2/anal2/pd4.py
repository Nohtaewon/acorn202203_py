import pandas as pd
import numpy as np

# DataFrame 객체 병합 : merge
df1=pd.DataFrame({'data1':range(7), 'key':['b','b','a','c','a','a','b']})
print(df1)
df2=pd.DataFrame({'key':['a','b','d'], 'data2':range(3)})
print(df2)
print('inner----------------------------------')
print(pd.merge(df1, df2, on='key'))     # key 를 기준으로 병합 (inner join : 교집합)
print()
print(pd.merge(df1, df2, on='key', how='inner')) 
print('outer----------------------------------')
print(pd.merge(df1, df2, on='key', how='outer'))    # key 를 기준으로 병합 (full outer join)
print('left----------------------------------')
print(pd.merge(df1, df2, on='key', how='left'))     # key 를 기준으로 병합 (left outer join)
print('right----------------------------------')
print(pd.merge(df1, df2, on='key', how='right'))    # key 를 기준으로 병합 (right outer join)

print('공통 칼럼명이 없는 경우----------df1 vs df3-------------')
df3=pd.DataFrame({'key2':['a','b','d'], 'data2':range(3)})
print(df3)
print(df1)
print(pd.merge(df1, df3, left_on='key', right_on='key2', how='inner'))

print('자료 이어 붙이기')
print(pd.concat([df1, df3], axis=0) )
print(pd.concat([df1, df3], axis=1) )

print('피봇(pivot)')
# 열을 기준으로 구조를 변경하여 새로운 집계표를 작성
data={'city':['강남', '강북','강남', '강북'],
      'year':[2000,2001,2002,2002],
      'pop':[3.3,3.5,3.0,2.0]
      }
df=pd.DataFrame(data)
print(df)

print('pivot------------------------------------')
print(df.pivot('city', 'year','pop'))
print()
# set_index : 기존의 행 인덱스를 제거하고 첫번째 열 인덱스 설정
print(df.set_index(['city', 'year']).unstack())


print('groupby------------------------------------')
hap=df.groupby(['city'])
print(hap.sum())
print(df.groupby(['city']).sum())   # 위 두줄을 한줄로 표현
print(df.groupby(['city','year']).mean())
print()
print(df.groupby(['city']).agg('sum'))
print()
print(df.groupby(['city','year']).agg('sum'))
print(df.groupby(['city','year']).agg('mean'))
print(df.groupby(['city','year']).agg(['mean','sum']))

print('pivot_table------------------------------------')
print(df)
print(df.pivot_table(index=['city']))   # 평균 계산
print(df.pivot_table(index=['city'], aggfunc=np.mean))   # 기본값
print(df.pivot_table(index=['city','year'], aggfunc=[len, np.sum]))
print(df.pivot_table(values=['pop'], index=['city'], aggfunc=np.mean))
print(df.pivot_table(values=['pop'], index=['city'], aggfunc=len))
print(df.pivot_table(values=['pop'], index=['year'], columns=['city']))
print(df.pivot_table(values=['pop'], index=['year'], columns=['city'],margins=True))
print(df.pivot_table(values=['pop'], index=['year'], columns=['city'],margins=True, fill_value=0))











