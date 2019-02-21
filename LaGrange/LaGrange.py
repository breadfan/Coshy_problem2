import numpy as np


print("Give us n, please(n<=m):")
n = int(input())
a = 0.4
b = 0.9
y = 0.75
m = 15


def func(x):
    return np.sin(x) + x**2/2


def lagrange(table, n):
    poly = np.poly1d([0])       # giving a type of a polynomial
    for k in range(n):
        psi = np.poly1d([1])
        for i in range(n):
            if i != k:
                psi *= np.poly1d([1, -(table[i][0])])   # multipl to a (x - x_i)
        psi /= psi(table[k][0])
        poly += table[k][1] * psi   # poly = poly + f(x_k)*psi - MAIN FORM OF LAGRANGE-POLYNOMIAL INTERPOLATION
    for k in range(n):
        if abs(poly[k]) < 0.00000001:
            poly[k] = 0
    return poly


def newton(table, n):
    poly = np.poly1d([table[0][1]])
    for k in range(1, n):
        row = []
        for i in range(n - k):      # n-k for the diagonal matrix
            row[i] = (table[k][i] - table[k][i + 1]) / (table[i + 1][0] - table[i][0])
        table += row
        poly += np.poly1d([table[0][k]])
    for k in range(n):
        if abs(poly[k]) < 0.00000001:
            poly[k] = 0
    return poly


table = [((a + j / 30), func(j)) for j in range(m)]
p = lagrange(table, n)
print(p)
for i in range(n):
   for j in range(n):
       print(table[i][j] + " ")
#        print(table[i][j] + " ")
#table.sort(key = lambda pair: abs(x - pair[0]))
# table = sorted(table, key = lambda a, b: a[0] < b[0])
# print(table)
# np.sort(table, key = lambda a, b: a[0] < b[0])
# print(p)
#
# p = newton(table, n)
# print(p)
