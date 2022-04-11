# https://pl.spoj.com/problems/VSR/

t = int(input())

for i in range(t):
    v1, v2 = [int(j) for j in input().split(" ")]
    print(int((2 * v1 * v2) / (v1 + v2)))
