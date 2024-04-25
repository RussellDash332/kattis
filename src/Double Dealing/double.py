from math import *
import sys; input = sys.stdin.readline
while True:
    n, k = map(int, input().split())
    if n+k:
        a = [[] for _ in range(k)]; p = []
        for i in range(n): a[i%k].append(i)
        for i in a: p.extend(i[::-1])
        s = [0]*n; c = 1
        for i in range(n):
            if s[i]: continue
            t = i; v = 1
            while p[t] != i: s[t] = 1; t = p[t]; v += 1
            c = lcm(c, v)
        print(c)
    else: break