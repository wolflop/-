# -*- coding: utf-8 -*-
import socket
import time
import threading

#创建tcp客户端函数
def Tcp_Client(PORT):
    HOST = '10.0.31.11'  #tcpserver的ip地址
    BUSIZ = 10240        #缓存大小
    ADDR = (HOST, PORT)  
    tcpCliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #穿件tcp的socket
    tcpCliSock.connect(ADDR)     #在监听的客户端连接符服务器程序上，打开一个连接到机器和端口的连接
    while True:
        # data = input('>>>:').strip()
        data = '我是一个好人啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊'    #要发送的数据
        tcpCliSock.send(bytes(data, 'utf-8'))            #在socket上发送数据到服务器
        if not len(data):
            continue
        data_ser = tcpCliSock.recv(BUSIZ)       # 读取服务器发送过来的数据
        if not data_ser:
            break
        # print(str(data_ser, 'utf-8'))
    tcpCliSock.close()

#创建线程检查函数

def checkThread(sleeptimes, initThreadName=[]):

    for i in range(400, 10000, 1):  #线程在400-10000循环
        nowThreadName=[]
        now = threading.enumerate() #获取当前线程名
        for i in now:
            nowThreadName.append(i.getName()) #保存当前线程名字
        for i in initThreadsName:
            if i in nowThreadName:
                pass #当前某线程在初始化线程组里，不做操作
            else:
                print("%s stop, now restart" %i)
                t = threading.Thread(target=Tcp_Server, args=(i, )) #如果当前线程不在初始化线程组里，重启线程
                t.setName(i) #重设线程名称
                t.start()
        time.sleep(sleeptimes) #隔一段时间重新运行，检测有没有线程down

if __name__ == '__main__':
    # for i in range(400, 10000, 1):
    #     t = threading.Thread(target=Tcp_Client, args=(i,))
    #     t.start()
        # time.sleep(30)
        # t.join()
    threadName = []
    # 获取当前线程名字
    initThreadsName = []  # 保存初始化线程组名字
    for i in range(400, 10000, 1):
        t = threading.Thread(target=Tcp_Client, args=(i,))
        t.setName(i)
        threadName.append(t)
    for t in threadName:
        t.start()
    init = threading.enumerate()  # 获取初始化的线程对象
    for i in init:
        initThreadsName.append(i.getName())  # 保存初始化线程的名字
    check = threading.Thread(target=checkThread, args=(60, initThreadsName))  # 用来检测是否有线程down并重启down线程
    check.setName('Thread:check')
    check.start()
