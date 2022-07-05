# 모듈의 멤버 중 클래스를 이용해 객체지향(중심)적인 프로그래밍 가능
# 클래스는 새로운 이름공간을 지원하는 단위로 멤버 메소드와 멤버변수를 갖는다
# 접근지정자 없다. 메소드 오버로딩 없다.

a=10
print('모듈의 멤버 중 a는 ', a, type(a))

# class 선언하기
class TestClass:
    aa=1 # 멤버 변수 (전역)
    
    def __init__(self):
        print('생성자')
        
    def printMsg(self): # 메소드(전역)
        name='홍길동'     # 지역 변수
        print(name)
        print(self.aa)
        
    def __del__(self):
        print('소멸자')
        
print('원형클래스의 주소:',id(TestClass))    # 원형 class는 프로그램 실행시 자동으로 객체화
print(TestClass.aa)
# TestClass.printMsg(self)
print()
test=TestClass()    # 생성자 호출. TestClass type의 객체가 생성됨
print('TestClass type의 새로운 객체의 주소:', id(test))
print(test.aa)
test.printMsg()     # Bound method call:자동으로 객체변수가 인수로 전달
print('-----------')
TestClass.printMsg(test)    # unBound method call

print()
print(type('kbs'))
print(type(test))
print(isinstance(test, TestClass))
del test    # 객체 삭제 할 때
# print(isinstance(test, TestClass))
print('종료')



















