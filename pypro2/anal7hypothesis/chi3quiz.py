import pandas as pd
import scipy.stats as stats

# 귀무: 부모학력 수준이 자녀의 진학여부와 관련이 없다. 독립적
# 대립: 부모학력 수준이 자녀의 진학여부와 관련이 있다. 독립적 x
data=pd.read_csv('testdata/cleanDescriptive.csv')
print(data.head(3))
print(data['pass'].unique())

ctab=pd.crosstab(index=data['level'], columns=data['pass'], dropna=True)
ctab.index=['고졸', '대졸', '대학원졸']
ctab.columns=['실패', '합격']
print(ctab)

chi2, p, ddof, exp = stats.chi2_contingency(ctab)
print('chi2:{}, p-value:{}, df:{}'.format(chi2, p, ddof))

# chi2:2.7669512025956684, p-value:0.25070568406521365, df:2
# 해석 : p-value:0.25 > 0.05 귀무가설 채택
# 대립: 부모학력 수준이 자녀의 진학여부와 관련이 없다.

print('-----------------------------------------------------')
import MySQLdb
import numpy as np
import pickle
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')     
plt.rcParams['axes.unicode_minus']=False  

try:
    with open("mydb.dat", mode='rb') as obj:
        config=pickle.load(obj)
except Exception as e:
    print('읽기 오류:',e)

# 귀무: 직급과 연봉은 관련이 없다. 독립적
# 대립: 직급과 연봉은 관련이 있다. 독립적 x

try:
    conn=MySQLdb.connect(**config)
    cursor=conn.cursor()
    sql="""
        select jikwon_jik, jikwon_pay from jikwon
    """
    df = pd.read_sql(sql, conn)
    df.columns = '직급', '연봉'
    df['직급'] = df['직급'].apply(
        lambda g:1 if g == '이사' else 2 if g == '부장' else 3 \
                    if g == '과장' else 4 if g == '대리' else 5)

    df['연봉'] = np.where(df['연봉'] < 3000, 1, df['연봉'])
    df['연봉'] = np.where((df['연봉'] >= 3000) & (df['연봉'] < 5000), 2, df['연봉'])
    df['연봉'] = np.where((df['연봉'] >= 5000) & (df['연봉'] < 7000), 3, df['연봉'])
    df['연봉'] = np.where(df['연봉'] >= 7000, 4, df['연봉'])

    ctab = pd.crosstab(index=df['직급'], columns=df['연봉'], dropna=True)
    print(ctab)
    chi2, p, ddof, exp = stats.chi2_contingency(ctab)
    print('chi2:{}, p-value:{}, df:{}'.format(chi2, p, ddof))
except Exception as e:
    print('처리 오류:',e) 
finally:
    cursor.close()
    conn.close()

# chi2:37.40349394195548, p-value:0.00019211533885350577, df:12
# 해석 : p-value:0.000192 < 0.05 이므로 귀무가설 기각 대립가설 채택
# 직급과 연봉은 관련이 있다.






