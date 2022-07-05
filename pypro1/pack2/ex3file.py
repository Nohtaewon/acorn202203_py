# 동(리)이름을 입력해서 해당 동(면)이름으로 시작되는 우편번호 자료 출력

def abc():
    try:
        dong=input('동(면)이름 입력:')
        print(dong)
        
        with open(r'zipcode.txt', mode='r', encoding='euc-kr') as f:
            # line=f.read()   # 전체 자료 읽기
            line=f.readline()   # 한 행 읽기
            # print(line)
            while line:
                # lines=line.split('\t')
                lines=line.split(chr(9))
                # print(lines)  ['135-806', '서울', '강남구', '개포1동 경남아파트', '', '1\n']
                if lines[3].startswith(dong):
                    print('['+lines[0]+']'+lines[1]+' '+\
                          lines[2]+' '+lines[3]+' '+lines[4])
                    
                line=f.readline()
    except Exception as e:
        print('err:',e)
        
if __name__=='__main__':
    abc() 
