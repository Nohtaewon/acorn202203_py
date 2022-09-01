# 네이버 영화 리뷰 데이터로 밀집표현(word2vec) 수행 후 단어 유사도 확인
import pandas as pd
import matplotlib.pyplot as plt
import urllib.request
from gensim.models.word2vec import Word2Vec
from konlpy.tag import Okt
"""
urllib.request.urlretrieve(url="https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/ratings.txt",
                            filename='rating.txt')
"""

train_data = pd.read_table('rating.txt')
print(train_data.head(3), train_data.shape) # (10295, 3)
print(train_data.isnull().any())    # label True
print(train_data.info())
print(train_data[train_data['label'].isnull()])
train_data = train_data.dropna(how='any')
print(train_data.shape)     # (10293, 3)
print(train_data.head(5))

# 정규표현식을 통해 필요없는 글자 제거
train_data['document'] = train_data['document'].str.replace("[^가-힣 ]","")
print(train_data.head(5))

# 불용어(stop words) : 의미가 없는 단어 token. 조사, 접미사 등
stopwords = ['을', '를', '으로', '은', '는', '들', '과', '와', '에', '한', '하다', '라고', '고', '이']

# 토큰 작업
okt = Okt()
tokenized_data = []
for sentence in train_data['document']:
    tmp = okt.morphs(sentence, stem=True)
    tmp = [word for word in tmp if not word in stopwords]   # 불용어 제거
    tokenized_data.append(tmp)

print(tokenized_data)












