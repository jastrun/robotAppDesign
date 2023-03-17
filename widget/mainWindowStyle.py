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



