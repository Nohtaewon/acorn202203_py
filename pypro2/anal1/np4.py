# 배열에 행 이나 열 추가 
import numpy as np

aa=np.eye(3)    # 3 by 3 단위행렬 생성
print(aa)

bb=np.c_[aa, aa[2]]     # 2열과 같은 열 추가
print(bb)

cc=np.r_[aa, [aa[2]]]     # 2행과 같은 행 추가
print(cc)

print()     # 행을 열로 변환
a=np.array([1,2,3])     # 1행 3열
print(np.c_[a])     # 3행 1열
print(a.reshape(3,1))   # 3행 1열

print('----------배열 요소 값 append, insert, delete------------------------')
print(a)    # 1차원
b=np.append(a, [4,5])   # 행기준
print(b)
c=np.insert(a, 0, [6,7])   #
print(c)
d=np.delete(a, [1])   # delete(a, 1)
print(d)

print()
aa=np.arange(1,10).reshape(3,3)
bb=np.arange(10,19).reshape(3,3)
print(aa)
print(bb)    # 2차원

cc=np.append(aa,bb) # axis를 지정하지 않으면 2차원배열이 1차원 배열이 됨
print(cc)

cc=np.append(aa,bb, axis=0) # 행방향 배열 쌓기
print(cc)
cc=np.append(aa,bb, axis=1) # 행방향 배열 쌓기
print(cc)

print()
print(np.delete(aa, 1))     # aa 배열을 1차원으로 변환 후 1번 인덱스 값 삭제
print(np.delete(aa, 1, axis=0))     # 1번 인덱스인 행을 삭제
print(np.delete(aa, 1, axis=1))     # 1번 인덱스인 열을 삭제
















