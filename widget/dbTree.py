import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from db.sheetOp import *


class dbTree(QTreeWidget):
    def __init__(self, db):
        super().__init__()
        self.root = QTreeWidgetItem(self)
        self.root.setText(0,"机器人数据库")
        self.robotList=[]
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
        root=self.root
        print(self.invisibleRootItem().removeChild(root))
        self.root = QTreeWidgetItem(self)
        self.root.setText(0,"机器人数据库")
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
            # 添加运动节点
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

    # 新建机器人
    def creatRobot(self):
        SixAxisRobot(self.db, '0013')

    def deleteRobot(self):
        # 删除节点
        item=self.currentItem()
        for item in self.selectedItems():
            item.parent().removeChild(item)



