# naver 제공 영화 5편의 평점을 읽어 영화 간 유사도 출력
from bs4 import BeautifulSoup
import requests
from konlpy.tag import Okt
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

def movie_scrap(url):
    result = []
    for p in range(1, 11):
        r = requests.get(url + "&page="+str(p))
        # print(r)
        soup = BeautifulSoup(r.content, 'lxml', from_encoding='ms949')
        # print(soup)
        title = soup.find_all("td", {"class":"title"})
        # print(title[0].text)
        sub_result = []
        for i in range(len(title)):
            sub_result.append(title[i].text
                              .replace('\r','')
                              .replace('\n','')
                              .replace('\t','')
                              .replace('별점 - 총 10점 중','')
                              .replace('신고','')
                              .replace('육사오(6/45)', '')
                              .replace('한산: 용의 출현', '')
                              .replace('우리들', '')
                              .replace('서울대작전', '')
                              .replace('헌트', '')
                              .replace('영화', '')
                              .replace('추천',''))
                
            
        result = result + sub_result
        
    return("".join(result))

six = movie_scrap("https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=204640&target=after")
hansan = movie_scrap("https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=194196&target=after")
woori = movie_scrap("https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=146504&target=after")
seoul = movie_scrap("https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=206591&target=after")
hunt = movie_scrap("https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=195758&target=after")

movies = [six, hansan, woori, seoul, hunt]

import time
time.sleep(2)

print(movies)

print('---------------------------------')
okt = Okt()

# 형태소 분석 : 명사, 형용사만 얻기
def word_sep(movies):
    result = []
    for m in movies:
        words = okt.pos(m)
        one_result = []
        for word in words:
            if word[1] in ['Noun', 'Adjective'] and len(word[0]) >= 2:
                one_result.append(word[0])
        result.append(" ".join(one_result))
    return result

word_list = word_sep(movies)
print(word_list)

# word_list 를 파일로 저장
import pickle

# with open('movie.pickle', 'wb') as fw:
#     pickle.dump(word_list, fw)
    
with open('movie.pickle', 'rb') as fr:
    word_list = pickle.load(fr)
    
print(word_list)

# feature vector(BOW)화 추출 방법1
print('CountVectorizer')
# 문서 집합으로 단어 수를 세어 BOW 벡터를 만듦
count = CountVectorizer(analyzer='word', min_df=2)  # 빈도 수 2미만 무시.
count_vec =count.fit_transform(raw_documents=word_list).toarray()
print(count_vec)

pd.set_option('display.max_columns', 500)
count_df = pd.DataFrame(count_vec, columns=count.get_feature_names())
print(count_df)

# feature vector(BOW)화 추출 방법2
print('TfidfVectorizer')
tfidf = TfidfVectorizer(analyzer='word', min_df=2)  # 빈도 수 2미만 무시.
count_tfidf =tfidf.fit_transform(raw_documents=word_list).toarray()
print(count_tfidf)
count_df2 = pd.DataFrame(count_tfidf, 
                         columns=count.get_feature_names(),
                         index = ['six', 'hansan', 'woori', 'seoul', 'hunt'])
print(count_df2)


print('영화 간 유사도 - 코사인 유사도 사용')
def cosin_func(doc1, doc2):
    bunja = sum(doc1*doc2)
    bunmo = (sum(doc1**2)*sum(doc2**2))**0.5
    return bunja / bunmo

res = np.zeros((5,5))   # 배열 선언

for i in range(5):
    for j in range(5):
        res[i, j] = cosin_func(count_df2.iloc[i], count_df2.iloc[j].values)
        
df = pd.DataFrame(res, index=['six', 'hansan', 'woori', 'seoul', 'hunt'],
                  columns = ['six', 'hansan', 'woori', 'seoul', 'hunt'])

print(df)







