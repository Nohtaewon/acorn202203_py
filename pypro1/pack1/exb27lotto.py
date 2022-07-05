# 로또 번호 생성기
import random
class LottoBall:
    def __init__(self, num):
        self.num=num
        
class LottoMachine:
    def __init__(self):
        self.ballList=[]
        for i in range(1, 46):
            self.ballList.append(LottoBall(i))  # 클래스의 포함
    
    def selectBall(self):
        # 섞기 전 공 출력
        for a in range(45):
            print(self.ballList[a].num, end=' ')
        print()
        random.shuffle(self.ballList)
        # 섞기 후 공 출력
        for a in range(45):
            print(self.ballList[a].num, end=' ') 
        
        return self.ballList[0:6]
class LottoStart:
    def __init__(self):
        self.machine=LottoMachine()   # 클래스의 포함
    
    def play_lotto(self):
        input("로또를 시작하려면 엔터 키를 누르세요")
        select_balls=self.machine.selectBall()
        print()
        for b in select_balls:
            print('%d'%(b.num), end=' ')
        
if __name__=='__main__':
    LottoStart().play_lotto() 
         
         
         
         
         
         
         
         
         
         
         
         
         
         