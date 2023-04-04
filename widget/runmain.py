import sys
from PyQt5.QtWidgets import *
import qdarkstyle
import mainWindow

# 默认标题栏

if __name__ == '__main__':
    app = QApplication(sys.argv)


    main = mainWindow.mainWindow()
    sys.exit(app.exec_())
