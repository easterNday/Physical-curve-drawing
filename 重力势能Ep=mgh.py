#coding:utf-8
import numpy as np
import matplotlib.pyplot as plt

# 支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签


# 控制图形的长和宽单位为英寸，
# 调用figure创建一个绘图对象，并且使它成为当前的绘图对象。
plt.figure(figsize=(5,5))
# 设置X轴的范围
plt.xlim(0,10)
# 设置Y轴的范围
plt.ylim(0,100)

# 曲线设置
x=np.linspace(0,10,10)
y=np.array(9.8*x)

#$可以让字体变得跟好看
#给所绘制的曲线一个名字，此名字在图示(legend)中显示。
# 只要在字符串前后添加"$"符号，matplotlib就会使用其内嵌的latex引擎绘制的数学公式。
#color : 指定曲线的颜色
#linewidth : 指定曲线的宽度
plt.plot(x,y, '--c',marker='o',label="$9.8*x$",color="red",linewidth=2, markersize=5)
#设置X轴的文字
plt.xlabel("High(下落高度)")
#设置Y轴的文字
plt.ylabel("Ep(重力势能)")
#设置图表的标题
plt.title("重力势能曲线")


#显示图示
plt.legend()
#显示出我们创建的所有绘图对象。
plt.show()