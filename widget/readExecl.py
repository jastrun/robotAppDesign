# -- coding: utf-8 --

import pandas as pd
from PyQt5.QtCore import pyqtSignal, QObject, QUrl
from PyQt5.QtWidgets import QFileDialog, QWidget

file_path = r'data.xlsx'
#df = pd.read_excel(file_path, sheet_name="Sheet1")  # sheet_name不指定时默认返回全表数据


class dataFile(QObject):
    fileinfo_signal = pyqtSignal(str)
    source_signal = pyqtSignal(str)

    def __init__(self):
        super(dataFile,self).__init__()



    def loadData(self,file_path):
         self.file = pd.read_excel(file_path, sheet_name="Sheet1")

    def openFile(self):
        # 其中self指向自身，"读取文件夹"为标题名，"./"为打开时候的当前路径
        wid=QWidget()
        directory1 = QFileDialog.getOpenFileUrl(wid,

                                                      "./")  # 起始路径
        directory1=directory1[0].toLocalFile()
        print(directory1)
        # 加载本地excel文件
        self.loadData(directory1)
        self.fileinfo_signal.emit(directory1)
        self.source_signal.emit("文件")


    def getJxAngle(self,Jx):
        data = self.file[Jx]
        return data

    def getJ1(self):
        data = self.file["J1"]
        return data
    def getJ2(self):
        data = self.file["J2"]
        return data
    def getJ3(self):
        data = self.file["J3"]
        return data
    def getJ4(self):
        data = self.file["J4"]
        return data
    def getJ5(self):
        data = self.file["J5"]
        return data
    def getJ6(self):
        data = self.file["J6"]
        return data

    def getTime(self):
        data = self.file["时间"]
        return data

    def list2str(data):
        str1=''
        for i in data:
            str1=str(i)+'*'+str1
        return str1


if __name__=='__main__':
    robotinfor=dataFile(file_path,"六轴工业机器人","001")
    J1data=robotinfor.getJxAngle('J1')
    datalist=list(J1data)
    print(datalist)
    print(type(datalist))
 #    str1=list2str(datalist)
 #    print(str1)







# 打印表数据，如果数据太多，会略去中间部分
# print(df)


# 打印列标题
# print(df.columns)

# 打印行
# print(df.index)

# 打印指定列
# print(df["J1"])

# 描述数据
# print(df.describe())
