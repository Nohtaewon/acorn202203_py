class Machine:      # Machine 이 CoinIn을 포함하고 있다
    cupCount=1
    def __init__(self):
        self.coinIn=CoinIn()    # 클래스의 포함
    def showData(self):
        self.coinIn.coin=int(input('동전을 입력하세요'))
        self.cupCount=int(input('몇 잔을 원하세요'))
        print(self.coinIn.culc(self.cupCount))
        
class CoinIn:
    
    coin=0
    change=0
        
    def culc(self, cupCount):
        result=''
        if self.coin<200:
            result='요금부족'
        elif cupCount*200>self.coin:
            result='요금부족'
        else:
            self.change=self.coin-(cupCount*200)
            result='커피'+str(cupCount)+'잔과 잔돈'+str(self.change)+'원'
        return result    
Machine().showData()
                
        

