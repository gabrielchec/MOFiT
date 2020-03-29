from constants import *
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from math import pow

x = [COMET_POS[0]]
y = [COMET_POS[1]]
v_x = [COMET_VEL[0]]
v_y = [COMET_VEL[1]]

dt = 5 * 60

time = (i for i in range(3 * 75 * 365 * 24 * 12))


def x_n_1(x_n, v_n):
    return x_n + v_n * dt


def v_n_1(x_n, v_n, r):
    return v_n - GRAVITY_CONST * SUN_MASS / pow(r, 3) * x_n * dt


def r(x_x, x_y):
    return pow(pow(x_x, 2) + pow(x_y, 2), .5)


for t in time:
    v_x.append(v_n_1(x[-1], v_x[-1], r(x[-1], y[-1])))
    v_y.append(v_n_1(y[-1], v_y[-1], r(x[-1], y[-1])))

    x.append(x_n_1(x[-1], v_x[-2]))
    y.append(x_n_1(y[-1], v_y[-2]))



fig, ax = plt.subplots()

def plot_x_t():
    ax.plot(y, x, 'b')
    ax.set(xlabel='v', ylabel="x", title="Jawna metoda Eulera")
    data_x_y = mlines.Line2D([], [], label='x(t)', color='blue')
    ax.legend(handles=[data_x_y], loc='upper left',
              fontsize='x-large')
    plt.savefig("x(t).png")

    plt.show()

plot_x_t()