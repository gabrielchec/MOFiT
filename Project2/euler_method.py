from constants import *
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from math import pow

x = [COMET_POS[0]]
y = [COMET_POS[1]]
v_x = [COMET_VEL[0]]
v_y = [COMET_VEL[1]]

dt = 15 * 60
time = [i for i in range(3 * 75 * 365 * 24 * 4)]


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


def plot_x_y():
    ax.plot(x, y, 'b')
    ax.set(xlabel='x [m]', ylabel="y [m]", title="Jawna metoda Eulera dla dt = 15 min")
    data_x_y = mlines.Line2D([], [], label='x(t)', color='blue')
    ax.legend(handles=[data_x_y], loc='upper left',
              fontsize='x-large')
    plt.savefig("euler_method_x_y.png")

    #plt.show()

def plot_y_t():
    ax.plot(time, y, 'b')
    ax.set(xlabel='t [s]', ylabel="y [m]", title="Jawna metoda Eulera dla dt = 15 min")
    data_x_y = mlines.Line2D([], [], label='x(t)', color='blue')
    ax.legend(handles=[data_x_y], loc='upper left',
              fontsize='x-large')
    plt.savefig("euler_method_y_t.png")

    #plt.show()

fig, ax = plt.subplots()
plot_x_y()
fig, ax = plt.subplots()
y.remove(y[-1])
plot_y_t()
