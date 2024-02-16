import sys; input = sys.stdin.readline
from collections import *
from array import *
n = int(input())
g = [[] for _ in range(n)]
for i in range(n):
    _, *r = map(int, input().split())
    for j in r: g[j-1].append(i)
indeg, top = array('i', [0]*n), n
for v in range(n):
    for w in g[v]: indeg[w] += 1
q = deque([(i, 0) for i in range(n) if indeg[i] == 0]); d = array('i', [0]*n)
while q:
    u, t = q.popleft()
    if d[u] < t: d[u] = t
    top -= 1
    for v in g[u]:
        indeg[v] -= 1
        if indeg[v] == 0: q.append((v, t+1))
if top: print('Omogulegt!')
else:
    print('Mogulegt!')
    r = [[] for _ in range(max(d)+1)]
    for i in range(n): r[d[i]].append(str(i+1))
    print(len(r))
    for i in r: sys.stdout.write(str(len(i))+' '+' '.join(i)+'\n')