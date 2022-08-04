import pandas as pd
import numpy as np

# pandas로 파일 읽기
# df=pd.read_csv('testdata/ex1.csv')
# df=pd.read_csv('testdata/ex1.csv', sep=',')
df=pd.read_table('../testdata/ex1.csv', sep=',')
print(df, type(df))

print()
df=pd.read_csv('../testdata/ex2.csv', header=None, names=['a','b','c','d','e'])
print(df)

print()
df=pd.read_csv('../testdata/ex3.txt')
print(df)

print()
df=pd.read_csv('../testdata/ex3.txt', sep='\s+')   # 구분자로 정규표현식
print(df)

print()
df=pd.read_table('../testdata/ex3.txt', sep='\s+', skiprows=[1,3])   # 구분자로 정규표현식
print(df)

print()
mydf=pd.read_fwf('../testdata/data_fwt.txt', widths=(10,3,5), header=None, names=('date','name','price'))
print(mydf)
print(mydf['date'])
print()
# 큰 규모의 파일인 경우 나누어 읽기 : chunk
test=pd.read_csv('../testdata/data_csv2.csv', header=None, chunksize=3)
print(test) # TextFileReader object

for piece in test:
    # print(piece)
    print(piece.sort_values(by=2, ascending=True))  # 2번째 열 기준 내림차순 정렬

print('-----------------------------------------')
# pandas 객체를 파일로 저장
items={'apple':{'count':10, 'price':1500}, 'orange':{'count':5, 'price':700}}
df=pd.DataFrame(items)
print(df)
df.to_clipboard()
print(df.to_html())
print(df.to_csv())
print(df.to_json())
print()
df.to_csv('result1.csv', sep=',')
df.to_csv('result2.csv', sep=',', index=False)
df.to_csv('result3.csv', sep=',', index=False, header=False)

print('----Quiz3-1------------------------------------------------')
df=pd.read_csv('../testdata/titanic_data.csv')
print(df)
bins=[1,20,35,60,150]
labels=['소년','청년','장년','노년']
df.Age=pd.cut(df.Age, bins, labels=labels)
print(df.Age.value_counts())
print()

print('----Quiz3-2------------------------------------------------')
df2=df.pivot_table(values=['Survived'], index=['Sex'], columns=['Pclass'],fill_value=0)
print(round(df2*100,2))
print('----Quiz4-2------------------------------------------------')
df=pd.read_csv('../testdata/tips.csv')
print(df.info()) 
print(df.head(3))
print(df.describe())
print(pd.value_counts(df['smoker']))
print(pd.unique(df['day']))
















