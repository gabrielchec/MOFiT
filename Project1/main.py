from math import exp, fabs
import matplotlib.pyplot as plt
#import bisection_method
#import newton_method
#import euler_integral_method
import euler_integral_method_resistance
#import trapeze_method
# -------------------------constant_values--------------------------------
mass = 1
energy = -0.6
velocity = 0


def equation(t):
    return -exp(-pow(t, 2)) - 1.2 * exp(-pow(t - 2, 2)) - energy

#bisection_method
#newton_method
euler_integral_method
#euler_integral_method_resistance
#trapeze_method