import numpy as np
from termcolor import colored
a = -3
b = 7
h = 0.5
# eps = 0.00001


def func(x):
    return 2*(x**2) - 2**x - 5


def funcFirstDerivative(x):
    return 4*x - (2**x)*np.log(2)


def funcSecondDerivative(x):
    return 4 - (2**x)*(np.log(2))**2


def bisection(a, b, eps):
    counter = 0
    while func(a) * func(b) < 0:
        counter += 1
        c = (a + b)/2
        if abs(func(c)) < eps:
            return counter, c, a, b
        if func(a) * func(c) < 0:
            b = c
        elif func(c) * func(b) < 0:
            a = c


def newton(a, b, eps):
    counter = 0
    if func(a) * funcSecondDerivative(a) > 0:
        root = a           # first approximation counting
    elif func(b) * funcSecondDerivative(b) > 0:
        root = b
    else:
        root = a
    while np.abs(func(root)/funcFirstDerivative(root)) >= eps:
        root -= func(root)/funcFirstDerivative(root)
        counter += 1
    return counter, root, a, b


def newtonUp(a, b, eps):
    counter = 0
    if func(a) * funcSecondDerivative(a) > 0:
        root = a
    elif func(b) * funcSecondDerivative(b) > 0:
        root = b
    else:
        raise ValueError("YOU did smth wrong in the newtonUp method")
    x_0 = root
    while np.abs(func(root)/funcFirstDerivative(x_0)) >= eps:
        root -= func(root)/funcFirstDerivative(x_0)
        counter += 1
    return counter, root, a, b


def secant(a, b, eps):
    counter = 1
    x_second = b
    x_new = x_second - (x_second - a)/(func(x_second) - func(a)) * func(x_second)
    while np.abs(x_new - x_second) >= eps:
        x_second_temp = x_second
        x_second = x_new
        x_new = x_new - (x_new - x_second_temp) / (func(x_new) - func(x_second_temp)) * func(x_new)
        counter += 1
    return counter, x_new, a, b


def functionPrinting(a, b, h, eps, currFunction):
    currA = a
    currB = currA + h
    rootNumber = 0
    while currB <= b:
        if func(currA)*func(currB) < 0:     # if there is a root
            rootNumber += 1
            resultArr = currFunction(currA, currB, eps)
            print("\nОтрезок, содержащий ", rootNumber, " корень: a =", currA, " b =", currB)
            print("Количество шагов N для достижения точности ", eps, ':', resultArr[0])
            print("Приближенное решение уравнения: ", resultArr[1])
            if (currFunction != newtonUp) & (currFunction != newton):
                print("Границы последнего отрезка: a = ", resultArr[2], " b = ", resultArr[3])
                print("Длина последнего отрезка: ", np.abs(resultArr[3] - resultArr[2]))
            print("Абсолютная величина невязки/погрешность: ", np.abs(func(resultArr[1])))
        currA = currB
        currB += h


print("Решение нелинейного трансцендентного уравнения".center(60))
print("Подготовил Данил Кизеев, 222 группа ".center(60))
print("2019".center(60))
print('\n')


def main():
    program = True
    while program:
        try:
            #a = float(input("Введите, пожалуйста, левую границу отрезка(A):"))
            #b = float(input("Введите, пожалуйста, правую границу отрезка(B):"))
            eps = float(input("Введите, пожалуйста, значение eps > 0:"))
            h = float(input("Введите, пожалуйста, значение шага(h): "))
            program = False
        except SyntaxError:
            print("Некорректно введен/ы параметр/ы функций, попробуйте снова.")

    print(colored("\nРезультаты, полученные с помощью метода бисекции:", 'red'))
    functionPrinting(a, b, h, eps, bisection)

    print(colored("\nРезультаты, полученные с помощью метода Ньютона касательных:", 'red'))
    functionPrinting(a, b, h, eps, newton)

    print(colored("\nРезультаты, полученные с помощью модифицированного метода Ньютона:", 'red'))
    functionPrinting(a, b, h, eps, newtonUp)

    print(colored("\nРезультаты, полученные с помощью метода секущих:", 'red'))
    functionPrinting(a, b, h, eps, secant)


main()
