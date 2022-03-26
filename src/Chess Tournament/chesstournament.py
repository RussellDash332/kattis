import sys
from collections import deque

class UFDS:
    def __init__(self, N):
        self.p = [i for i in range(N)]
        self.rank = [0 for _ in range(N)]
        self.indeg = [0 for _ in range(N)]
        self.num_sets = N

    def find_set(self, i):
        if self.p[i] == i: return i
        self.p[i] = self.find_set(self.p[i])
        return self.p[i]

    def is_same_set(self, i, j):
        return self.find_set(i) == self.find_set(j)

    def union(self, i, j):
        if not self.is_same_set(i, j):
            self.num_sets -= 1
            x, y = self.find_set(i), self.find_set(j)
            if self.rank[x] > self.rank[y]:
                self.p[y] = x
                self.indeg[x] += self.indeg[y]
            else:
                self.p[x] = y
                self.indeg[y] += self.indeg[x]
                if self.rank[x] == self.rank[y]:
                    self.rank[y] += 1

v, e = map(int, input().split())
g = {}
ufds = UFDS(v)
wait = []
for line in sys.stdin:
    a, r, b = line.split()
    a, b = ufds.find_set(int(a)), ufds.find_set(int(b))
    if r == '=':
        ufds.union(a, b)
    else:
        wait.append((a, b))

added = set()
for a, b in wait:
    a, b = ufds.find_set(int(a)), ufds.find_set(int(b))
    if a == b:
        print('inconsistent')
        sys.exit(0)
    if a not in g:
        g[a] = set()
    g[a].add(b)
    if (a, b) not in added:
        added.add((a, b))
        ufds.indeg[b] += 1

top = set()
q = set()
for i in range(v):
    par = ufds.find_set(i)
    if ufds.indeg[par] == 0:
        q.add(par)
        top.add(par)

q = deque(list(q))
while q:
    u = q.popleft()
    if u in g:
        decreased = set()
        for w in g[u]:
            w = ufds.find_set(w)
            if w not in decreased:
                if w in top:
                    print('inconsistent')
                    sys.exit(0)
                decreased.add(w)
                ufds.indeg[w] -= 1
                if ufds.indeg[w] == 0:
                    q.append(w)
                    top.add(w)
                elif ufds.indeg[w] < 0:
                    print('inconsistent')
                    sys.exit(0)
print(['inconsistent', 'consistent'][int(sum(ufds.indeg) == 0)])