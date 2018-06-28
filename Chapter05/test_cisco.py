import matplotlib.pyplot as plt
import numpy as np
import psutil
from matplotlib import animation

fig = plt.figure()
ax = plt.axes(xlim=(0, 100), ylim=(0, 100))


def animate(i):
    xar = []
    yar = []
    x = np.linspace(i, i + 1)
    y = psutil.cpu_percent(interval=1)
    xar.append(x)
    yar.append(y)
    plt.plot(xar, yar, 'ro')
    print xar
    print yar


anim = animation.FuncAnimation(fig, animate, frames=200, interval=5, blit=False)
# anim = animation.FuncAnimation(fig, animate,interval=1000)
plt.show()
