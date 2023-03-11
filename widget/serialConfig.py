import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from serialOp.serialdemo import *

def readQss(style):

    with open(style, 'r') as f:
        return f.read()




class serialConfig(QDialog, Pyqt5_Serial):
    serialInfo_signal = pyqtSignal(str, str,str,str)

    def __init__(self, parent):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        str = os.getcwd() + "\\..\\qssStyle\\new7.qss"
        qssStyle = readQss(str)
        self.setStyleSheet(qssStyle)
        self.setWindowTitle("串口配置")
        self.setWindowIcon(QIcon(os.getcwd() + "\\..\\image\\串口配置.png"))
        settinglayout = QFormLayout()
        settinglayout.addRow(self.s1__lb_3, self.s1__box_3)
        settinglayout.addRow(self.s1__lb_4, self.s1__box_4)
        settinglayout.addRow(self.s1__lb_5, self.s1__box_5)
        settinglayout.addRow(self.s1__lb_6, self.s1__box_6)

        btns = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        settinglayout.addWidget(btns)
        self.setLayout(settinglayout)

        btns.accepted.connect(self.accept)
        btns.rejected.connect(self.reject)

        self.adjustSize()

    def accept(self):
        super().accept()
        self.serialInfo_signal.emit(self.s1__box_3.currentText(),
                                   self.s1__box_4.currentText(),
                                   self.s1__box_6.currentText(),
                                   self.s1__box_5.currentText())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = serialConfig(None)
    main.show()
    sys.exit(app.exec_())
