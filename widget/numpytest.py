import numpy as np
import pyqtgraph.opengl as gl
from pyqtgraph.Qt import QtCore, QtGui

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
def drawCube(pos, size):
    chang, kuan, gao = size
    baseX, baseY, baseZ = pos

    vertexes = np.array([
        [baseX, baseY, baseZ], [chang, baseY, baseZ], [chang, kuan, baseZ], [baseX, kuan, baseZ],  # 底面
        [baseX, baseY, gao], [chang, baseY, gao], [chang, kuan, gao], [baseX, kuan, gao]  # 顶面
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
    offset = [-chang / 2, -kuan / 2, -gao / 2]
    vertexes = xyzOffset(vertexes, offset)
    mesh = gl.GLMeshItem(vertexes=vertexes, faces=faces, smooth=False, drawEdges=True, color=[0.5, 0.5, 1, 1])
    return mesh


# 创建一个圆柱体




# 创建GLMeshItem对象，并将其添加到窗口中
mesh = gl.GLMeshItem(vertexes=vertexes, faces=faces, smooth=False, drawEdges=True)
mesh = drawCube([0, 0, 0], [5, 5, 8])
win.addItem(mesh)

# 进入Qt事件循环
app.exec_()
