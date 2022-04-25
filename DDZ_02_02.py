# https://pl.spoj.com/problems/DDZ_02_02/

n = int(input())

s = ""
for i in range(n):
    instruction, x = input().split(' ')

    if instruction == "DODAJ":
        s += x
    elif instruction == "USUN":
        if int(x) > len(s):
            s = ""
        else:
            s = s[0:-int(x)]
    elif instruction == "ZAMIEN":
        if s == "":
            continue

        s = s[:-1] + x

print(s)
