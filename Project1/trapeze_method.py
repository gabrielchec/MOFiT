from math import exp, pow
import matplotlib.pyplot as plt


def equation(t):
    return -exp(-pow(t, 2)) - 1.2 * exp(-pow(t - 2, 2)) + 0.6


def derivative(t):
    return 2 * t * exp(-pow(t, 2)) - 1.2 * (4 - 2 * t) * exp(-pow(t - 2, 2))


dt = 0.2
t = [i * dt for i in range(500)]
alpha = [0]
x = [2.8328820498299936]
v = [0]
F_1 = []
F_2 = []
Ek = []
for i in t:
    x.append(x[-1] + v[-1] * dt)
    v.append(v[-1] - derivative(x[-1]) * dt - alpha[0] * v[-1] * dt)
    F_1.append(x[-1] - x[-2] - dt / 2 * v[-1] - dt / 2 * v[-2])
    F_2.append(v[-1] - v[-2] - dt / 2 * (derivative(x[-1] - alpha[0] * v[-1])) -
               dt / 2 * (derivative(x[-2] - alpha[0] * v[-2])))
    Ek.append(pow(F_2[-1], 2) / 2)

fig, ax = plt.subplots()

x.remove(x[-1])
v.remove(v[-1])


def plot_x_t():
    ax.plot(t, Ek, 'r')
    ax.set(xlabel='t', ylabel="x", title="Metoda trapezów")
    plt.show()
    plt.savefig("x(t)_trapeze.png")


plot_x_t()
