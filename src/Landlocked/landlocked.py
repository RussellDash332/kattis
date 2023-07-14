import sys; input = sys.stdin.readline
from collections import deque
R, C = map(int, input().split())
m = [[*map(lambda x: ord(x)-64, input())] for _ in range(R)]
delta = ((1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1))
q, d, vis = deque([(i, -1) for i in range(R*C) if m[i//C][i%C] == 23]), {}, [0]*(R*C)
while q:
    u, s = q.popleft()
    if vis[u]: continue
    r, c = u//C, u%C
    if m[r][c] not in d: d[m[r][c]] = s
    vis[u] = 1
    for dr, dc in delta: # expand on-the-go
        if 0<=r+dr<R and 0<=c+dc<C:
            w = u+dr*C+dc
            if vis[w]: continue
            q.appendleft((w, s)) if m[r+dr][c+dc] == m[r][c] else q.append((w, s+1))
for i in range(1, 27):
    if i != 23 and i in d: print(chr(i+64), d[i])