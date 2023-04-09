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

app = QtGui.QApplication([])

# 创建一个窗口并设置显示属性
win = gl.GLViewWidget()
win.opts['distance'] = 40
win.show()

# 定义立方体的顶点坐标
vertexes = np.array([
    [0, 0, 0], [5, 0, 0], [5, 5, 0], [0, 5, 0],  # 底面
    [0, 0, 5], [5, 0, 5], [5, 5, 5], [0, 5, 5]  # 顶面
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
    def __init__(self, pos=[0,0,0], len=6):
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

        self.nextJx.translate(0,0,self.len)
        self.nextJx.setParentItem(self)

# 创建一个只可以绕z轴旋转的轴
class rotateJx_1(creatJx):
    def __init__(self,pos=[0,0,0], len=6):
        super().__init__(pos,len)

    def rotate(self, angle):
        super().rotate(angle, 0, 0, 1, local=True)

# 创建一个只可以绕y轴旋转的轴
class rotateJx_2(creatJx):
    def __init__(self, pos=[0,0,0], len=6):
        super().__init__(pos, len)

    def rotate(self, angle):
        super().rotate(angle, 0, 1, 0, local=True)


class cread3drobot(GLGraphicsItem):
    def __init__(self):
        super().__init__()

    def linkJx(self):
        pass

# 创建GLMeshItem对象，并将其添加到窗口中
mesh1 = drawCube([1, 1, 6])
mesh2 = drawCube([1, 1, 6])
mesh3 = drawSphere(1)

mesh1.translate(0, 0, 3)
mesh2.rotate(90, 1, 0, 0)
mesh2.translate(0, 0, 6)
mesh3.translate(0, 0, 6)
y = GLGraphicsItem()
# win.addItem(mesh1)
# win.addItem(mesh2)
# win.addItem(mesh3)

parent = GLGraphicsItem()

# mesh1.setParentItem(parent)
# mesh2.setParentItem(parent)
# mesh3.setParentItem(parent)

# win.addItem(parent)
# parent.translate(0, 0, 5)

J1 = rotateJx_1()
J2 = rotateJx_2()
J3 = rotateJx_1()
J4 = rotateJx_2()
J5 = rotateJx_1()
J6 = rotateJx_2()


J1.setParentItem(parent)
J1.link(J2)
J2.link(J3)
J3.link(J4)
J4.link(J5)
J5.link(J6)


print('sJ2:', J2)
datafile=dataFile()
datafile.loadData(r'data.xlsx')
angle1=(list(datafile.getJ1()))
angle2=(list(datafile.getJ2()))
angle3=(list(datafile.getJ3()))
angle4=(list(datafile.getJ4()))
angle5=(list(datafile.getJ5()))
angle6=(list(datafile.getJ6()))
timeseries=(list(datafile.gettimeseries()))
print(angle1)

def progress():
    i = 1
    while True:
        i=i+1
        sleep(0.026167)

        J1.rotate(angle1[i]-angle1[i-1])
        J2.rotate(angle2[i]-angle2[i-1])
        J3.rotate(angle3[i]-angle3[i-1])
        J4.rotate(angle4[i]-angle4[i-1])
        J5.rotate(angle5[i]-angle5[i-1])
        J6.rotate(angle6[i]-angle6[i-1])


        win.update()


t1 = threading.Thread(target=progress)
t1.start()

grid = gl.GLGridItem()  # 创建 GLGridItem 对象
grid.setSize(x=50, y=50)  # 设置网格大小
win.addItem(grid)

win.addItem(parent)

# 进入Qt事件循环


app.exec_()
