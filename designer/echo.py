import sys

from PyQt5.QtWidgets import *

class QlineEditEchoMode(QWidget):
    def __init__(self):
        super(QlineEditEchoMode,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('文本输入框的回显模式')

        formLayout=QFormLayout(self)

        normallineEdit=QLineEdit()
        noEcholineEdit=QLineEdit()
        passwordlineEdit=QLineEdit()
        password2lineEdit=QLineEdit()

        formLayout.addRow("normal",normallineEdit)
        formLayout.addRow("noEcho", noEcholineEdit)
        formLayout.addRow("passwordlineEdit", passwordlineEdit)
        formLayout.addRow("password2lineEdit", password2lineEdit)

        normallineEdit.setPlaceholderText('normal')
        noEcholineEdit.setPlaceholderText('noEcho')
        passwordlineEdit.setPlaceholderText('passwordlineEdit')
        password2lineEdit.setPlaceholderText('password2lineEdit')

        normallineEdit.setEchoMode(QLineEdit.Normal)
        noEcholineEdit.setEchoMode(QLineEdit.NoEcho)
        passwordlineEdit.setEchoMode(QLineEdit.Password)
        password2lineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QlineEditEchoMode()
    mainWindow.show()
    sys.exit(app.exec_())