# /usr/bin/python
# -*- coding: utf-8 -*-

import socket
import json
from time import sleep

# 打开文件
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from readExecl import dataFile, file_path


# listJ1 = list(robotinfor.getJ1())


class robotsimlink():
    # 静态变量
    endFlag = '0'  # 结束标志
    server_address = ("127.0.0.1", 12345)

    def __init__(self):
        self.initFile()
        self.initSock()

    def initFile(self):
        self.datafile = dataFile(None)
        self.datafile.loadData(file_path)
        print("initfile ok!")

    def initSock(self):

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('Connecting to %s:%s.' % self.server_address)
        self.sock.connect(self.server_address)
        print("initSock ok!")
 #       self.sendOnedata("testing")

        self.initdata()

    def sendOnedata(self,data_str):
        data_str_encode = data_str.encode()
        self.sock.sendall(data_str_encode)

    def sendEndflag(self):
        self.sendOnedata(self.endFlag)

    def initdata(self):
        # 获取时间序列
        timeseries = list(self.datafile.gettimeseries())
        # 获取六个轴的角度
        angle_J1 = list(self.datafile.getJ1())
        angle_J2 = list(self.datafile.getJ2())
        angle_J3 = list(self.datafile.getJ3())
        angle_J4 = list(self.datafile.getJ4())
        angle_J5 = list(self.datafile.getJ5())
        angle_J6 = list(self.datafile.getJ6())
        # 获取末端的三个坐标
        data_xAxis = list(self.datafile.getxAxis())
        data_yAxis = list(self.datafile.getyAxis())
        data_zAxis = list(self.datafile.getzAxis())
        # 获取实时功率
        motorPower = list(self.datafile.getPower())
        # 获取总能量
        motorEnergy = list(self.datafile.getEnergy())
        # 获取速度
        speed = list(self.datafile.getSpeed())

        print("file ok!")
        i = 0
        # 获取角度增量
        while i <= len(timeseries):
            sleep(0.026167)
            if i == 0:
                a1 = angle_J1[i]
                a2 = angle_J2[i]
                a3 = angle_J3[i]
                a4 = angle_J4[i]
                a5 = angle_J5[i]
                a6 = angle_J6[i]
            else:
                a1 = (angle_J1[i] - angle_J1[i - 1])
                a2 = (angle_J2[i] - angle_J2[i - 1])
                a3 = (angle_J3[i] - angle_J3[i - 1])
                a4 = (angle_J4[i] - angle_J4[i - 1])
                a5 = (angle_J5[i] - angle_J5[i - 1])
                a6 = (angle_J6[i] - angle_J6[i - 1])
            # 发送时间序列和绝对角度
            dataunit1 = [timeseries[i], angle_J1[i], angle_J2[i], angle_J3[i],
                                        angle_J4[i], angle_J5[i], angle_J6[i]]
            # 发送时间序列和相对角度
            dataunit2 = [timeseries[i], a1, a2, a3, a4, a5, a6]

            data = json.dumps(((dataunit1,dataunit2),
                              (motorPower[i], motorEnergy[i],speed[i]),
                              ([angle_J1[i], angle_J2[i], angle_J3[i],
                                angle_J4[i], angle_J5[i], angle_J6[i],
                                data_xAxis[i], data_yAxis[i], data_zAxis[i]]))
                              )
            self.sock.send(data.encode('utf-8'))




            print("send ok!")

#            self.sendOnedata(str(dataunit1, dataunit2))
#            self.sendOnedata(str(motorPower[i], motorEnergy[i], speed[i]))
#            self.sendOnedata(str([angle_J1[i], angle_J2[i], angle_J3[i],
#                 angle_J4[i], angle_J5[i], angle_J6[i],
#                 data_xAxis[i],data_yAxis[i], data_zAxis[i]]))

            i = i + 1
        print("send  ok!")


def check_tcp_status(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = (ip, port)
    print('Connecting to %s:%s.' % server_address)
    sock.connect(server_address)

    print("开始发送listJ1")
    for mes in listJ1:
        sleep(1)
        print(str(mes))
        str_mes = str(mes)
        sock.sendall(str_mes.encode())

    sock.sendall('0')






    print('Closing socket.')
    sleep(1)
    data = sock.recv(1024)
    print(data.decode())
    sock.close()


if __name__ == "__main__":
 #   print (check_tcp_status("127.0.0.1", 12345))
    robot_net = robotsimlink()