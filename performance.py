from timeit import timeit


def f1():
    lst = [1, 2, 3]
    lst = lst + list(range(100000000))
    lst = lst + list(range(100000000))
    lst = lst + list(range(100000000))
    return lst


def f2():
    lst = [1, 2, 3]
    lst.extend(range(100000000))
    lst.extend(range(100000000))
    lst.extend(range(100000000))
    return lst


def f3():
    lst = [1, 2, 3]
    for n in range(100000000):
        lst.append(n)
    for n in range(100000000):
        lst.append(n)
    for n in range(100000000):
        lst.append(n)
    return lst


n1 = timeit(f1, number=1)
n2 = timeit(f2, number=1)
n3 = timeit(f3, number=1)

print(n1, n2, n3)
