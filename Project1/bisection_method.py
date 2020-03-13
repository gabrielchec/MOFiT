from functions import bisection
from math import exp, fabs
import matplotlib.pyplot as plt



def equation(t):
    return -exp(-pow(t, 2)) - 1.2 * exp(-pow(t - 2, 2)) + 0.6


point_one_x = bisection(equation, 1, 4, 0.000001)
point_one_y = list(map(equation, point_one_x))
fun_point_one = [i * 0.01 + 2 for i in range(200)]
point_two_x = bisection(equation, -2, 2, 0.0000001)
point_two_y = list(map(equation, point_two_x))
fun_point_two = [i * 0.01 - 2 for i in range(400)]


fig, ax = plt.subplots()


def plot_bis_one():
    ax.plot(point_one_x, point_one_y, 'bo')
    ax.set(xlabel='X', ylabel="V", title="Metoda bisekcji")
    ax.plot(fun_point_one, list(map(equation, fun_point_one)))
    plt.show()
    plt.savefig("bis_point_one.png")


def plot_bis_two():
    ax.plot(point_two_x, point_two_y, 'go')
    ax.set(xlabel='X', ylabel="V", title="Metoda bisekcji")
    ax.plot(fun_point_two, list(map(equation, fun_point_two)))
    plt.show()
    plt.savefig("bis_point_two.png")

print(point_one_x)
