# -*- coding: utf-8 -*-
import socket
import threading

class Server():
    def __init__(self, ip_host, port):
        self.ip_host = ip_host     #定义ip地址     
        self.port = port           #定义端口
        self.addr = (self.ip_host, self.port) #绑定ip地址和端口号
        self.BUFSIZE = 10240          #定义buffer的大小喂10240字节
    def tcpServer(self):
        tcpSerSoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)          #创建TCPlsocket
        tcpSerSoc.bind(self.addr)                     #绑定ip地址和端口
        tcpSerSoc.listen(5)                           #配置监听数量为5
        while True:
            print("waiting for connection")
            tcpCliSoc, addr = tcpSerSoc.accept()         #接收tcp client发送的消息
            print('...connect from :', addr)
            while True:
                data = tcpCliSoc.recv(self.BUFSIZE)      #将tcp client收到的数据赋值给data 
                if not data:
                    break
                tcpCliSoc.send(data)                    #将收到的client发送的数据返回给client
                tcpCliSoc.close()                       #关闭发送连接
            tcpSerSoc.close()                           #关闭tcp server的连接
    def udpServer(self):
         udpSerSoc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #创建udp的socket
         udpSerSoc.bind(self.addr)                   #绑定ip地址和端口号
         while True:
             print('udp server waiting fro connection')
             udpMsg, addr=udpSerSoc.recvfrom(self.BUFSIZE)        #接收udp client发送的消息
             print(udpMsg, addr)                  
             udpSerSoc.sendto(udpMsg)                             #将udp client发送过来的消息再发送给udp client
             udpSerSoc.close()                             #关闭udp 连接

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
    ip_host = '10.0.5.1'
    port = 5200
    tcpServer = Server(ip_host, port)
    tcpServer.tcpServer()
    tcpServer.udpServer()
