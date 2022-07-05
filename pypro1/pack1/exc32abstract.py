# 추상 클래스 - 추상 메소드
# 하위 클래스에서 부모의 메소드를 반드시 오버라이드 하도록 강요가 목적
# 다형성, 강요
from abc import *

class AbstractClass(metaclass=ABCMeta): # 추상 클래스
    @abstractmethod
    def aaMethod(self): # 추상 메소드
        pass
    
    def normalMethod(self): # 일반 메소드
        print('추상 클래스 내의 일반 메소드')
        
# p=AbstractClass()    TypeError: Can't instantiate abstract class AbstractClass with abstract method aaMethod

class Child1(AbstractClass):
    name='난 Child1'
    
    def aaMethod(self): # 오버라이딩을 강요 당함
        print('추상메소드를 일반 메소드로 재정의')
    
c1=Child1()
print(c1.name)
c1.aaMethod()
c1.normalMethod()

print('-------------------------------')
class Child2(AbstractClass): 
    def aaMethod(self): # 오버라이딩을 강요 당함
        print('Child2에서 추상메소드를 일반 메소드로 오버라이딩')
        a=120
        print('a:',a-20)
        
    def normalMethod(self): # 일반 메소드를 필요에 의해 선택적으로 재정의
        print('Child2에서 부모와 기능이 다른 일반 메소드 변경')  
        
c2=Child2()

kbs=c1
kbs.aaMethod()
kbs.normalMethod()
print()
kbs=c2 
kbs.aaMethod()
kbs.normalMethod()       
        
        
        
        
        
        
        
        
        
        
         
    