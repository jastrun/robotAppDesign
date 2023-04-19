import sys
from datetime import time
from time import sleep

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import *
from ThreeDeRobot import *
from dataFFT import dataFFT
from dbtableview import dataselect
from graphMDI import *
from numpytest import sixMotorRobot3d


class TabDemo(QTabWidget):
    def __init__(self,parent=None):
        super(TabDemo, self).__init__(parent)
        self.parent=parent
        #创建4个选项卡小控件窗口
        self.tab1=QWidget()
        self.tab2=QWidget()
        self.tab3=QWidget()
        self.tab4 =QWidget()

        #将三个选项卡添加到顶层窗口中
        self.addTab(self.tab1, "Tab 1")
        self.addTab(self.tab2, "Tab 2")
        self.addTab(self.tab3, "Tab 3")
        self.addTab(self.tab4, "Tab 4")

        #每个选项卡自定义的内容
        self.tab1UI()
        self.tab2UI()
        self.tab3UI()
        self.tab4UI()

        self.parent.PAEAS_signal.connect(self.receivePAEAS)
        self.parent.alldata_signal.connect(self.receiveAllData)



    def receiveAllData(self,alldata):
        self.str_alldata = "setdata__all({});".format(alldata)
        self.webview.page().runJavaScript(self.str_alldata)

    def receivePAEAS(self,power,energy,speed):
        self.str_power = "setdata_power({:.2f});".format(power)
        self.str_powerg = "setdata_powerg({:.2f});".format(power)
        self.str_energy = "document.getElementById('energy').innerHTML = {:.2f}; ".format(energy)

        self.webview.page().runJavaScript(self.str_power)
        self.webview.page().runJavaScript(self.str_powerg)
        self.webview.page().runJavaScript(self.str_energy)

    def clearall(self):
        self.str_power = "setdata_power({:.2f});".format(0)
        self.str_powerg = "setdata_powerg({:.2f});".format(0)
        self.str_energy = "document.getElementById('energy').innerHTML = {:.2f}; ".format(0)
        self.str_alldata = "setdata__all({});".format([0,0,0,0,0,0,0,0,0])

        self.webview.page().runJavaScript(self.str_power)
        self.webview.page().runJavaScript(self.str_powerg)
        self.webview.page().runJavaScript(self.str_energy)
        self.webview.page().runJavaScript(self.str_alldata)


    def tab1UI(self):
        # 垂直布局
        self.layoutweb=QHBoxLayout()
        # 加载web
        self.webview = QWebEngineView(self)
        url="D:/莫愁/Documents/pythonproj/robotAPP/html2/index.html"
        self.webview.load(QUrl(url))
        self.webview.setZoomFactor(0.8)
        self.webview.adjustSize()
        self.layoutweb.addWidget(self.webview)
        self.setTabText(0,'静态信息')
        self.tab1.setLayout(self.layoutweb)

    def resizeEvent(self, QResizeEvent):
        super(TabDemo, self).resizeEvent(QResizeEvent)
        # 重新设置web大小
        if self.width()==1166 and self.height()==813:
            self.webview.setZoomFactor(1)
        if self.width() == 804 and self.height() == 813:
            self.webview.setZoomFactor(0.75)


    def tab2UI(self):
        #zhu表单布局，次水平布局
        layout=QHBoxLayout()


        _3dwidget=gl.GLViewWidget()
        self.robot3d = sixMotorRobot3d(self,_3dwidget)
        _3dwidget.addItem(self.robot3d)
        _3dwidget.opts['distance'] = 40
#        _3dwidget.show()

        layout.addWidget(_3dwidget)

        #设置标题与布局
        self.setTabText(1,'3d实时显示')
        self.tab2.setLayout(layout)

    def tab3UI(self):
        #水平布局
        layout=QHBoxLayout()

        self.graphMdi = graphMDI(self)
        layout.addWidget(self.graphMdi)

        #设置小标题与布局方式
        self.setTabText(2,'波形')
        self.tab3.setLayout(layout)

    def tab4UI(self):
        layout=QHBoxLayout()
        #设置小标题与布局方式
        self.setTabText(3,'数据分析')
        self.datafft=dataFFT()
        layout.addWidget(self.datafft)
        self.tab4.setLayout(layout)


if __name__ == '__main__':
    app=QApplication(sys.argv)
    demo=TabDemo()
    demo.show()
    sys.exit(app.exec_())