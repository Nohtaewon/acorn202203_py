# 선형회귀 모형을 수식으로 작성해보기
import tensorflow as tf
import numpy as np
opti = tf.keras.optimizers.SGD()

tf.random.set_seed(2)
w = tf.Variable(tf.random.normal((1,)))
b = tf.Variable(tf.random.normal((1,)))
print(w.numpy(), b.numpy())

# 모델 학습방법 1) keras의 내장 API를 사용
# 모델 학습방법 2) GradientTape 객체를 사용해 직접 구현 : 복잡한 로직을 구현할 수 있다.
# 자동미분을 하기 위해 필요한 함수와 계산 식의 연산 과정과 입력값에 대한 정보가 즉시실행모드에서는 없기 때문입니다.
# tensorflow 는 중간 연산 과정(함수, 연산)을 테이플(tape)에 차곡차곡 기록해주는 Gradient tapes를 제공
@tf.function
def train_step(x,y):
    with tf.GradientTape() as tape:
        hypo = tf.add(tf.multiply(w, x), b) # y = wx +b
        # 예측값 - 실제값의 제곱의 합을 전체 수로 나누기
        loss = tf.reduce_mean(tf.square(tf.subtract(hypo, y)))
    grad = tape.gradient(loss, [w, b])  # 자동 미분
    opti.apply_gradients(zip(grad, [w,b]))  # 경사하강법 실행
    return loss

x = [1., 2., 3., 4., 5.]
y = [1.2, 2.0, 3.0, 3.5, 5.5]
print(np.corrcoef(x, y))

w_val = []  # 가중치(w)의 변화값
cost_val = []   # cost의 변화값

for i in range(1, 101):    # 학습
    loss_val = train_step(x, y)
    cost_val.append(loss_val.numpy())
    w_val.append(w.numpy())
    if i%10 == 0:
        print(loss_val)

print('cost(loss):', cost_val)
print('w_val:', w_val)

import matplotlib.pyplot as plt
plt.plot(w_val, cost_val, 'o--')
plt.xlabel('w')
plt.xlabel('cost')
plt.show()

print('cost가 최소일때 w:', w.numpy())
print('cost가 최소일때 b:', b.numpy())

# 수식 얻기  y= wx+b
# y=0.9893332x+0.08461335
pred = tf.multiply(x, w)+b
print('예측값:', pred.numpy())
print('실제값:', y)

plt.plot(x, y, 'o', label='real')
plt.plot(x, pred, 'b-', label='pred')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()


# 미지의 새 값으로 예측
new_x = [3.5, 9.0]
new_pred = tf.multiply(new_x, w)+b
print('새 예측값:', new_pred.numpy())









