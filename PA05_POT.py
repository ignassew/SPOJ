# https://pl.spoj.com/problems/PA05_POT/

n = int(input())

t = {
    0: [0],
    1: [1],
    2: [2, 4, 8, 6],
    3: [3, 9, 7, 1],
    4: [4, 6],
    5: [5],
    6: [6],
    7: [7, 9, 3, 1],
    8: [8, 4, 2, 6],
    9: [9, 1]
}

for i in range(n):
    a, b = input().split(" ")
    a = int(a[-1])
    b = int(b)

    x = t[a]
    print(x[b % len(x) - 1])
