def swap(arr, f, s):
    temp = arr[f]
    arr[f] = arr[s]
    arr[s] = temp


def quicksort(arr, l, r):
    i = l
    j = r - 1
    p = l - 1
    q = r
    v = arr[r]
    while i <= r:
        while arr[i] < v:
            i += 1
        while arr[j] > v:
            j -= 1
        if i >= j:
            break
        swap(arr, i, j)
        if arr[i] == v:
            p += 1
            swap(arr, p, i)
        i += 1
        if arr[j] == v:
            q -= 1
            swap(arr, q, j)
        j -= 1

        j = i - 1
        i += 1
        for k in range(l, p):
            swap(arr, k, j)
            j -= 1
        for k in range(r, q):
            swap(arr, k, i)
            i += 1
        quicksort(arr, l, j)
        quicksort(arr, i, r)


arr = {1, 2, 4, -2, 3, 10, 10, 3, 3, 3, 3, 3, 10}
quicksort(arr, 0, len(arr) - 1)