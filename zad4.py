import numpy as np

# zad1

# liczby = np.arange(3, 46, 3)
# print(liczby)

# zad2

# a = np.array([0.1, 1.1])
# a = np.arange(2, dtype='int64')
# print(a.dtype)

# zad3

def zad3(n):
    m = np.zeros((n,n))
    yos = 1

    for i in range(n):
        for j in range(n):
            m[i, j] = yos
            yos += 1
    print(m)


def zad4(n, m):
    x = np.logspace(1, m, num=m, base=n)
    print(x)


def main():

    # zad3(4)
    zad4(2, 4)




main()
