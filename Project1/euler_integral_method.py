from math import exp, pow
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

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
    x.append(x[-1] + v[-1] * dt)
    v.append(v[-1] - derivative(x[-1]) * dt)
    Ek.append(v[-1] * v[-1] / 2)
    Ek_V.append(Ek[-1] + equation(x[-1]))
fig, ax = plt.subplots()

x.remove(x[-1])
v.remove(v[-1])


def plot_x_t():
    ax.plot(t, x, 'b')
    ax.plot(t, v, 'g')
    ax.plot(t, Ek, 'r')
    ax.plot(t, Ek_V, 'y')
    ax.set(xlabel='v', ylabel="x", title="Jawna metoda Eulera")
    data_x = mlines.Line2D([], [], label='x(t)', color='blue')
    data_v = mlines.Line2D([], [], label='v(t)', color='green')
    data_Ek = mlines.Line2D([], [], label='Ek(t)', color='red')
    data_Ek_V = mlines.Line2D([], [], label='Ek(t) - Ep(t)', color='yellow')
    ax.legend(handles=[data_x, data_v, data_Ek, data_Ek_V], loc='upper left',
              fontsize='x-large')
    plt.savefig("x(t).png")

    #plt.show()

plot_x_t()

def plot_phase_portrait():
    ax.plot(x, v, 'b', markersize=1)
    ax.set(xlabel='x', ylabel="v", title="Portret fazowy jawnej metody Eulera dla t = 10000s i dt = 0.1")
    plt.savefig("my_euler_phase_01_10000.png")
    plt.show()


#plot_phase_portrait()
