from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier 
from sklearn.metrics import accuracy_score
import numpy as np
import matplotlib.pyplot as plt

# Create your views here.
flag = False

def mainFunc(request):
    global flag, acc, pt_data_ilbu
    if flag == False:
        acc, pt_data_ilbu = makeModel()
        flag = True
    
    context = {'acc':acc, 'pt_data_ilbu':pt_data_ilbu.to_html(index=False)}
    return render(request, 'main.html', context)

def makeModel():
    pt_data = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/patient.csv')
    pt_data_ilbu = pt_data.head(3)
    print(pt_data_ilbu)
    
    # print(pt_data.isnull().any()) # 결측치 없음
    # 독립변수 / 종속변수 설정
    x = pt_data.iloc[:, 2:]   # 독립변수 STA를 제외한 나머지
    print(x[:2])
    
    y = pt_data['STA']
    print(y[:2])
    
    train_x, test_x, train_y, test_y = train_test_split(x,y)
    
    # 모델 생성
    model = RandomForestClassifier(criterion='entropy', n_estimators=500, random_state=0)
    model.fit(train_x, train_y)
    pred = model.predict(test_x)
    acc = np.round(accuracy_score(test_y, pred), 2)
    print('예측값 : ', pred[:5])
    print('실제값 : ', np.array(test_y[:5]))
    print('분류 정확도 : ', acc)
    
    # 모델 저장
    joblib.dump(model, 'django15rf_patient/myapp/static/django15.model')
    
    return acc, pt_data_ilbu


def inputFunc(request):
    return render(request, 'show.html')


def predictFunc(request):
    # AGE SEX RACE SER CAN CRN INF CPR HRA
    AGE = int(request.POST.get('AGE'))
    SEX = int(request.POST.get('SEX'))
    RACE = int(request.POST.get('RACE'))
    SER = int(request.POST.get('SER'))
    CAN = int(request.POST.get('CAN'))
    CRN = int(request.POST.get('CRN'))
    INF = int(request.POST.get('INF'))
    CPR = int(request.POST.get('CPR'))
    HRA = int(request.POST.get('HRA'))
    print('AGE : ', AGE)
    
    # 모델을 읽어 입력된 년도에 해당하는 연봉을 예측하여 클라이언트로 반환
    model = joblib.load('django15rf_patient/myapp/static/django15.model')
    new_data = np.array([[AGE, SEX, RACE, SER, CAN, CRN, INF, CPR, HRA]])
    print('new_data ', new_data)
    new_pred = model.predict(new_data)
    print('new_pred : ', new_pred[0]) 
    
    context = {'new_pred':new_pred[0]}
    return render(request, 'list.html', context) 
