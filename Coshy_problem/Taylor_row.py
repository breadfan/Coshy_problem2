import numpy as np
from termcolor import colored

h = 0.1
N = 10


def taylor_method(x):
    return 1 - x + x**2 - x**3 + x**4


def adams(table, number_first):
    temp_vec = []
    ddtable = []
    y_result = []
    for i in range(number_first + 2):
        temp_vec.append(h*-(table[1][i])**2)  # adding etta-vector
    ddtable.append(temp_vec)
    for number in range(number_first + 2, N + 3):
        for k in range(1, 5):       # on columns
            if number == number_first + 2:
                ddtable.append([])
                for i in range(number - k):      # n-k for the diagonal matrix
                    ddtable[k].append(ddtable[k - 1][i + 1] - ddtable[k - 1][i])
            else:
                ddtable[k].append(ddtable[k - 1][number - k] - ddtable[k - 1][number - k - 1])
        y_result.append(table[1][number - 1] + ddtable[0][number - 1] + 1/2*ddtable[1][number - 2]
                        + 5/12*ddtable[2][number - 3] + 3/8*ddtable[3][number - 4] + 251/720*ddtable[4][number - 5])
        ddtable[0].append(h * -(y_result[y_result.__len__() - 1])**2)
        table[1].append(y_result[y_result.__len__() - 1])
    return y_result


def runge_cutta(table):
    y_result = []
    for number in range(1, N + 1):
        const_first = h * (-(table[1][number - 1])**2)
        const_second = h * (-(table[1][number - 1] + const_first/2)**2)
        const_third = h * (-(table[1][number - 1] + const_second/2)**2)
        const_fourth = h * (-(table[1][number - 1] + const_third)**2)
        y_result.append(table[1][number - 1] + 1/6*(const_first + 2*const_second + 2*const_third + const_fourth))
        table[1].append(y_result[y_result.__len__() - 1])
    return y_result


def euler_first(table):
    y_result = []
    for number in range(1, N + 1):
        y_result.append(table[1][number - 1] + h * (-(table[1][number - 1])**2))
        table[1].append(y_result[y_result.__len__() - 1])
    return y_result


def euler_second(table):
    y_result = []
    for number in range(1, N + 1):
        y_temp = table[1][number - 1] + 1/2*h*(-(table[1][number - 1])**2)
        y_result.append(table[1][number - 1] + h * (-y_temp**2))
        table[1].append(y_result[y_result.__len__() - 1])
    return y_result


def euler_third(table):
    y_result = []
    for number in range(1, N + 1):
        y_temp = table[1][number - 1] + h * (-(table[1][number - 1]) ** 2)
        y_result.append(table[1][number - 1] + 1/2 * h * (-(table[1][number - 1]) ** 2 + (-y_temp ** 2)))
        table[1].append(y_result[y_result.__len__() - 1])
    return y_result


# values for derivatives:
# first_der = -1; second_der = 2; third_der = -6; fourth_der = 24


def main():
    print("Программа для численного решения задачи Коши.".center(100))
    print("Выполнил Данил Кизеев".center(100))
    print("222 group".center(100))
    print("2019".center(100))
    while input("\nХотите ли вы выполнить программу(выполнить программу снова)?").lower().__eq__("да"):
        print("Вывод таблицы точных значений интегралов: \n")
        accurate_values = []
        for i in range(-2, N + 1):
            accurate_values.append(1/(i * h + 1))
            print("y = {0}".format(accurate_values[accurate_values.__len__() - 1]))
        # Taylor's method
        taylor_values = []
        result = list()
        taylor_values.append([x for x in range(-2, N + 1)])  # appending x values
        temp_vector = []
        print('\n')
        for i in range(-2, N + 1):
            temp = taylor_method(i * h)
            temp_vector.append(temp)
            print("Приближённое решение для x = {0}: ".format(i * h), temp)
            print("Абсолютная погрешность приближённого решения: {0}".format(np.abs(accurate_values[i + 2] - temp)))
        taylor_values.append(temp_vector)   # appending y values
        # Adams's method
        table_for_adams = [[], []]
        for i in range(5):
            table_for_adams[0].append(taylor_values[0][i])      # copying x-coordinates
            table_for_adams[1].append(taylor_values[1][i])      # copying y-coordinates
        result.append(adams(table_for_adams, 3))
        table_cauchy_initial_conditions = [[0], [1]]         # as a parameter
        # Runge-Cutta's method
        result.append(runge_cutta(table_cauchy_initial_conditions))
        # Euler first method
        result.append(euler_first(table_cauchy_initial_conditions))
        # Euler second method
        result.append(euler_second(table_cauchy_initial_conditions))
        # Euler third method
        result.append(euler_third(table_cauchy_initial_conditions))

        # OUTPUT
        print('\n')
        print(colored("Результаты для метода Адамса 4-го порядка: ", 'red'))
        result[0].insert(0, table_for_adams[1][4])
        result[0].insert(0, table_for_adams[1][3])
        print(result[0])
        print(colored("Результаты для метода Рунге-Кутты: ", 'red'))
        print(result[1])
        print(colored("Результаты для первого метода Эйлера: ", 'red'))
        print(result[2])
        print(colored("Результаты для второго метода Эйлера: ", 'red'))
        print(result[3])
        print(colored("Результаты для третьего метода Эйлера: ", 'red'))
        print(result[4])

        # ERRORS block
        print("\nБлок ошибок(указаны погрешности последних членов):\n")
        errors = []
        for i in range(5):
            errors.append(np.abs(result[i][N - 1] - accurate_values[N + 2]))
        print(colored("Погрешность для метода Адамса 4-го порядка: ", 'blue'))
        print(errors[0])
        print(colored("Погрешность для метода Рунге-Кутты: ", 'blue'))
        print(errors[1])
        print(colored("Погрешность для первого метода Эйлера: ", 'blue'))
        print(errors[2])
        print(colored("Погрешность для второго метода Эйлера: ", 'blue'))
        print(errors[3])
        print(colored("Погрешность для третьего метода Эйлера: ", 'blue'))
        print(errors[4])


main()
