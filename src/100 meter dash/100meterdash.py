import sys; input = sys.stdin.readline
from collections import *
Z = 10**9; P = [(0, 0)]
for _ in range(int(input())): x, y, t = map(float, input().split()); P += [(x+y*1j, t)]
for _ in range(2):
    Q = deque(); S = 0; P = P[::-1]
    for p, t in P:
        if not Q: Q.append((p, t)); continue
        d = abs(p-Q[-1][0])
        while Q and S+d >= 100:
            Z = min(Z, abs(Q[-1][1]-Q[0][1]+(100-S)/d*(t-Q[-1][1])))
            if len(Q) > 1: S -= abs(Q[0][0]-Q[1][0])
            Q.popleft()
        if Q: S += d
        Q.append((p, t))
print(Z)