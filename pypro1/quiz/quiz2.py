print('Q1------------------------')
result=0
i=1
while i <=1000:
    if i%3==0:
        result+=i
    i+=1
print(result)
print('Q2------------------------')
i=0
while True:
    i+=1
    if i > 5 :break
    print('*'*i)
print('Q3------------------------')
for i in range(1, 101):
    print(i, end=' ')
print('Q4------------------------')
A=[70,60,55,75,95,90,80,80,85,100]
tot=0
for score in A:
    tot += score
ave=tot/len(A)
print(ave)
print('Q5------------------------')
# [표현식 for 항목 in 반복 가능 객체 if 조건]
numbers=[1,2,3,4,5]
result=[]
for n in numbers:
    if n%2==1:
        result.append(n*2)
result=[n*2 for n in numbers if n%2==1]
print(result)