import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import *
import pyqtgraph as pg
from creatSubGraph import *


class graphSubWin(pg.PlotWidget):
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    #   app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    main = graphSubWin()
    sys.exit(app.exec_())
