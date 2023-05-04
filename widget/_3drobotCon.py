import os
import sys

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import *

def readQss(style):
    with open(style, 'r') as f:
        return f.read()

class _3drobotCon(QWidget):

    # 初始化信号
    styledata_singal = pyqtSignal(list)

    def __init__(self):
        super().__init__()
        self.style = style_robot()

        self.initUI()
        self.initSlot()


    def initUI(self):
        self.layout = QGridLayout()
        # 长度设置
        self.setJ1_Len = QSpinBox()
        self.setJ1_Len.setValue(6)
        self.setJ2_Len = QSpinBox()
        self.setJ2_Len.setValue(6)
        self.setJ3_Len = QSpinBox()
        self.setJ3_Len.setValue(6)
        self.setJ4_Len = QSpinBox()
        self.setJ4_Len.setValue(6)
        self.setJ5_Len = QSpinBox()
        self.setJ5_Len.setValue(6)
        self.setJ6_Len = QSpinBox()
        self.setJ6_Len.setValue(6)
        #宽度设置
        self.setJ1_Width = QSpinBox()
        self.setJ1_Width.setValue(6)
        self.setJ2_Width  = QSpinBox()
        self.setJ2_Width.setValue(6)
        self.setJ3_Width  = QSpinBox()
        self.setJ3_Width.setValue(6)
        self.setJ4_Width  = QSpinBox()
        self.setJ4_Width.setValue(6)
        self.setJ5_Width  = QSpinBox()
        self.setJ5_Width.setValue(6)
        self.setJ6_Width  = QSpinBox()
        self.setJ6_Width.setValue(6)
        # 颜色设置
        self.setJ1_color1 = QPushButton()
        self.setJ2_color1 = QPushButton()
        self.setJ3_color1 = QPushButton()
        self.setJ4_color1 = QPushButton()
        self.setJ5_color1 = QPushButton()
        self.setJ6_color1 = QPushButton()

        self.setJ1_color2 = QPushButton()
        self.setJ2_color2 = QPushButton()
        self.setJ3_color2 = QPushButton()
        self.setJ4_color2 = QPushButton()
        self.setJ5_color2 = QPushButton()
        self.setJ6_color2 = QPushButton()

        self.setJ1_color3 = QPushButton()
        self.setJ2_color3 = QPushButton()
        self.setJ3_color3 = QPushButton()
        self.setJ4_color3 = QPushButton()
        self.setJ5_color3 = QPushButton()
        self.setJ6_color3 = QPushButton()

        self.okBtn = QPushButton("确定")
        self.cancelBtn = QPushButton("取消")

        self.layout.addWidget(QLabel("轴"), 0, 0)
        self.layout.addWidget(QLabel("长度"), 0, 1)
        self.layout.addWidget(QLabel("宽度"), 0, 2)
        self.layout.addWidget(QLabel("颜色"), 0, 3)
        self.layout.addWidget(QLabel("颜色"), 0, 4)
        self.layout.addWidget(QLabel("颜色"), 0, 5)
        self.layout.addWidget(QLabel("J1"),1,0)
        self.layout.addWidget(self.setJ1_Len, 1, 1)
        self.layout.addWidget(self.setJ1_Width, 1, 2)
        self.layout.addWidget(self.setJ1_color1, 1, 3)
        self.layout.addWidget(self.setJ1_color2, 1, 4)
        self.layout.addWidget(self.setJ1_color3, 1, 5)

        self.layout.addWidget(QLabel("J2"), 2, 0)
        self.layout.addWidget(self.setJ2_Len, 2, 1)
        self.layout.addWidget(self.setJ2_Width, 2, 2)
        self.layout.addWidget(self.setJ2_color1, 2, 3)
        self.layout.addWidget(self.setJ2_color2, 2, 4)
        self.layout.addWidget(self.setJ2_color3, 2, 5)

        self.layout.addWidget(QLabel("J3"), 3, 0)
        self.layout.addWidget(self.setJ3_Len, 3, 1)
        self.layout.addWidget(self.setJ3_Width, 3, 2)
        self.layout.addWidget(self.setJ3_color1, 3, 3)
        self.layout.addWidget(self.setJ3_color2, 3, 4)
        self.layout.addWidget(self.setJ3_color3, 3, 5)

        self.layout.addWidget(QLabel("J4"), 4, 0)
        self.layout.addWidget(self.setJ4_Len, 4, 1)
        self.layout.addWidget(self.setJ4_Width, 4, 2)
        self.layout.addWidget(self.setJ4_color1, 4, 3)
        self.layout.addWidget(self.setJ4_color2, 4, 4)
        self.layout.addWidget(self.setJ4_color3, 4, 5)

        self.layout.addWidget(QLabel("J5"), 5, 0)
        self.layout.addWidget(self.setJ5_Len, 5, 1)
        self.layout.addWidget(self.setJ5_Width, 5, 2)
        self.layout.addWidget(self.setJ5_color1, 5, 3)
        self.layout.addWidget(self.setJ5_color2, 5, 4)
        self.layout.addWidget(self.setJ5_color3, 5, 5)

        self.layout.addWidget(QLabel("J6"), 6, 0)
        self.layout.addWidget(self.setJ6_Len, 6, 1)
        self.layout.addWidget(self.setJ6_Width, 6, 2)
        self.layout.addWidget(self.setJ6_color1, 6, 3)
        self.layout.addWidget(self.setJ6_color2, 6, 4)
        self.layout.addWidget(self.setJ6_color3, 6, 5)

        self.layout.addWidget(self.okBtn, 7, 0,1,3)
        self.layout.addWidget(self.cancelBtn, 7, 3,1,3)


        self.setLayout(self.layout)

        str = os.getcwd() + "\\..\\qssStyle\\new7.qss"
        qssStyle = readQss(str)
        self.setStyleSheet(qssStyle)
        self.resize(200,200)

    def showDialog(self,motor):
        col = QColorDialog.getColor()

        if col.isValid():
            motor.setStyleSheet('QWidget{background-color:%s} ' % col.name())  # 设置按钮颜色
            self.setStyle()  # 设置样式
            self.sendData()
        print(col.red(),col.green(),col.blue())
        return col.red()/255,col.green()/255,col.blue()/255

    def initSlot(self):
        self.okBtn.clicked.connect(self.sendData)
        self.okBtn.clicked.connect(self.close)
        self.cancelBtn.clicked.connect(self.close)

        # 实时改变
        self.setJ1_Len.valueChanged.connect(self.sendData)
        self.setJ2_Len.valueChanged.connect(self.sendData)
        self.setJ3_Len.valueChanged.connect(self.sendData)
        self.setJ4_Len.valueChanged.connect(self.sendData)
        self.setJ5_Len.valueChanged.connect(self.sendData)
        self.setJ6_Len.valueChanged.connect(self.sendData)
        self.setJ1_Width.valueChanged.connect(self.sendData)
        self.setJ2_Width.valueChanged.connect(self.sendData)
        self.setJ3_Width.valueChanged.connect(self.sendData)
        self.setJ4_Width.valueChanged.connect(self.sendData)
        self.setJ5_Width.valueChanged.connect(self.sendData)
        self.setJ6_Width.valueChanged.connect(self.sendData)



        self.setJ1_color1.clicked.connect(lambda :self.showDialog(self.setJ1_color1))
        self.setJ2_color1.clicked.connect(lambda :self.showDialog(self.setJ2_color1))
        self.setJ3_color1.clicked.connect(lambda :self.showDialog(self.setJ3_color1))
        self.setJ4_color1.clicked.connect(lambda :self.showDialog(self.setJ4_color1))
        self.setJ5_color1.clicked.connect(lambda :self.showDialog(self.setJ5_color1))
        self.setJ6_color1.clicked.connect(lambda :self.showDialog(self.setJ6_color1))

        self.setJ1_color2.clicked.connect(lambda: self.showDialog(self.setJ1_color2))
        self.setJ2_color2.clicked.connect(lambda: self.showDialog(self.setJ2_color2))
        self.setJ3_color2.clicked.connect(lambda: self.showDialog(self.setJ3_color2))
        self.setJ4_color2.clicked.connect(lambda: self.showDialog(self.setJ4_color2))
        self.setJ5_color2.clicked.connect(lambda: self.showDialog(self.setJ5_color2))
        self.setJ6_color2.clicked.connect(lambda: self.showDialog(self.setJ6_color2))

        self.setJ1_color3.clicked.connect(lambda: self.showDialog(self.setJ1_color3))
        self.setJ2_color3.clicked.connect(lambda: self.showDialog(self.setJ2_color3))
        self.setJ3_color3.clicked.connect(lambda: self.showDialog(self.setJ3_color3))
        self.setJ4_color3.clicked.connect(lambda: self.showDialog(self.setJ4_color3))
        self.setJ5_color3.clicked.connect(lambda: self.showDialog(self.setJ5_color3))
        self.setJ6_color3.clicked.connect(lambda: self.showDialog(self.setJ6_color3))


    def sendData(self):
        # 更新样式里的数据
        self.setStyle()
        self.styledata_singal.emit(self.style.getdata())
        print(self.style.getdata())




    def setStyle(self):
        # 设置长度
        self.style.style_J1.len = self.setJ1_Len.value()
        self.style.style_J2.len = self.setJ2_Len.value()
        self.style.style_J3.len = self.setJ3_Len.value()
        self.style.style_J4.len = self.setJ4_Len.value()
        self.style.style_J5.len = self.setJ5_Len.value()
        self.style.style_J6.len = self.setJ6_Len.value()
        # 设置宽度
        self.style.style_J1.width = self.setJ1_Width.value()
        self.style.style_J2.width = self.setJ2_Width.value()
        self.style.style_J3.width = self.setJ3_Width.value()
        self.style.style_J4.width = self.setJ4_Width.value()
        self.style.style_J5.width = self.setJ5_Width.value()
        self.style.style_J6.width = self.setJ6_Width.value()
        # 设置第一列颜色
        self.style.style_J1.color[0][0] = self.setJ1_color1.palette().color(QPalette.Background).red() / 255
        self.style.style_J1.color[0][1] = self.setJ1_color1.palette().color(QPalette.Background).green() / 255
        self.style.style_J1.color[0][2] = self.setJ1_color1.palette().color(QPalette.Background).blue() / 255

        self.style.style_J2.color[0][0] = self.setJ2_color1.palette().color(QPalette.Background).red() / 255
        self.style.style_J2.color[0][1] = self.setJ2_color1.palette().color(QPalette.Background).green() / 255
        self.style.style_J2.color[0][2] = self.setJ2_color1.palette().color(QPalette.Background).blue() / 255

        self.style.style_J3.color[0][0] = self.setJ3_color1.palette().color(QPalette.Background).red() / 255
        self.style.style_J3.color[0][1] = self.setJ3_color1.palette().color(QPalette.Background).green() / 255
        self.style.style_J3.color[0][2] = self.setJ3_color1.palette().color(QPalette.Background).blue() / 255

        self.style.style_J4.color[0][0] = self.setJ4_color1.palette().color(QPalette.Background).red() / 255
        self.style.style_J4.color[0][1] = self.setJ4_color1.palette().color(QPalette.Background).green() / 255
        self.style.style_J4.color[0][2] = self.setJ4_color1.palette().color(QPalette.Background).blue() / 255

        self.style.style_J5.color[0][0] = self.setJ5_color1.palette().color(QPalette.Background).red() / 255
        self.style.style_J5.color[0][1] = self.setJ5_color1.palette().color(QPalette.Background).green() / 255
        self.style.style_J5.color[0][2] = self.setJ5_color1.palette().color(QPalette.Background).blue() / 255

        self.style.style_J6.color[0][0] = self.setJ6_color1.palette().color(QPalette.Background).red() / 255
        self.style.style_J6.color[0][1] = self.setJ6_color1.palette().color(QPalette.Background).green() / 255
        self.style.style_J6.color[0][2] = self.setJ6_color1.palette().color(QPalette.Background).blue() / 255

        # 设置第二列颜色
        self.style.style_J1.color[1][0] = self.setJ1_color2.palette().color(QPalette.Background).red() / 255
        self.style.style_J1.color[1][1] = self.setJ1_color2.palette().color(QPalette.Background).green() / 255
        self.style.style_J1.color[1][2] = self.setJ1_color2.palette().color(QPalette.Background).blue() / 255

        self.style.style_J2.color[1][0] = self.setJ2_color2.palette().color(QPalette.Background).red() / 255
        self.style.style_J2.color[1][1] = self.setJ2_color2.palette().color(QPalette.Background).green() / 255
        self.style.style_J2.color[1][2] = self.setJ2_color2.palette().color(QPalette.Background).blue() / 255

        self.style.style_J3.color[1][0] = self.setJ3_color2.palette().color(QPalette.Background).red() / 255
        self.style.style_J3.color[1][1] = self.setJ3_color2.palette().color(QPalette.Background).green() / 255
        self.style.style_J3.color[1][2] = self.setJ3_color2.palette().color(QPalette.Background).blue() / 255

        self.style.style_J4.color[1][0] = self.setJ4_color2.palette().color(QPalette.Background).red() / 255
        self.style.style_J4.color[1][1] = self.setJ4_color2.palette().color(QPalette.Background).green() / 255
        self.style.style_J4.color[1][2] = self.setJ4_color2.palette().color(QPalette.Background).blue() / 255

        self.style.style_J5.color[1][0] = self.setJ5_color2.palette().color(QPalette.Background).red() / 255
        self.style.style_J5.color[1][1] = self.setJ5_color2.palette().color(QPalette.Background).green() / 255
        self.style.style_J5.color[1][2] = self.setJ5_color2.palette().color(QPalette.Background).blue() / 255

        self.style.style_J6.color[1][0] = self.setJ6_color2.palette().color(QPalette.Background).red() / 255
        self.style.style_J6.color[1][1] = self.setJ6_color2.palette().color(QPalette.Background).green() / 255
        self.style.style_J6.color[1][2] = self.setJ6_color2.palette().color(QPalette.Background).blue() / 255

        # 设置第三列颜色
        self.style.style_J1.color[2][0] = self.setJ1_color3.palette().color(QPalette.Background).red() / 255
        self.style.style_J1.color[2][1] = self.setJ1_color3.palette().color(QPalette.Background).green() / 255
        self.style.style_J1.color[2][2] = self.setJ1_color3.palette().color(QPalette.Background).blue() / 255

        self.style.style_J2.color[2][0] = self.setJ2_color3.palette().color(QPalette.Background).red() / 255
        self.style.style_J2.color[2][1] = self.setJ2_color3.palette().color(QPalette.Background).green() / 255
        self.style.style_J2.color[2][2] = self.setJ2_color3.palette().color(QPalette.Background).blue() / 255

        self.style.style_J3.color[2][0] = self.setJ3_color3.palette().color(QPalette.Background).red() / 255
        self.style.style_J3.color[2][1] = self.setJ3_color3.palette().color(QPalette.Background).green() / 255
        self.style.style_J3.color[2][2] = self.setJ3_color3.palette().color(QPalette.Background).blue() / 255

        self.style.style_J4.color[2][0] = self.setJ4_color3.palette().color(QPalette.Background).red() / 255
        self.style.style_J4.color[2][1] = self.setJ4_color3.palette().color(QPalette.Background).green() / 255
        self.style.style_J4.color[2][2] = self.setJ4_color3.palette().color(QPalette.Background).blue() / 255

        self.style.style_J5.color[2][0] = self.setJ5_color3.palette().color(QPalette.Background).red() / 255
        self.style.style_J5.color[2][1] = self.setJ5_color3.palette().color(QPalette.Background).green() / 255
        self.style.style_J5.color[2][2] = self.setJ5_color3.palette().color(QPalette.Background).blue() / 255

        self.style.style_J6.color[2][0] = self.setJ6_color3.palette().color(QPalette.Background).red() / 255
        self.style.style_J6.color[2][1] = self.setJ6_color3.palette().color(QPalette.Background).green() / 255
        self.style.style_J6.color[2][2] = self.setJ6_color3.palette().color(QPalette.Background).blue() / 255

class Data_c:
    # 一行数据
    def __init__(self,name):

        self.name=name
        self.len=6
        self.width=6
        self.color=[[1,0,1,1],[1,0,1,1],[1,0,1,1]]

    def getdata(self):
        self.data=[[self.len,self.width],self.color]
        return self.data

class style_robot:

    def __init__(self):
        self.style_J1 = Data_c('J1')
        self.style_J2 = Data_c('J2')
        self.style_J3 = Data_c('J3')
        self.style_J4 = Data_c('J4')
        self.style_J5 = Data_c('J5')
        self.style_J6 = Data_c('J6')

    def getdata(self):
        self.data=[
            self.style_J1.getdata(),
            self.style_J2.getdata(),
            self.style_J3.getdata(),
            self.style_J4.getdata(),
            self.style_J5.getdata(),
            self.style_J6.getdata()
        ]
        return self.data


if __name__ == '__main__':
    app1 = QApplication(sys.argv)
    main = _3drobotCon()
    p = style_robot()
    print(p.getdata())
    main.show()
    sys.exit(app1.exec_())