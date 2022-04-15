
d = [0] * 100

count = 0


def fibo(x):
    global count
    if x == 3:
        count += 1
    if x == 1 or x == 2:
        return 1

    if d[x] != 0:
        return d[x]

    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]


print(fibo(99))
