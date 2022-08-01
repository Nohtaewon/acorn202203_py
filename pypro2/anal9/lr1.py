# 선형회귀식 얻기
# 최소제곱법으로 최적의 추세선을 구할 수 있는 기울기와 절편을 얻는다.
# 직접 수식을 쓸 수 있으나 numpy의 최소제곱 해 얻기 함수 사용. lstsq(array like, array like, rcond....)

import numpy as np
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')
import numpy.linalg as lin

x = np.array([0,1,2,3])
y = np.array([-1, 0.2, 0.5, 2.1])

# plt.scatter(x, y)
# plt.xlabel('x축값')
# plt.ylabel('y축값')
# plt.show() 

A = np.vstack([x, np.ones(shape=len(x))]).T
print(A)    # lstsq() 가 2차원 배열을 원하므로 


w, b = lin.lstsq(A, y, rcond=None)[0] # 최소제곱법
print(w, b)     # w(기울기, slope):0.9599999999999999 b(y절편, bias):-0.9899999999999995
# 수식(모델) 완성 : y = 0.9599 * x + -0.9899

print(0.9599 * 0 + -0.9899)
print(0.9599 * 1 + -0.9899)
print(0.9599 * 2 + -0.9899)
print(0.9599 * 3 + -0.9899)
plt.scatter(x, y, label='실제값')
plt.plot(x, w*x+b, 'r', label='최적화된 선형직선')  # 실제값 , 추세선에의한 예측값
plt.xlabel('x축값')
plt.ylabel('y축값')
plt.legend()
plt.show() 


