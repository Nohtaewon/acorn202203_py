# 멀티 채팅 서버 : socket, thread
import socket
import threading

ss=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(('127.0.0.1', 5000))
ss.listen(5)
print('채팅 서버 서비스 시작 ...')
users=[]

def chatUser(conn):
    name=conn.recv(1024)
    data='^^ '+name.decode('utf-8')+'님 입장^^'
    print(data)
    
    try:
        for p in users:
            p.send(data.encode('utf-8'))
            
        while True:
            msg = conn.recv(1024)
            suda_data=name.decode('utf-8')+'님 메세지:'+msg.decode('utf-8')
            print(suda_data)
            for p in users:
                p.send(suda_data.encode('utf-8'))
            
    except:
        users.remove(conn)      # 채팅방을 나간 경우
        data='~~ '+name.decode('utf-8')+'님 퇴장 ~~'
        print(data)
        if users:
            for p in users:
                p.send(data.encode('utf-8'))
        else:
            print('exit')
        
        
while True:
    conn, addr=ss.accept()  # 채팅을 원하는 컴이 접속한 경우 실행
    users.append(conn)
    th=threading.Thread(target=chatUser, args=(conn,))
    th.start()
    
    
    
    
    
    
    
    
    
    
    