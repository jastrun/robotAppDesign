import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from dbTree import *


class menuBar(QMenuBar):
    def __init__(self,parent=None):
        super().__init__()
        initBar()

    def initBar(self):

