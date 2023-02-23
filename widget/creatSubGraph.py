import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class creatSubGraph(QDialog):
    graphInfo_signal = pyqtSignal(str, str)

    def __init__(self, parent):
        super().__init__(parent)
        self.titleEdit = QLineEdit()
        self.portEdit = QLineEdit()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("创建新绘图")
        layout = QFormLayout()

        self.titleEdit.setPlaceholderText("请输入标题")
        self.portEdit.setPlaceholderText("请输入端口")
        self.portEdit.setValidator(QRegExpValidator(QRegExp("[0-9]*$"), self))
        layout.addRow("标题", self.titleEdit)
        layout.addRow("端口", self.portEdit)

        btns = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        layout.addWidget(btns)
        self.setLayout(layout)

        btns.accepted.connect(self.accept)
        btns.rejected.connect(self.reject)

    def accept(self):
        if self.titleEdit.text() == '' or self.portEdit.text() == '':
            QMessageBox.warning(self, 'Warning', 'Please enter some text.')
        else:
            super().accept()
            self.graphInfo_signal.emit(self.titleEdit.text(), self.portEdit.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = creatSubGraph(None)
    main.show()
    sys.exit(app.exec_())
