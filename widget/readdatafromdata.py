import json

from PyQt5.QtGui import QIcon

from db.sheetOp import SheetQuary, db
from graphMDI import *
from readExecl import *

def readQss(style):
    with open(style, 'r') as f:
        return f.read()

class dataselect(QWidget):
    datas_signal = pyqtSignal(list,list)

    # 信号初始化
    source_signal = pyqtSignal(str)
    dataunit_signal = pyqtSignal(list, list)
    powerAndEnergyAndspeed_signal = pyqtSignal(float, float, float)
    alldata_signal = pyqtSignal(list)

    def __init__(self):
        super().__init__()
        self.resize(800,400)
        # 初始化标志
        self.runningFLag = False
        self.startFlag = False

        self.initUI()
        self.initSlot()
        self.setWindowTitle("从数据库中选取数据")



    def initUI(self):
        self.layout=QVBoxLayout()

        # tableview
        self.table=QTableView()
        self.model=QStandardItemModel()  # 初始化model
        self.model.setHorizontalHeaderLabels(['机器人', '保存时间'])
        self.table.setModel(self.model)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.readdata()

        str = os.getcwd() + "\\..\\qssStyle\\new7.qss"
        qssStyle = readQss(str)
        self.setStyleSheet(qssStyle)

        # 按钮
        self.btnlayout=QHBoxLayout()
        self.readdataBtn=QPushButton("加载数据")
        self.okBtn=QPushButton("确认选择")
        self.cancelBtn=QPushButton("取消选择")
#        self.btnlayout.addWidget(self.readdataBtn)
        self.btnlayout.addWidget(self.okBtn)
        self.btnlayout.addWidget(self.cancelBtn)

        # 设置layout
        self.layout.addWidget(self.table)
        self.layout.addLayout(self.btnlayout)
        self.setLayout(self.layout)


    def initSlot(self):
        self.readdataBtn.clicked.connect(self.readdata)
        self.okBtn.clicked.connect(self.receivedata)
        self.cancelBtn.clicked.connect(self.closeself)

    def receivedata(self):
        currentrow=self.table.currentIndex().row()
        angledata=self.datas[currentrow][2]
        self.data = json.loads(angledata)
        self.source_signal.emit("数据库")
        self.close()
     #   self.startemit()

    def closeself(self):
        self.close()

    def startemit(self):
        print("start emit!")
        i = 0
        # 获取角度增量
        while i <= len(self.data)-1 and self.startFlag:
            sleep(0.026167)


            print(self.data[i][0])
            print(self.data[i][1])
            print(self.data[i][2])
            self.signalSend(self.data[i][0], self.data[i][1], self.data[i][2])

            print("send mes:" + str(i))

            i = i + 1
        print("send ok!")

    def signalSend(self,dataunit,PAE,alldata):


        self.dataunit_signal.emit(dataunit[0], dataunit[1])
        self.powerAndEnergyAndspeed_signal.emit(PAE[0],PAE[1],PAE[2])
        self.alldata_signal.emit(alldata)

    def changeState(self):
        # 初始化标志

        if self.startFlag:  # 若此时正在开始 点击按钮
            print(self.sendTh.is_alive())
            self.runningFLag = False
            self.startFlag = False


        else:
            self.runningFLag = True
            self.startFlag = True

            self.sendTh = threading.Thread(target=lambda: self.startemit())
            self.sendTh.start()
            print(self.sendTh.is_alive())



    def readdata(self):
        self.datas=SheetQuary(db,'dataunit')
        self.model.setRowCount(len(self.datas))
        i = 0
        for data in self.datas:
            self.model.setItem(i,0,QStandardItem(data[0]))
            self.model.setItem(i, 1, QStandardItem(str(data[1])))
            i=i+1
        self.table.setModel(self.model)
        print(list(data))







if __name__ == '__main__':
    app=QApplication(sys.argv)
    demo=dataselect()
    demo.show()
    sys.exit(app.exec_())