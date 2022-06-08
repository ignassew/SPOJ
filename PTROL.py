# https://pl.spoj.com/problems/PTROL/

n = int(input())

for i in range(n):
    x = [i for i in input().split(" ")]
    x1 = int(x.pop(0))
    for _ in range(x1 + 1):
        y = x.pop(0)
        x.append(y)
    
    print(' '.join(x))