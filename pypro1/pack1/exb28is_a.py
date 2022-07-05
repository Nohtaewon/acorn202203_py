# 자원의 재활용을 목적으로 클래스를 상속 가능. 다중 상속도 허용
class Animal:
    nai=1
    def __init__(self):
        print('Animal 생성자')
    def move(self):
        print('움직이는 생물')
        
class Dog(Animal):
    irum='난 댕댕이'
    def __init__(self):
        print('Dog 생성자')
    def my(self):
        print(self.irum+'만세')

dog1=Dog()
dog1.my()
dog1.move()
print('nai:',dog1.nai)

print()
class Horse(Animal):
    pass

horse1=Horse()
horse1.move()
print('nai:',horse1.nai)
