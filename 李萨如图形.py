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