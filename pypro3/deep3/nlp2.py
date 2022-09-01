# 다음 제공 뉴스 문서를 읽어 형태소 분석 후 word2vec을 이용해 단어 간 유사도 확인
# 코사인 유사도 사용 : 두 벡터(단어)가 가까울수록 절대값 1에 근사함
import pandas as pd
from konlpy.tag import Okt

okt = Okt()

with open('news.txt', mode='r', encoding='utf-8') as obj:
    lines = obj.read().split('\n')
    
print(lines, len(lines))

wordDic = {}    # 명사만 추출해 단어 수 확인 
for line in lines:
    datas = okt.pos(line)   # 품사 태깅
    # print(datas)
    for word in datas:
        if word[1] == 'Noun':
            if len(word[0]) > 1:
                if not(word[0] in wordDic):
                    wordDic[word[0]] = 1
                
                wordDic[word[0]] += 1

print(wordDic)    

# 결과를 파일로 저장
fileName = 'daumnews.txt'
with open(fileName, mode='w', encoding='utf-8') as obj2:
    obj2.write('\n'.join(wordDic))

# 단어 건수별 내림차순
keys = sorted(wordDic.items(), key=lambda x : x[1], reverse = True)
print(keys)
# DataFrame에 담기 : 단어, 건수
wordList= []
countList= []
for word, count in keys[:30]:
    wordList.append(word)
    countList.append(count)

df = pd.DataFrame()
df['word']=wordList
df['count']=countList
print(df.head(3))

print('----------------------')
results = []

with open('news.txt', mode='r', encoding='utf-8') as obj:
    lines = obj.read().split('\n')
    
    for line in lines:
        datas = okt.pos(line, stem=True)    # 원형 어근으로 출력
        print(datas)
        
        imsi = []
        for word in datas:
            if not word[1] in ['Number', 'Josa', 'Foreign', 'Puctuation', 'Alpha', 'Suffix', 'Determiner']:
                if len(word[0]) >=2:
                    imsi.append(word[0])
                    
        imsi2 = (" ".join(imsi)).strip()
        results.append(imsi2)
        
print(results)

# 결과를 파일로 저장
fileName2 = 'daumnews2.txt'
with open(fileName, mode='w', encoding='utf-8') as obj2:
    obj2.write('\n'.join(results))

print('word2vec으로 밀집벡터를 만들어 단어 간 유사도 확인')
from gensim.models import word2vec

lineObj = word2vec.LineSentence(fileName2)  # 텍스트파일을 word2vec 형식으로 읽기
print(lineObj)

model = word2vec.Word2Vec(sentences=lineObj, vector_size=100, window=10, min_count=1, sg=1)
# sg=0 : CBOW - 주변단어로 중심단어 예측, sg=1 : Skip-Gram : 중심단어로 주변단어 예측 window=10 주변단어는 앞뒤로 10개 참조
# model.init_sims(replace = True)     # 필요없는 메모리 해제

# positive : 단어 사전에 해당 단어가 있을 확률. 가까운 단어 찾음
# negative : 단어 사전에 해당 단어가 없을 확률. 먼 단어 찾음
print(model.wv.most_similar(positive=['태풍']))
print(model.wv.most_similar(positive=['태풍'], topn=3))
print(model.wv.most_similar(positive=['태풍', '경로'], topn=3))
print(model.wv.most_similar(positive=['태풍']))
















