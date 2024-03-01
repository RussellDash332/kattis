import sys; input = sys.stdin.readline
from heapq import *
n, k, c = map(int, input().split())
q1, q2, r, h = [], [], [], {}
for i in range(n):
    t, s = map(int, input().split())
    q1.append((i, t, s)); h[s] = 0
heapify(q1)
while q1 and len(r) < k:
    u, t, s = heappop(q1)
    if h[s] < c: h[s] += 1; r.append((u, t))
    else: q2.append((u, t, s))
heapify(q2)
for _ in range(k-len(r)):
    u, t, s = heappop(q2)
    r.append((u, t))
for _, i in sorted(r): print(i)