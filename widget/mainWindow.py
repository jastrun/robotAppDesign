import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from dbTree import *
from serialOp import serialdemo, serialdemo_ui
from serialOp.serialdemo import *

# 连接数据库
try:
    db = pymysql.connect(host="localhost",
                         user="root",
                         password="aoteman000",
                         database="robotinfo",
                         charset="utf8"
                         )
    print("数据库连接成功")
except pymysql.Error as e:
    print("数据库连接失败：" + str(e))
    cur = db.cursor()


class mainWindow(QMainWindow, Pyqt5_Serial):
    def __init__(self):
        super().__init__()
        self.robotTree = dbTree(db)
        self.initUI()

    def initUI(self):
        # 主布局窗口
        mainWidget = QWidget()
        Hlayout = QHBoxLayout()
        # 设置标题
        self.setWindowTitle('机器人运动信息存储与显示工具')
        # 菜单栏设置
        self.initMenuBar()
        # 设置机器人树
        Hlayout.addWidget(self.robotTree)
        Vlayout = QVBoxLayout()
        Vlayout.addLayout(Hlayout)
        mainWidget.setLayout(Vlayout)

        serialLayout = QGridLayout()
        settinglayout = QFormLayout()
        settinglayout.addRow(self.s1__lb_1, self.s1__box_1)
        settinglayout.addRow(self.s1__lb_2, self.s1__box_2)
        settinglayout.addRow("串口状态", self.state_label)
        settinglayout.addRow(self.s1__lb_3, self.s1__box_3)
        settinglayout.addRow(self.s1__lb_4, self.s1__box_4)
        settinglayout.addRow(self.s1__lb_5, self.s1__box_5)
        settinglayout.addRow(self.s1__lb_6, self.s1__box_6)
        settinglayout.addRow(self.open_button)
        settinglayout.addRow(self.close_button)
        settinglayout.addRow(self.label,self.lineEdit)
        settinglayout.addRow(self.label_2, self.lineEdit_2)
        settinglayout.addRow(self.serialstateLabel)
        serialLayout.addLayout(settinglayout, 0, 0)

        sendLayout = QGridLayout()
        sendLayout.addWidget(self.s3__send_text,0,0,1,3)
        sendLayout.addWidget(self.s3__send_button,1,0)
        sendLayout.addWidget(self.s3__clear_button, 1, 1)
        sendLayout.addWidget(self.hex_send, 1, 2)
        sendLayout.addWidget(self.timer_send_cb, 2, 0)
        sendLayout.addWidget(self.lineEdit_3, 2, 1)
        sendLayout.addWidget(self.dw, 2, 2)

        receiveLayout=QFormLayout()
        receiveLayout.addRow(self.s2__receive_text)
        receiveLayout.addRow(self.hex_receive,self.s2__clear_button)

        serialLayout.addLayout(receiveLayout, 0, 1)
        serialLayout.addLayout(sendLayout, 0, 2)
        Vlayout.addLayout(serialLayout)

        self.setCentralWidget(mainWidget)

        # 设置大小
        self.resize(800, 800)

        self.show()

    def initMenuBar(self):
        menubar = self.menuBar()
        dbmenu = menubar.addMenu("数据库")

        dbAct_syndb = QAction('同步数据库到树', self)  # 创建动作
        dbmenu.addAction(dbAct_syndb)  # 添加动作
        dbAct_syndb.triggered.connect(self.robotTree.TBdb)  # 关联相关操作

        dbAct_newRobot = QAction('新建机器人', self)  # 创建动作
        dbmenu.addAction(dbAct_newRobot)  # 添加动作
        dbAct_newRobot.triggered.connect(self.robotTree.creatRobot)  # 关联相关操作

        dbAct_deleteRobot = QAction('删除机器人', self)  # 创建动作
        dbmenu.addAction(dbAct_deleteRobot)  # 添加动作
        dbAct_deleteRobot.triggered.connect(self.robotTree.deleteRobot)  # 关联相关操作
