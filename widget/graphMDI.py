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
        self.data_J1 = []
        self.data_J2 = []
        self.data_J3 = []
        self.data_J4 = []
        self.data_J5 = []
        self.data_J6 = []
        self.subwinlist=[]
        self.parent=parent
        self.setViewMode(QMdiArea.TabbedView)
        self.setTabsClosable(True)

        # 槽
        self.parent.parent.dataunit_abs_signal.connect(self.setsubwindata)

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

        subWin = graphSubWin(self,self.robot,self.robotnode,self.motornode,timeseries,data)  # 创建子窗口

        if 'J' in motor:  # 设置绘图样式


            pen = pg.mkPen({'color': (155, 200, 160), 'width': 2})  # 画笔设置
 #           subWin.graph.plot(timeseries,data,clear=True, pen=pen)  # 画出从excel中读取到的数据





        subWin.graph.setBackground((210, 240, 240))  # 背景色
        subWin.graph.showGrid(y=True)

        subWin.setWindowTitle(self.robotnode.text(0)+self.robotnode.text(1)+':'+self.motornode.text(0))  # 设置标题
        self.addSubWindow(subWin)  # 将子窗口添加到MDI中
        self.subwinlist.append(subWin)
        subWin.show()
        print(self.subWindowList(),end='\n')

    def setsubwindata(self,data):
        print("subwindow:",data,end='\n')
        self.data_J1.append(data[1])
        self.data_J2.append(data[2])
        self.data_J3.append(data[3])
        self.data_J4.append(data[4])
        self.data_J5.append(data[5])
        self.data_J6.append(data[6])


        pen = pg.mkPen({'color': (155, 200, 160), 'width': 2})  # 画笔设置
        for subwin in self.subwinlist:
            if subwin.motorname=='J1':
                subwin.plotwid.setData(self.data_J1,clear=True, pen=pen)
            if subwin.motorname=='J2':
                subwin.plotwid.setData(self.data_J2,clear=True, pen=pen)
            if subwin.motorname=='J3':
                subwin.plotwid.setData(self.data_J3,clear=True, pen=pen)
            if subwin.motorname=='J4':
                subwin.plotwid.setData(self.data_J4,clear=True, pen=pen)
            if subwin.motorname=='J5':
                subwin.plotwid.setData(self.data_J5,clear=True, pen=pen)
            if subwin.motorname=='J6':
                subwin.plotwid.setData(self.data_J6,clear=True, pen=pen)


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
