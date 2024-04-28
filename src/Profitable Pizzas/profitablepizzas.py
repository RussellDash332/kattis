import sys; input = sys.stdin.readline
from heapq import *
n = int(input()); q = []; h = [[] for _ in range(2*10**6)]; M = 0
for _ in range(n): t, d = map(int, input().split()); h[t-1].append(d)
while h:
    for i in h.pop(): heappush(q, -i)
    if q: M -= heappop(q)
print(M)