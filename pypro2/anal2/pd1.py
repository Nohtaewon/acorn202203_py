# pandas : 고수준의 자료구조와 빠르고 쉬운 분석용 자료구조 및 함수를 지원
# data munging or data wrangling 작업을 효율적으로 처리 가능
# : 원자료(raw data)를 보다 쉽게 접근하고 분석할 수 있도록 데이터를 정리하고 통합하는 과정

import pandas as pd
from pandas import Series, DataFrame
import numpy as np
# Series : 일련의 자료를 담을 수 있는 1차원 배열과 유사한 자료구조로 색인을 갖음

obj = pd.Series([3,7,-5,4])
# obj = pd.Series((3,7,-5,4))
# obj = pd.Series({3,7,-5,4})     TypeError: 'set' type is unordered
print(obj, type(obj))

obj2 = pd.Series([3,7,-5,4], index=['a','b','c','d'])
print(obj2)
print(obj2.sum(), sum(obj2), np.sum(obj2))
print(obj2.mean(), obj2.std())

print()
print(obj2.values)
print(obj2.index)

print('슬라이싱--------------------------------')
print(obj2['a'], ' ', obj2[['a']])
print(obj2[0])
print(obj2[['a','b']])
print(obj2['a':'c'])
print(obj2[1:4])
print(obj2[[2, 1]])
print(obj2 > 1)
print('a' in obj2)

print('dict type 으로 Series 객체 생성 ------------')
names={'mouse':5000, 'keyboard':35000, 'monitor':550000}
obj3=Series(names)
print(obj3, type(obj3))
obj3.index=['마우스','키보드','모니터']
print(obj3)
print(obj3['마우스'])
print(obj3[0])

obj3.name='상품가격'
print(obj3)
print('----------------------------------------------------')
print('-----DataFrame : 표 모양의 자료구조----------------------')
df = DataFrame(obj3)
print(df, type(df))

data = {
    'irum':['홍길동', '한국인', '신기해', '공기밥', '한가해'],
    'juso':('역삼동', '신당동', '역삼동', '역삼동','신사동'),  
    'nai':[23,25,33,30,35], 
}
print(data, type(data))

frame=DataFrame(data)
print(frame.irum, type(frame.irum))
print(frame['irum'])

print(DataFrame(data, columns=['juso','nai','irum']))

print()
frame2=DataFrame(data, columns=['irum','juso','nai','tel'], index=['a', 'b', 'c', 'd', 'e'])
print(frame2)

frame2['tel']='111-1111'
print(frame2)

val=Series(['222-2222','333-1111', '444-1111'], index=['b','c','e'])
print(val)
frame2['tel']=val
print(frame2)

print()
print(frame2.T) # 행렬 위치변경 Transpose
print(frame2.values[0, 1])
print(frame2.values[0:2])
print(type(frame2.values[0:2]))

print('행 또는 열 삭제')  # axis=0 행, axis=1 열
frame3=frame2.drop('d')    # axis=0 생략
print(frame3) 

frame4=frame2.drop('tel', axis=1)    # 열 삭제
print(frame4)

print('-----정렬-------------------------------')
print(frame2.sort_index(axis=0, ascending=False))
print(frame2.sort_index(axis=1, ascending=False))
print(frame2.rank(axis=0))

counts=frame2['juso'].value_counts()
print('칼럼값 개수',counts)

print('문자열 자르기 -------------')
data={
    'juso':['강남구 역삼동', '중구 신당동', '강남구 대치동'],
    'inwon':[23, 25, 15]
}
fr=DataFrame(data)
print(fr)

result1=Series([x.split()[0] for x in fr.juso])
result2=Series((x.split()[0] for x in fr.juso))
print(result1)
print(result2)
print(result1.value_counts())

# -----------------------------------------
print('Series의 재색인')
data=Series([1,3,2], index=(1,4,2))
print(data)
data2=data.reindex((1,2,4))
print(data2)

print('재색인 시 값 채워넣기')
data3=data2.reindex([0,1,2,3,4,5])  # 대응값이 없는 인덱스는 NaN(결측치)이 됨
print(data3)

data3=data2.reindex([0,1,2,3,4,5], fill_value = 77)
print(data3)

data3=data2.reindex([0,1,2,3,4,5], method = 'ffill')
# data3=data2.reindex([0,1,2,3,4,5], method = 'pad')
print(data3)

data3=data2.reindex([0,1,2,3,4,5], method = 'bfill')
# data3=data2.reindex([0,1,2,3,4,5], method = 'backfill')
print(data3)

print('bool 처리 ---------------')
df = DataFrame(np.arange(12).reshape(4,3),
               index=['1월','2월','3월','4월'], columns=['강남','강북','서초']
               )
print(df)
print(df['강남']>3)
print(df[df['강남']>3])   # 조건이 참인 행 출력
print()

print(df<3)
df[df<3] = 0    # 3보다 작은 값은 0으로 대체
print(df)
print()
print('-----DataFrame 관련 슬라이싱 함수 : loc() - 라벨 지원, iloc() - 순서(숫자) 지원')
print(df.loc['3월', :])
print(df.loc['3월', ])
print(df.loc[:'2월', ['서초']])    # 2월 행 이하, 서초 열 반환
print()

print(df.iloc[2])   # 2행 모두 출력
print(df.iloc[2, :])
print(df.iloc[:3])  # 3행 미만
print(df.iloc[:3, 2])  # 3행 미만, 2열 반환
print(df.iloc[1:3, 1:3])  # 1,2행 반환, 1, 2열 반환
