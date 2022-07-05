# 클래스의 이해
print('어쩌구 저쩌구 하다가...')

class Car:
    handle = 0
    speed = 0
    
    def __init__(self, speed, name):    #객체를 만들때 쓰는 생성자
        self.speed=speed
        self.name=name
    
    def show_data(self):
        km='킬로미터'
        msg='속도: '+str(self.speed)+km
        return msg + ', 핸들은 '+str(self.handle)

print(Car.handle, Car.speed)
print()

car1=Car(5, 'tom')  # 생성자를 부름 self로 감 
print(car1.handle, car1.speed, car1.name)
car1.color='파랑'
print('car1 자동차 색은', car1.color)
print()
car2=Car(10, 'john')
print(car2.handle, car2.speed, car2.name)
# print('car2 자동차 색은', car2.color)    AttributeError: 'Car' object has no attribute 'color'

print('method')
print('car1:', car1.show_data())
print('car2:', car2.show_data())
print()
car1.speed=100
print('car1:', car1.show_data())
print('car2:', car2.show_data())
print('원형클래스의 speed:', Car.speed)
print()
Car.handle=1
print('car1:', car1.show_data())
print('car2:', car2.show_data())
print()
print(id(Car), id(car1), id(car2))
print(type(car1), type(car2))
print()
print(car1.__dict__)    # 객체의 멤버 확인
print(car2.__dict__)






