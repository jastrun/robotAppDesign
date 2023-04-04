import pymysql
import time
import datetime
from datetime import date

from readExecl import dataFile

try:
    db = pymysql.connect(host="localhost",
                         user="root",
                         password="aoteman000",
                         database="robotinfo",
                         charset="utf8")
    print("数据库连接成功")
except pymysql.Error as e:
    print("数据库连接失败：" + str(e))
    cur = db.cursor()


# 数据格式基类
class DataFormat:
    def __init__(self, name):
        self.name = name
        today = datetime.datetime.now()
        self.time = str(today)

    # 上载数据
    def uploadData(self):
        pass

    def __str__(self):
        return '无'


# 角度数据格式
class AngleData(DataFormat):
    def __init__(self, name, OfMotorName, angle, angleSpeed):
        super().__init__(name)
        self.OfMotorName = OfMotorName
        self.angle = angle
        self.angleSpeed = angleSpeed

    # 上载数据
    def uploadData(self, db):
        cur = db.cursor()
        try:
            sql = "INSERT AngleData(name,time,OfMotorName,angle,angleSpeed) " \
                  "VALUES('{}','{}','{}','{}','{}')" \
                  "".format(self.name, self.time, self.OfMotorName, self.angle, self.angleSpeed)
            cur.execute(sql)
            # 提交数据
            db.commit()
            print("数据已存入数据库中！")
        except pymysql.Error as e:
            print("数据存入数据库失败!" + str(e))

    def __str__(self):
        return 'AngleData'


# 运动节点基类
class Motor:
    def __init__(self, name, ofRobotNum, funtion='无', dataFormat='无'):
        self.name = name
        self.ofRobotNum = ofRobotNum
        self.funtion = funtion
        self.dataFormat = dataFormat

    #       self.__creatMotor()

    def creatMotor(self, db):
        cur = db.cursor()
        try:
            sql = "INSERT motor(name,ofRobotNum,funtion,dataFormat) " \
                  "VALUES('{}','{}','{}','{}')" \
                  "".format(self.name, self.ofRobotNum, self.funtion, self.dataFormat)
            cur.execute(sql)
            # 提交数据
            db.commit()
            print("创建机器人节点: {} 成功！".format(self.name))
        except pymysql.Error as e:
            print("创建机器人节点失败！" + str(e))

    # 记录数据
    def recordData(self):
        pass


# 运动节点实体
class MotorOfSix(Motor):
    def __init__(self, name, ofRobotNum, db):
        super().__init__(name, ofRobotNum)
        self.funtion = '角度运动'
        self.dataFormat = 'AngleData'
        self.creatMotor(db)

    # 在表motor中创建一个运动单元记录
    def creatMotor(self, db):
        super().creatMotor(db)

    # 将运动单元的数据存入数据库中(dataunit表)
    def recordData(self, name, angle, angleSpeed):
        data = AngleData(name, self.name, angle, angleSpeed)
        data.uploadData()


# robot实体基类
class Robot:
    def __init__(self, db, num, label='default', insertOrNot=True):
        self.num = num
        self.label = label  # 机器人基类默认标签为default
        if insertOrNot:  # 用于判断是创建操作还是更新操作
            self.__creat(db)  # 创建则需要插入数据库信息
        else:
            pass  # 同步操作仅需要创建对象即可，无需插入

    # 往数据库插入相关信息
    def __creat(self, db):
        cur = db.cursor()
        try:
            sql = "INSERT robot(Rnum,Rlabel) VALUES('{}','{}')".format(self.num, self.label)
            cur.execute(sql)
            # 提交数据
            db.commit()
            print("创建机器人: {}  {} 成功！".format(self.num, self.label))
        except pymysql.Error as e:
            print("创建机器人{}失败！".format(self.num) + str(e))

    # 删除自身
    def deleteSelf(self, db):
        cur = db.cursor()
        try:
            sql = "DELETE FROM robot WHERE Rnum='{}'".format(self.num)
            cur.execute(sql)
            # 提交数据
            db.commit()
            print("删除机器人: {}  {} 成功！".format(self.num, self.label))
        except pymysql.Error as e:
            print("删除机器人{}失败！".format(self.num) + str(e))

    # 打印自身信息
    def __str__(self):
        return "机器人的编号是:{} 标签是：{}".format(self.num, self.label)

    # 获得编号
    def getNum(self):
        return self.num

    # 获得标签
    def getLabel(self):
        return self.label

    # 以列表的形式获得属性
    def getAtt(self):
        return self.num, self.label

    # 更新属性
    def updateAtt(self, num, label, db):
        cur = db.cursor()
        try:
            sql = "UPDATE robot SET Rnum='{}',Rlabel='{}' WHERE Rnum='{}'".format(num, label, self.num)
            cur.execute(sql)
            # 提交数据
            db.commit()
            self.num = num
            self.label = label
            print("更新属性: {}  {} 成功！".format(num, label))
        except pymysql.Error as e:
            print("更新属性失败！".format(num) + str(e))


# 六轴工业机器人
class SixAxisRobot(Robot):
    def __init__(self, db, num, label='六轴工业机器人', insertOrNot=True):
        super().__init__(db, num, label, insertOrNot)
        self.label = label
        self.__generate6Motor(db)

    # 产生机器人运动节点
    def __generate6Motor(self, db):
        try:
            self.motor1 = MotorOfSix('J1', self.num, db)
            self.motor2 = MotorOfSix('J2', self.num, db)
            self.motor3 = MotorOfSix('J3', self.num, db)
            self.motor4 = MotorOfSix('J4', self.num, db)
            self.motor5 = MotorOfSix('J5', self.num, db)
            self.motor6 = MotorOfSix('J6', self.num, db)
        except pymysql.Error as e:
            print("创建机器人节点失败！" + str(e))



# 表查询操作
def SheetQuary(db, sheetName, condition=''):
    sheetList = []
    cur = db.cursor()
    sql = "select * from {} {}".format(sheetName,condition)
    cur.execute(sql)
    try:
        for row in cur.fetchall():
            sheetList.append(row)
        print("同步数据库成功！")
    except pymysql.Error as e:
        print("同步数据库失败" + str(e))
    db.commit()
    return sheetList


if __name__ == "__main__":
    # 测试代码
    print(SheetQuary(db, 'motor','where ofRobotNum={}'.format('009')))
    if __name__ == "__main__":
        datafile = dataFile()
# 若当前代码不是main则数据库不会自己关闭
