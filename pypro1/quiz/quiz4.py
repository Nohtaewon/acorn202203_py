print('Q1---------------------------')
a=all([1, 2, abs(-3)-3])
print(a)
b=chr(ord('a'))=='a'
print(b)
print('Q2---------------------------')
li=[1,-2,3,-5,8,-3]
print(list(filter(lambda a:a>0, li)))
print('Q3---------------------------')
# 걸러줌
print(hex(234))
print(int(0xea), 16)
print('Q4---------------------------')
# 수행한 거 돌려줌
print(list(map(lambda a:a*3, [1,2,3,4])))
print('Q5---------------------------')
li=[-8,2,7,5,-3,5,0,1]
print(max(li))
print(min(li))
print('Q6---------------------------')
a=17/3
print(round(a, 4))
print('Q7---------------------------')
import random
result=[]
while len(result)<6:
    a=random.randint(1, 45)
    if a not in result:
        result.append(a)
print(result)















