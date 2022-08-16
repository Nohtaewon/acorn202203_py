# MLP : 다충 신경만 - 여러 개의 노드를 겹쳐서 신경망을 구성
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

feature = np.array([[0,0], [0,1], [1,0], [1,1]])
print(feature)
# label = np.array([0,0,0,1]) # and
# label = np.array([0,1,1,1]) # or
label = np.array([0,1,1,0]) # xor

# MLP로 xor 문제를 해결
ml = MLPClassifier(hidden_layer_sizes=3, solver='adam', learning_rate_init=0.01)
ml.fit(feature, label)

pred = ml.predict(feature)
print('pred:',pred)
print('acc:', accuracy_score(label, pred))



















