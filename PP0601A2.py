# https://pl.spoj.com/problems/PP0601A2/

c = 0
p = 42
while True:
    x = int(input())
    print(x)
    
    if x == 42 and p != 42:
        c += 1
    
    if c == 3:
        break

    p = x
