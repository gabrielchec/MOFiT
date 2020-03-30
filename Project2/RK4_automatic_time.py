from constants import *
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from math import log10

d_t = 60 * 15
tol = 1000
time = 60 * 60 * 24 * 365 * 75 * 4
time_list = [0]
t = 0
data_rk = [[COMET_POS[0], COMET_POS[1], COMET_VEL[0], COMET_VEL[1]]]
step_list = [d_t]


def acc_x(x, y):
    return - GRAVITY_CONST * SUN_MASS * x / pow(pow(x, 2) + pow(y, 2), 1.5)


def acc_y(x, y):
    return - GRAVITY_CONST * SUN_MASS * y / pow(pow(x, 2) + pow(y, 2), 1.5)


def step(x, y, v_x, v_y, dt):
    u_k = [x, y, v_x, v_y]

    x_k = [[1, 1, 1, 1],
           [1, 1, 1, 1],
           [1, 1, 1, 1],
           [1, 1, 1, 1]]

    x_k[0][0] = v_x
    x_k[0][1] = v_y
    x_k[0][2] = acc_x(x, y)
    x_k[0][3] = acc_y(x, y)

    x_k[1][0] = v_x + x_k[0][2] * dt / 2.
    x_k[1][1] = v_y + x_k[0][3] * dt / 2.
    x_k[1][2] = acc_x(x + dt / 2. * x_k[0][0], y + dt / 2. * x_k[0][1])
    x_k[1][3] = acc_y(x + dt / 2. * x_k[0][0], y + dt / 2. * x_k[0][1])

    x_k[2][0] = v_x + x_k[1][2] * dt / 2.
    x_k[2][1] = v_y + x_k[1][3] * dt / 2.
    x_k[2][2] = acc_x(x + dt / 2. * x_k[1][0], y + dt / 2. * x_k[1][1])
    x_k[2][3] = acc_y(x + dt / 2. * x_k[1][0], y + dt / 2. * x_k[1][1])

    x_k[3][0] = v_x + x_k[2][2] * dt
    x_k[3][1] = v_y + x_k[2][3] * dt
    x_k[3][2] = acc_x(x + dt * x_k[2][0], y + dt * x_k[2][1])
    x_k[3][3] = acc_y(x + dt * x_k[2][0], y + dt * x_k[2][1])

    u = [0, 0, 0, 0]
    for i in range(4):
        u[i] = u_k[i] + dt / 6. * (x_k[0][i] + x_k[3][i] + 2 * x_k[1][i] + 2 * x_k[2][i])
    return u


def plot_x_y():
    ax.plot(x_fin, y_fin, 'b')
    ax.set(xlabel='x [m]', ylabel="y [m]", title="RK4 z automatycznym doborem kroku czasowego")
    plt.savefig("RK4_auto_x_y_1000.png")

    #plt.show()


def plot_y_t():
    ax.plot(time_list, y_fin, 'b')
    ax.set(xlabel='t [s]', ylabel="y", title="RK4 z automatycznym doborem kroku czasowego ")
    plt.savefig("RK4_auto_x_t_1000.png")

    #plt.show()

def plot_step_r():
    ax.plot(dist, step_list, 'b*')
    ax.set(xlabel='odległość [AU]', ylabel="krok [dni]",
    title="RK4 z automatycznym doborem kroku czasowego")
    plt.savefig("RK4_auto_step_r_1000.png")

    # plt.show()


while t < time:
    data_temp = step(*(data_rk[-1]), d_t)
    data_temp_short = step(*(data_rk[-1]), d_t / 2)
    data_temp_short = step(*data_temp_short, d_t / 2)

    if data_temp_short[0] - data_temp[0] > data_temp_short[1] - data_temp_short[1]:
        fault = data_temp_short[0] - data_temp[0]
    else:
        fault = data_temp_short[1] - data_temp[1]

    fault /= (2 ** 4 - 1)
    if fault < tol:
        data_rk.append(data_temp)
        time_list.append(t)
        step_list.append(d_t)
        t += d_t
    d_t *= 0.9 * pow(tol / abs(fault), 0.2)

x_fin = [i[0] for i in data_rk]
y_fin = [i[1] for i in data_rk]

dist = list(map(lambda x, y: pow(pow(x, 2) + pow(y, 2), .5) / AU, x_fin, y_fin))
step_list = list(map(lambda x: log10(x / 3600 / 24), step_list))
dist.sort()

step_list.sort()
fig, ax = plt.subplots()
plot_x_y()
fig, ax = plt.subplots()
plot_y_t()
fig, ax = plt.subplots()
plot_step_r()
