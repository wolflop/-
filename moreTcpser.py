# -*- coding: utf-8 -*-
import socket# -*- coding: utf-8 -*-
import socket
import threading
import time

#创建TCPserver
def Tcp_Server(PORT):
    HOST = '10.0.31.11' #tcpserver的ip地址
    BUFSIZ = 10240  #tcpserver的缓存
    # PORT = 8898
    ADDR = (HOST, PORT)   #绑定IP和端口号
    tcpSerSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP) #创建TCP的套接字对象
    tcpSerSock.bind(ADDR) #绑定本地信息
    tcpSerSock.listen(5)  #监听来自客户端的连接，允许保留5个挂起的请求
    while True:           #等待客户端建立连接
        # print('waiting fro connection...')
        tcpCliSock, addr = tcpSerSock.accept()  #建立连接后，建立一个新的socket对象，在此socket上可以与客户端上转移数据  
        print('...connect from :', addr)
        while True:
            data = tcpCliSock.recv(BUFSIZ)      #从客户端读取数据，最大为BUFSIZ的字节
            if not data:
                break
            tcpCliSock.send(data)               #将收到的数据发送给客户端
        tcpCliSock.close()                      #关闭连接
    tcpSerSock.close()

def checkThread(sleeptimes, initThreadName=[]):
    for i in range(400, 10000, 1):
        nowThreadName=[]
        now = threading.enumerate() #获取当前线程名
        for i in now:
            nowThreadName.append(i.getName()) #保存当前线程名字
        for i in initThreadsName:
            if i in nowThreadName:
                pass #当前某线程在初始化线程组里，不座操作
            else:
                print("%s stop, now restart" %i)
                t = threading.Thread(target=Tcp_Server, args=(i, )) #当当前线程不在初始化线程组里，重启线程
                t.setName(i) #重设线程名称
                t.start()
        time.sleep(sleeptimes) #隔一段时间重新运行，检测有没有线程down

if __name__ == '__main__':
    threadName = []
    # #获取当前线程名字
    initThreadsName = []  # 保存初始化线程组名字
    for i in range(400, 10000, 1):
        t = threading.Thread(target=Tcp_Server, args=(i,))   #运行tcp_server的线程
        t.setName(i)   #设置线程名字
        threadName.append(t)  #把线程名字保存到线程名称中
    for t in threadName:
        t.start()
    init = threading.enumerate() #获取初始化的线程对象
    for i in init:
        initThreadsName.append(i.getName())  #保存初始化线程的名字
    check = threading.Thread(target=checkThread, args=(60, initThreadsName))  # 用来检测是否有线程down并重启down线程
    check.setName('Thread:check')
    check.start()
