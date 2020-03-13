from math import fabs


def bisection(fun, a, b, precision):
    '''
    Function return list with growing precision of point 0 of function using bisection method from compartment [a, b]
    :param fun: equation
    :param a: lower point
    :param b: upper point
    :param precision: to which precision function have to counts
    :return: list
    '''
    point_list = []

    while fabs(b - a) > precision:
        average = (a + b) / 2
        point_list.append(average)
        if fun(average) * fun(a) < 0:
            b = average
        elif fun(average) * fun(b) < 0:
            a = average
    return point_list


def newton_method(x, fun, fun_derivative):
    '''
    Function to find point 0 by using newton method
    :param x: point that is close to 0
    :param fun: equation
    :param fun_derivative:  derivative of function
    :return: value which is closer to 0 than :param x
    '''
    return x - fun(x) / fun_derivative(x)
