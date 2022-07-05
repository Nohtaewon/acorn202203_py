# 냉장고 클래스에 음식 클래스 담기 - 포함 연습

class Fridge:
    isOpened=False
    foods=[]
    
    def open(self):
        self.isOpened=True
        print('냉장고 문 열기')
        
    def put(self, thing):
        if self.isOpened:
            self.foods.append(thing)    # 클래스의 포함
            print('냉장고 속에 음식을 저장함')
            self.list()
        else:
            print('냉장고 문이 닫혀서 속에 음식을 저장할 수 없어요')
    
    def list(self):     # 냉장고 속 음식물 목록 확인
        for f in self.foods:
            print('-', f.irum, f.expiry_date)
        
    def close(self):
        self.isOpened=False
        print('냉장고 문 닫기')
        
class FoodData:
    def __init__(self, irum, expiry_date):
        self.irum=irum
        self.expiry_date=expiry_date
        
f=Fridge()

apple=FoodData('사과', '2022-7-10')       
f.put(apple)  
f.open()
f.put(apple)
f.close()
print()     
tera=FoodData('테라', '2023-12-10')
f.open()
f.put(tera)
f.close()
        
        
        
        
        
        
        
        
        