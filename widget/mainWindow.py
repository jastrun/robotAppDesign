
from PyQt5.QtWebEngineWidgets import *

from db.dbTree import *
from serialConfig import serialConfig
from serialOp.serialdemo import *
import pyqtgraph as pg
from graph import *
import os
from PyQt5.QtGui import QIcon
import ctypes


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
        self.dbToolBar = self.addToolBar("db")
        self.robotTree = dbTree(db)  # 获取数据库部分的树
        self.serialWidget = self.initSerial()  # 获取串口部分设置的窗口
        self.graph = graphDemo(self)
        #       self.pw = self.initGraph()
        self.initUI()

    def initUI(self):
        # 主布局窗口
        mainWidget = QWidget()
        # 设置标题
        self.setWindowTitle('机器人运动信息存储与显示工具')
        # 图标设置
        self.setWindowIcon(QIcon(os.getcwd() + "\\..\\image\\机器人icon.png"))
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(os.getcwd() + "\\..\\image\\机器人.png")
        # 菜单栏设置
        self.initMenuBar()
        self.initToolBar()
        # 创建可拖拽的条
        splitter1 = QSplitter(Qt.Horizontal)  # 水平
        splitter2 = QSplitter(Qt.Vertical)  # 垂直
        Vlayout = QVBoxLayout()  # 垂直布局
        # 设置机器人数据库树
        #       splitter1.addWidget(self.robotTree)
        self.treedock = QDockWidget("database", self)
        self.treedock.setWidget(self.robotTree)
        self.treedock.hide()
        self.addDockWidget(Qt.LeftDockWidgetArea, self.treedock)


        #  添加绘图区
 #       splitter1.addWidget(self.graph)
        self.webview = QWebEngineView(self)
        url="D:/莫愁/Documents/pythonproj/robotAPP/widget/test.html"
        self.webview.load(QUrl(url))
        splitter1.addWidget(self.webview)


        # 设置串口窗口
        self.serialConfigDialog = serialConfig(self)
        self.serialConfigDialog.serialInfo_signal.connect(self.acceptSerialInfo)

        splitter1.setStretchFactor(10, 1)

        splitter2.addWidget(splitter1)
        # 添加串口
        #    splitter2.addWidget(self.serialWidget)  # 添加到窗口中

        #    self.serialdock = QDockWidget("串口", self)
        #    self.serialdock.setWidget(self.serialWidget)
        #    self.addDockWidget(Qt.BottomDockWidgetArea, self.serialdock)

        Vlayout.addWidget(splitter2)
        mainWidget.setLayout(Vlayout)

        self.setCentralWidget(mainWidget)
        # 设置大小
        self.resize(1200, 900)
        self.show()

    def initMenuBar(self):
        self.menubar = self.menuBar()
        self.menubar.addMenu(QIcon(os.getcwd() + "\\..\\image\\机器人icon.png"), "工具")
        # 数据库窗口
        self.dbmenu = self.menubar.addMenu("数据库")

        self.dbAct_syndb = QAction(QIcon(os.getcwd() + "\\..\\image\\同步.png"), '同步数据库到树', self)  # 创建动作
        self.dbmenu.addAction(self.dbAct_syndb)  # 添加动作
        self.dbAct_syndb.triggered.connect(self.robotTree.TBdb)  # 关联相关操作

        self.dbAct_newRobot = QAction(QIcon(os.getcwd() + "\\..\\image\\新建机器人.png"), '新建机器人', self)  # 创建动作
        self.dbmenu.addAction(self.dbAct_newRobot)  # 添加动作
        self.dbAct_newRobot.triggered.connect(self.robotTree.creatRobot)  # 关联相关操作

        self.dbAct_deleteRobot = QAction(QIcon(os.getcwd() + "\\..\\image\\删除机器人.png"), '删除机器人', self)  # 创建动作
        self.dbmenu.addAction(self.dbAct_deleteRobot)  # 添加动作
        self.dbAct_deleteRobot.triggered.connect(self.robotTree.deleteRobot)  # 关联相关操作
        # 图窗口
        self.graphmenu = self.menubar.addMenu("图")

        self.graAct_creatGra = QAction(QIcon(os.getcwd() + "\\..\\image\\绘图.png"), '新建图', self)  # 创建动作
        self.graphmenu.addAction(self.graAct_creatGra)  # 添加动作
        self.graAct_creatGra.triggered.connect(self.graph.graSlot_creatGra)  # 关联相关操作

        self.graAct_CascadeMode = QAction(QIcon(os.getcwd() + "\\..\\image\\级联.png"), '级联模式', self)  # 创建动作
        self.graphmenu.addAction(self.graAct_CascadeMode)  # 添加动作
        self.graAct_CascadeMode.triggered.connect(self.graph.graSlot_CascadeMode)  # 关联相关操作

        self.graAct_TabMode = QAction(QIcon(os.getcwd() + "\\..\\image\\平铺.png"), '平铺模式', self)  # 创建动作
        self.graphmenu.addAction(self.graAct_TabMode)  # 添加动作
        self.graAct_TabMode.triggered.connect(self.graph.graSlot_TabMode)  # 关联相关操作
        # 串口窗口
        self.serialmenu = self.menubar.addMenu("串口")

        self.serial_Config = QAction(QIcon(os.getcwd() + "\\..\\image\\串口配置.png"), '串口配置', self)
        self.serialmenu.addAction(self.serial_Config)  # 添加动作
        self.serial_Config.triggered.connect(lambda x: self.serialConfigDialog.exec_())

        self.serial_Check = QAction(QIcon(os.getcwd() + "\\..\\image\\串口检测.png"), '串口检测', self)
        self.serialmenu.addAction(self.serial_Check)  # 添加动作
        self.serial_Check.triggered.connect(self.port_check)

        self.serial_Open = QAction(QIcon(os.getcwd() + "\\..\\image\\打开串口.png"),'打开串口', self)
        self.serialmenu.addAction(self.serial_Open)  # 添加动作
        self.serial_Open.triggered.connect(self.port_open)

        self.serial_Close = QAction(QIcon(os.getcwd() + "\\..\\image\\连接断开.png"),'关闭串口', self)
        self.serialmenu.addAction(self.serial_Close)  # 添加动作
        self.serial_Close.triggered.connect(self.port_close)
        self.serial_Close.setEnabled(False)
        # 视图窗口
        self.viewmenu = self.menubar.addMenu("视图")

        self.dbTreeView = QAction(QIcon(os.getcwd() + "\\..\\image\\树状图.png"),'机器人树', self)
        self.viewmenu.addAction(self.dbTreeView)  # 添加动作
        self.dbTreeView.triggered.connect(self.dbTreeVisable)

        self.serialsendView = QAction(QIcon(os.getcwd() + "\\..\\image\\发送.png"),'串口发送', self)
        self.viewmenu.addAction(self.serialsendView)  # 添加动作
        self.serialsendView.triggered.connect(self.serialsendVisable)

        self.serialreceiveView = QAction(QIcon(os.getcwd() + "\\..\\image\\接收.png"),'串口接收', self)
        self.viewmenu.addAction(self.serialreceiveView)  # 添加动作
        self.serialreceiveView.triggered.connect(self.serialreceiveVisable)

    def port_open(self):
        super().port_open()
        if self.ser.isOpen():
            self.serial_Open.setEnabled(False)
            self.serial_Close.setEnabled(True)
    def port_close(self):
        super().port_close()
        if not self.ser.isOpen():
            self.serial_Open.setEnabled(True)
            self.serial_Close.setEnabled(False)


    def dbTreeVisable(self):
        self.treedock.show()

    def serialreceiveVisable(self):
        self.serialreceivedock.show()

    def serialsendVisable(self):
        self.serialsenddock.show()

    def initToolBar(self):
        # 数据库
        self.dbToolBar.addAction(self.dbAct_syndb)
        self.dbToolBar.addAction(self.dbAct_newRobot)
        self.dbToolBar.addAction(self.dbAct_deleteRobot)

        # 图
        self.graphToolBar = QToolBar("graph", self)
        self.addToolBar(self.graphToolBar)
        self.graphToolBar.addAction(self.graAct_creatGra)
        self.graphToolBar.addAction(self.graAct_CascadeMode)
        self.graphToolBar.addAction(self.graAct_TabMode)

        # 串口
        self.graphToolBar = QToolBar("serial", self)
        self.addToolBar(self.graphToolBar)
        self.graphToolBar.addAction(self.serial_Config)
        self.graphToolBar.addAction(self.serial_Close)
        self.graphToolBar.addAction(self.serial_Open)
        self.graphToolBar.addAction(self.serial_Check)
        self.graphToolBar.addWidget(self.s1__box_2)

        # Using a QToolBar object and a toolbar area
        helpToolBar = QToolBar("Help", self)
        self.addToolBar(Qt.LeftToolBarArea, helpToolBar)

    def initSerial(self):
        self.serialWidget = QWidget()  # 串口窗口
        self.serialLayout = QGridLayout()  # 串口布局
        # 设置部分布局
        self.settinglayout = QFormLayout()
        self.settinglayout.addRow(self.s1__lb_1, self.s1__box_1)
        self.settinglayout.addRow(self.s1__lb_2, self.s1__box_2)
        self.settinglayout.addRow("串口状态", self.state_label)
        self.settinglayout.addRow(self.s1__lb_3, self.s1__box_3)
        self.settinglayout.addRow(self.s1__lb_4, self.s1__box_4)
        self.settinglayout.addRow(self.s1__lb_5, self.s1__box_5)
        self.settinglayout.addRow(self.s1__lb_6, self.s1__box_6)
        self.settinglayout.addRow(self.open_button)
        self.settinglayout.addRow(self.close_button)
        self.settinglayout.addRow(self.label, self.lineEdit)
        self.settinglayout.addRow(self.label_2, self.lineEdit_2)
        self.settinglayout.addRow(self.serialstateLabel)
        self.serialLayout.addLayout(self.settinglayout, 0, 0)
        # 发送部分布局
        self.sendLayout = QGridLayout()
        self.sendLayout.addWidget(self.s3__send_text, 0, 0, 1, 3)
        self.sendLayout.addWidget(self.s3__send_button, 1, 0)
        self.s3__send_button.setIcon(QIcon(os.getcwd() + "\\..\\image\\发送.png"))
        self.sendLayout.addWidget(self.s3__clear_button, 1, 1)
        self.s3__clear_button.setIcon(QIcon(os.getcwd() + "\\..\\image\\清除.png"))
        self.sendLayout.addWidget(self.hex_send, 1, 2)
        self.sendLayout.addWidget(self.timer_send_cb, 2, 0)
        self.sendLayout.addWidget(self.lineEdit_3, 2, 1)
        self.sendLayout.addWidget(self.dw, 2, 2)
        #        self.serialLayout.addLayout(self.sendLayout, 0, 2) #将发送窗口添加到总窗口上

        self.serialsendwidget = QWidget()  # 使用dockWidget
        self.serialsendwidget.setLayout(self.sendLayout)
        self.serialsenddock = QDockWidget("串口发送", self)
        self.serialsenddock.setTitleBarWidget(None)
        self.serialsenddock.setWidget(self.serialsendwidget)
        self.serialsenddock.hide()
        self.addDockWidget(Qt.BottomDockWidgetArea, self.serialsenddock)
        self.serialsenddock.setWindowTitle("send")

        # 接收部分布局
        self.receiveLayout = QFormLayout()
        self.receiveLayout.addRow(self.s2__receive_text)
        self.receiveLayout.addRow(self.hex_receive, self.s2__clear_button)
        self.s2__clear_button.setIcon(QIcon(os.getcwd() + "\\..\\image\\清除.png"))
        # self.serialLayout.addLayout(self.receiveLayout, 0, 1) #将接收窗口添加到总窗口上
        self.serialreceivewidget = QWidget()  # 使用dockWidget
        self.serialreceivewidget.setLayout(self.receiveLayout)
        self.serialreceivedock = QDockWidget("串口接收", self)
        self.serialreceivedock.setWidget(self.serialreceivewidget)
        self.serialreceivedock.hide()
        self.addDockWidget(Qt.BottomDockWidgetArea, self.serialreceivedock)
        self.serialreceivedock.setWindowTitle("receive")


        # 设置总布局
        self.serialWidget.setLayout(self.serialLayout)
        return self.serialWidget

    def initGraph(self):
        # 绘图部分页面布置

        pw = pg.PlotWidget()

        return pw

    def acceptSerialInfo(self, Baudrate, bytesize, stopbits, parity):
        print(Baudrate, bytesize, stopbits, parity)

        self.s1__box_3.setCurrentText(Baudrate)
        self.s1__box_4.setCurrentText(bytesize)
        self.s1__box_6.setCurrentText(stopbits)
        self.s1__box_5.setCurrentText(parity)
