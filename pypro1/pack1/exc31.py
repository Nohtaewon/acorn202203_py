# 다중 상속

class Tiger:
    data='호랑이 세계'

    def cry(self):
        print('호랑이: 어흥')
        
    def eat(self):
        print('맹수는 고기를 좋아함. 고기 먹은 후 아아 마심')
        
class Lion:
    def cry(self):
        print('사자: 으르렁')
    
    def hobby(self):
        print('백수의 왕은 낮잠을 즐김')
        
class Liger1(Tiger, Lion):  # 다중 상속은 순서가 중요
    pass

l1=Liger1()
l1.cry()
l1.eat()
l1.hobby()
print(l1.data)

def hobby():
    print('이건 함수라고 해~')
    
print('---------------------------')

class Liger2(Lion, Tiger):  # 다중 상속은 순서가 중요
    data='라이거 만세'  
    def play(self):
        print('라이거 고유 메소드')

    def hobby(self):
        print('라이거는 프로그램 짜기가 취미')

    def showData(self):
        self.hobby()
        super().hobby()
        hobby()
        self.eat()
        super().eat()
        print(self.data+ ' '+super().data)
        
l2=Liger2()
l2.play()
l2.showData()
      
        
        
        
        
        
        
        
        