# https://pl.spoj.com/problems/PRZEDSZK/

def nwd(a, b):  # Euclidean algorithm
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a

    return a

def nww(a, b):  # Least common multiple
    return int((a * b) / nwd(a, b))

n = int(input())

for i in range(n):
    a, b = [int(i) for i in input().split(' ')]
    print(nww(a, b))
