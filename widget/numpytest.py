import os
from time import sleep
import threading, time

import numpy as np
import pyqtgraph.opengl as gl
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
import math

from pyqtgraph.opengl.GLGraphicsItem import GLGraphicsItem

from readExecl import dataFile





def xyzOffset(pos, offset):
    newpos = []
    offsetX, offsetY, offsetZ = offset
    print(offset)
    for x, y, z in pos:
        p = [x + offsetX, y + offsetY, z + offsetZ]
        newpos.append(p)
    return np.array(newpos)


# 创建一个立方体
def drawCube(size):
    chang, kuan, gao = size

    vertexes = np.array([
        [0, 0, 0], [chang, 0, 0], [chang, kuan, 0], [0, kuan, 0],  # 底面
        [0, 0, gao], [chang, 0, gao], [chang, kuan, gao], [0, kuan, gao]  # 顶面
    ])
    # 定义立方体的面，每个面由三个顶点组成，即一个三角形
    faces = np.array([
        [0, 1, 2], [2, 3, 0],  # 底面
        [0, 3, 4], [4, 3, 7],  # 左侧面
        [3, 2, 7], [7, 2, 6],  # 后侧面
        [2, 1, 6], [6, 1, 5],  # 右侧面
        [1, 0, 5], [5, 0, 4],  # 前侧面
        [5, 4, 6], [6, 4, 7]  # 顶面
    ])
    # 将中心点转移到中心点
    mesh = gl.GLMeshItem(vertexes=vertexes, faces=faces, smooth=False, drawEdges=True, color=[0.5, 0.5, 1, 1])
    mesh.translate(-chang / 2, -kuan / 2, -gao / 2)
    return mesh


def drawSphere(radius):
    bitMd = gl.MeshData.sphere(rows=20, cols=20, radius=radius)
    sphere_mesh = gl.GLMeshItem(meshdata=bitMd,
                                smooth=True, drawEdges=True, color=[1, 0, 0, 1])
    return sphere_mesh


# 创建一个旋转轴


#    translation = np.array([1, 2, 3])  # 设置平移向量
#    sphere_mesh.translate(1, 2, 3)
#    mesh.rotate(60,0,0,1)

# 创建一个广义轴
class creatJx(GLGraphicsItem):
    def __init__(self, pos=[0, 0, 0], len=6):
        super().__init__()
        self.pos = pos
        self.nextJx = None
        self.len = len
        self.mesh3 = drawSphere(1)
        self.mesh2 = drawCube([1, 1, self.len])
        self.mesh1 = drawCube([1, 1, self.len])
        self.local = [0, 0, 0]

        self.initShape()
        self.translate(*pos)

    def initShape(self):
        self.mesh1.translate(0, 0, self.len / 2)
        self.mesh2.rotate(90, 1, 0, 0)
        self.mesh2.translate(0, 0, self.len)
        self.mesh3.translate(0, 0, self.len)

        self.mesh1.setParentItem(self)
        self.mesh2.setParentItem(self)
        self.mesh3.setParentItem(self)

    def link(self, nextJx):
        self.nextJx = nextJx

        self.nextJx.pos = [self.pos[0], self.pos[1], self.pos[2] + self.len]

        self.nextJx.translate(0, 0, self.len)
        self.nextJx.setParentItem(self)

    def setLen(self,len):
        self.len=len

        self.mesh1.hide()
        self.mesh2.hide()
        self.mesh3.hide()

        self.mesh3 = drawSphere(1)
        self.mesh2 = drawCube([1, 1, self.len])
        self.mesh1 = drawCube([1, 1, self.len])


        self.initShape()


# 创建一个只可以绕z轴旋转的轴
class rotateJx_1(creatJx):
    def __init__(self, pos=[0, 0, 0], len=6):
        super().__init__(pos, len)

    def rotate(self, angle):
        super().rotate(angle, 0, 0, 1, local=True)


# 创建一个只可以绕y轴旋转的轴
class rotateJx_2(creatJx):
    def __init__(self, pos=[0, 0, 0], len=6):
        super().__init__(pos, len)

    def rotate(self, angle):
        super().rotate(angle, 0, 1, 0, local=True)


