import socket
import threading
import time

lock=threading.Lock()
host=input('请输入服务端ip')
port=int(input('请输入要服务端的端口'))
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen(10)
print('已经开始在%s的%d上侦听'%(host,port))

msgs=[]
clients={}


def colmsg(client):
    global msgs
    global clients
    while True:
        
        try:
            usermsg='用户%d:%s'%(clients[client],client.recv(1145).decode('utf-8'))
            client.send(('已成功发送消息').encode())
            lock.acquire()
            msgs.append([client,usermsg])
            print(msgs)
            lock.release()
        except:
            print('用户%d已中断连接'%(clients[client]))
            client.close()
            break



def conveymsg():
   
    global msgs
    global clients
    
    while True:
        lock.acquire()
        if msgs:
            print(msgs)
            for msg in msgs:
                cli=msg[0]
                usmsg=(msg[1]).encode()
                for client in clients.keys():
                    if not client == cli:
                        client.send(usmsg)
        msgs=[]
        lock.release()
        time.sleep(1)

cvmsg=threading.Thread(target=conveymsg,args=())
cvmsg.start()




while True:

    client,addip=server.accept()
    print('已连接到',addip)
    
    clients[client]=(len(clients)+1)
    welcmeg=('已成功连接,您是用户%d'%(len(clients)))
    client.send(welcmeg.encode())
    clthr=threading.Thread(target=colmsg,args=(client,))
    clthr.start()

