import socket
import threading
host=input('请输入服务端ip')
port=int(input('请输入要服务端的端口'))
user=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
user.connect((host,port))
print('欢迎使用,键入exit一推出')

def recev():
    while True:
        try:
            retm=user.recv(1145)
            print(retm.decode('utf-8'))
        except:
            print('连接异常')
            user.close()
            break

rece=threading.Thread(target=recev,args=())
rece.start()

while True:
    try:
        mesg=input(':')
        if mesg=='exit':
            user.close()
            break
        user.send(mesg.encode())
    except:
        print('连接异常')
        user.close()
        break

    
    