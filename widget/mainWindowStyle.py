import mainWindow
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import os


def readQss(style):

    with open(style, 'r') as f:
        return f.read()


class diyStyleOfmainWindow(mainWindow.mainWindow):
    def __init__(self):
        super().__init__()
        self.adjustSize()
        str=os.getcwd()+"\\..\\qssStyle\\new1.qss"
        qssStyle = readQss(str)
        self.setStyleSheet(qssStyle)

    def adjustSize(self):
        self.robotTree.setMinimumWidth(350)
