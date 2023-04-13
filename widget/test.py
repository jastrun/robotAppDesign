from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


class WindowPattern(QWidget):
    """
    设置窗口样式（主要是窗口边框、标题栏和窗口本身的样式）

    """
    def __init__(self):
        super().__init__()


        # 最顶端 永远在最前面 无边框（无法拖动）
        self.setWindowFlags(Qt.WindowMaximizeButtonHint)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = WindowPattern()
    print(example.__doc__)
    example.show()
    sys.exit(app.exec_())

