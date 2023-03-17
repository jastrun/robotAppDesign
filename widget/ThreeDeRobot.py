## build a QApplication before building other widgets
import numpy
import pyqtgraph as pg
import sys

## make a widget for displaying 3D objects
import pyqtgraph.opengl as gl
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication

# 默认初始坐标
initbsposition = [[1, 1, 1],
                [2, 2, 2],
                [3, 3, 3],
                [4, 4, 4],
                [5, 5, 5],
                [6, 6, 6]]

class sixRobot(gl.GLViewWidget):
    def __init__(self,initbsPosition=initbsposition):
        super().__init__()
        self.originPos=[0,0,0]  # 原点
        xgrid = gl.GLGridItem()  # 添加栅格
#       xgrid.rotate(0, 1, 0, 0)  # 旋转栅格
        self.addItem(xgrid)
        self.links = []  # 机械臂列表
        self.initbsposition = initbsPosition
        self.position    = [[1, 1, 1],
                            [1, 1, 1],
                            [1, 1, 1],
                            [1, 1, 1],
                            [1, -1, 1],
                            [1, 1, 1]]
        self.resize(1200, 800)
        self.structself(self.initbsposition)  # 构造自身机械臂
        self.setRelaposition(self.position)
        self.show()

# 添加直线
    def add_line(self, p1, p2, setcolor):
        lines = numpy.array([[p1[0], p1[1], p1[2]], [p2[0], p2[1], p2[2]]])
        lines_item = gl.GLLinePlotItem(
            pos=lines, mode="lines", color=setcolor, width=10, antialias=True
        )
        self.links.append(lines_item)
        self.addItem(lines_item)

# 构造机械臂
    def structself(self,position):
        position.insert(0,self.originPos)
        colordic = [(0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 1)]  # 颜色字典
        for i in range(0, 6):
            self.add_line(position[i], position[i + 1], (*colordic[i], 1))

# 设置坐标(通过绝对坐标)
    def setAbsposition(self, position):  # 绝对坐标
        position.insert(0, self.originPos)
        print(len(position))
        for i in range(0, 6):
            self.links[i].setData(pos=numpy.array([position[i], position[i + 1]]),width=10)
        QtGui.QApplication.processEvents()

# 设置坐标(通过相对坐标)
    def setRelaposition(self, position):  # 相对坐标
        base = self.originPos  # 设置基点坐标
        absposition=[]
        # 转化成绝对坐标
        for i in range(len(position)):
            newpos = []
            for j in range(len(position[i])):
                newpos.append(position[i][j]+base[j])
            base=newpos
            absposition.append(newpos)

        # 设置坐标
        self.setAbsposition(absposition)

# 设置原点
    def setBase(self,base):
        self.originPos=base




        QtGui.QApplication.processEvents()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    robot = sixRobot()
    robot.show()
    sys.exit(app.exec_())
