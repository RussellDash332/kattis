import sys
from heapq import *
n, s = map(int, input().split())
a = [*map(int, sys.stdin)]
dp = [[] for _ in range(n)]
c = [0]
for i in a: c.append(c[-1]+i)
for i in range(1, n):
    # k1 = largest k such that sum(a[i-k:i]) <= s
    lo, hi = 0, i
    while hi-lo > 1:
        k1 = (lo + hi)//2
        if c[i]-c[i-k1] <= s: lo = k1
        else: hi = k1-1
    if i-hi >= 0 and c[i]-c[i-hi] <= s: k1 = hi
    elif i-lo >= 0 and c[i]-c[i-lo] <= s: k1 = lo
    else: k1 = 0
    # k2 = largest k such that sum(a[i:i+k]) <= s
    lo, hi = 0, n-i
    while hi-lo > 1:
        k2 = (lo + hi)//2
        if c[i+k2]-c[i] <= s: lo = k2
        else: hi = k2-1
    if i+hi <= n and c[i+hi]-c[i] <= s: k2 = hi
    elif i+lo <= n and c[i+lo]-c[i] <= s: k2 = lo
    else: k2 = 0
    # dp[i] = middle points
    dp[i-min(k1, k2)].append(-i)
q = []
for i in range(n):
    for j in dp[i]: heappush(q, j)
    while q and q[0] > -i: heappop(q)
    print(2*(-q[0]-i) if q else 0)