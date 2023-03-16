import pyqtgraph.opengl as gl
import numpy as np

# 生成球体的顶点和面数据
from PyQt5 import QtGui


def make_sphere(radius, sectors, stacks):
    phi = np.linspace(0, np.pi, stacks+1)
    theta = np.linspace(0, 2*np.pi, sectors+1)
    phi, theta = np.meshgrid(phi, theta)
    x = radius*np.sin(phi)*np.cos(theta)
    y = radius*np.sin(phi)*np.sin(theta)
    z = radius*np.cos(phi)
    vertices = np.vstack([x.flatten(), y.flatten(), z.flatten()]).T
    faces = []
    for i in range(stacks):
        for j in range(sectors):
            p1 = i*(sectors+1) + j
            p2 = p1 + (sectors+1)
            faces.append([p1, p2, p2+1])
            faces.append([p1, p2+1, p1+1])
    return vertices, faces

# 创建一个Qt应用
app = QtGui.QApplication([])
w = gl.GLViewWidget()
w.show()

# 创建一个球体的GLMeshItem对象
sphere_radius = 1.0
sphere_sectors = 20
sphere_stacks = 20
sphere_vertices, sphere_faces = make_sphere(sphere_radius, sphere_sectors, sphere_stacks)
sphere_mesh = gl.GLMeshItem(vertexes=sphere_vertices, faces=sphere_faces, smooth=True, drawEdges=True, color=[0.5, 0.5, 1, 1])
w.addItem(sphere_mesh)

# 设置相机位置和方向
w.opts['distance'] = 5*sphere_radius
w.opts['elevation'] = 30
w.opts['azimuth'] = 30

# 开始Qt应用的事件循环
QtGui.QApplication.instance().exec_()
