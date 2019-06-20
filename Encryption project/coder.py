import numpy as np
import random

def main():
    np.seterr(all='ignore')
    file_code = open('code.txt', 'w')
    np.random.seed()
    for i in range(437):
        file_code.write(str(random.randint(0, 1)))      # creating a long code
    file_code.close()
    file_code = open('code.txt', 'r')
    code_of_string = file_code.read()
    polynomial_first = np.poly1d([int(code_of_string[i]) for i in range(code_of_string.__len__())])
    coeffs_for_forming_polynomial = []

    for i in range(30):             # creating forming polynomial: p(x) = x^29 + x^22 + x^19 - x^10 - x^3 - 1
        if i == 29 or i == 22 or i == 19:
            coeffs_for_forming_polynomial.append(-1)
        elif i == 10 or i == 3 or i == 0:
            coeffs_for_forming_polynomial.append(1)
        else:
            coeffs_for_forming_polynomial.append(0)

    forming_polynomial = np.poly1d(coeffs_for_forming_polynomial)
    print(forming_polynomial)

    syndrome_polynomial = polynomial_first / forming_polynomial
    print(syndrome_polynomial[0])
    # print(syndrome_polynomial[1])
    # ex1 = np.poly1d([1, 1, 0, 1, 1])
    # ex2 = np.poly1d([1, 0, 1, 1])
    # print((ex1/ex2)[0])
    file_code.close()
    return


main()
