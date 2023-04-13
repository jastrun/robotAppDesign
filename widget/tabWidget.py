import sys
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

    def tab1UI(self):
        # 垂直布局
        layout=QHBoxLayout()
        # 加载web
        self.webview = QWebEngineView(self)
        url="D:/莫愁/Documents/pythonproj/robotAPP/html2/index.html"
        self.webview.load(QUrl(url))
        self.webview.setZoomFactor(0.8)
        layout.addWidget(self.webview)
        self.setTabText(0,'静态信息')
        self.tab1.setLayout(layout)

    def tab2UI(self):
        #zhu表单布局，次水平布局
        layout=QHBoxLayout()


        _3dwidget=gl.GLViewWidget()
        self.robot3d = sixMotorRobot3d(self,_3dwidget)
        _3dwidget.addItem(self.robot3d)
        _3dwidget.opts['distance'] = 40
        _3dwidget.show()

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