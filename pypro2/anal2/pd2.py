# 연산
from pandas import Series, DataFrame
import numpy as np

s1 = Series([1,2,3], index=['a','b','c'])
s2 = Series([4,5,6,7], index=['a','b','d','c'])
print(s1)
print(s2)
print(s1+s2)    # Series 객체 간 연산. +-*/
print(s1.add(s2))

print()     # DataFrame 객체 간 연산. +-*/
df1=DataFrame(np.arange(9.).reshape(3,3), columns=list('kbs'), index=['서울','대전','부산'])
df2=DataFrame(np.arange(12.).reshape(4,3), columns=list('kbs'), index=['서울','대전','제주','수원'])
print(df1)
print(df2)
print(df1+df2)
print(df1.add(df2,fill_value=0))    # NaN은 0으로 채운 후 연산에 참여
# add, sub, mul, div

seri=df1.iloc[0]
print(seri)
print(df1)
print()
print(df1+seri) # DataFrame/Series 연산 : Broadcasting

# 기술 통계 관련 함수 :수집한 데이터를 요약, 묘사, 설명하는 통계 기법
print('결측 값 처리')
df=DataFrame([[1.4, np.nan],[7, -1.5], [np.NaN, np.NAN],[0.5, -1]], columns=['one','two'])
print(df)
print()
print(df.drop(1))   # 1행(특정) 삭제
print(df.isnull())  # null 값 탐지
print(df.notnull())
print(df.dropna())
print(df.dropna(how='any')) # NaN이 하나라도 있으면 해당 행 삭제
print(df.dropna(how='all')) # 모든 값이 NaN 인 경우 해당 행 삭제
print(df.dropna(subset=['one']))    # 'one' 열 값이 NaN인 경우 해당 행 삭제
print(df.dropna(axis='rows'))   # NaN이 있는 행의 해당 행 삭제
print(df.dropna(axis='columns'))    # NaN이 있는 열의 해당 열 삭제
print()
print(df.fillna(0)) # NaN 값을 0으로 채우기
print(df.fillna(method='ffill'))
print(df.fillna(method='bfill'))

print('내장 함수')
print(df)
print(df.sum())     # 열의 합
print(df.sum(axis=0)) 
print()
print(df.sum(axis=1))   # 행의 합
print(df.mean(axis=1))  # 행의 평균
print(df.mean(axis=1, skipna=False))    # 행의 평균. NaN은 연산에서 제외
print()
print(df.describe())    # 요약 통계량 출력
print(df.info())    # 구조 출력

words=Series(['봄','여름','봄'])
print(words.describe())

print('-----Quiz1----------------------------------------------')
# pandas 문제 1)
# a) 표준정규분포를 따르는 9 X 4 형태의 DataFrame을 생성하시오. 
#    np.random.randn(9, 4)
# b) a에서 생성한 DataFrame의 칼럼 이름을 - No1, No2, No3, No4로 지정하시오
# c) 각 컬럼의 평균을 구하시오. mean() 함수와 axis 속성 사용
data=np.random.randn(9, 4)
df=DataFrame(data, columns=['No1', 'No2', 'No3', 'No4'])
print(df)
print(df.mean(axis=0))

print('-----Quiz2----------------------------------------------')
# pandas 문제 2)
# a) DataFrame으로 위와 같은 자료를 만드시오. colume(열) name은 numbers, row(행) name은 a~d이고 값은 10~40.
# b) c row의 값을 가져오시오.
# c) a, d row들의 값을 가져오시오.
# d) numbers의 합을 구하시오.
# e) numbers의 값들을 각각 제곱하시오. 아래 결과가 나와야 함.
# f) floats 라는 이름의 칼럼을 추가하시오. 값은 1.5, 2.5, 3.5, 4.5    아래 결과가 나와야 함.
# g) names라는 이름의 다음과 같은 칼럼을 위의 결과에 또 추가하시오. Series 클래스 사용.
data={'a':10, 'b':20, 'c':30, 'd':40}
df=DataFrame(Series(data), columns=['numbers'])
print(df)
print(df.loc['c'])
print(df.loc[['a', 'd']])
print(df.sum())
print(df*df)
print()
df['floats']=['1.5','2.5', '3.5','4.5']
print(df)
df['names']=Series(['길동','오정', '팔계','오공'], index=['d','a','b','c'])
print(df)







