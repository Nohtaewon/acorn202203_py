import pandas as pd

# DtypeWarning : 열 (2,36,37)에 혼합 유형이 있다. 가져 오기의 경우에 dtype 옵션을 지정하거나 low_memory = False를 설정.
data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/movies_metadata.csv", encoding = 'ISO-8859-1', low_memory=False)
print(data.head(2))       # [2 rows x 45 columns]
data=data.head(20000)
print(data['overview'].isnull().sum())  # 135
data['overview'] = data['overview'].fillna('')    # overview에서 Null 값을 가진 경우에는 값 제거

# 이제 tf-idf를 수행
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(data['overview'])

# overview에 대해서 tf-idf 수행
print(tfidf_matrix.shape)  # (20000, 47181)

# overview 열에 대해서 tf-idf를 수행했다. 20,000개의 영화를 표현하기 위해 총 47,487개의 단어가 사용되었음을 보여주고 있다. 이제 코사인 유사도를 사용하면 바로 문서의 유사도를 구할 수 있다.
from sklearn.metrics.pairwise import linear_kernel
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)  # 코사인 유사도
indices = pd.Series(data.index, index=data['title']).drop_duplicates()
print(indices.head())

# 이 테이블의 용도는 영화의 타이틀을 입력하면 인덱스를 리턴하기 위함.
idx = indices['Father of the Bride Part II']
print(idx)   # 4

# 이제 선택한 영화에 대해서 코사인 유사도를 이용하여, 가장 overview가 유사한 10개의 영화를 찾아내는 함수를 만든다.
def get_recommendations(title, cosine_sim=cosine_sim):

    # 선택한 영화의 타이틀로부터 해당되는 인덱스를 받아옵니다. 이제 선택한 영화를 가지고 연산할 수 있다.
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))  # 모든 영화에 대해서 해당 영화와의 유사도를 구한다.
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)  # 유사도에 따라 영화들을 정렬
    sim_scores = sim_scores[1:11]                   # 가장 유사한 10개의 영화를 받아온다.
    movie_indices = [i[0] for i in sim_scores]     # 가장 유사한 10개의 영화의 인덱스를 받아온다.
    return data['title'].iloc[movie_indices]           # 가장 유사한 10개의 영화의 제목을 리턴

# 영화 다크 나이트 라이즈와 overview가 유사한 영화들을 찾아보겠다.
print(get_recommendations('The Dark Knight Rises'))

# 가장 유사한 영화가 출력되는데, 영화 다크 나이트가 첫번째고, 그 외에도 전부 배트맨 영화를 찾아낸 것을 확인할 수 있다.