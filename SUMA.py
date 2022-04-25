# https://pl.spoj.com/problems/SUMA/

ns = []
while True:
    try:
        n = int(input())
    except EOFError:
        break
    
    ns.append(n)

    sum = 0
    for i in ns:
        sum += i
    
    print(sum)
