import urllib.request as req
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

url="https://kyochon.com/menu/chicken.asp"
menu=req.urlopen(url)

soup=BeautifulSoup(menu, 'lxml')

name=soup.select('dl.txt > dt')
price=soup.select('p.money strong')

nameDatas=[]
for p in name:
    nameDatas.append(p.string)
    
priceDatas=[]
for p in price:
    p2=p.text.strip().replace(',','')
    priceDatas.append(int(p2))

df=pd.DataFrame()
df['상품명']=nameDatas
df['가격']=priceDatas
print(df)

print('평균', round(df.가격.mean(), 2))
print('편차', round(df.가격.std(), 2))





