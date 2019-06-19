#coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
import math

# 支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
#显示负号
plt.rcParams['axes.unicode_minus'] = False


# 控制图形的长和宽单位为英寸，
# 调用figure创建一个绘图对象，并且使它成为当前的绘图对象。
plt.figure(figsize=(5,5))
# 设置X轴的范围
plt.xlim(-10,10)
# 设置Y轴的范围
plt.ylim(-10,10)

# 曲线设置
x=np.linspace(0,10,10)
y=np.array(x)

#$可以让字体变得跟好看
#给所绘制的曲线一个名字，此名字在图示(legend)中显示。
# 只要在字符串前后添加"$"符号，matplotlib就会使用其内嵌的latex引擎绘制的数学公式。
#color : 指定曲线的颜色
#linewidth : 指定曲线的宽度
rad = 0
for i in range(-50,50):
    y = math.tan(rad)*x
    rad += math.pi/6
    plt.plot(x,y, '--c',marker='^',color="red",linewidth=2, markersize=5)
    plt.plot(-x,y, '--c',marker='^',color="red",linewidth=2, markersize=5)
plt.plot(0,0, '--c',marker='o',label="点电荷",color="blue",linewidth=2, markersize=15)
#设置图表的标题
plt.title("点电荷电力线分布")


#显示图示
plt.legend()
#显示出我们创建的所有绘图对象。
plt.show()