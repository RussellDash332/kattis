import os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline; from collections import *
N, M = map(int, input().split()); G = [{} for _ in range(N)]; Z = -10**18; Q = deque(); S = L = 0
for _ in range(M):
    a, b, w = map(int, input().split()); a -= 1; b -= 1
    if b not in G[a]: G[a][b] = G[b][a] = []
    G[a][b].append(w)
    if len(G[a][b]) == 2: Q.append((min(a, b), max(a, b)))
R = deque(i for i in range(N) if len(G[i]) == 2)
while Q or R:
    while Q:
        i, j = Q.popleft(); G[i][j].sort()
        if len(G[i][j]) > 1: Z = max(Z, G[i][j][-1]+G[i][j][-2]); G[i][j] = G[j][i] = [G[i][j][-1]]
        if len(G[i]) == 2:
            a, b = G[i]
            if len(G[i][a]) == len(G[i][b]) == 1: R.append(i)
        if len(G[j]) == 2:
            a, b = G[j]
            if len(G[j][a]) == len(G[j][b]) == 1: R.append(j)
    while R:
        u = R.popleft()
        if not G[u]: continue
        if len(G[u]) != 2: continue
        a, b = G[u]
        if len(G[u][a]) == len(G[u][b]) == 1:
            if b not in G[a]: G[a][b] = G[b][a] = []
            G[a][b].append(G[u][a][0]+G[u][b][0]); G[a].pop(u); G[b].pop(u); G[u].clear()
            if len(G[a][b]) > 1: Q.append((min(a, b), max(a, b)))
            if len(G[a]) == 2: R.append(a)
            if len(G[b]) == 2: R.append(b)
for i in range(N):
    for j in G[i]: S += sum(G[i][j]); L += len(G[i][j])
if L > 2: Z = max(Z, S//2)
print(Z)