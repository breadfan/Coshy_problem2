import numpy as np
import sys
import cmath

a = 0
b = 1
N = 2
#m = 100


def f_function(x):
    return np.sin(x)


def w_function(x):
    return np.cos(x)


def f_to_w_function(x):
    return np.cos(x) * np.sin(x)


def w_to_xk_function(x, k):
    return np.cos(x) * x**k


def square_equation(a, b, c):
    d = (b ** 2) - (4 * a * c)
    sol1 = (-b - np.sqrt(d)) / (2 * a)
    sol2 = (-b + np.sqrt(d)) / (2 * a)
    return sol1, sol2


def simpson_method(a, b, h, func, power_for_mu_moments):
    x = b
    integral = 0
    while x > a:
        integral += (func(x - h, power_for_mu_moments) + 4*func((2*x - h) / 2, power_for_mu_moments) 
                     + func(x, power_for_mu_moments))/6
        x -= h
    return integral*h


def gauss_first_method(a, b, m):
    h = (b - a)/m
    curr_x = a
    result_Integral = 0
    while curr_x < b:
        result_Integral += f_to_w_function(h/2*(1/np.sqrt(3) + 1) + curr_x) + \
                           f_to_w_function(h/2*(-1/np.sqrt(3) + 1) + curr_x)
        curr_x += h
    return result_Integral*h/2


def gauss_second_method(a, b, m):
    muTable = [simpson_method(a, b, 0.001, w_to_xk_function, i) for i in range(2*N)]    # 0 para
    print("Полученные значения моментов:\n")
    for i in range(2*N):
        print(muTable[i], " ")
    c_p_coeffs = np.linalg.solve(((muTable[1], muTable[0]), (muTable[2], muTable[1])),
                                 (-muTable[2], -muTable[3]))  # 1-2-3 para
    print("\nПолученный ортогональный многочлен: w_2(x) = x^2", end=" ")
    if c_p_coeffs[0] > 0:
        print("+", end="")
    print(c_p_coeffs[0], "x", end=" ")
    if c_p_coeffs[1] > 0:
        print("+", end=" ")
    print(c_p_coeffs[1])
    roots = square_equation(1, c_p_coeffs[0], c_p_coeffs[1])  # 4 para
    print("\nПолученные узлы: x_1=", roots[0], " x_2=", roots[1])
    if roots[0] == roots[1]:
        print("У уравнения получились два одинаковых корня, чего быть не может.\nExterminatus...")
        sys.exit()
    elif roots[0] < a or roots[0] > b or roots[1] < a or roots[1] > b:
        print("Полученные корни не принадлежат промежутку [a, b].\nExterminatus...")
        sys.exit()
    A_coeffs = np.linalg.solve(((1, 1), (roots[0], roots[1])), (muTable[0], muTable[1]))
    print("\nПолученные коэффициенты КФ: A_1=", A_coeffs[0], " A_2=", A_coeffs[1])
    print("Дополнительная проверка коэффициентов КФ: ",
          np.abs(muTable[3] - A_coeffs[0]*roots[0]**3 - A_coeffs[1]*roots[1]**3))
    return A_coeffs[0]*f_function(roots[0]) + A_coeffs[1]*f_function(roots[1])


def main():
    print("Програма для вычисления интегралов при помощи составных квадратурных формул Наивысшей Алгебраической"
          " Степени Точности (КФ НАСТ)".center(100))
    print("Выполнил Данил Кизеев".center(100))
    print("222 group".center(100))
    print("2019".center(100))
    while input("\nХотите ли вы выполнить программу(выполнить программу снова)?").lower().__eq__("да"):
        try:
            a = int(input("Введите, пожалуйста, значение левой границы промежутка (а):"))
            b = int(input("Введите, пожалуйста, значение левой границы промежутка (b):"))
            N = int(input("Введите, пожалуйста, количество узлов для формулы Гаусса(N):"))
            m = int(input("Введите, пожалуйста, число промежутков деления отрезка [a, b] (m):"))
        except SyntaxError:
            print("Ошибка, некорректно введены значения")
            sys.exit()
        
        print("Приближённое значение интеграла, полученное с помощью первого метода Гаусса: ", 
              gauss_first_method(a, b, m))
        print("Приближённое значение интеграла, полученное с помощью второго метода Гаусса: ",
              gauss_second_method(a, b, m))


main()
