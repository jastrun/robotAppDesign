import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import *
import pyqtgraph as pg
from creatSubGraph import *

from graph_ui import Ui_Form


class graphDemo(QWidget, Ui_Form):
    creatGra_signal = pyqtSignal(str)
    CascadeMode_signal = pyqtSignal()
    TileMode_signal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__()
        self.graphWinDic = {}
        self.setupUi(self)

    # 槽
    def graSlot_creatGra(self):
        dialog = creatSubGraph(self)
        dialog.graphInfo_signal.connect(self.acceptNewGraph)
        dialog.exec_()

    def acceptNewGraph(self, title, port):
        subWin = QMdiSubWindow()  # 创建子窗口
        subGraph = pg.PlotWidget()  # 创建绘图窗口
        subGraph.setBackground('w')
        subWin.setWidget(subGraph)  # 将绘图添加到子窗口中和
        subWin.setWindowTitle(title)  # 设置标题
        self.graphWinDic[title] = port  # 关联端口并将键值对存储到字典中
        self.midArea.addSubWindow(subWin)  # 将子窗口添加到MDI中
        subGraph.show()

    def graSlot_TabMode(self):
        print("平铺模式")
        self.midArea.tileSubWindows()

    def graSlot_CascadeMode(self):
        print('层叠模式')
        self.midArea.cascadeSubWindows()
