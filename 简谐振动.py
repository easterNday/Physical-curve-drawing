import matplotlib.pyplot as plt
import numpy as np


def f(t):
    return np.cos(2 * np.pi * t)


a = np.arange(0.0, 5.0, 0.02)

plt.plot(a, f(a))
plt.xlabel('横坐标(时间)', fontproperties='Kaiti', fontsize=14, color='red')
plt.ylabel('纵坐标(振幅)', fontproperties='SimHei', fontsize=18, color='red')
plt.title('简谐运动 y=cos(2πx)', fontproperties='SimHei', fontsize=18, color='green')
plt.grid(True)
plt.axis([-1, 6, -2, 2])
plt.annotate('简谐运动曲线', xy=(3, 1), xytext=(4, 1.5), arrowprops=dict(facecolor='black', shrink=0.2),
             fontproperties='SimHei', fontsize=12, color='red')

plt.show()