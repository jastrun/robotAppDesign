import time


class timeseries:
    def __init__(self):
        self.startFlag = False
        self.stopFlag = False  # 中间是否有过停止
        self.endFlag = True

        self.stopTime = 0


    def start(self):
        if self.startFlag == False:
            self.time_Base = time.time()
            self.startFlag = True
        else:
            print("计时器已经开始！无法再次开始！")

    def getCurTime(self):
        if self.startFlag == True:
            # 计算非停止时的时间
            if self.stopFlag == False:
                # 实际时间=当前时间-基时间-停止时间
                curTime = time.time() - self.time_Base - self.stopTime
                return curTime

            # 计算停止时的时间
            if self.stopFlag == True:
                stopTime = time.time() - self.stopstartTime # 计算停止到现在的时间
                # 实际时间=当前时间-基时间-停止时间
                curTime = time.time() - self.time_Base - stopTime
                return curTime
        else:
            print("计时器尚未开始，无法获取当前时间！")
            return False

    def stop(self):
        if self.stopFlag == False:
            self.stopFlag = True  # 确定中间有过停止
            self.stopstartTime = time.time()
        else:
            print("停止标志为真，不能再次停止！")

    def reStart(self):
        if self.stopFlag == True:
            self.stopTime = time.time() - self.stopstartTime  # 计算出中间停止的时间
            self.stopFlag = False
        else:
            print("停止标志为否，计时器尚未停止!")

    def end(self):
        if self.startFlag == True:
            self.startFlag = False
            self.stopTime = 0
        else:
            print("开始标志为否，不能再次停止！")


if __name__ == '__main__':
    #  计时器测试
    timer = timeseries()
    timer.start()
    time.sleep(1)
    print(timer.getCurTime())
    timer.stop()
    time.sleep(1)
    print(timer.getCurTime())
    timer.reStart()
    time.sleep(1)
    print(timer.getCurTime())
    print("type:", type(timer.getCurTime()))
    timer.end()
    print(timer.getCurTime())


    timer.start()
    time.sleep(1)
    print(timer.getCurTime())
    timer.stop()
    time.sleep(1)
    print(timer.getCurTime())
    timer.reStart()
    time.sleep(1)
    print(timer.getCurTime())
    timer.end()
    print(timer.getCurTime())
