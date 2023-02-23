from db.dbTree import *
from serialOp.serialdemo import *
import pyqtgraph as pg
from graph import *

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
        # 菜单栏设置
        self.initMenuBar()
        # 创建可拖拽的条
        splitter1 = QSplitter(Qt.Horizontal)  # 水平
        splitter2 = QSplitter(Qt.Vertical)  # 垂直
        Vlayout = QVBoxLayout()  # 垂直布局
        # 设置机器人数据库树
        splitter1.addWidget(self.robotTree)
        #  添加绘图区
        splitter1.addWidget(self.graph)

        splitter2.addWidget(splitter1)
        # 添加串口
        splitter2.addWidget(self.serialWidget)  # 添加到窗口中

        Vlayout.addWidget(splitter2)
        mainWidget.setLayout(Vlayout)

        self.setCentralWidget(mainWidget)
        # 设置大小
        self.resize(1200, 900)
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

        graphmenu = menubar.addMenu("图")

        graAct_creatGra = QAction('新建图', self)  # 创建动作
        graphmenu.addAction(graAct_creatGra)  # 添加动作
        graAct_creatGra.triggered.connect(self.graph.graSlot_creatGra)  # 关联相关操作

        graAct_CascadeMode = QAction('级联模式', self)  # 创建动作
        graphmenu.addAction(graAct_CascadeMode)  # 添加动作
        graAct_CascadeMode.triggered.connect(self.graph.graSlot_CascadeMode)  # 关联相关操作

        graAct_TabMode = QAction('平铺模式', self)  # 创建动作
        graphmenu.addAction(graAct_TabMode)  # 添加动作
        graAct_TabMode.triggered.connect(self.graph.graSlot_TabMode)  # 关联相关操作

    def initSerial(self):
        serialWidget = QWidget()  # 串口窗口
        serialLayout = QGridLayout()  # 串口布局
        # 设置部分布局
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
        settinglayout.addRow(self.label, self.lineEdit)
        settinglayout.addRow(self.label_2, self.lineEdit_2)
        settinglayout.addRow(self.serialstateLabel)
        serialLayout.addLayout(settinglayout, 0, 0)
        # 发送部分布局
        sendLayout = QGridLayout()
        sendLayout.addWidget(self.s3__send_text, 0, 0, 1, 3)
        sendLayout.addWidget(self.s3__send_button, 1, 0)
        sendLayout.addWidget(self.s3__clear_button, 1, 1)
        sendLayout.addWidget(self.hex_send, 1, 2)
        sendLayout.addWidget(self.timer_send_cb, 2, 0)
        sendLayout.addWidget(self.lineEdit_3, 2, 1)
        sendLayout.addWidget(self.dw, 2, 2)
        serialLayout.addLayout(sendLayout, 0, 2)
        # 接收部分布局
        receiveLayout = QFormLayout()
        receiveLayout.addRow(self.s2__receive_text)
        receiveLayout.addRow(self.hex_receive, self.s2__clear_button)
        serialLayout.addLayout(receiveLayout, 0, 1)
        # 设置总布局
        serialWidget.setLayout(serialLayout)
        return serialWidget

    def initGraph(self):
        # 绘图部分页面布置

        pw = pg.PlotWidget()

        return pw
