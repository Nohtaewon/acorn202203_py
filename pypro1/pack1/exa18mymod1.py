# 현재 모듈은 다른 모듈에서 필요한 멤버를 적어 놓은 파일
name='파이썬 만세'
def list_hap(*ar):
    print(ar)

    if __name__=='__main__':
        print('여기가 최상위 모듈')
        
def kbs():
    print('대한민국 대표 방송')
    
def mbc():
    print('문화방송 채널')
    

