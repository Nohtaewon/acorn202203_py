from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
from myapp.models import Jikwon, Buser
from _datetime import date
plt.rc('font', family='malgun gothic')

# Create your views here.
def mainFunc(request):
    return render(request, 'main.html')

def showFunc(request):
    # https://brownbears.tistory.com/101
    # 형식 : table1.objects.extra(tables=['table2'], where=['table2.id=table1.num'])
    data=Jikwon.objects.extra(select={'buser_name':'buser_name'},
                              tables=['Buser'],
                              where=['Buser.buser_no=Jikwon.buser_num']).values\
                              ('jikwon_no', 'jikwon_name','buser_name','jikwon_jik','jikwon_pay','jikwon_ibsail','jikwon_gen').\
                              order_by('buser_name','jikwon_name')
                              
    df = pd.DataFrame(data) 
    df.columns=['부서명', '사번', '직원명', '직급', '연봉', '입사', '성별'] 
    del df['입사']
    
    # 근무년수
    period=[]
    for i in data.values('jikwon_ibsail'):
        period.append((date.today()).year - (i['jikwon_ibsail']).year)
    
    df['근무년수']=period
    
    # 부서명에 대한 연봉합과 연봉 평균
    groupBpay=df['연봉'].groupby(df['부서명'])
    groupBpay_sm={'sum':groupBpay.sum(), 'mean':round(groupBpay.mean())}
    # 직급에 대한 연봉합과 연봉 평균
    groupJpay=df['연봉'].groupby(df['직급'])
    groupJpay_sm={'sum':groupJpay.sum(), 'mean':round(groupJpay.mean())}
    
    df2=pd.DataFrame(groupBpay_sm)
    df2.columns=['연봉합', '연봉평균']
    df3=pd.DataFrame(groupJpay_sm)
    df3.columns=['연봉합', '연봉평균']
    print(df2)
    print(df3)
    
    # 부서명별 연봉합, 평균 세로막대 그래프
    result=groupBpay.agg(['sum', 'mean'])
    result.plot(kind='bar')
    plt.title("부서명별 연봉합, 평균")
    plt.ylabel('연봉') 
    fig=plt.gcf()
    fig.savefig('django_9_ex/myapp/static/images/jik.png')
    ypays=list(df['연봉'])
    names=list(df['사번'])
    
    # 성별, 직급별 빈도표
    print(df)
    ctab=pd.crosstab(df['성별'], df['직급'], margins=True)
    
    return render(request, 'show.html', 
                  {'data':df.to_html(),
                   'pay_sm1':df2.to_html(),
                   'pay_sm2':df3.to_html(),
                   'ctab':ctab.to_html(),
                   'ypays':ypays,
                   'names':names
                   })
    
    
    
    
    
    
    
    