# 자연어 처리
# 용어 : copus, sentense, document, token, vocab....
# 기존적인 과제는 '어떻게 자연어를 컴퓨터가 인식할 수 있도록 하는가?' 이다.
# 단어표현(Word Representation)이란 분야를 통해 문제를 해결할 수 있다.
# 워드임베딩(희소표현, 밀집표현), 카운트 기반, 예측모델.....

# 워드임베딩(단어를 벡터로 표현)

# 데이터 인코딩 : 카테고리컬 인코딩(레이블 인코딩, 원핫 인코딩)
print('---레이블 인코딩---')
# for
datas = ['python', 'lan', 'program', 'computer', 'say']
print(datas)

values = []
for x in range(len(datas)):
    values.append(x)
    
print(values, ' ', type(values))

print('--원핫 인코딩----')

# numpy
import numpy as np
onehot = np.eye(len(datas))
print(onehot, ' ', type(onehot))

print('--레이블 인코딩(클래스)---')
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder().fit(datas)
values = encoder.transform(datas)
print(values, ' ', type(values))    # [3 1 2 0 4]
print(encoder.classes_) # ['computer' 'lan' 'program' 'python' 'say']

print('--원핫 인코딩(클래스)---')
from sklearn.preprocessing import OneHotEncoder
labels = values.reshape(-1, 1)
print(labels, ' ', labels.shape)
onehot = OneHotEncoder().fit(labels)
onehotValues = onehot.transform(labels) 
print(onehotValues.toarray())

print('---------')
import pandas as pd
df = pd.DataFrame({'datas':['python', 'lan','program', 'computer', 'say']})
print(df)
print(pd.get_dummies(df))


# 참고 : 케라스의 Embedding 레이어는 처음에 무작위로 초기화된 상태에서 정수로 오는 word를 정해진 크기의 벡터로 바꿔서 다음 레이어로 넘기고,
# 학습단계에서는 역전파되는 기울기를 바탕으로 해당 word의 임베딩 값을 조정한다. 즉 주변 문맥을 반영하지 않는다. 
# 그럼 Dense레이어랑  같은거 아닌가 싶지만  차이점은 원핫벡터로 값을 안넣어줘도 되서 덕분에 메모리 절약할 수 있고, 
# 케라스에서 지원하는 masking 기능을 사용할 수 있고, 꼭 문장뿐만아니라 추천 시스템 등에서 User 등을 벡터로 나타낼 때도 사용할 수 있다.
# 하지만 웬만하면 weights 지정 기능을 이용해서 pre-trained 된 word2vec 등을 지정해야 할 것이다.

from keras.layers import Embedding
text=[['Hope', 'to', 'see', 'you', 'soon'], ['Nice', 'to', 'see', 'you', 'again']]
text=[[0, 1, 2, 3, 4],[5, 1, 2, 3, 6]]     # 각 단어에 대한 정수 인코딩
# 위 데이터가 임베딩 층의 입력이 된다.

emb=Embedding(7, 2, input_length=5)
# 7은 단어의 개수. 즉, 단어 집합(vocabulary)의 크기이며, 2는 임베딩한 후의 벡터의 크기.
# 2는 임베딩 벡터의 출력 차원. 결과로서 나오는 임베딩 벡터의 크기
# input_length=5는 각 입력 시퀀스의 길이.
# 각 정수는 아래의 테이블의 인덱스로 사용되며 Embeddig()은 각 단어에 대해 임베딩 벡터를 리턴한다.
import numpy as np
print(emb(np.array(text)))

print('word2vec : 단어의 의미를 다차원 공간에 실수로 벡터화하는 분산표현 기법. 단어 간 유사성을 표현 가능')
from gensim.models import word2vec

sentence = [['python', 'lan','program', 'computer', 'say']]
model = word2vec.Word2Vec(sentences=sentence, min_count=1, vector_size=50)
print(model)
word_vectors = model.wv     # 단어 벡터 생성
print('word_vectors : ', word_vectors)

print('key_to_index : ', word_vectors.key_to_index)
print('key_to_index keys : ', word_vectors.key_to_index.keys())

vocabs = word_vectors.key_to_index.keys()
word_vector_list = [word_vectors[v] for v in vocabs]
print(word_vector_list[0], len(word_vector_list[0]))

# 단어간 유사도를 확인
print(word_vectors.similarity(w1='python', w2='computer'))
print(word_vectors.similarity(w1='python', w2='say'))
print(word_vectors.most_similar(positive='computer'))

# 시각화
import matplotlib.pyplot as plt
def plt_func(vocabs, x, y):
    plt.figure(figsize=(8,6))
    plt.scatter(x, y)
    for i, v in enumerate(vocabs):
        plt.annotate(v, xy=(x[i], y[i]))

from sklearn.decomposition import PCA
pca = PCA(n_components = 2)
xys = pca.fit_transform(word_vector_list)
xs = xys[:, 0]
ys = xys[:, 1]
# print(xs)   # [ 0.02605113 -0.01793008 -0.03214882  0.06832034 -0.04429257]
plt_func(vocabs, xs, ys)
plt.show()




