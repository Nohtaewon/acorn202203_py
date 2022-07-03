print('Q1------------------------------')
def is_odd(number):
    if number %2==1:
        return True 
    else:
        return False
print(is_odd(3), is_odd(4))
is_odd=lambda x:True if x%2==1 else False
print(is_odd(3))
print('Q2------------------------------')
def avg_numbers(*args):
    result=0
    for i in args:
        result+=i
    return result/len(args)
a=avg_numbers(1,2)
b=avg_numbers(1,2,3,4,5)
print(a, b)
print('Q3------------------------------')
input1=input("첫번째 숫자를 입력하세요:")
input2=input("두번째 숫자를 입력하세요:")

tot=int(input1)+int(input2)
print("두 수의 합은 %s 입니다"%tot)
print('Q4------------------------------')




















