# https://pl.spoj.com/problems/CALC/

while True:
    try:
        x = input()
    except EOFError:
        break
    
    x = x.split(' ')

    s = x[0]        # Sign
    n1 = int(x[1])  # First number
    n2 = int(x[2])  # Second number

    if s == "+":
        print(n1 + n2)
    elif s == "-":
        print(n1 - n2)
    elif s == "*":
        print(n1 * n2)
    elif s == "/":
        print(int(n1 / n2))
    elif s == "%":
        print(n1 % n2)
