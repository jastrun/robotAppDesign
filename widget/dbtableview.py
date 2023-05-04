
from PyQt5.QtGui import QIcon

from db.sheetOp import SheetQuary, db
from graphMDI import *
from readExecl import *

class dataselect(QWidget):
    datas_signal = pyqtSignal(list,list)

    # 信号初始化
    fileinfo_signal = pyqtSignal(str)
    source_signal = pyqtSignal(str)
    dataunit_signal = pyqtSignal(list, list)
    powerAndEnergyAndspeed_signal = pyqtSignal(float, float, float)
    alldata_signal = pyqtSignal(list)

    def __init__(self):
        super().__init__()
        self.resize(800,400)
        self.initUI()
        self.initSlot()
        self.setWindowTitle("从数据库中选取数据")



    def initUI(self):
        self.layout=QVBoxLayout()

        # tableview
        self.table=QTableView()
        self.model=QStandardItemModel()  # 初始化model
        self.model.setHorizontalHeaderLabels(['ofRobotNum', 'time', 'OfMotorName'])
        self.table.setModel(self.model)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.readdata()

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
        angledata=self.datas[currentrow][4]
        timeseries = self.datas[currentrow][3]
        angledata= angledata.split("*")
        timeseries = timeseries.split("*")

        self.datas_signal.emit(timeseries,angledata)
        print(angledata)
        self.close()

    def closeself(self):
        self.close()




    def readdata(self):
        self.datas=SheetQuary(db,'angledata')
        self.model.setRowCount(len(self.datas))
        i = 0
        for data in self.datas:
            self.model.setItem(i,0,QStandardItem(data[0]))
            self.model.setItem(i, 1, QStandardItem(str(data[1])))
            self.model.setItem(i, 2, QStandardItem(data[2]))
            i=i+1
        self.table.setModel(self.model)




        print(list(data))





if __name__ == '__main__':
    app=QApplication(sys.argv)
    demo=dataselect()
    demo.show()
    sys.exit(app.exec_())