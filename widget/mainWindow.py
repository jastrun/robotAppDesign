import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from dbTree import *


class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置标题
        self.setWindowTitle('机器人运动信息存储与显示工具')
        # 添加菜单栏
        LinkDbAct = QAction('连接数据库', self)
        LinkDbAct.setStatusTip('连接数据库')

        #   连接数据库操作     LinkDbAct.triggered.connect(qApp.quit)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('数据库')
        fileMenu.addAction(LinkDbAct)

        Hlayout = QHBoxLayout()
        mainWidget = QWidget()
        # 机器人树
        robotTRee = dbTree()
        Hlayout.addWidget(robotTRee)

        mainWidget.setLayout(Hlayout)
        self.setCentralWidget(mainWidget)

        # 设置大小
        self.resize(800, 800)

        self.show()
