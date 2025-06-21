import sys; input = sys.stdin.readline
from collections import *
from bisect import *
def lis(A):
    B = []
    for e in A:
        p = bisect(B, e-1)
        if p == len(B): B.append(e)
        else: B[p] = e
    return len(B)
n, m, d = map(int, input().split()); g = {}; indeg = Counter(); top = []
for _ in range(m):
    a, b = map(int, input().split())
    if a not in g: g[a] = set()
    if b not in g[a]: g[a].add(b); indeg[b] += 1; indeg[a] = indeg[a]
q = deque([i for i in indeg if indeg[i] == 0])
while q:
    u = q.popleft()
    top.append(u)
    if u not in g: continue
    for v in g[u]:
        indeg[v] -= 1
        if indeg[v] == 0: q.append(v)
aa = [int(input()) for _ in range(n)]
c = []; r = {e:i for i,e in enumerate(top)}
for i in range(len(aa)):
    if aa[i] in r: c.append(r[aa[i]])
print(len(top)+n-2*(lis(c) if c else 0))