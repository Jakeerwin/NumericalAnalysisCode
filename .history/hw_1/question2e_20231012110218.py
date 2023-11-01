import numpy as np

def f(x):
    return 1 / (1 + x)

def trapezoid_rule(a, b, n):
    h = (b - a) / n
    sum_terms = f(a) + f(b)
    for i in range(1, n):
        sum_terms += 2 * f(a + i * h)
    integral_approximation = (h / 2) * sum_terms
    return integral_approximation

target_accuracy = 3e-3
a, b = 0, 2
n = 2  # Initial number of intervals
integral_approximation = abs(trapezoid_rule(a, b, n) - target_accuracy)


print(integral_approximation)