print('Q1----------------------------------------')
a=80
b=75
c=55
print((a+b+c)/3)
print('Q2----------------------------------------')
a=13
print(13%2)
print('Q3----------------------------------------')
pin="881120-1068234"
yyyymmdd=pin[:6]
num=pin[7:]
print(yyyymmdd)
print(num)
print('Q4----------------------------------------')
pin="881120-1068234"
print(pin[7])
print('Q5----------------------------------------')
a="a:b:c:d"
b=a.replace(':', '#')
print(b)
print('Q6---------------------------------------')
a=[1,3,5,4,2]
a.sort()
a.reverse()
print(a)
print('Q7----------------------------------------')
a=['Life', 'is', 'too', 'short']
result=' '.join(a)
print(result)
print('Q8----------------------------------------')
a=(1,2,3)
a=a+(4,)
print(a)
print('Q9----------------------------------------')
a=dict()
a['name']='python'
print(a)
a[('a',)]='python'
print(a)
# a[[1]]='python' 변하는 값을 사용할 수 없음 [1] 은 list 로 변하는 값
print(a)
a[250]='python'
print(a)
print('Q10----------------------------------------')
a={'A':90, 'B':80, 'C':70}
result=a.pop('B')
print(a)
print(result)
print('Q11----------------------------------------')
a=[1,1,1,2,2,3,3,3,4,4,5]
aSet=set(a)
b=list(aSet)
print(b)
print('Q12----------------------------------------')
# 동일한 객체 가리킴
a=b=[1,2,3]
a[1]=4
print(b)
















