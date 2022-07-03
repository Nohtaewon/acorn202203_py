# 함수 (사용자 정의)
a=10
b=a
print(a)
print('뭔가를 하다가 함수가 필요하면 선언')

# 함수 작성
def doFunc1():
    print('doFunc1 처리')

def doFunc2(arg1, arg2):    #doFunc2(para1, para2)
    # pass    함수의 내용을 적지 않을 경우
    tmp=arg1+arg2
    # return tmp
    """
    if tmp%2==1:
        return      # None을 반환
    else:
        return tmp
    """
    if tmp%2==1:
        return      
    print(tmp)
    

# 함수 호출
aa=doFunc1
print(doFunc1)
print(aa)
doFunc1()
print('b:',b)
doFunc1()
print('-----------')
bb=doFunc2(4, 6)
print('반환된 bb는 ', bb)

print('~~'*20)
def area_tri(a, b):
    print('a')
    result=a*b/2
    area_print(result)      # 함수가 다른 함수 호출
    print('c')
    
def area_print(result):
    print('삼각형의 면적은 '+str(result))
    print('b')
    
area_tri(5, 4)

print()

def swapfunc(a,b):
    return b,a  # tuple type 으로 묶여 하나의 값으로 반환

a=10; b=20
print(a,b)
imsi=swapfunc(a, b)
print(imsi)
a,b=swapfunc(a, b)
print(a,b)

print()
def func1():
    print('func1 처리')
    def func2():    # 내부 함수
        print('func2 처리')
    func2()
    
func1()

# if 조건식에서 함수 사용
def is_odd(para):
    return para % 2 == 1

mydict={x:x*x for x in range(11) if is_odd(x)}
print(mydict)







print('종료')






















