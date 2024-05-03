import os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
from array import *

class UFDS:
    def __init__(self, N):
        self.p = [*range(N)]; self.rank = [0]*N
    def find(self, i):
        if self.p[i] == i: return i
        self.p[i] = self.find(self.p[i])
        return self.p[i]
    def union(self, i, j):
        if (x:=self.find(i)) != (y:=self.find(j)):
            if self.rank[x] > self.rank[y]: self.p[y] = x
            else: self.p[x] = y; self.rank[y] += self.rank[x] == self.rank[y]

n, m, z = map(int, input().split()); el = []; mst = array('b', [0]*m); u = UFDS(n)
for _ in range(m): a, b, w = map(int, input().split()); el.append((w, a-1, b-1))
el.sort(key=lambda x: x[0])
for i, (w, a, b) in enumerate(el):
    if u.find(a) != u.find(b): u.union(a, b); mst[i] = 1
for i, (w, a, b) in enumerate(el):
    if not mst[i]:
        g = [[] for _ in range(n)]; g[a].append((b, w)); g[b].append((a, w)); s = array('b', [0]*n); t = [(a, -1, 0)]
        for j in range(m):
            if mst[j]: x, u, v = el[j]; g[u].append((v, x)); g[v].append((u, x))
        while t:
            u, p, d = t.pop()
            if s[u]: print(w*w+z*d); break
            s[u] = 1
            for v, x in g[u]:
                if x != p: t.append((v, x, d+1))
        exit(0)
print('Poor girl')