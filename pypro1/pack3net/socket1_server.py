# 단순 서버: 1회용
from socket import *
serversock=socket(AF_INET, SOCK_STREAM)     # socket(소켓종류, 소켓유형)
serversock.bind(('192.168.45.127', 8888))    # ip, port 번호 지정
serversock.listen(1)    # TCP listener 설정
print('server start ...')

conn, addr=serversock.accept()  # 연결 대기
print('client addr: ', addr)
print('from client msg: ',conn.recv(1024).decode())
conn.close()
serversock.close()
