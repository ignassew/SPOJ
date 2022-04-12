# https://pl.spoj.com/problems/PP0501A/

t = int(input())

for i in range(t):
    a, b = [int(j) for j in input().split(" ")]

    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    
    print(a)
