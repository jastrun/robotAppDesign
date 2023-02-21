import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class creatRobotWidget(QDialog):
    robotinfo_signal=pyqtSignal(str,str)
    def __init__(self,parent):
        super().__init__(parent)
        self.numEdit=QLineEdit()
        self.nameEdit=QLineEdit()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("创建机器人")
        layout=QFormLayout()
        btns=QDialogButtonBox(QDialogButtonBox.Ok|QDialogButtonBox.Cancel)
        layout.addRow(QLabel("机器人标签"),self.nameEdit)
        layout.addRow(QLabel("机器人编码"), self.numEdit)
        layout.addWidget(btns)
        self.setLayout(layout)

        btns.accepted.connect(self.accept)
        btns.rejected.connect(self.reject)

    def accept(self):
        super().accept()
        self.robotinfo_signal.emit(self.numEdit.text(),self.nameEdit.text())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = creatRobotWidget()
    sys.exit(app.exec_())