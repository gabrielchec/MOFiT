from constants import *
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from math import pow, log10

x = [COMET_POS[0]]
y = [COMET_POS[1]]
v_x = [COMET_VEL[0]]
v_y = [COMET_VEL[1]]

d_t = 60 * 15
tol = 1
time = 60 * 60 * 24 * 365 * 76 * 3
time_list = [0]
step_list = [d_t]
t = 0


def x_n_1(x_n, v_n, dt):
    return x_n + v_n * dt


def v_n_1(x_n, v_n, r, dt):
    return v_n - GRAVITY_CONST * SUN_MASS / pow(r, 3) * x_n * dt


def r(x_x, x_y):
    return pow(pow(x_x, 2) + pow(x_y, 2), .5)


def plot_x_y():
    ax.plot(x, y, 'b')
    ax.set(xlabel='x [m]', ylabel="y [m]", title="Metoda Eulera z automatycznym doborem kroku czasowego")
    plt.savefig("Euler_auto_x_y_1.png")

    # plt.show()


def plot_y_t():
    ax.plot(time_list, y, 'b')
    ax.set(xlabel='t [s]', ylabel="y [m]", title="Metoda Eulera z automatycznym doborem kroku czasowego")
    plt.savefig("Euler_auto_y_1.png")

    # plt.show()


def plot_step_r():
    ax.plot(dist, step_list, 'b*')
    ax.set(xlabel='odległość [AU]', ylabel="krok [dni]", title="Metoda Eulera z automatycznym doborem kroku czasowego")
    plt.savefig("Euler_auto_step_r_1.png")

    # plt.show()


while t < time:
    v_x_tem = v_n_1(x[-1], v_x[-1], r(x[-1], y[-1]), d_t)
    v_y_tem = v_n_1(y[-1], v_y[-1], r(x[-1], y[-1]), d_t)

    v_x_tem_short = v_n_1(x[-1], v_x[-1], r(x[-1], y[-1]), d_t / 2)
    v_y_tem_short = v_n_1(y[-1], v_y[-1], r(x[-1], y[-1]), d_t / 2)

    x_tem_big = x_n_1(x[-1], v_x_tem, d_t)
    y_tem_big = x_n_1(y[-1], v_y_tem, d_t)

    x_tem_short = x_n_1(x[-1], v_x[-1], d_t / 2.)
    y_tem_short = x_n_1(y[-1], v_y[-1], d_t / 2.)

    v_x_tem_short = v_n_1(x_tem_short, v_x_tem_short, r(x_tem_short, y_tem_short), d_t / 2)
    x_tem_short = x_n_1(x_tem_short, v_x_tem_short, d_t / 2.)

    v_y_tem_short = v_n_1(y_tem_short, v_y_tem_short, r(x_tem_short, y_tem_short), d_t / 2)
    y_tem_short = x_n_1(y_tem_short, v_y_tem_short, d_t / 2.)

    if x_tem_short - x_tem_big > y_tem_short - y_tem_big:
        fault = x_tem_short - x_tem_big
    else:
        fault = y_tem_short - y_tem_big

    if fault < tol:
        v_x.append(v_n_1(x[-1], v_x[-1], r(x[-1], y[-1]), d_t))
        v_y.append(v_n_1(y[-1], v_y[-1], r(x[-1], y[-1]), d_t))
        x.append(x_tem_big)
        y.append(y_tem_big)
        time_list.append(t)
        t += d_t
        step_list.append(d_t)
    d_t *= 0.9 * pow(tol / abs(fault), 0.5)

dist = list(map(lambda x, y: r(x, y) / AU, x, y))
step_list = list(map(lambda x: log10(x / 3600 / 24), step_list))
dist.sort()
step_list.sort()

fig, ax = plt.subplots()
plot_step_r()
fig, ax = plt.subplots()
plot_x_y()
fig, ax = plt.subplots()
plot_y_t()
