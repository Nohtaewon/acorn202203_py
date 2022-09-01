# CountVectorizer : 각 텍스트에서 단어 출현 횟수를 카운팅한 벡터
# 단위별 등장횟수를 카운팅하여 수치벡터(BOW)화 한다.
# 단위 : 문서단위, 문장단위, 단어단위, 글자단위, 자소단위....
# TfidfVectorizer : TF-IDF라는 값을 사용하여 CountVectorizer의 단점을 보완함

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

print('------CountVectorizer------------')
text_data = ['나는 배 고프다 아니 배가 고프다.', '내일 점심 뭐 먹지?', '내일 공부 해야겠다', '점심 먹고 공부 해야지']
count_vec = CountVectorizer()
count_vec.fit(text_data)    # 단어 사전 생성, 한 글자 짜리는 제외
print(count_vec.get_feature_names_out())
print(count_vec.vocabulary_)

# transform()을 사용해 BOW 생성
print(text_data[0])
sentence = [text_data[0]]
print(count_vec.transform(sentence))
print(count_vec.transform(sentence).toarray())

sentence2 = ['나는 공부 이건 점심 먹고 공부 해야 배가 부르다 라고 생각한다']
print(count_vec.transform(sentence2).toarray())
print(count_vec.transform(sentence2).toarray().sum(axis=1))
# 단점 : 의미없는 단어가 많이 발생할 경우 좋지 않은 결과가 나올 수 있다.

print()
# 한글의 경우는 어간 추출을 하는 것을 추천
from konlpy.tag import Okt

okt = Okt()

my_words = []
for i, doc in enumerate(text_data):
    for word in okt.pos(doc, stem = True):  # 어간 추출
        # print(word)
        if word[1] in ['Noun', 'Verb', 'Adjective']:
            my_words.append(word[0])
            
print(my_words)

count_vec2 = CountVectorizer(analyzer='word')
count_vec2.fit(my_words)
print(count_vec2.get_feature_names_out())
print(count_vec2.vocabulary_)


print('\n\n------TfidfVectorizer------------')
text_data = ['나는 배 고프다 아니 배가 고프다.', '내일 점심 뭐 먹지?', '내일 공부 해야겠다', '점심 먹고 공부 해야지']
tfidf_vec = TfidfVectorizer()
tfidf_vec.fit(text_data)    # 단어 사전 생성, 한 글자 짜리는 제외
print(tfidf_vec.get_feature_names_out())
print(tfidf_vec.vocabulary_)
print()
print(tfidf_vec.transform(text_data).toarray())

print()
sentence = [text_data[3]]
print(tfidf_vec.transform(sentence))
print(tfidf_vec.transform(sentence).toarray())

# 빈도에 단수 횟수를 이용하는 것보다 각 단어의 특성을 좀 더 잘 반영할 수 있다.










