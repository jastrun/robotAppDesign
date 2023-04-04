import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import *
import pyqtgraph as pg
from creatSubGraph import *
import numpy as np


class graphSubWin(QMainWindow):
    def __init__(self,motor):
        super().__init__()
        self.graph=pg.PlotWidget()

        self.motor=motor.text(0)
        self.robot = motor.parent().text(0)
        self.robotnum=motor.parent().text(1)



        self.initUI()

    def initUI(self):
        self.mainWidget=QWidget()
        self.layout=QVBoxLayout()
        self.layout.addWidget(self.graph)
        self.Hlayout=QHBoxLayout()
        self.save2dbBtn=QPushButton("保存到数据库")
        self.save2localBtn=QPushButton("保存到本地")

        self.Hlayout.addWidget(self.save2dbBtn)
        self.Hlayout.addWidget(self.save2localBtn)

        self.layout.addLayout(self.Hlayout)
        self.initToolBar()
        self.mainWidget.setLayout(self.layout)
        self.setCentralWidget(self.mainWidget)

        self.show()

    def initSlot(self):
        self.save2dbBtn.clicked.connect()

    def initToolBar(self):
        self.savedataToolBar = QToolBar("保存数据", self)
        self.addToolBar(self.savedataToolBar)
   #     self.savedataToolBar.addWidget(QLabel("保存到数据库"))




if __name__ == '__main__':
    app = QApplication(sys.argv)

    #   app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    main = graphSubWin()
    sys.exit(app.exec_())
