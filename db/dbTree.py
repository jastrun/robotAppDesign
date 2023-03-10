from db.sheetOp import *
from db.creatRobotWidget import *
import os


class dbTree(QTreeWidget):
    def __init__(self, db):
        super().__init__()
        self.root = QTreeWidgetItem(self)
        self.root.setText(0, "机器人数据库")
        self.robotList = []
        self.db = db
        self.initTree()
        self.header().setSectionResizeMode(QHeaderView.Stretch)
        self.header().setSectionResizeMode(0, QHeaderView.ResizeToContents)

    def initTree(self):
        # 设置树控件
        self.setColumnCount(2)  # 制定树控件为两列
        self.setHeaderLabels(["编码", "名字"])  # 设置列标签
        self.expandAll()  # 设置所有的节点为展开的状态
        self.TBdb()  # 初始化同步数据库

    # 同步数据库中的机器人到树
    def TBdb(self):
        # 将数据同步到表格中
        root = self.root
        print(self.invisibleRootItem().removeChild(root))
        self.root = QTreeWidgetItem(self)
        self.root.setText(0, "机器人数据库")
        self.root.setExpanded(True)
        # 查询机器人表格
        robotSheet = SheetQuary(self.db, 'robot')
        print(robotSheet)
        for num, name in robotSheet:
            # 添加机器人
            robot = QTreeWidgetItem(self.root)
            if name == '六轴工业机器人':
                robot.setIcon(1, QIcon(os.getcwd() + "\\..\\image\\工业机器人.png"))
            elif name=='机器人':
                robot.setIcon(1, QIcon(os.getcwd() + "\\..\\image\\机器人.png"))
            robot.setText(0, num)
            robot.setText(1, name)
            # 查询运动节点表格
            motorSheet = SheetQuary(db, 'motor', 'where ofRobotNum={}'.format(num))
            for name in motorSheet:
                motor = QTreeWidgetItem(robot)
                motor.setIcon(1, QIcon(os.getcwd() + "\\..\\image\\轴承.png"))
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
        dialog = creatRobotWidget(self)
        dialog.robotinfo_signal.connect(self.acceptNewRobot)
        dialog.exec_()

    def acceptNewRobot(self, num, name, type):
        print(type)
        if type == ' 六轴工业机器人':
            temprobot = SixAxisRobot(self.db, num, name)
        self.robotList.append(temprobot)
        # 同步数据库
        self.TBdb()

    def deleteRobot(self):
        # 删除节点
        item = self.currentItem()
        for robot in self.robotList:
            if robot.num == item.data(0, 0):
                robot.deleteSelf(self.db)  # 从数据库中删除机器人
        item.parent().removeChild(item)
