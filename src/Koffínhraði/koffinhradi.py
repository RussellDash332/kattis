import sys; input = sys.stdin.readline; from heapq import *
d = []; q = []; u = r = 0
for _ in range(int(input())): a, b = map(int, input().split()); d.append((b, a))
for s, t in sorted(d):
    heappush(q, -t); u += t
    while u > s: r += 1; p = -heappop(q); heappush(q, -(p//2)); u += p//2-p
print(r)