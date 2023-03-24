import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

t = np.linspace(0, 20, 100)

x = np.sin(np.pi / 5 * t)
y = np.sin(x)
z = np.linspace(0, 100, 100)

dataSet = np.array([x, y, z])
numDataPoints = len(t)


def animate_func(num):
    ax.plot3D(dataSet[0, :num + 1], dataSet[1, :num + 1],
              dataSet[2, :num + 1], c='blue')
    ax.plot3D(dataSet[0, 0], dataSet[1, 0], dataSet[2, 0],
              c='black', marker='.')
    ax.set_xlim3d([-1, 1])
    ax.set_ylim3d([-1, 1])
    ax.set_zlim3d([0, 100])


fig = plt.figure()
ax = plt.axes(projection='3d')
line_ani = animation.FuncAnimation(fig, animate_func, interval=100,
                                   frames=numDataPoints)
plt.show()