# 클래스의 상속 이해
# Person <- Employee
#        <- Worker <- Programmer

class Person:
    say='난 사람이야~'
    nai='20'
    __good='체력을 다지자'    # private 멤버가 됨
    
    def __init__(self, nai):
        print('Person 생성자')
        self.nai=nai
        
    def printInfo(self):
        print('나이:{}, 이야기:{}'.format(self.nai, self.say))
        
    def hello(self):
        print('안녕')
        print('private 멤버 출력:', self.__good)
    
    @staticmethod
    def sbs(tel):
        print('static method : 클래스 소속 - 클래스 멤버와 상관없는 독립적 처리를 할 경우에 사용')
        
print(Person.say, Person.nai)
p=Person('22')
p.printInfo()
p.hello()
print('------------------')
class Employee(Person):
    say='일하는 동물'
    subject='근로자'
    def __init__(self):
        print('Employee 생성자')
        
    def printInfo(self):
        print('Employee 클래스의 printInfo')
        
    def e_printInfo(self):
        self.printInfo()    # 현재 클래스에서 찾다가 없으면 바로 윗대 찾음
        super().printInfo() # 바로 윗대 찾음

e=Employee()
print(e.say, e.nai, e.subject)
e.printInfo()
e.e_printInfo()

print('------------------')
class Worker(Person):
    def __init__(self, nai):
        print('Worker 생성자')
        super().__init__(nai)   # Bound method call
        
    def w_printInfo(self):
        super().printInfo()
        
w=Worker('30')
print(w.say, w.nai)
w.w_printInfo()
w.printInfo()

print('------------------------')
class Programmer(Worker):
    def __init__(self, nai):
        print('Programmer 생성자')
        # super().__init__(nai)   # Bound method call
        Worker.__init__(self, nai)# unBound method call
        
    def w_printInfo(self):
        print('Programmer 에서 부모 생성자 override')
        
    # def hello(self):
    #     print('private 멤버 출력:', self.__good)
        
pr=Programmer('33')
print(pr.say, pr.nai)
pr.w_printInfo()
pr.printInfo()

print('~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(type(1.2))
print(type(pr))
print(type(w))
print(Programmer.__bases__)   
print(Worker.__bases__)
print(Person.__bases__)       

print()
# pr.hello()  # AttributeError: 'Programmer' object has no attribute '_Programmer__good'
pr.sbs('111-1111')
Person.sbs('222-2222') #권장




















    