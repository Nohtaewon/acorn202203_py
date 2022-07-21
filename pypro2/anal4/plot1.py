# 시각화 : matplotlib 라이브러리를 사용
# figure : 그래프(차트)가 그려지는 영역

import numpy as np
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')      # 한글 깨질때
plt.rcParams['axes.unicode_minus']=False    # 음수 깨질때
"""
x= ['서울','인천','수원']     # set X
y= [5,3,7]
plt.xlim([-1,3])
plt.ylim([0, 10])
plt.yticks(list(range(0,11,3)))
plt.plot(x,y)
plt.show()
"""
"""
data=np.arange(1,11,2)
print(data)
plt.plot(data)
x=[0,1,2,3,4]
for a, b in zip(x, data):
    plt.text(a,b,str(b))
plt.show()
"""
"""
x=np.arange(10)
y=np.sin(x)
print(x, y)
# plt.plot(x,y,'bo')
# plt.plot(x,y,'r+')    # + , - , -- , -. 
plt.plot(x,y,'r-.', linewidth=3, markersize=12)
plt.show()
"""
"""
# hold : 하나의 Figure 내에 plot을 복수로 표현
x=np.arange(0, np.pi*3, 0.1)
y_sin=np.sin(x)
y_cos=np.cos(x)
plt.figure(figsize=(10, 5))
plt.plot(x, y_sin, color='r')   # 선그래프
plt.scatter(x, y_cos, color='b')    # 산점(포)도
plt.xlabel('x축')
plt.ylabel('사인&코사인')
plt.legend(['sine','cosine'])
plt.show()
"""
"""
# subplot : figure 영역을 여러 개로 분할
x=np.arange(10)
y=np.sin(x)

plt.subplot(2,1,1)
plt.plot(x)
plt.title('첫번째')

plt.subplot(2,1,2)
plt.plot(y)
plt.title('두번째')
plt.show()
"""

irum=['a','b','c','d','e']
kor=[80,50,70,70,90]
eng=[60,20,80,70,50]
plt.plot(irum, kor, 'ro-')
plt.plot(irum, eng, 'bs--')
plt.ylim([0, 100])
plt.title('시험점수')
plt.legend(['국어','영어'], loc=1)  # loc 는 사분면에 위치
plt.grid(True)

# 차트를 이미지로 저장
fig=plt.gcf()
plt.show()
fig.savefig('test.png')

# 이미지 파일 읽기
from matplotlib.pyplot import imread
img = imread('test.png')
plt.imshow(img)
plt.show()





