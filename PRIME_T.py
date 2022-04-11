# https://pl.spoj.com/problems/PRIME_T/

n = int(input())

for i in range(n):
    x = int(input())
    is_prime = True

    if x == 1:
        is_prime = False
    else:
        for j in range(2, int(x**0.5) + 1):
            if x % j == 0:
                is_prime = False
                break
    
    if is_prime:
        print("TAK")
    else:
        print("NIE")
