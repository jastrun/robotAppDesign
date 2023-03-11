import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import *
import pyqtgraph as pg


class Ui_Form(object):
    def setupUi(self, Form):
        if False:
            Form = QWidget()
        self.layout = QVBoxLayout()

        self.midArea = QMdiArea()
   #     self.midArea.setViewMode(QMdiArea.TabbedView)

        self.layout.addWidget(self.midArea)
        Form.setLayout(self.layout)
