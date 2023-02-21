import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class dbTree(QWidget):
    def __init__(self,parent=None):
        super().__init__()
        self.initTree()

    def initTree(self):
        # 设置树控件
        self.tree = QTreeWidget(self)
        self.tree.setColumnCount(1)  # 制定树控件为两列
        self.tree.setHeaderLabels(["项目"])  # 设置列标签

        # 添加根节点1
        root = QTreeWidgetItem(self.tree)
        root.setText(0, "机器人")
        self.tree.setColumnWidth(0, 300)

        # 添加子节点1
        n1 = QTreeWidgetItem(root)
        n1.setText(0, "机器人1")
        # 添加子节点2
        n2 = QTreeWidgetItem(root)
        n2.setText(0, "机器人2")

        # 为子节点再添加子节点2-1
        n3 = QTreeWidgetItem(n2)
        n3.setText(0, "节点1")

        self.tree.expandAll()  # 设置所有的节点为展开的状态

