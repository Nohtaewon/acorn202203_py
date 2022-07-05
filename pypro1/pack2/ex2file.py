# file i/o

import os

print(os.getcwd())

try:
    print('파일 읽기')
    # f1=open(r'C:\work\psou\pypro1\pack2\ftest.txt', mode='r', encoding='utf-8')
    # f1=open(os.getcwd()+r'\ftest.txt', mode='r', encoding='utf-8')
    f1=open('ftest.txt', mode='r', encoding='utf-8')
    
    print(f1)
    print(f1.read())
    f1.close()
    
    print('파일 저장')
    f2=open('ftest2.txt', mode='w', encoding='utf-8')
    f2.write('손오공\n')
    f2.write('사오정\n')
    f2.write('저팔계\n')
    f2.close()
    
    print('파일 추가')
    f2=open('ftest2.txt', mode='a', encoding='utf-8')
    f2.write('김칫국\n')
    f2.write('공기밥\n')
    f2.close()

except Exception as e:
    print('err: ',e)
    
print('with 구문을 사용하면 close() 자동 처리--------')
try:
    #저장
    with open('ftest3.txt', mode='w', encoding='utf-8') as obj1:
        obj1.write('파이썬으로 파일 처리\n')
        obj1.write('with 처리\n')
        obj1.write('close 생략\n')
    
    #읽기
    with open('ftest3.txt', mode='r', encoding='utf-8') as obj2:
        print(obj2.read())
except Exception as e2:
    print('err: ',e2)
print() 
print('----피클링(객체를 파일로 저장 및 읽기)--------')
import pickle

try:
    # 객체 저장
    dicData={'tom':'111-1111', 'john':'222-2222'}
    listData={'장마철','장대비 예고'}
    tupleData=(dicData, listData)
    
    with open('hello.data', mode='wb') as ob1:
        pickle.dump(tupleData, ob1)   # pickle.dump(대상, 파일객체)
        pickle.dump(listData, ob1) 
        
    # 객체 읽기
    with open('hello.data', mode='rb') as ob2:
        a, b=pickle.load(ob2)
        print(a)
        print(b)
        print()
        c=pickle.load(ob2)
        print(c)
except Exception as e3:
    print('err: ',e3)
       
    
    
    
    
    