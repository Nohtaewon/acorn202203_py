# 예외 처리: 프로그램 진행 도중 발생되는 에러에 대한 처리 방법 중 하나
# try ~ except

def divide(a,b):
    return a/b

# c=divide(5,2)
# c=divide(5,0)   # ZeroDivisionError: division by zero
# print('c: ',c)

try:
    c=divide(5,2)
    # c=divide(5,0)
    print('c: ',c)
    
    mbc=[1,2]
    print(mbc[0])
    # print(mbc[2])
    
    f=open('c:/work/aa.txt')
    
except ZeroDivisionError:
    print('두번째 인자 0을 주지 마세요')
except IndexError as err:
    print('참조범위 오류: ', err)
except Exception as e:
    print('기타 나머지 에러: ', e)
finally:
    print('에러 유무와 상관없이 반드시 수행됨')








print('프로그램 종료')