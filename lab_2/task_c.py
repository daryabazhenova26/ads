from math import *

def f(x):
    return x**2 + sqrt(x)


C = float(input())
eps = 1e-10
left = 0
right = C

while (right - left) > eps:
    middle = (left + right) / 2
    if f(middle) < C:
        left = middle
    else:
        right = middle
print(middle)