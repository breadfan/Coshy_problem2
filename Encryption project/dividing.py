def less(a, b):
    if len(a) < len(b):
        a = ['0'] * (len(b) - len(a)) + a
    if len(a) > len(b):
        b = ['0'] * (len(a) - len(b)) + b
    return a < b


def crop(a):
    k = 0
    while k < len(a) and a[k] == '0':
        k += 1
    if k == len(a):
        return ['0']
    return a[k:]


def division(x, y):
    a = [l for l in x]
    b = [l for l in y]
    crop(b)
    c = ['0']
    n = 0
    while not less(a, b):
        n += 1
        while less(a[:n], b):
            n += 1
            c += ['0']
        for i in range(1, len(b) + 1):
            if a[n - i] == '1' and b[-i] == '1':
                a[n - i] = '0'

            elif a[n - i] == '0' and b[-i] == '1':
                j = n - i
                while a[j] != '1':
                    j -= 1
                a[j] = '0'
                for k in range(j + 1, n - i):
                    a[k] = '1'

        c += ['1']
    return ''.join(crop(c))


print(division('1011010010111111', '101101'))
