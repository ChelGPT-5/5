from math import radians, factorial

x = radians(20)
n = 0
summa = 0
eps = 0.0001
next_step = 1

while abs(next_step) > eps:
    next_step = pow(-1, n) * ((pow(x, 2 * n + 1)) / factorial(2 * n + 1))
    summa += next_step
    n += 1

print(round(summa, 5))
