import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import *
from ThreeDeRobot import *
from graphMDI import *





class TabDemo(QTabWidget):
    def __init__(self,parent=None):
        super(TabDemo, self).__init__(parent)
        self.parent=parent
        #创建3个选项卡小控件窗口
        self.tab1=QWidget()
        self.tab2=QWidget()
        self.tab3=QWidget()

        #将三个选项卡添加到顶层窗口中
        self.addTab(self.tab1, "Tab 1")
        self.addTab(self.tab2, "Tab 2")
        self.addTab(self.tab3, "Tab 3")

        #每个选项卡自定义的内容
        self.tab1UI()
        self.tab2UI()
        self.tab3UI()

    def tab1UI(self):
        # 垂直布局
        layout=QHBoxLayout()
        # 加载web
        self.webview = QWebEngineView(self)
        url="D:/莫愁/Documents/pythonproj/robotAPP/html1/index.html"
        self.webview.load(QUrl(url))
        self.webview.setZoomFactor(0.8)
        layout.addWidget(self.webview)
        self.setTabText(0,'静态信息')
        self.tab1.setLayout(layout)

    def tab2UI(self):
        #zhu表单布局，次水平布局
        layout=QHBoxLayout()

        robot3d=sixRobot()

        layout.addWidget(robot3d)

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
if __name__ == '__main__':
    app=QApplication(sys.argv)
    demo=TabDemo()
    demo.show()
    sys.exit(app.exec_())