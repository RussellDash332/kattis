class UFDS:
    def __init__(self, a):
        self.p = [*range(len(a))]; self.rank = [0]*len(a); self.c = [*a]; self.h = [*range(len(a))]
    def find(self, i):
        if self.p[i] == i: return i
        self.p[i] = self.find(self.p[i])
        return self.p[i]
    def union(self, i, j):
        if (x:=self.find(i)) != (y:=self.find(j)):
            if self.rank[x] > self.rank[y]: self.p[y] = x; self.c[x] += self.c[y]; self.h[x] = max(self.h[x], self.h[y])
            else: self.p[x] = y; self.rank[y] += self.rank[x] == self.rank[y]; self.c[y] += self.c[x]; self.h[y] = max(self.h[x], self.h[y])
import sys; input = sys.stdin.readline
n, q = map(int, input().split())
a = [*map(int, input().split())]
z = [n]*n; s = []; u = UFDS(a)
for i in range(n):
    while s and s[-1][1] < a[i]: z[s.pop()[0]] = i
    s.append((i, a[i]))
for _ in range(q):
    c, *r = input().split()
    if c == '+':
        l, v = map(int, r); p = u.find(l-1)
        while v and p != n:
            p = u.find(p); x = min(v, u.c[p]); v -= x; u.c[p] -= x
            if (y:=z[u.h[p]]) != n and u.c[p] == 0 and v: u.union(p, y)
            p = y
    else: x = int(r[0])-1; y = u.find(x); print(a[x] if x-u.h[y] else a[x]-u.c[y])