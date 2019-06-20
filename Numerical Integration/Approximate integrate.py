import numpy as np
import sys
from termcolor import colored


def f_function(x):
    return np.sin(x)


def first_der_f_function(x):
    return np.cos(x)


def second_der_f_function(x):
    return -np.sin(x)


def fourth_der_f_function(x):
    return np.sin(x)


def int_f_function(x):
    return -np.cos(x)


def left_rectangle_method(a, b, h, func):
    x = a
    integral = 0
    while np.abs(b - x) > 0.00001:
        integral += func(x)
        x += h
    return integral*h


def right_rectangle_method(a, b, h, func):
    x = b
    integral = 0
    while np.abs(x - a) > 0.00001:
        integral += func(x)
        x -= h
    return integral*h


def middle_rectangle_method(a, b, h, func):
    x = b
    integral = 0
    while np.abs(x - a) > 0.00001:
        integral += func((2*x - h)/2)
        x -= h
    return integral*h


def trapezoid_method(a, b, h, func):
    x = b
    integral = 0
    while np.abs(x - a) > 0.00001:
        if (x - b) < 0.00001 or np.abs(x - h - a) < 0.00001:
            integral += (func(x - h) + func(x))*0.5
        else:
            integral += (func(x - h) + func(x))
        x -= h
    return integral * h


def simpson_method(a, b, h, func):
    x = b
    integral = 0
    while np.abs(x - a) > 0.00001:
        integral += (func(x - h) + 4*func((2*x - h) / 2) + func(x))/6
        x -= h
    return integral*h


def main():
    print("Программа для приближённого вычисления интеграла при помощи составных квадратурных формул".center(100))
    print("Выполнил Данил Кизеев".center(100))
    print("222 group".center(100))
    print("2019".center(100))
    while input("\nХотите ли вы выполнить программу(выполнить программу снова)?").lower().__eq__("да"):
        try:
            a = float(input("Введите, пожалуйста, значение левой границы промежутка (А):"))
            b = float(input("Введите, пожалуйста, значение правой границы промежутка (В):"))
            # coeffs = input("Введите, пожалуйста, коэффициенты многочлена в порядке убывания степеней").split(" ")
            #for i in range(coeffs.__len__()):
            #   coeffs[i] = int(coeffs[i])
            #f_function = np.poly1d(coeffs)
            m = int(input("Введите, пожалуйста, количество узлов разбиения промежутка (значение m):"))
        except SyntaxError:
            print("Ошибка, некорректно введены значения")
            sys.exit()

        h = (b - a) / m
        print("Полученный шаг функции: ", h)
        #print("Функция, которую вы ввели:\n ", f_function)
        #J = f_function()
        #print("Интеграл от этой функции:\n ", J)
        #J = (f_function(b) - f_function(a))/3
        J = int_f_function(b) - int_f_function(a)
        errorTable = []
        print("\nТочное значение интеграла: ", J)
        temp = left_rectangle_method(a, b, h, f_function)
        print("\nЗначение интеграла для", colored("метода левых прямоугольников: "
                                                  , 'green'), temp)
        errorTable.append(np.abs(J - temp))
        print("Погрешность метода левых прямоугольников:", errorTable[0])

        temp = right_rectangle_method(a, b, h, f_function)
        print("\nЗначение интеграла для", colored("метода правых прямоугольников: "
                                                  , 'green'), temp)
        errorTable.append(np.abs(J - temp))
        print("Погрешность метода правых прямоугольников:", errorTable[1])

        temp = middle_rectangle_method(a, b, h, f_function)
        print("\nЗначение интеграла для", colored("метода средних прямоугольников: "
                                                  , 'green'), temp)
        errorTable.append(np.abs(J - temp))
        print("Погрешность метода средних прямоугольников:", errorTable[2])

        temp = trapezoid_method(a, b, h * 0.5, f_function)
        print("\nЗначение интеграла для", colored("метода трапеций: "
                                                  , 'green'), temp)
        errorTable.append(np.abs(J - temp))
        print("Погрешность метода трапеций:", errorTable[3])

        temp = simpson_method(a, b, h * 0.5, f_function)
        print("\nЗначение интеграла для", colored("метода Симпсона: "
                                                  , 'green'), temp)
        errorTable.append(np.abs(J - temp))
        print("Погрешность метода Симпсона:", errorTable[4])

        print("\n\nБлок теоретической оценки:".center(100))
        print("Проверим точность для каждого из методов с помощью формулы:"
              "|R_{m}(f)| <= const*(B - A)*h^(d+1)*M_{d+1}, \nгде R_{m} - погрешность для метода из таблицы, "
              "const - константа из таблицы, \nA, B - пределы интегрирования, h - шаг, M_{d+1} - максимум из производных")

        first_der_function_table = []
        second_der_function_table = []
        fourth_der_function_table = []
        curr_a = a
        while np.abs(curr_a - b) > 0.00001:
            first_der_function_table.append(first_der_f_function(curr_a))
            second_der_function_table.append(second_der_f_function(curr_a))
            fourth_der_function_table.append(fourth_der_f_function(curr_a))
            curr_a += h

        print("Константа теоретической оценки для метода левых прямоугольников: ",
              1/2 * (b - a) * h * max(np.abs(first_der_function_table)))
        print("Явная погрешность метода левых прямоугольников:", errorTable[0])
        print("Константа теоретической оценки для метода правых прямоугольников: ",
              1/2 * (b - a) * h * max(np.abs(first_der_function_table)))
        print("Явная погрешность метода правых прямоугольников:", errorTable[1])
        print("Константа теоретической оценки для метода средних прямоугольников: ",
              1/24 * (b - a) * h**2 * max(np.abs(second_der_function_table)))
        print("Явная погрешность метода средних прямоугольников:", errorTable[2])
        print("Константа теоретической оценки для метода трапеций: ",
              1/12 * (b - a) * h**2 * max(np.abs(second_der_function_table)))
        print("Явная погрешность метода трапеций:", errorTable[3])
        print("Константа теоретической оценки для метода Симпсона: ",
              1/2880 * (b - a) * h**4 * max(np.abs(fourth_der_function_table)))
        print("Явная погрешность метода Симпсона:", errorTable[4])
        print("Меньше ли явная погрешность погрешности теоретической оценки: ".center(100))
        print("Для метода левых прямоугольников:", np.abs(errorTable[0]) <= 1 / 2 * (b - a) * h * max(np.abs(first_der_function_table)))
        print("Для метода правых прямоугольников:", np.abs(errorTable[1]) <= 1 / 2 * (b - a) * h * max(np.abs(first_der_function_table)))
        print("Для метода средних прямоугольников:", np.abs(errorTable[2]) <= 1 / 24 * (b - a) * h ** 2 * max(np.abs(second_der_function_table)))
        print("Для метода трапеций:", np.abs(errorTable[3]) <= 1 / 12 * (b - a) * h ** 2 * max(np.abs(second_der_function_table)))
        print("Для метода Симпсона:", np.abs(errorTable[4]) <= 1 / 2880 * (b - a) * h ** 4 * max(np.abs(fourth_der_function_table)))
    sys.exit()


main()