# 创建一个六轴工业机器人
class sixMotorRobot3d(GLGraphicsItem):
    def __init__(self,parent,win):
        super().__init__()
        # 创建机器人各个关节
        self.J1 = rotateJx_1()
        self.J2 = rotateJx_2()
        self.J3 = rotateJx_2()
        self.J4 = rotateJx_1()
        self.J5 = rotateJx_2()
        self.J6 = rotateJx_1()

        self.J1.setParentItem(self)
        self.J1.link(self.J2)
        self.J2.link(self.J3)
        self.J3.link(self.J4)
        self.J4.link(self.J5)
        self.J5.link(self.J6)

        self.angle_J1 = 0
        self.angle_J2 = 0
        self.angle_J3 = 0
        self.angle_J4 = 0
        self.angle_J5 = 0
        self.angle_J6 = 0

        grid = gl.GLGridItem()  # 创建 GLGridItem 对象
        grid.setSize(x=50, y=50)  # 设置网格大小
        grid.setParentItem(self)

        self.parent=parent
        self.win=win

        print("3d机器人:",self.parent)


        self.linkJx()

        # 槽
        self.parent.parent.dataunit_abs_signal.connect(self.receiveData)

    def linkJx(self):
        pass

    def setRelaAngle(self, a1, a2, a3, a4, a5, a6):
        self.J1.rotate(a1)
        self.J2.rotate(a2)
        self.J3.rotate(a3)
        self.J4.rotate(a4)
        self.J5.rotate(a5)
        self.J6.rotate(a6)

        self.angle_J1 = self.angle_J1+a1
        self.angle_J2 = self.angle_J2+a2
        self.angle_J3 = self.angle_J3+a3
        self.angle_J4 = self.angle_J4+a4
        self.angle_J5 = self.angle_J5+a5
        self.angle_J6 = self.angle_J6+a6


    def setlen(self, l1, l2, l3, l4, l5, l6):
        self.J1.setLen(l1)
        self.J2.setLen(l2)
        self.J3.setLen(l3)
        self.J4.setLen(l4)
        self.J5.setLen(l5)
        self.J6.setLen(l6)

    def receiveData(self,datalist):
        self.initializePos()  # 回归初始坐标
        # 转动相对初始坐标的绝对坐标
        self.setRelaAngle(datalist[1],
                          datalist[2],
                          datalist[3],
                          datalist[4],
                          datalist[5],
                          datalist[3]
                          )

        self.win.update()

    def initializePos(self):
        self.setRelaAngle(-self.angle_J1,
                          -self.angle_J2,
                          -self.angle_J3,
                          -self.angle_J4,
                          -self.angle_J5,
                          -self.angle_J6
                          )
        self.angle_J1 = 0
        self.angle_J2 = 0
        self.angle_J3 = 0
        self.angle_J4 = 0
        self.angle_J5 = 0
        self.angle_J6 = 0


        self.win.update()



def progress():
    i = 1
    while True:
        i = i + 1
        sleep(0.026167)

        a1 = (angle1[i] - angle1[i - 1])
        a2 = (angle2[i] - angle2[i - 1])
        a3 = (angle3[i] - angle3[i - 1])
        a4 = (angle4[i] - angle4[i - 1])
        a5 = (angle5[i] - angle5[i - 1])
        a6 = (angle6[i] - angle6[i - 1])

        robot.setRelaAngle(a1, a2, a3, a4, a5, a6)

        win.update()

        robot.initializePos()
        win.update()

if __name__=='__main__':
    app = QtGui.QApplication([])

    # 创建一个窗口并设置显示属性
    win = gl.GLViewWidget()
    win.opts['distance'] = 40
    win.show()

    datafile = dataFile()
    datafile.loadData(r'data.xlsx')
    angle1 = (list(datafile.getJ1()))
    angle2 = (list(datafile.getJ2()))
    angle3 = (list(datafile.getJ3()))
    angle4 = (list(datafile.getJ4()))
    angle5 = (list(datafile.getJ5()))
    angle6 = (list(datafile.getJ6()))
    timeseries = (list(datafile.gettimeseries()))

    robot = sixMotorRobot3d(None,win)

    t1 = threading.Thread(target=progress)
    t1.start()


    win.addItem(robot)

    # 进入Qt事件循环

    app.exec_()
