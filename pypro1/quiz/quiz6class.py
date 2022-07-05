# 다중상속 연습:cafe 연습문제 3

class Animal:
    def move(self):
        pass

class Dog(Animal):
    name='개'
    
    def move(self):
        print('댕댕이는 낮에 활기차게 돌아다님')
        
class Cat(Animal):  # 단일 상속
    name='고양이'
    def move(self):
        print('냥냥이는 밤에 돌아다님')
        print('눈빛이 빛남')
        
class Wolf(Dog, Cat):   # 다중 상속
    pass

class Fox(Cat, Dog):
    def move(self):
        print('여우처럼 민첩하게')
    def foxMethod(self):
        print('여우 고유메소드')
        
dog=Dog()
print(dog.name)
dog.move() 
print()
cat=Cat()
print(cat.name)
cat.move()
print('---------------')
wolf=Wolf()
fox=Fox()

ani=wolf
ani.move()
ani=fox 
ani.move() 
print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
anis=[dog, cat, wolf, fox]
for a in anis:
    a.move()
    print()
    
print()
print(Fox.__mro__)
print(Wolf.__mro__)