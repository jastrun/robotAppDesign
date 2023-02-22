import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class creatRobotWidget(QDialog):
    robotinfo_signal = pyqtSignal(str, str,str)

    def __init__(self, parent):
        super().__init__(parent)
        self.numEdit = QLineEdit()
        self.nameEdit = QLineEdit()
        self.typeofrobot = QComboBox()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("创建机器人")
        layout = QFormLayout()
        btns = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        self.nameEdit.setPlaceholderText("请输入名称")
        self.numEdit.setPlaceholderText("请输入编码(数字)")
        self.numEdit.setValidator(QRegExpValidator(QRegExp("[0-9]*$"), self))
        self.typeofrobot.addItem("六轴工业机器人")
        self.typeofrobot.currentText()

        layout.addRow("机器人标签", self.nameEdit)
        layout.addRow("机器人编码", self.numEdit)
        layout.addRow("机器人种类", self.typeofrobot)
        layout.addWidget(btns)
        self.setLayout(layout)

        btns.accepted.connect(self.accept)
        btns.rejected.connect(self.reject)

    def accept(self):
        if self.numEdit.text()=='' or self.nameEdit.text()=='':
            QMessageBox.warning(self, 'Warning', 'Please enter some text.')
        else:
            super().accept()
            self.robotinfo_signal.emit(self.numEdit.text(), self.nameEdit.text(),self.typeofrobot.currentText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = creatRobotWidget()
    sys.exit(app.exec_())
