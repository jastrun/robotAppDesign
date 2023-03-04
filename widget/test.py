import serial
import threading
import time


# 串口打开函数
def open_ser():
    port = 'com7'  # 串口号
    baudrate = 9600  # 波特率
    try:
        global ser
        ser = serial.Serial(port, baudrate, timeout=0.01,xonxoff=False)
        if (ser.isOpen() == True):
            print("串口打开成功")
    except Exception as exc:
        print("串口打开异常", exc)


# 数据发送
def send_msg():
    try:
        send_datas = input("请输入要发送的数据\n")
        ser.write(str(send_datas).encode("gbk"))
        print("已发送数据:", send_datas)
    except Exception as exc:
        print("发送异常", exc)


# 接收数据
def read_msg():
    try:
        print("等待接收数据")
        while True:
            data = ser.read(ser.inWaiting()).decode('gbk')

 #           print(ser.in_waiting)
            if data != '':
                break
        print("已接受到数据:", data)
        print(type(data))
    except Exception as exc:
        print("读取异常", exc)


def read():
    data = ser.read(ser.in_waiting)
    print(ser.in_waiting)
    if data != '':
        return
    else:
        print("已接受到数据:", str(data))


# 关闭串口
def close_ser():
    try:
        ser.close()
        if ser.isOpen():
            print("串口未关闭")
        else:
            print("串口已关闭")
    except Exception as exc:
        print("串口关闭异常", exc)


if __name__ == '__main__':
    open_ser()  # 打开串口


#    a = threading.Thread(target=read_msg, name='aa')
#    a.start()



    while True:
        read_msg()
    read_msg()
    close_ser()  # 关闭串口
