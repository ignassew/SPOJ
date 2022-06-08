# https://pl.spoj.com/problems/GLUTTON/

import math

t = int(input())

for i in range(t):
    n, m = [int(j) for j in input().split(" ")]

    c = 0
    for j in range(n):
        x = int(input())
        s = 24 * 60 * 60
        while True:
            # print(s)
            s -= x
            if s < 0:
                break
            c += 1
    
    p = math.ceil(c / m)
    
    print(p)
