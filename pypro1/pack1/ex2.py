# 연산자
v1=3
v1=v2=v3=5
print(v1, v2, v3)
print('출력1', end=',')
print('출력2')
v1=1,2,3
print(v1)
v1, v2=10, 20
print(v1, v2)
v2, v1=v1, v2
print(v1, v2)

print('값 할당 packing 연산')
v1, *v2=1,2,3,4,5
print(v1)
print(v2)

*v1, v2, v3=1,2,3,4,5
print(v1)
print(v2)
print(v3)

print('-------')
print(5+3,5-3,5*3,5/3,5//3,5%3)
print(divmod(5,3))
a,b=divmod(5,3)
print(a)
print(b)
print(5 ** 3)

print('우선 순위:', 3+4*5,(3+4)*5) #소괄호>산술(*, / > +, -) > 관계 > 논리 > 치환
print(5>3, 5==3, 5!=3)
print(5>3 and 4<3, 5>3 or 4<3, not(5>=3))

print()
print('한'+'국인'+' '+"파'이'팅"+' '+'파"이"팅')
print('한국인'*10)

print('누적')
a=10
a=a+1
a+=1
#a++ 증감 연산자 X
++a
print('a:', a)
print(a, a*-1,-a,--a,+a)

print()
print('bool 처리:',True,False)
print(bool(True), bool(1), bool(-3.4), bool('a'))
print(bool(False), bool(0), bool(0.0), bool(''),bool([]),bool({}),bool(None))

print('aa\nbb')
print('aa\tbb')
print('aa\bbb')
print(r'c:\aa\nbc') # r(raw string)을 사용해 escape 기능 해제

print('print 관련 서식')
print(format(1.5678, '10.3f'))
print ('{0:.3f}'.format(1.0/3))
print('나는 나이가 %d 이다.'%23)
print('나는 나이가 %s 이다.'%'스물셋')
print('나는 나이가 %d 이고 이름은 %s이다.'%(23, '홍길동'))
print('나는 나이가 %s 이고 이름은 %s이다.'%(23, '홍길동'))
print('나는 키가 %f이고, 에너지가 %d%%.'%(177.7, 100))
print('이름은 {0}, 나이는 {1}'.format('한국인', 33))
print('이름은 {}, 나이는 {}'.format('신선해', 33))
print('이름은 {1}, 나이는 {0}'.format(34, '강나루'))

print(divmod(14,3))
print(14//3)
print(14%3)



















