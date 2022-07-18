# numpy 배열은 c 배열을 이용한 파이썬 객체

import numpy as np

ss = [1, 2.5, True, 'tom']
print(ss, type(ss))

# numpy의 배열로 변환 : 같은 type 자료로만 구성
ss2 = np.array(ss)
print(ss2, type(ss2))   # class 'numpy.ndarray'

# 메모리 비교(list vs ndarray)
li = list(range(1, 10))
print(li)
print(id(li), id(li[0]), id(li[1]))
print(li * 10)  # li 요소를 10번 반복해~
print('~~'*10)

# li 요소와 각각 10을 곱한 결과를 얻고 싶다면 for
for i in li:
    print(i*10, end=' ')
print() 
print([i*10 for i in li])   # 콤마 있음

print('---1차원 배열 : vector-------------')
num_arr = np.array(li)
print(id(num_arr), id(num_arr[0]), id(num_arr[1]))
print(num_arr*10)   # 콤마 없음
print('-----------------------')
a=np.array([1,2,3])     # 상위 type int-> float -> complex -> str
print(a)
print(type(a), a.dtype, a.shape, a.ndim, a.size)
print(a[0], a[1], a[2])
a[0]=5
print(a)

print('---2차원 배열 : matrix-------------')
b=np.array([[1,2,3],[4,5,6]]) 
print(b)
print(type(b), b.dtype, b.shape, b.ndim, b.size)
print(b[0,0], b[0,1], b[1,0])
print(b[[0]])
print(b[[0]].flatten()) # 차원 축소
print(b[[0]].ravel())   # 차원 축소

print()
c=np.zeros((2, 3))
print(c)

d=np.ones((2, 3))
print(d)

e=np.full((2, 3), 7)
print(e)

f=np.eye(3)
print(f)

print()
print(np.random.rand(5), np.mean(np.random.rand(50)))  # 균등분포
print(np.random.randn(5), np.mean(np.random.randn(50)))# 정규분포
print(np.random.normal(0,1,(2,3)))

np.random.seed(0)
x1 = np.random.randint(10, size=6)
x2 = np.random.randint(10, size=(3,4))
x3 = np.random.randint(10, size=(3,4,5))
print(x1, x1.ndim, x1.size)
print(x2, x2.ndim, x2.size)
print(x3, x3.ndim, x3.size)

print('------------------------------')
a=np.array([1,2,3,4,5])
print(a[1])
print(a[1:5:2])
print(a[1:])
print(a[-2:])

b = a   # 주소 치환
b[0]=77
print(a)
print(b)
del b

c=np.copy(a)    # 복사본
c[0]=88
print(a)
print(c)
del c
# print(c)
print()

a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(a)
print(a[0]) # vector [1 2 3 4]
print(a[0,0])   # scalar 1
print(a[[0]])   # matrix [[1 2 3 4]]
print(a[1:, 0:2])

# sub array
print()
print(a)

b=a[:2, 1:3]
print(b)
print(b[0,0])
b[0,0]=99
print(b)
print(a)













