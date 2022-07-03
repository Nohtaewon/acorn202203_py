'''
여러 줄
주석
'''
"""
여러줄
주석
"""
# 한 줄 주석
print("표준 출력장치로 출력")
var1='안녕 파이썬'
print(var1)
var1=3; print(var1)
var1='변수 선언시 타입을 적지 않음. 참조 데이터에 의해 타입이 결정'
print(var1)

print()
a=10
b=12.3
c=b
print(a,b,c)
print(id(a),type(a))
print(id(b),type(b))
print(id(c),type(c))
print(a is b, a==b) #False False    is 주소 비교, == 값 비교
print(b is c, b==c) #True True
aa=[100]
bb=[100]
print(aa==bb, aa is bb)
print(id(aa), id(bb))

print()
A=1; a=2;
print(A,'',a)

# for = 1 #키워드를 변수로 사용할 수 없다
import keyword
print('키워드 목록:', keyword.kwlist)

print('\n숫자 진법')
print(10, oct(10), hex(10), bin(10))
print(10, 0o12, 0xa, 0b1010)

print('\n자료형 확인')
print(3, type(3))
print(3.4, type(3.4))
print(3+4j, type(3+4j))
print(True, type(True))
print('3', type('3'))

print((3,), type((3,)))
print([3], type([3]))
print({3}, type({3}))
print({'key':3}, type({'key':3}))
















