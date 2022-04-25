# https://pl.spoj.com/problems/JPESEL/

n = int(input())

for i in range(n):
    pesel = input()

    multipliers = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 1]
    psum = 0
    
    for i in range(11):
        psum += int(pesel[i]) * multipliers[i]

    if psum > 0:
        if psum % 10 == 0:
            print("D")
        else:
            print("N")
    else:
        print("N")
