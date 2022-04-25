# https://pl.spoj.com/problems/PP0502B/

t = int(input())

for i in range(t):
    ns = input().split(" ")
    ns = ns[::-1][:-1]  # Reverse all elements and remove the last one
    print(' '.join(ns))
