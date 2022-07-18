# 배열에서 조건 연산 where(조건, 참, 거짓)
import numpy as np

x=np.array([1,2,3])
y=np.array([4,5,6])
conditionData=np.array([True, False, True])
result=np.where(conditionData, x, y)
print(result)

print()
aa=np.where(x >= 2)
print(aa)
print(np.where(x >= 2, 'T', 'F'))
print(np.where(x >= 2, x, x+100))

print()
bb=np.random.randn(4, 4)
print(bb)
print(np.where(bb > 0, 2, bb))

print() # 배열 결합
kbs=np.concatenate([x, y])
print(kbs)

print() # 배열 분할
x1, x2 = np.split(kbs, 2)
print(x1)
print(x2)

print()
a = np.arange(1, 17).reshape(4, 4)
print(a)
x1, x2 = np.hsplit(a, 2)
print(x1)
print(x2)
x1, x2 = np.vsplit(a, 2)
print(x1)
print(x2)

# 표본 추출(sampling)
# 복원 / 비복원 추출

li=np.array([1,2,3,4,5,6,7])

# 복원 추출
for _ in range(5):
    print(li[np.random.randint(0, len(li) - 1)], end = ' ') 

print()
import random
# 비복원 추출 통계는 비복원이 기본 값
print(random.sample(list(li), k=5))
print()
print(random.sample(range(1, 46), k=6))

# 복원 추출
print()
print(list(np.random.choice(range(1, 46), 6)))
print(list(np.random.choice(range(1, 46), 6, replace=True)))
# 비복원 추출
print(list(np.random.choice(range(1, 46), 6, replace=False)))

# 가중치를 부여한 random 추출
ar = 'air book cat d e f god'
ar = ar.split(' ')
print(ar)
print(np.random.choice(ar, 3, p=[0.1,0.1,0.1,0.1,0.1,0.1,0.4]))     # 선택 확률

print('-Quiz1----------------------------------------------------')
step1=np.random.randn(5, 4)
print(step1)
print('1행 합계:', np.sum(step1, axis=1)[0])
print('1행 최댓값:', np.max(step1, axis=1)[0])
print('2행 합계:', np.sum(step1, axis=1)[1])
print('2행 최댓값:', np.max(step1, axis=1)[1])
print('3행 합계:', np.sum(step1, axis=1)[2])
print('3행 최댓값:', np.max(step1, axis=1)[2])

print('-Quiz2----------------------------------------------------')
step2=np.zeros((6, 6))
print(step2)
cnt=0
for i in range(6):
    for j in range(6):
        cnt+=1
        step2[i, j]=cnt
        
print(step2)
print(step2[1,:])
print(step2[:,4])
print(step2[2:5,2:5])
print('-Quiz3----------------------------------------------------')
step3=np.zeros([6,4])
print(step3)
ran=np.random.randint(20, 100, 6)
ran=list(ran)
print(ran)

for r in range(len(step3)):
    num = ran.pop(0)
    for c in range(len(step3[0])):
        step3[r][c] = num
        num += 1
print(step3)
print()
step3[0,:]=1000
step3[-1,:]=6000
print(step3)
print('-Quiz4----------------------------------------------------')
step4=np.random.randn(4, 5)
print(step4)
print('평균:', np.mean(step4))
print('합계:', np.sum(step4))
print('표준편차:', np.std(step4))
print('분산:', np.var(step4))
print('최댓값:', np.max(step4))
print('최솟값:', np.min(step4))
print('1사분위수:', np.percentile(step4, 25))
print('2사분위수:', np.percentile(step4, 50))
print('3사분위수:', np.percentile(step4, 75))
print('요소값 누적합:', np.cumsum(step4))














