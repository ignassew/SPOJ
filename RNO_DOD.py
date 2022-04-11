# https://pl.spoj.com/problems/RNO_DOD/

t = int(input())

for i in range(t):
    int(input())
    ns = [int(j) for j in input().split(" ")]

    x = 0
    for n in ns:
        x += n
    
    print(x)
