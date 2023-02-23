import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import *
import pyqtgraph as pg

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
        subGraph = pg.PlotWidget()
#        self.graphWinDic
        self.midArea.addSubWindow(subGraph)
        subGraph.show()

    def graSlot_TabMode(self):
        print("平铺模式")
        self.midArea.tileSubWindows()

    def graSlot_CascadeMode(self):
        print('层叠模式')
        self.midArea.cascadeSubWindows()
