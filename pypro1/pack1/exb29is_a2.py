# 클래스의 상속 이해
# Person <- Employee
#        <- Worker <- Programmer

class Person:
    say='난 사람이야~'
    nai='20'
    
    def __init__(self, nai):
        print('Person 생성자')
        self.nai=nai
        
    def printInfo(self):
        print('나이:{}, 이야기:{}'.format(self.nai, self.say))
        
    def hello(self):
        print('안녕')
        
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















    