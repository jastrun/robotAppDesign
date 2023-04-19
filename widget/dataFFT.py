
# 导入必要的模块
import os

import matplotlib
from PyQt5.QtWidgets import *

from dbtableview import dataselect

matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5 import QtCore, QtWidgets,QtGui
import matplotlib.pyplot as plt
import sys
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar

from scipy.fftpack import fft, ifft
from matplotlib.pylab import mpl

import numpy as np
def readQss(style):

    with open(style, 'r') as f:
        return f.read()


class dataFFT(QtWidgets.QWidget):
    def __init__(self,parent=None):
        mpl.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
        mpl.rcParams['axes.unicode_minus'] = False  # 显示负号

        super().__init__()
        # 重新调整大小
        self.resize(800, 659)
        self.fftwidget = QWidget()
        self.fftwidget.setWindowTitle("傅里叶变换")

        str = os.getcwd() + "\\..\\qssStyle\\new7.qss"
        qssStyle = readQss(str)
        self.setStyleSheet(qssStyle)
        self.fftwidget.setStyleSheet(qssStyle)



        self.initUI()
        self.initSlot()

    def initUI(self):
        self.centrallayout=QVBoxLayout()

        # 清屏
        plt.cla()
        # 获取绘图并绘制
        self.fig = plt.figure()
        self.ax = self.fig.add_axes([0.1, 0.1, 0.8, 0.8])
        self.ax.set_xlim([-1, 500])
        self.ax.set_ylim([-1, 500])

        # 获取傅里叶变换的绘图的绘制
        self.f1 = plt.figure()
        self.a1 = self.f1.add_axes([0.1, 0.1, 0.8, 0.8])
        self.f2 = plt.figure()
        self.a2 = self.f2.add_axes([0.1, 0.1, 0.8, 0.8])
        self.cavans1 = FigureCanvas(self.f1)
        self.cavans2 = FigureCanvas(self.f2)
        layout = QVBoxLayout()
        figtoolbar = NavigationToolbar(self.cavans1, self)
        layout.addWidget(figtoolbar)
        layout.addWidget(self.cavans1)
        figtoolbar = NavigationToolbar(self.cavans2, self)
        layout.addWidget(figtoolbar)
        layout.addWidget(self.cavans2)
        self.fftwidget.setLayout(layout)


        self.cavans = FigureCanvas(self.fig)
        self.figtoolbar = NavigationToolbar(self.cavans, self)

        self.centrallayout.addWidget(self.figtoolbar)
        self.centrallayout.addWidget(self.cavans)

        self.btnlayout=QHBoxLayout()
        self.readDataBtn_db = QPushButton("从数据库读取数据")
        self.readDatalocal_db = QPushButton("从本地读取数据")
        self.FFT = QPushButton("傅里叶变换")
        self.btnlayout.addWidget(self.readDataBtn_db)
#        self.btnlayout.addWidget(self.readDatalocal_db)
        self.btnlayout.addWidget(self.FFT)

        self.centrallayout.addLayout(self.btnlayout)
        self.setLayout(self.centrallayout)

    def plotdata(self,timeseries,data):
        self.datalist=[]
        self.timeserieslist = []
        for i in data:
            if i=='' :
                i=0
            self.datalist.append(float(i))
        for i in timeseries:
            if i=='':
                i=0
            self.timeserieslist.append(float(i))


        self.ax.cla()
        self.ax.set_xlim([-1, max(self.timeserieslist)])
        self.ax.set_ylim([min(self.datalist), max(self.datalist)])
        self.ax.plot(self.timeserieslist,self.datalist)
        # 更新画布中的数据

        self.cavans.draw()
        self.cavans.flush_events()


    def readdatafromdb(self):
        self.dataselectWidget=dataselect()
        str = os.getcwd() + "\\..\\qssStyle\\new7.qss"
        qssStyle = readQss(str)
        self.dataselectWidget.setStyleSheet(qssStyle)
        self.dataselectWidget.datas_signal.connect(self.plotdata)
        self.dataselectWidget.show()


    def initSlot(self):
        self.readDataBtn_db.clicked.connect(self.readdatafromdb)
        self.FFT.clicked.connect(self.fftConvert)

    def fftConvert(self):

        self.datalist_fft=fft(self.datalist)
        abs_y = np.abs(self.datalist_fft)  # 取复数的绝对值，即复数的模(双边频谱)
        angle_y = np.angle(self.datalist_fft)  # 取复数的角度

        self.a1.cla()
        self.a1.plot( abs_y)
        self.a1.set_title("双边振幅谱（未归一化）")

        self.a2.cla()
        self.a2.plot( angle_y)
        self.a2.set_title("双边相位谱（未归一化）")


        self.cavans1.draw()
        self.cavans1.flush_events()

        self.cavans2.draw()
        self.cavans2.flush_events()

        self.fftwidget.show()




        # 更新画布中的数据
        self.cavans1.draw()
        self.cavans1.flush_events()

        self.cavans2.draw()
        self.cavans2.flush_events()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = dataFFT()
    main_window.show()
    app.exec()


