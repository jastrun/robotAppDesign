import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import pyqtgraph as pg

from creatSubGraph import creatSubGraph
from graphSubWin import graphSubWin

class graphMDI(QMdiArea):
    def __init__(self):
        super().__init__()
        self.setViewMode(QMdiArea.TabbedView)
        self.setTabsClosable(True)

    # 槽
    def graSlot_creatGra(self):
        dialog = creatSubGraph(self)
        dialog.graphInfo_signal.connect(self.acceptNewGraph)
        dialog.exec_()

    def acceptNewGraph(self, title, port):
        subWin = graphSubWin()  # 创建子窗口
        subWin.setWindowTitle(title)  # 设置标题
        self.addSubWindow(subWin)  # 将子窗口添加到MDI中
        subWin.show()

    def graSlot_TabMode(self):
        print("平铺模式")
        self.tileSubWindows()

    def graSlot_CascadeMode(self):
        print('层叠模式')
        self.cascadeSubWindows()



if __name__ == '__main__':
    app = QApplication(sys.argv)

    #   app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    main = graphMDI()
    sys.exit(app.exec_())
