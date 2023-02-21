import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from db.sheetOp import *
from creatRobotWidget import *


class dbTree(QTreeWidget):
    def __init__(self, db):
        super().__init__()
        self.root = QTreeWidgetItem(self)
        self.root.setText(0, "机器人数据库")
        self.robotList = []
        self.db = db
        self.initTree()

    def initTree(self):
        # 设置树控件
        self.setColumnCount(2)  # 制定树控件为两列
        self.setHeaderLabels(["编码", "名字"])  # 设置列标签
        self.expandAll()  # 设置所有的节点为展开的状态

    # 同步数据库中的机器人到树
    def TBdb(self):
        # 将数据同步到表格中
        root = self.root
        print(self.invisibleRootItem().removeChild(root))
        self.root = QTreeWidgetItem(self)
        self.root.setText(0, "机器人数据库")
        self.root.setExpanded(True)
        # 查询机器人表格
        robotSheet = []
        cur = self.db.cursor()
        sql = "select * from robot"
        cur.execute(sql)
        try:
            for row in cur.fetchall():
                robotSheet.append(row)
            print("同步机器人成功！")
        except pymysql.Error as e:
            print("同步机器人失败！" + str(e))
        print(robotSheet)
        for num, name in robotSheet:
            # 添加根节点
            robot = QTreeWidgetItem(self.root)
            robot.setText(0, num)
            robot.setText(1, name)
            # 查询运动节点表格
            motorSheet = []
            sql = "select * from motor where ofRobotNum={}".format(num)
            cur.execute(sql)
            try:
                for row in cur.fetchall():
                    motorSheet.append(row)
                print("同步运动节点成功！")
            except pymysql.Error as e:
                print("同步运动节点失败" + str(e))
            for name in motorSheet:
                motor = QTreeWidgetItem(robot)
                motor.setText(0, name[0])
        self.db.commit()
        # 更新总列表
        self.robotList = []
        for num, name in robotSheet:
            self.robotList.append(SixAxisRobot(self.db, num, name, insertOrNot=False))
        item = list(robot.num for robot in self.robotList)
        print(item)

    # 新建机器人
    def creatRobot(self):
        dialog=creatRobotWidget(self)
        dialog.robotinfo_signal.connect(self.acceptNewRobot)
        dialog.exec_()

    def acceptNewRobot(self, num, name):
        temprobot = SixAxisRobot(self.db, num,name)
        self.robotList.append(temprobot)

    def deleteRobot(self):
        # 删除节点
        item = self.currentItem()
        for robot in self.robotList:
            if robot.num == item.data(0, 0):
                robot.deleteSelf(self.db) # 从数据库中删除机器人
        item.parent().removeChild(item)

