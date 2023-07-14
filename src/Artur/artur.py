import sys; input = sys.stdin.readline
N = int(input()); segs = [[*map(int, input().split())] for _ in range(N)]
g = [[] for _ in range(N)]
for i in range(N-1):
    x1, y1, x2, y2 = segs[i]
    if x1 > x2 or (x1 == x2 and y1 > y2): x1, y1, x2, y2 = x2, y2, x1, y1
    for j in range(i+1, N):
        x3, y3, x4, y4 = segs[j]
        if x3 > x4 or (x3 == x4 and y3 > y4): x3, y3, x4, y4 = x4, y4, x3, y3
        if x1 <= x3 <= x2:
            c = (y2-y1)*(x3-x1)-(y3-y1)*(x2-x1)
            if c < 0: g[i].append(j)
            elif c > 0: g[j].append(i)
            elif y2 < y3: g[i].append(j)
            elif y1 > y3: g[j].append(i)
        elif x3 <= x1 <= x4:
            c = (y4-y3)*(x1-x3)-(y1-y3)*(x4-x3)
            if c > 0: g[i].append(j)
            elif c < 0: g[j].append(i)
            elif y1 < y3: g[i].append(j)
            elif y1 > y4: g[j].append(i)
from collections import deque
indeg, q = [0]*N, deque()
for v in range(N):
    for w in g[v]: indeg[w] += 1
for v in range(N):
    if indeg[v] == 0: q.append(v)
while q:
    u = q.popleft(); print(u+1)
    for v in g[u]:
        indeg[v] -= 1
        if indeg[v] == 0: q.append(v)