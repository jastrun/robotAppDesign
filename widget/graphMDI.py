import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import pyqtgraph as pg
from sympy.plotting.intervalmath.tests.test_interval_functions import np

from creatSubGraph import creatSubGraph
from graphSubWin import graphSubWin

class graphMDI(QMdiArea):
    def __init__(self,parent):
        super().__init__()
        self.parent=parent
        self.setViewMode(QMdiArea.TabbedView)
        self.setTabsClosable(True)

    # 槽
    def graSlot_creatGra(self):
        # 获得树中的机器人节点
        self.robotnode=self.parent.parent.robotTree.currentItem().parent()
        self.motornode = self.parent.parent.robotTree.currentItem()
        # 获取机器人列表
        robotlist=self.parent.parent.robotTree.robotList
        # 遍历机器人列表找到对应的机器人数据元
        for i in robotlist:
            if i[1]==self.robotnode:
                self.robot=i[0]  # 找到对应及机器人数据元

        print(self.robot)  # 测试输出机器人信息
        print(self.motornode.text(0))  #测试获得轴信息
        dialog = creatSubGraph(self)
        dialog.graphInfo_signal.connect(self.acceptNewGraph)
        dialog.exec_()

    def acceptNewGraph(self, title, port):
        motor = self.motornode.text(0)
        print('*****************************************************')
        print(motor)
        data = self.parent.parent.datafile.getJxAngle(motor)
        timeseries=self.parent.parent.datafile.gettimeseries()
        subWin = graphSubWin(self.robot,self.robotnode,self.motornode,timeseries,data)  # 创建子窗口


        if 'J' in motor:  # 设置绘图样式


            pen = pg.mkPen({'color': (155, 200, 160), 'width': 2})  # 画笔设置
            subWin.graph.plot(timeseries,data,clear=True, pen=pen)  # 画出从excel中读取到的数据

            datalist=list(data)




        subWin.graph.setBackground((210, 240, 240))  # 背景色
        subWin.graph.showGrid(y=True)

        subWin.setWindowTitle(self.robotnode.text(0)+self.robotnode.text(1)+':'+self.motornode.text(0))  # 设置标题
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
