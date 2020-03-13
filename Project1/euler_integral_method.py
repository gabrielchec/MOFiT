from math import exp, pow
import matplotlib.pyplot as plt


def equation(t):
    return -exp(-pow(t, 2)) - 1.2 * exp(-pow(t - 2, 2)) + 0.6


def derivative(t):
    return 2 * t * exp(-pow(t, 2)) - 1.2 * (4 - 2 * t) * exp(-pow(t - 2, 2))


dt = 0.01
t = [i * dt for i in range(3000)]

x = [2.8328820498299936]
v = [0]
Ek = []
Ek_V = []
for i in t:
    x.append(x[-1] + v[-1]*dt)
    v.append(v[-1] - derivative(x[-1]) * dt)
    Ek.append(v[-1] * v[-1]/2)
    Ek_V.append(Ek[-1] + equation(x[-1]))
fig, ax = plt.subplots()

x.remove(x[-1])
v.remove(v[-1])
def plot_x_t():
    ax.plot(t, x, 'b')
    ax.plot(t,v,'g')
    ax.plot(t,Ek,'r')
    ax.plot(t,Ek_V)
    ax.set(xlabel='t', ylabel="x", title="Jawna metoda Eulera")
    plt.show()
    plt.savefig("x(t).png")


plot_x_t()
