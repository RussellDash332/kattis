import sys; input = sys.stdin.readline; from heapq import *
n, p, q, s = map(int, input().split()); P = sorted(int(input()) for _ in range(p)); Q = sorted(int(input()) for _ in range(q))

def f(x):
    m = cp = 0; pq = []
    for i in Q:
        while cp<p and P[cp]-x<=i: heappush(pq, min(P[cp]+x, s-P[cp])); cp += 1
        while pq:
            if heappop(pq)>=i: m += 1; break
        if m == n: return 1

lo, hi = 0, 10**9
while hi-lo>1:
    mi = (lo+hi)//2
    if f(mi): hi = mi
    else: lo = mi+1
ans = lo if f(lo) else lo+1; print([ans, -1][ans>10**9])