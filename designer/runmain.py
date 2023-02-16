import sys

import untitled
from PyQt5.QtWidgets import *


class QLabelBuddy(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QLabel与伙伴控件')
        passwordlabel = QLabel('&Password')
        passwordEdit = QLineEdit()
        passwordlabel.setBuddy(passwordEdit)

        namelabel = QLabel('&Name')
        namelineEdit = QLineEdit()
        namelabel.setBuddy(namelineEdit)

        btnOK = QPushButton('&OK')
        btnCancel = QPushButton('&Cancel')


        mainlayout = QGridLayout()
        mainlayout.addWidget(namelabel, 0, 0)
        mainlayout.addWidget(namelineEdit, 0, 1,1,2)

        mainlayout.addWidget(passwordlabel,1,0)
        mainlayout.addWidget(passwordEdit, 1, 1, 1, 2)

        mainlayout.addWidget(btnOK,2,1)
        mainlayout.addWidget(btnCancel, 2, 2)

        self.setLayout(mainlayout)

    def onclickbtn(self):
        self.close(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QLabelBuddy()
    mainWindow.show()
    sys.exit(app.exec_())
