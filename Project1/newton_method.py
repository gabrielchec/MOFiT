from math import exp
from functions import newton_method
import matplotlib.pyplot as plt

def equation(t):
    return -exp(-pow(t, 2)) - 1.2 * exp(-pow(t - 2, 2)) + 0.6


def derivative(t):
    return 2 * t * exp(-pow(t, 2)) - 1.2 * (4 - 2 * t) * exp(-pow(t - 2, 2))


point_one_x = [-1]
point_two_x = [2.5]
for i in range(10):
    point_one_x.append(newton_method(point_one_x[-1], equation, derivative))
    point_two_x.append(newton_method(point_two_x[-1], equation, derivative))


point_one_y = list(map(equation, point_one_x))
point_two_y = list(map(equation, point_two_x))

fun_point_two = [i * 0.01 + 2.2 for i in range(100)]
fun_point_one = [i * 0.01 - 1.1 for i in range(100)]

fig, ax = plt.subplots()

def plot_new_one():
    ax.plot(point_one_x, point_one_y, 'bo')
    ax.set(xlabel='X', ylabel="V", title="Metoda Newtona-Raphsona")
    ax.plot(fun_point_one, list(map(equation, fun_point_one)))
    plt.savefig("new_point_one.png")
    plt.show()


def plot_new_two():
    ax.plot(point_two_x, point_two_y, 'go')
    ax.set(xlabel='X', ylabel="V", title="Metoda Newtona-Raphsona")
    ax.plot(fun_point_two, list(map(equation, fun_point_two)))
    plt.savefig("new_point_two.png")
    plt.show()



plot_new_two()
