# 정규 표현식 :정규 표현식( 영어: regular expression)또는 정규식은 특정한 규칙을 가진 문자열의 집합을 표현하는 데 사용하는 형식 언어이다. 
import re

ss="1234 56 abc가나다mbc\nabcABC_123556_6python is fun파이썬 만세"

print(re.findall(r'123', ss))
print(re.findall(r'가나', ss))
print(re.findall(r'[0-9]', ss))
print(re.findall(r'[0-9]+', ss)) # *, +, ?, {횟수}
print(re.findall(r'[a-z,A-B]', ss))
print(re.findall(r'[a-z,A-B]+', ss))
print(re.findall(r'[^a-z,A-B]+', ss))
print(re.findall(r'[가-힣]+', ss))
print(re.findall(r'[^가-힣]+', ss))
print(re.findall(r'[0-9]{2,3}', ss))
pa=re.compile('[0-5]+')
print(re.findall(pa, ss))
imsi=re.findall(pa, ss)
print(imsi[0])
print()
print(re.findall(r'.bc', ss))
print(re.findall(r'a..', ss))
print(re.findall(r'^1', ss))
print(re.findall(r'만세$', ss))
print()
print(re.findall(r'\d', ss)) #숫자만
print(re.findall(r'\d+', ss))
print(re.findall(r'\d{2}', ss))
print(re.findall(r'\D', ss)) # \d를 뺀 나머지
print(re.findall(r'\s', ss))
print(re.findall(r'\S', ss))
print(re.findall(r'\w+', ss))
print(re.findall(r'\W+', ss))

print()
m=re.match(r'[0-9]+', ss)
print(m.group())
print()
p=re.compile('the', re.IGNORECASE) # flag 사용
print(p.findall('The dog the dog'))

print()
ss="""My name is tom.
I am happy"""
print(ss)

p=re.compile('^.+', re.MULTILINE)
print(p.findall(ss))
imsi=p.findall(ss)
print(imsi[0])
print(imsi[1])








