# 기상청 중기 예보 xml 문서 읽기
import urllib.request as req
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

url="https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"
data=req.urlopen(url).read()
# print(data.decode('utf-8'))

soup=BeautifulSoup(data, 'lxml')
# print(soup)

title=soup.find('title').string
print(title)

city=soup.find_all('city')
# print(city)
cityDatas=[]
for c in city:
    # print(c.string)
    cityDatas.append(c.string)
    
df=pd.DataFrame()
df['city']=cityDatas
print(df.head(3))

tempMins=soup.select('location > province + city +data > tmn')

tempDatas=[]
for t in tempMins:
    tempDatas.append(t.string)

df['temp_min']=tempDatas
print(df.head(3), len(df))
df.columns=['지역','최저기온']
print(df.head(3))

df.to_csv('날씨정보.csv', index=False)

print('~~~~~~~~~~~~~~~~~~~~~~~')
print(df.iloc[0], type(df.iloc[0]))
print()
print(df.iloc[0:2], type(df.iloc[0:2])) #df.iloc[0:2, :]
print()
print(df.iloc[0:2, 0:1])
print(df.iloc[0:2, 0:2])
print()
print(df['지역'][0:2])
print(df['지역'][:2])
# print(df[:])
print(df.loc[1:3])
print()
print(df.loc[[1,3]])
print()
print(df.loc[:,'지역'].head(2))
print()
print(df.loc[1:3, ['최저기온', '지역']])
print()
print(df.loc[:,'지역'][1:4])
print()
print(df.loc[2:5,'지역'][0:3])
print('-------------------------------')
df=df.astype({'최저기온':'int'})    # 문자를 숫자로 형변환
print(df.info())
print()
print(df['최저기온'].mean())
print(df.loc[df['최저기온'] >= 24])
print()
print(df.sort_values(['최저기온'], ascending=True))
