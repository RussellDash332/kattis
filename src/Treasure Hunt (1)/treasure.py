import sys
n, m, k = map(int, input().split())
g = []
for l in sys.stdin: g.append(list(l.strip()))
for i in range(n):
    for j in range(m):
        if g[i][j] == 'S': s = i*m+j
        if g[i][j] == 'G': e = i*m+j
delta = ((0, 1), (0, -1), (-1, 0), (1, 0))

from heapq import *
from collections import defaultdict
D = defaultdict(lambda: 1e9)
D[(k, s)] = 1
pq = [(1, k, s)]
while pq:
    days, stamina, pos = heappop(pq)
    if pos == e: print(days), exit(0)
    r, c = pos//m, pos%m
    if days == D[(stamina, pos)]:
        succ, can_recharge = [], False
        for dr, dc in delta:
            if 0<=r+dr<n and 0<=c+dc<m:
                if g[r+dr][c+dc] in '.SG':
                    if stamina >= 1: succ.append((days, (stamina-1, (r+dr)*m+c+dc)))
                    else: can_recharge = True
                if g[r+dr][c+dc] == 'F':
                    if stamina >= 2: succ.append((days, (stamina-2, (r+dr)*m+c+dc)))
                    else: can_recharge = True
                if g[r+dr][c+dc] == 'M':
                    if stamina >= 3: succ.append((days, (stamina-3, (r+dr)*m+c+dc)))
                    else: can_recharge = True
        if can_recharge: succ.append((days+1, (k, pos)))
        for dd, (nn) in succ:
            if D[nn] > dd: D[nn] = dd; heappush(pq, (dd, *nn))
print(-1)