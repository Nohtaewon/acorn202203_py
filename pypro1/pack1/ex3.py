# 집합(묶음)형 자료형: str, list, tuple, set, dict

print('-----str----')
# str : 문자열 자료형. 순서O - 인덱싱, 슬라이싱 가능, 수정 불가(int, float, complex, bool, str, tuple)

s='sequence'
print(len(s), s.count('e'))
print(s.find('e'), s.find('e', 3), s.rfind('e'))
# 다양한 문자열 관련함수들 검색을 통해 사용

ss='mbc'
print(ss, id(ss))
ss='abc'
print(ss, id(ss))

print()
print(s) #sequence
print(s[0], s[7]) # s[8] err    인덱싱
print(s[-1], s[-2]) 
print(s[0:5], s[:3], s[3:]) # 슬라이싱 [이상:미만]
print(s[-4:-1], s[-4:], s[1:8:2])
s='fre'+s[2:]
print(s)

sss='mbc sbs kbs'
imsi=sss.split(' ')
print(imsi)
imsi2=','.join(imsi)
print(imsi2)
aa='Life is too long'
bb=aa.replace('Life', 'Your leg')
print(bb)

print('-----List-----') # 형식 list(), [요소...], 순서O, 수정O, 중복O
a=[1,2,3]
print(a)
b=[10, a, 20.5, True, '문자열']
print(b, id(b))
print(b[0], b[1], b[1][2])
print(b[2:5])
print(b[-2::2])
print(b[1][:2])

print()
family=['엄마', '아빠', '나']
family.append('남동생')
family.insert(0, '할머니')
family.extend(['삼촌', '고모']) # iterable: 집합형 자료
family+=['아저씨', '이모']
family.remove('나')  # 값에 의한 삭제
del family[0]   #순서에 의한 삭제
print(family, len(family))

print('엄마' in family)
print('나' in family)
aa=[1,2,3,1,2]
print(aa, id(aa))
aa[0]=77 # 요소 값 수정
print(aa, id(aa))

print('자료구조 관련:LiFO')
kbs=[1,2,3]
kbs.append(4)
print(kbs)
kbs.pop()
print(kbs)
kbs.pop()
print(kbs)

print('자료구조 관련:FiFO')
kbs=[1,2,3]
kbs.append(4)
print(kbs)
kbs.pop(0)
print(kbs)
kbs.pop(0)
print(kbs)

print('-----Tuple-----') # 형식 tuple(), (요소...), List와 유사, 순서O, 수정X, 중복O, 검색 속도 빠름 Read Only
#t=('a', 'b', 'c','d')
t='a', 'b', 'c','d'
print(t, type(t), id(t), len(t), t.index('c'))

p=(1,2,3,1,2)
print(p, id(p), type(p))
# p[0]=77 #err:'tuple' object does not support item assignment

# 형변환
p2=list(p)
print(p2, type(p2))
p3=tuple(p2)
print(p3, type(p3))

print('-----Set-----') # 형식 set(), {요소...}, 순서X, 수정O, 중복X Unique
a={1,2,3,1,3}
print(a, type(a), len(a))
b={3, 4}
print(a.union(b)) # 합집합
print(a.intersection(b)) # 교집합
print(a | b) # 합집합
print(a - b) # 차집합
print(a & b) # 교집합
# print(b[0]) #TypeError: 'set' object is not subscriptable
b.add(5)
b.update({6,7})
b.update([8,9])
b.update((10,11,12))
b.discard(8) # 값에 의한 삭제
b.remove(9)  # 값에 의한 삭제
b.discard(8)
# b.remove(9) 
print(b)

li=[1,2,2,3,4,4,5,3]
print(li)
imsi=set(li)
li=list(imsi)
print(li)

print('-----Dict-----') # 형식 dict(), {'key':value, ...}, 순서X, 수정O, key는 중복X, value는 중복O
mydic=dict(k1=1, k2='abc', k3=1.2)
print(mydic, type(mydic), id(mydic))

dic={'파이썬':'뱀', '자바':'커피', '스프링':'용수철'}
dic['여름']='장마철'
print(dic, type(dic), len(dic))
del dic['여름']
# dic.clear()
dic['파이썬']='만능 언어'
print(dic, type(dic), len(dic))

print(dic.keys())
print(dic.values())
print(dic.get('파이썬'))
print('파이썬' in dic)
print('파이' in dic)










