import sys; input = sys.stdin.readline
from collections import deque
n, e = map(int, input().split())
z = input().strip().split()
k = {e:i for i,e in enumerate(z)}
g = [[] for _ in range(n)]
for _ in range(e): a, x, b = input().strip().split(); g[k[a]].append(k[b]) if x == '<' else g[k[b]].append(k[a])
indeg, top = [0]*n, []
for v in range(n):
    for w in g[v]: indeg[w] += 1
q = deque([i for i in range(n) if indeg[i] == 0])
if len(q) != 1: print('veit ekki'), exit(0)
while q:
    u = q.popleft()
    top.append(u); x = 0
    for v in g[u]:
        indeg[v] -= 1
        if indeg[v] == 0: q.append(v); x += 1
    if x > 1: print('veit ekki'), exit(0)
print(*(z[i] for i in top)) if len(top) == n else print('veit ekki')