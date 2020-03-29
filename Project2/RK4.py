from constants import *
import matplotlib.pyplot as plt
import matplotlib.lines as mlines


def acc_x(x, y):
    return - GRAVITY_CONST * SUN_MASS * x / pow(pow(x, 2) + pow(y, 2), 1.5)

def acc_y(x, y):
    return - GRAVITY_CONST * SUN_MASS * y / pow(pow(x, 2) + pow(y, 2), 1.5)

def step(x, y, v_x, v_y):
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


dt = 15 * 60

time = (i for i in range( 4 * 75 * 365 * 24 * 4))
data_rk = [[COMET_POS[0], COMET_POS[1], COMET_VEL[0], COMET_VEL[1]]]

for t in time:
    data_rk.append(step(*(data_rk[-1])))

fig, ax = plt.subplots()

x_fin = [i[0] for i in data_rk]
y_fin = [i[1] for i in data_rk]


def plot_x_y():
    ax.plot(x_fin, y_fin, 'b')
    ax.set(xlabel='x', ylabel="y", title="Metoda RK4 dla dt = 15 min")
    plt.savefig("RK4_x_y.png")

    plt.show()


def plot_y_t():
    ax.plot(y_fin, time, 'b')
    ax.set(xlabel='x', ylabel="y", title="Metoda RK4 dla dt = 15 min")
    plt.savefig("RK4_x_y.png")

    plt.show()


plot_x_y()
