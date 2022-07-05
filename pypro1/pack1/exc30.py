# method override(재정의)    상속에서만 나오는 이야기

class Parent:
    def printData(self):
        pass
    
class Child1(Parent):
    def printData(self):
        print('Child1에서 override')
        
class Child2(Parent):
    def printData(self):
        print('Child2에서 override')
        print('부모 메소드와 이름은 같으나 다른 기능을 가짐')
        
    def abc(self):
        print('Child2 고유 메소드')
        
c1=Child1()
c1.printData()
print()
c2=Child2()
c2.printData()
print('다형성 처리')
# par=Parent()
par=c1
par.printData()
print()
par=c2
par.printData()
print('----------------------')
plist=[c1, c2]
for i in plist:
    i.printData()
    print()









