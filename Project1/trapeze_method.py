from math import exp, pow
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

def equation(t):
    return -exp(-pow(t, 2)) - 1.2 * exp(-pow(t - 2, 2)) + 0.6


def derivative(t):
    return 2 * t * exp(-pow(t, 2)) - 1.2 * (4 - 2 * t) * exp(-pow(t - 2, 2))


dt = 0.01
t = [i * dt for i in range(134)]
alpha = [0]
x = [2.8328820498299936]
v = [0]
F_1 = []
F_2 = []
Ek = []
Ev = []
for i in t:
    v.append(v[-1] - derivative(x[-1]) * dt - alpha[0] * v[-1] * dt)
    x.append(x[-1] + v[-1] * dt)
    F_1.append(x[-1] - x[-2] - dt / 2 * v[-1] - dt / 2 * v[-2])
    F_2.append(v[-1] - v[-2] - dt / 2 * (derivative(x[-1]) - alpha[0] * v[-1]) -
               dt / 2 * (derivative(x[-2]) - alpha[0] * v[-2]))
    Ek.append(F_2[-1] * F_2[-1] / 2)
    Ev.append(equation(F_1[-1]))

fig, ax = plt.subplots()

x.remove(x[-1])
v.remove(v[-1])


def plot_x_t():
    ax.plot(t, x, 'r')
    ax.plot(t, v, 'b')
    data_x = mlines.Line2D([], [], label='x(t)', color='blue')
    data_v = mlines.Line2D([], [], label='v(t)', color='green')
    ax.legend(handles=[data_x, data_v], loc='upper left',
              fontsize='x-large')

    ax.set(xlabel='t', ylabel="x, v", title="Metoda trapezów")
    plt.savefig("x(t)_trapeze.png")
    plt.show()


def plot_Ek_t():
    ax.plot(t, F_1, 'r')
    ax.plot(t, F_2, 'b')
    data_x = mlines.Line2D([], [], label='F_1(t)', color='red')
    data_v = mlines.Line2D([], [], label='F_2(t)', color='blue')
    ax.legend(handles=[data_x, data_v], loc='upper left',
              fontsize='x-large')

    ax.set(xlabel='t', ylabel="x", title="Metoda trapezów")
    plt.savefig("x(t)_trapeze.png")
    plt.show()


plot_Ek_t()

