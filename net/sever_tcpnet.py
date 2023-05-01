#! /usr/bin/python
# -*- coding: utf-8 -*-
import json
import socket
import threading
import time

import sys
from PyQt5.QtWidgets import *

# 用 socket() 函数来创建套接字
from PyQt5.QtWidgets import *

from readExecl import dataFile, file_path


# 打开文件
# robotinfor=dataFile(None)
# robotinfor.loadData(file_path)
# listJ1 = list(robotinfor.getJ1())

class tcpconnect(QWidget):
    def __init__(self):
        super().__init__()
        self.initFlags()
        self.initUI()
        self.initSock()
        self.initSlot()


    def initFlags(self):
        self.runningFLag = False
        self.startFlag = False

    def initUI(self):
        self.statelabel = QLabel("点击开始链接")
        self.opbtn = QPushButton("开始")
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.statelabel)
        self.layout.addWidget(self.opbtn)
        self.setLayout(self.layout)
        self.resize(200, 100)

        self.show()
        print("initUI ok!")

    def initSlot(self):
        self.opbtn.clicked.connect(self.changeState)

    def initSock(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 初始化地址和端口
        server_address = ('127.0.0.1', 12345)
        print("Starting up on %s:%s" % server_address)
        self.sock.bind(server_address)
        # 开始TCP监听。backlog指定在拒绝连接之前，操作系统可以挂起的最大连接数量。该值至少为1，大部分应用程序设为5就可以了
        self.sock.listen(1)
        print("initSock ok!")

    def changeState(self):
        # 初始化标志


        if self.startFlag:  # 若此时正在开始 点击按钮
            self.statelabel.setText("点击开始链接")
            self.opbtn.setText("开始")
            self.runningFLag = False
            self.startFlag = False
        else:
            self.statelabel.setText("等待链接...")
            self.opbtn.setText("停止")
            self.runningFLag = True
            self.startFlag = True



        self.severTh = threading.Thread(target=lambda: self.runsever())
        self.severTh.start()

    def runsever(self):
        print(self.runningFLag)
        while self.runningFLag:
            print("Waiting for a connection")
            # 被动接受TCP客户端连接,(阻塞式)等待连接的到来
            connection, client_address = self.sock.accept()
            print("Connection from", client_address)
            try:


                while True:
                    # 需要做一个判断确定对方主机是否断开了链接
                    data = connection.recv(1024)
                    json_string = json.loads(data)
                    print(json_string[0])
                    print(json_string[1])
                    print(json_string[2])

                    if data == '0' or self.runningFLag == False:
                        break
#                    print("Receive '%s'" % json.loads(data))


            finally:
                pass
     #           connection.close()
     #           print("close sock!")






if __name__ == '__main__':
    app1 = QApplication(sys.argv)
    main = tcpconnect()

    sys.exit(app1.exec_())




