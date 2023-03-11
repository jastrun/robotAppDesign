import sys
from PyQt5.QtWidgets import *
import qdarkstyle
import mainWindow
import mainWindowStyle
from qt_material import apply_stylesheet

from CallTitleTest import TitleWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)


 #   app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    main = mainWindowStyle.diyStyleOfmainWindow()
    sys.exit(app.exec_())
