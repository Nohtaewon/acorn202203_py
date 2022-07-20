# BeautifulSoup의 find / select 함수 연습

from bs4 import BeautifulSoup

html_page="""
<html><body>
<h1>제목</h1>
<p>웹 문서 읽기</p>
<p>원하는 자료 선택</p>
</body></html>
"""
print(html_page, type(html_page))  # <class 'str'> 

soup = BeautifulSoup(html_page, 'html.parser')  # BeautifulSoup 객체 생성
print(soup, type(soup)) # <class 'bs4.BeautifulSoup'>

print()
h1 = soup.html.body.h1
print("h1:",h1.string, h1.text)
p1 = soup.html.body.p
print("p1:",p1.text)
p2 = p1.next_sibling.next_sibling
print("p2:",p2.text)
print()
print('find 함수 사용 : 반환값이 1개 ---------------------------------')

html_page2="""
<html><body>
<h1 id="title">제목 태그</h1>
<p>웹 문서 읽기</p>
<p id="my" class="our" kbs='공영방송'>원하는 자료 선택</p>
</body></html>
"""
soup2 = BeautifulSoup(html_page2, 'lxml')
print(soup2.p, soup2.p.string)
print(soup2.find('p').string)
print(soup2.find(['p','h1']))
print(soup2.find('p', id="my").string)
print(soup2.find(id="my").string)
print(soup2.find(id="title").string)
print(soup2.find(class_="our").string)
print(soup2.find(attrs={'class':'our'}).string)
print(soup2.find(attrs={'id':'my'}).string)
print(soup2.find(attrs={'kbs':'공영방송'}).string)

print()
print('find_all, findAll 함수 사용 : 반환값이 복수 ---------------------------------')

html_page3="""
<html><body>
<h1 id="title">제목 태그</h1>
<p>웹 문서 읽기</p>
<p id="my" class="our" kbs='공영방송'>원하는 자료 선택</p>
<div>
    <a href="http://www.naver.com">네이버</a>
    <a href="http://www.daum.net">다음</a>
</div>
</body></html>
"""
soup3 = BeautifulSoup(html_page3, 'lxml')
print(soup3.find_all('a'))
print(soup3.find_all(['p']))
print(soup3.find_all(['p','a']))
print(soup3.findAll(['p','a']))

links=soup3.find_all('a')
for i in links:
    href=i.attrs['href']
    text=i.string
    print(href, ' ', text)

print('---------------------------------------------')
# https://music.bugs.co.kr/chart 에서 자료 읽기
from urllib.request import urlopen
url= urlopen("https://music.bugs.co.kr/chart")
soup=BeautifulSoup(url.read(), 'html.parser')
# print(soup)
musics = soup.find_all('td', class_='check')
# print(musics)

for i, music in enumerate(musics):
    print("{}위:{}".format(i+1, music.input['title']))

print()
print('select_one, select 함수 사용 -----------------------')

html_page4="""
<html><body>
<div id="hello">
    <a href="http://www.naver.com">네이버</a>
    <span>
        <a href="http://www.daum.net">다음</a>
    </span>
    <ul class="world">
        <li>여름은</li>
        <li>즐거워</li>
    </ul>
</div>
<div id="hi" class="good">
 두번째 div태그
</div>
</body></html>
"""
soup4 = BeautifulSoup(html_page4, 'lxml')
print(soup4.select_one("div"))
print()
print(soup4.select_one("div a"))    # div의 자손
print(soup4.select_one("div > a"))  # div의 자식
print()
print(soup4.select("div a"))    
print(soup4.select("div > a"))
print()
print(soup4.select("div#hello"))
print(soup4.select("div#hi"))
print(soup4.select("div.good"))
print()
print(soup4.select("div#hello ul.world > li"))

imsi=soup4.select("div#hello ul.world > li")
for i in imsi:
    print(i.string)








