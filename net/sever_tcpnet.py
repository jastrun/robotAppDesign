#! /usr/bin/python
# -*- coding: utf-8 -*-
import json
import os
import socket
import threading
import time

import sys
from os import error

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import *

# 用 socket() 函数来创建套接字
from PyQt5.QtWidgets import *

from readExecl import dataFile, file_path


# 打开文件
# robotinfor=dataFile(None)
# robotinfor.loadData(file_path)
# listJ1 = list(robotinfor.getJ1())
from timerSeries import timeseries

def readQss(style):
    with open(style, 'r') as f:
        return f.read()

class tcpconnect(QWidget):
    # 信号初始化
    fileinfo_signal = pyqtSignal(str)
    source_signal = pyqtSignal(str)
    dataunit_signal = pyqtSignal(list, list)
    powerAndEnergyAndspeed_signal = pyqtSignal(float, float, float)
    alldata_signal = pyqtSignal(list)

    def __init__(self,Parent=None):
        super().__init__(Parent)
        self.initFlags()
        self.initUI()
        self.initSlot()


    def initFlags(self):
        self.runningFLag = False
        self.startFlag = False

    def initUI(self):
        self.statelabel = QLabel("点击开始链接")
        self.opbtn = QPushButton("开始")
        self.layout = QVBoxLayout()
        self.statelabel.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.statelabel)
        self.layout.addWidget(self.opbtn)
        self.setLayout(self.layout)
        self.resize(400, 300)

        str = os.getcwd() + "\\..\\qssStyle\\new7.qss"
        qssStyle = readQss(str)
        self.setStyleSheet(qssStyle)


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
            print(self.severTh.is_alive())
            self.statelabel.setText("点击开始链接")
            self.opbtn.setText("开始")
            self.statelabel.setAlignment(Qt.AlignCenter)
            self.runningFLag = False
            self.startFlag = False

            self.sock.close()

        else:
            self.statelabel.setText("等待链接...")
            self.opbtn.setText("停止")
            self.runningFLag = True
            self.startFlag = True

            self.initSock()
            self.severTh = threading.Thread(target=lambda: self.runsever())
            self.severTh.start()
            print(self.severTh.is_alive())

    def deadtimeshow(self,sec,mes):
        timer = timeseries()
        timer.start()
        cur=0
        for cur in range(int(sec)):
            print(int(sec-timer.getCurTime()))
            time.sleep(1)

        timer.end()
        print(mes)

    def runsever(self):
        self.source_signal.emit("TCP/IP")
        try:
            print("Waiting for a connection")
            # 被动接受TCP客户端连接,(阻塞式)等待连接的到来
            self.connection, self.client_address = self.sock.accept()
            print("Connection from", self.client_address)
            self.statelabel.setText("Connection from"+str(self.client_address))
        except socket.error as err:
            print(err)

        while self.startFlag:

            try:
                data = self.connection.recv(1024)  # 阻塞接收
                json_string = json.loads(data)
                print(json_string[0])
                print(json_string[1])
                print(json_string[2])
                self.signalSend(json_string[0],json_string[1],json_string[2])
            except AttributeError as err:
                print(err)
                break
        try:
            self.connection.close()
        except AttributeError as err:
            print(err)

    def signalSend(self,dataunit,PAE,alldata):


        self.dataunit_signal.emit(dataunit[0], dataunit[1])
        self.powerAndEnergyAndspeed_signal.emit(PAE[0],PAE[1],PAE[2])
        self.alldata_signal.emit(alldata)








if __name__ == '__main__':
    app1 = QApplication(sys.argv)
    main = tcpconnect()
    main.show()
    sys.exit(app1.exec_())




