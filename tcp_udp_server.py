# -*- coding: utf-8 -*-
import socket
import threading

class Server():
    def __init__(self, ip_host, port):
        self.ip_host = ip_host
        self.port = port
        self.addr = (self.ip_host, self.port)
        self.BUFSIZE = 10240
    def tcpServer(self):
        tcpSerSoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpSerSoc.bind(self.addr)
        tcpSerSoc.listen(5)
        while True:
            print("waiting for connection")
            tcpCliSoc, addr = tcpSerSoc.accept()
            print('...connect from :', addr)
            while True:
                data = tcpCliSoc.recv(self.BUFSIZE)
                if not data:
                    break
                tcpCliSoc.send(data)
                tcpCliSoc.close()
            tcpSerSoc.close()
    def udpServer(self):
         udpSerSoc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
         udpSerSoc.bind(self.addr)
         while True:
             print('udp server waiting fro connection')
             udpMsg, addr=udpSerSoc.recvfrom(self.BUFSIZE)
             print(udpMsg, addr)
             udpSerSoc.sendto(udpMsg)
             udpSerSoc.close()

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
