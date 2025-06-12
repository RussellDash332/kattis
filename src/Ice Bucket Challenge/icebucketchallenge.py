import sys; input = sys.stdin.readline
from collections import *
r, c, d = map(int, input().split())
rs, cs = map(int, input().split())
h = [[*map(int, input().split())] for _ in range(r)]
K = ((0, -1), (-1, 0), (1, 0), (0, 1))
V = [[0]*c for _ in range(r)]
Q = deque([(rs-1, cs-1, d)]); T = set()
while Q:
    while Q:
        i, j, k = Q.popleft()
        if V[i][j] >= k: continue
        V[i][j] = k
        if k < 2: continue
        for p, q in K:
            if r>i+p>-1<j+q<c:
                if h[i][j] == h[i+p][j+q]: Q.append((i+p, j+q, k-1))
                elif h[i][j] > h[i+p][j+q]: T.add((i+p, j+q))
    Q.extend((i, j, d) for i, j in T); T = set()
for v in V: print(*v)