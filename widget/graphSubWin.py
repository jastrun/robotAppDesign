import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import *
import pyqtgraph as pg
from creatSubGraph import *
import numpy as np

from db.sheetOp import list2str

class disClose(QWidget):
    def __init__(self):
        super().__init__()


        # 最顶端 永远在最前面 无边框（无法拖动）
        self.setWindowFlags(Qt.WindowMaximizeButtonHint)

class graphSubWin(disClose):
    def __init__(self, parent, robot, robotnode, motornode):
        super().__init__()

        self.graph = pg.PlotWidget()
        self.graph.setWindowFlags(Qt.FramelessWindowHint)
        self.plotwid = self.graph.plot()
        self.parent = parent
        self.data=[]
        self.timeseries = []
        self.motorname = motornode.text(0)
        self.robotname = robotnode.text(0)
        self.robotnum = robotnode.text(1)
        self.robot = robot

        self.initUI()
        self.initSlot()

        self.setWindowFlags(Qt.WindowMaximizeButtonHint)

    def closeEvent(self, event):

        flag=self.parent.parent.parent.startFlag
        print(flag)
        if flag:
            QMessageBox.warning(self, "注意：", "数据正在接收，无法关闭窗体！", QMessageBox.Cancel)
            event.ignore()
        else:
            event.accept()

    def initUI(self):
        self.mainWidget = QWidget()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.graph)
        self.Hlayout = QHBoxLayout()
        self.save2dbBtn = QPushButton("保存到数据库")
        self.save2localBtn = QPushButton("保存到本地")

        self.Hlayout.addWidget(self.save2dbBtn)
        self.Hlayout.addWidget(self.save2localBtn)

        self.layout.addLayout(self.Hlayout)
#        self.initToolBar()

#        self.mainWidget.setLayout(self.layout)
#        self.setCentralWidget(self.mainWidget)
        self.setLayout(self.layout)


    def initSlot(self):
        self.save2dbBtn.clicked.connect(self.save2db)

    def initToolBar(self):
        self.savedataToolBar = QToolBar("保存数据", self)
        self.addToolBar(self.savedataToolBar)

    #     self.savedataToolBar.addWidget(QLabel("保存到数据库"))

    def save2db(self):
        #   print(SheetQuary(db, 'motor','where ofRobotNum={}'.format('009')))
        #   datafile = dataFile(r'data.xlsx', '六轴工业机器人', '999')
        if self.motorname == 'J1':
            self.robot.motor1.recordData(list2str(self.timeseries), list2str(self.data), list2str(self.data))
        if self.motorname == 'J2':
            self.robot.motor2.recordData(list2str(self.timeseries), list2str(self.data), list2str(self.data))
        if self.motorname == 'J3':
            self.robot.motor3.recordData(list2str(self.timeseries), list2str(self.data), list2str(self.data))
        if self.motorname == 'J4':
            self.robot.motor4.recordData(list2str(self.timeseries), list2str(self.data), list2str(self.data))
        if self.motorname == 'J5':
            self.robot.motor5.recordData(list2str(self.timeseries), list2str(self.data), list2str(self.data))
        if self.motorname == 'J6':
            self.robot.motor6.recordData(list2str(self.timeseries), list2str(self.data), list2str(self.data))

        print("存入成功！")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    #   app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    main = graphSubWin()
    sys.exit(app.exec_())
