import sys; input = sys.stdin.readline
from bisect import *
h = {}; p = 31; m = 10**18+7; n = int(input()); w = {}
for i in range(n):
    h1 = 0
    for k in input().strip():
        h1 *= p; h1 += ord(k); h1 %= m
        if h1 not in h: h[h1] = []
        h[h1].append(i)
    w[h1] = i
for _ in range(int(input())):
    q = input().strip(); r = len(q)
    h1 = 0; ans = 0; hh = []
    for pos in range(r):
        h1 *= p; h1 += ord(q[pos]); h1 %= m
        hh.append(h1)
    t = w.get(h1, n-1)+1
    for x in hh:
        if x in h: ans += bisect_left(h[x], t)
    print(ans+t)