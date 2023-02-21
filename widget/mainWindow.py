import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from dbTree import *
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


class mainWindow(QMainWindow):
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

        mainWidget.setLayout(Hlayout)
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


