# CountVectorizer : 각 텍스트에서 단어 출현 횟수를 카운팅한 벡터
# 단위별 등장횟수를 카운팅하여 수치벡터(BOW)화 한다.
# 단위 : 문서단위, 문장단위, 단어단위, 글자단위, 자소단위....
# TfidfVectorizer : TF-IDF라는 값을 사용하여 CountVectorizer의 단점을 보완함
# TF(Term Frequency) : 특정 단어가 하나의 데이터 안에서 등장하는 횟수
# DF(Document Frequency) : 특정 단어가 여러 데이터에 자주 등장하는지를 알려주는 지표.
# IDF(Inverse Document Frequency) : DF에 역수를 취해(inverse) 구함
# TF-IDF : TF와 IDF를 곱한 값. 즉 TF가 높고, DF가 낮을수록 값이 커지는 것을 이용하는 것입니다.
#     조금 더 풀어 설명하자면, 해당 단위(문장) 안에서는 많이 등장하지만, 
#     다른 문서들까지 전체에서는 적게 사용될수록 분별력 있는 특징이란 것입니다.

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

content = ['How to format my hard disk', 'hard disk format format problems']

count_vec = CountVectorizer(analyzer='word', min_df = 1)
print(count_vec)

tran = count_vec.fit_transform(raw_documents=content)   # 수치벡터(BOW)화
print(tran)
print(count_vec.get_feature_names())
print(tran.toarray())
# ['disk', 'format', 'hard', 'how', 'my', 'problems', 'to']
#    0        1        2       3     4        5         6

print('------TfidfVectorizer------------')
# 문서에서 자주 나오는 단어에 대해 높은 가중치를 주되, 모든 문서에서 자주 나타나는 단어에 대해서는 패널티를 주는 방식.
tfidf_vec = TfidfVectorizer(analyzer='word', min_df = 1)
print(tfidf_vec)
tran_idf = tfidf_vec.fit_transform(raw_documents=content)   # 수치벡터화
print(tran_idf)
print(tfidf_vec.get_feature_names())
print(tran_idf.toarray())

















