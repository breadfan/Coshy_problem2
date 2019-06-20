import numpy as np
import sys

def func(x):
    return np.e**(3*x)


def funcFirstDerivative(x):
    return (np.e**(3*x))*3


def funcSecondDerivative(x):
    return (np.e**(3*x))*9


def main():
    print("Програма для нахождения производных таблично-заданной функции".center(100))
    print("Выполнил Данил Кизеев".center(100))
    print("222 group".center(100))
    print("2019".center(100))
    while input("\nХотите ли вы выполнить программу(выполнить программу снова)?").lower().__eq__("да"):
        table = []
        try:
            m = int(input("Введите, пожалуйста, количество узлов разбиения промежутка (значение m):"))
            a = int(input("Введите, пожалуйста, значение левой границы промежутка (а):"))
            h = np.float64(input("Введите, пожалуйста, значение шага промежутка(h):"))
            for i in range(m + 1):
                x = a + i * h
                table.append((x, func(x)))
        except SyntaxError:
            print("Ошибка, некорректно введены значения")

        tableOfDerivatives = []
        tableOfDerivatives.append(((-3*func(a) + 4*func(a + h) - func(a + 2*h))/(2*h),
                                   np.abs((-3*func(a) + 4*func(a + h) - func(a + 2*h))/(2*h) - funcFirstDerivative(a)),
                                   "NONE",
                                   "NONE"))
        currA = a + h
        for i in range(m - 1):
            firstDerApprox = (func(currA + h) - func(currA - h))/(2*h)
            secondDerApprox = (func(currA + h) - 2*func(currA) + func(currA - h))/h**2
            vec = ((firstDerApprox, np.abs(funcFirstDerivative(currA) - firstDerApprox),
                    secondDerApprox, np.abs(secondDerApprox - funcSecondDerivative(currA)))
                   )
            tableOfDerivatives.append(vec)
            currA += h
        firstDerApprox = (3*func(currA) - 4*func(currA - h) + func(currA - 2*h)) / (2 * h)
        vec = (firstDerApprox, np.abs(funcFirstDerivative(currA) - firstDerApprox),
                "NONE", "NONE"
               )
        tableOfDerivatives.append(vec)

        # printing the table
        print("Таблица производных:".center(100))
        for i in range(m + 1):
            print("\nx_i= ", '{:<1}'.format(table[i][0]), "f(x_i)= ", '{:<2}'.format(table[i][1]),
                  "f\'(x_i)= ", '{:>5}'.format(tableOfDerivatives[i][0]),
                  "|f\'(x_i)_т - f\'(x_i)_пр|= ", '{:>6}'.format(tableOfDerivatives[i][1]),
                  "f\"(x_i)= ", '{:>7}'.format(tableOfDerivatives[i][2]),
                  "|f\"(x_i)_т - f\"(x_i)_пр|= ", '{:>8}'.format(tableOfDerivatives[i][3]))
    sys.exit()


main()
