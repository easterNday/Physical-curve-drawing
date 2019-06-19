# 物理曲线的Pytthon绘制
## 所需Lib
1. matplotlib
2. numpy
## 所绘制曲线
1. 重力势能曲线
2. 抛体运动曲线
3. 点电荷电力线分布
4. 电偶极子电力线和等势面分布
5. 简谐振动
6. 李萨如图形
## 代码实现
```Python
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
```
```Python
import numpy as np
import matplotlib.pyplot as plt

def projectile(V_initial, theta, bouyancy=True, drag=True):
    g = 9.81
    m = 1
    C = 0.47
    r = 0.5
    S = np.pi*pow(r, 2)
    ro_mars = 0.0175

    time = np.linspace(0, 100, 10000)
    tof = 0.0
    dt = time[1] - time[0]
    bouy = ro_mars*g*(4/3*np.pi*pow(r, 3))
    gravity = -g * m
    V_ix = V_initial * np.cos(theta)
    V_iy = V_initial * np.sin(theta)
    v_x = V_ix
    v_y = V_iy
    r_x = 0.0
    r_y = 0.0
    r_xs = list()
    r_ys = list()
    r_xs.append(r_x)
    r_ys.append(r_y)
    # This gets a bit 'hand-wavy' but as dt -> 0 it approaches the analytical solution.
    # Just make sure you use sufficiently small dt (dt is change in time between steps)
    for t in time:
        F_x = 0.0
        F_y = 0.0
        if (bouyancy == True):
            F_y = F_y + bouy
        if (drag == True):
            F_y = F_y - 0.5*C*S*ro_mars*pow(v_y, 2)
            F_x = F_x - 0.5*C*S*ro_mars*pow(v_x, 2) * np.sign(v_y)
        F_y = F_y + gravity

        r_x = r_x + v_x * dt + (F_x / (2 * m)) * dt**2
        r_y = r_y + v_y * dt + (F_y / (2 * m)) * dt**2
        v_x = v_x + (F_x / m) * dt
        v_y = v_y + (F_y / m) * dt
        if (r_y >= 0.0):
            r_xs.append(r_x)
            r_ys.append(r_y)
        else:
            tof = t
            r_xs.append(r_x)
            r_ys.append(r_y)
            break

    return r_xs, r_ys, tof

v = 30
theta = np.pi/4

fig = plt.figure(figsize=(8,4), dpi=100)
r_xs, r_ys, tof = projectile(v, theta, True, True)
plt.plot(r_xs, r_ys, 'g:', label="Gravity, Buoyancy, and Drag")
r_xs, r_ys, tof = projectile(v, theta, False, True)
plt.plot(r_xs, r_ys, 'b:', label="Gravity and Drag")
r_xs, r_ys, tof = projectile(v, theta, False, False)
plt.plot(r_xs, r_ys, 'k:', label="Gravity")
plt.title("Trajectory", fontsize=14)
plt.xlabel("Displacement in x-direction (m)")
plt.ylabel("Displacement in y-direction (m)")
plt.ylim(bottom=0.0)
plt.legend()
plt.show()
```
```Python
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
```
```Python
from matplotlib.tri import (
  Triangulation, UniformTriRefiner, CubicTriInterpolator)
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

#-----------------------------------------------------------------------------
# Electrical potential of a dipole
#-----------------------------------------------------------------------------
def dipole_potential(x, y):
  """ The electric dipole potential V """
  r_sq = x**2 + y**2
  theta = np.arctan2(y, x)
  z = np.cos(theta)/r_sq
  return (np.max(z) - z) / (np.max(z) - np.min(z))

#-----------------------------------------------------------------------------
# Creating a Triangulation
#-----------------------------------------------------------------------------
# First create the x and y coordinates of the points.
n_angles = 30
n_radii = 10
min_radius = 0.2
radii = np.linspace(min_radius, 0.95, n_radii)

angles = np.linspace(0, 2 * np.pi, n_angles, endpoint=False)
angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)
angles[:, 1::2] += np.pi / n_angles

x = (radii*np.cos(angles)).flatten()
y = (radii*np.sin(angles)).flatten()
V = dipole_potential(x, y)

# Create the Triangulation; no triangles specified so Delaunay triangulation
# created.
triang = Triangulation(x, y)

# Mask off unwanted triangles.
triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
             y[triang.triangles].mean(axis=1))
        < min_radius)

#-----------------------------------------------------------------------------
# Refine data - interpolates the electrical potential V
#-----------------------------------------------------------------------------
refiner = UniformTriRefiner(triang)
tri_refi, z_test_refi = refiner.refine_field(V, subdiv=3)

#-----------------------------------------------------------------------------
# Computes the electrical field (Ex, Ey) as gradient of electrical potential
#-----------------------------------------------------------------------------
tci = CubicTriInterpolator(triang, -V)
# Gradient requested here at the mesh nodes but could be anywhere else:
(Ex, Ey) = tci.gradient(triang.x, triang.y)
E_norm = np.sqrt(Ex**2 + Ey**2)

#-----------------------------------------------------------------------------
# Plot the triangulation, the potential iso-contours and the vector field
#-----------------------------------------------------------------------------
fig, ax = plt.subplots()
ax.set_aspect('equal')
# Enforce the margins, and enlarge them to give room for the vectors.
ax.use_sticky_edges = False
ax.margins(0.07)

ax.triplot(triang, color='0.8')

levels = np.arange(0., 1., 0.01)
cmap = cm.get_cmap(name='hot', lut=None)
ax.tricontour(tri_refi, z_test_refi, levels=levels, cmap=cmap,
       linewidths=[2.0, 1.0, 1.0, 1.0])
# Plots direction of the electrical vector field
ax.quiver(triang.x, triang.y, Ex/E_norm, Ey/E_norm,
     units='xy', scale=10., zorder=3, color='blue',
     width=0.007, headwidth=3., headlength=4.)

ax.set_title('Gradient plot: an electrical dipole')
plt.show()
```
```Python
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
```
```Python
import numpy as np
from matplotlib.pyplot import plot
from matplotlib.pyplot import show
a = float(input())
b = float(input())
t = np.linspace(-np.pi, np.pi, 201)
x = np.sin(a * t + np.pi/2)
y = np.sin(b * t)
plot(x, y)
show()
```
## GITHUB链接
[东方怂天的GitHub][1]


[1]:https://github.com/easternDay/Physical-curve-drawing
