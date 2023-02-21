import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from dbTree import *
import pymysql
from db.sheetOp import *
from mainWindow import *



class setdbMenu(QMenu):
    def __init__(self, parentMenu, parentWidget):
        self.parentMenu = parentMenu
        self.parentWidget = parentWidget
        self.initMenu()

    def initMenu(self):
        dbAct_link = QAction('连接数据库', self.parentWidget)  # 创建动作
        self.parentMenu.addAction(dbAct_link)  # 添加动作
        dbAct_link.triggered.connect(dislinkdb)  # 关联相关操作

        dbAct_dislink = QAction('断开数据库', self.parentWidget)  # 创建动作
        self.parentMenu.addAction(dbAct_dislink)  # 添加动作
        dbAct_dislink.triggered.connect(dislinkdb)  # 关联相关操作

        dbAct_syndb = QAction('同步数据库到树', self.parentWidget)  # 创建动作
        self.parentMenu.addAction(dbAct_syndb)  # 添加动作
        dbAct_syndb.triggered.connect(dislinkdb)  # 关联相关操作



