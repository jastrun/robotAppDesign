import numpy as np
import pyqtgraph.opengl as gl
from pyqtgraph.Qt import QtCore, QtGui

# 创建二维数据网格
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# 创建GLViewWidget并添加到图形窗口
app = QtGui.QApplication([])
w = gl.GLViewWidget()
w.opts['distance'] = 20
w.show()

# 创建GLSurfacePlotItem并添加到GLViewWidget
surf = gl.GLSurfacePlotItem(x=X, y=Y, z=Z, shader='normalColor')
surf.scale(2, 2, 1)
w.addItem(surf)

# 进入事件循环
QtGui.QApplication.instance().exec_()
