# 배열 연산 : 기본적인 수학함수는 배열에 요소별로 적용

import numpy as np

x = np.array([[1,2],[3,4]], dtype=np.float32)
y = np.arange(5,9).reshape((2,2))
y = y.astype(np.float32)
print(x, x.dtype)
print(y, y.dtype)

print()
print(x + y)    # 요소별 합
print(np.add(x, y))

print()
print(x - y)    # 요소별 차
print(np.subtract(x, y))

print()
print(x * y)    # 요소별 곱
print(np.multiply(x, y))

print()
print(x / y)    # 요소별 나누기
print(np.divide(x, y))

print('행렬곱 : 내적')
v = np.array([9,10])    # vector
w = np.array([11, 12])
print(v * w)    # 요소별 곱셈 9*11, 10*12
print(v.dot(w)) # 1차원 벡터에 행렬곱(내적)을 하면 결과는 scalar 가 됨
print(np.dot(v, w))     # v[0]*w[0]+v[1]*w[1]

print()
print(x)
print(v)
print(x*v)  # 요소별 곱. 결과는 큰 차원을 따름
print(x.dot(v)) # 행렬곱(내적). 낮은 차원을 따름
# x[0,0]*v[0]+x[0,1]*v[0]=29, x[1,0]*v[0]+x[1,1]*v[0]=67
print(np.dot(x, v))
print()

print(x)
print(y)
print(x.dot(y))
# x[0,0]*y[0,0]+x[0,1]*y[1,0]=19
# x[0,0]*y[0,1]+x[0,1]*y[1,1]=22
# x[1,0]*y[0,0]+x[1,1]*y[1,0]=43

print(np.dot(x,y))

print()
print(x)
print(np.sum(x))
print(np.sum(x, axis=0))    # 열방향 연산
print(np.sum(x, axis=1))    # 행방향 연산

print(np.mean(x))
print(np.argmax(x))
print(np.cumsum(x)) # 누적합

print(x)
print(x.T)  # 전치
print(x.transpose())
print(x.swapaxes(0,1))

# Broadcasting 연산 : 크기가 다른 배열간의 연산
# 작은 배열과 큰 배열이 연산할 경우 작은 배열이 큰 배열의 크기만큼 연산에 반복적으로 참여
x = np.arange(1, 10).reshape(3,3)
y = np.array([1,2,3])
z = np.empty_like(x)
print(x)
print(y)
# print(z)

# x와 y간 더하기 연산
for i in range(3):
    z[i] = x[i]+y

print(z)

kbs = x+y
print(kbs)




