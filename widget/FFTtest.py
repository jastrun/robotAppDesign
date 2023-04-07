import numpy as np
from scipy.fftpack import fft, ifft
from matplotlib.pylab import mpl

# 导入必要的模块
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5 import QtCore, QtWidgets,QtGui
import matplotlib.pyplot as plt
import sys

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
mpl.rcParams['axes.unicode_minus'] = False  # 显示负号

# 采样点选择1400个，因为设置的信号频率分量最高为600赫兹，根据采样定理知采样频率要大于信号频率2倍，所以这里设置采样频率为1400赫兹（即一秒内有1400个采样点，一样意思的）
x = np.linspace(0, 1, 1400)

# 设置需要采样的信号，频率分量有200，400和600
y = 7 * np.sin(2 * np.pi * 200 * x) + 5 * np.sin(2 * np.pi * 400 * x) + 3 * np.sin(2 * np.pi * 600 * x)
plt.figure()
plt.plot(x, y)
plt.title('原始波形')

plt.figure()
plt.plot(x[0:50], y[0:50])
plt.title('原始部分波形（前50组样本）')
plt.show()

fft_y=fft(y)                          #快速傅里叶变换
print(len(fft_y))
print(fft_y[0:5])
'''运行结果如下：
1400
[-4.18864943e-12+0.j   9.66210986e-05-0.04305756j   3.86508070e-04-0.08611996j 
   8.69732036e-04-0.12919206j    1.54641157e-03-0.17227871j]
'''
