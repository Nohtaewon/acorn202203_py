# 내가 그린 숫자 이미지 판정하기
from PIL import Image   # 이미지 확대/축소 기능
import numpy as np
import matplotlib.pyplot as plt

im = Image.open('num.png')
img = np.array(im.resize((28,28), Image.ANTIALIAS).convert('L'))
print(img)
plt.imshow(img, cmap='Greys')
plt.show()

# 이미지 분류 판정
data = img.reshape([1, 784])
print(data)
data = data / 255.0
print(data)

import tensorflow as tf
mymodel = tf.keras.models.load_model('tf11.hdf5')
pred = mymodel.predict(data)
print('결과:', np.argmax(pred, 1))

















