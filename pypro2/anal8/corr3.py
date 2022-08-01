# 공공데이터 (data.go.kr) 에서 다운로드한 파일 사용
# 서울 유료 관광지에 외국인(미국, 일본, 중국) 방문 데이터로 상관분석 실시

import json
import matplotlib.pyplot as plt
import pandas as pd
plt.rc('font', family='malgun gothic')

# 차트 그리기용 함수
def setScatterFunc(tour_table, all_table, tpoint):
    # print(tpoint)
    # 계산할 관광지명에 해당하는 데이터만 추출해 별도 저장(tour)하고 외국인 자료와 병합
    tour = tour_table[tour_table['resNm'] == tpoint]
    # print(tour)
    merge_table = pd.merge(tour, all_table, left_index=True, right_index=True)
    # print(merge_table[:3])
    
    # 시각화
    fig = plt.figure()
    fig.suptitle(tpoint + '상관관계 분석')
    
    plt.subplot(1, 3, 1)
    plt.xlabel('중국인 입국수')
    plt.ylabel('외국인 입장객수')
    lamb1 = lambda p:merge_table['china'].corr(merge_table['ForNum'])
    r1 = lamb1(merge_table)
    print('r1:',r1)
    plt.title('r={:.5f}'.format(r1))
    plt.scatter(merge_table['china'], merge_table['ForNum'], s=6, c='red')
    
    plt.subplot(1, 3, 2)
    plt.xlabel('일본인 입국수')
    plt.ylabel('외국인 입장객수')
    lamb2 = lambda p:merge_table['japan'].corr(merge_table['ForNum'])
    r2 = lamb2(merge_table)
    print('r2:',r2)
    plt.title('r={:.5f}'.format(r2))
    plt.scatter(merge_table['japan'], merge_table['ForNum'], s=6, c='green')
    
    plt.subplot(1, 3, 3)
    plt.xlabel('미국인 입국수')
    plt.ylabel('외국인 입장객수')
    lamb3 = lambda p:merge_table['usa'].corr(merge_table['ForNum'])
    r3 = lamb3(merge_table)
    print('r3:',r3)
    plt.title('r={:.5f}'.format(r3))
    plt.scatter(merge_table['usa'], merge_table['ForNum'], s=6, c='blue')
        
    plt.tight_layout()  # flot 간격 자동 설정
    plt.show()
    
    return [tpoint, r1, r2, r3]
    
    
    
    
def chulbalFunc():
    # 서울 관광정보 파일 읽기
    fname = '서울특별시_관광지입장정보.json'
    jsonTp = json.loads(open(fname, 'r', encoding='utf-8').read())      # str -> dict : json decoding
    tour_table = pd.DataFrame(jsonTp, columns=('yyyymm', 'resNm', 'ForNum'))    # 년월, 관광지명, 입장객수
    tour_table = tour_table.set_index('yyyymm')
    print(tour_table[:2])
    
    resNm = tour_table.resNm.unique()
    # print('관광지명 종류:', resNm)
    print('관광지명 종류:', resNm[:5])    # ['창덕궁' '운현궁' '경복궁' '창경궁' '종묘'] 5군데만 참여
    
    print()
    # 중국인 관광 정보 읽기
    cdf = '중국인방문객.json'
    jdata = json.loads(open(cdf, 'r', encoding='utf-8').read()) 
    # print(jdata)
    china_table = pd.DataFrame(jdata, columns=('yyyymm', 'visit_cnt'))
    china_table = china_table.rename(columns={'visit_cnt':'china'})
    china_table = china_table.set_index('yyyymm')
    print(china_table[:2])

    print()
    # 일본인 관광 정보 읽기
    jdf = '일본인방문객.json'
    jdata = json.loads(open(jdf, 'r', encoding='utf-8').read()) 
    # print(jdata)
    japan_table = pd.DataFrame(jdata, columns=('yyyymm', 'visit_cnt'))
    japan_table = japan_table.rename(columns={'visit_cnt':'japan'})
    japan_table = japan_table.set_index('yyyymm')
    print(japan_table[:2])
    
    print()
    # 미국인 관광 정보 읽기
    udf = '미국인방문객.json'
    jdata = json.loads(open(udf, 'r', encoding='utf-8').read()) 
    # print(jdata)
    usa_table = pd.DataFrame(jdata, columns=('yyyymm', 'visit_cnt'))
    usa_table = usa_table.rename(columns={'visit_cnt':'usa'})
    usa_table = usa_table.set_index('yyyymm')
    print(usa_table[:2])

    all_table = pd.merge(china_table, japan_table, left_index=True, right_index=True)
    all_table = pd.merge(all_table, usa_table, left_index=True, right_index=True)
    print(all_table[:2])
    
    r_list = [] # 나라별 상관계수 기억용
    for tpoint in resNm[:5]:
        r_list.append(setScatterFunc(tour_table, all_table, tpoint))
        
    r_df = pd.DataFrame(r_list, columns=('관광지명', '중국', '일본', '미국'))
    r_df = r_df.set_index('관광지명')
    print(r_df)
    
    r_df.plot(kind='bar', rot=50)
    plt.show()

if __name__ == '__main__':
    chulbalFunc()



