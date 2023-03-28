import sys
from collections import deque

class UFDS:
    def __init__(self, N):
        self.p = list(range(N))
        self.rank = [0]*N
        self.n = N
    def find_set(self, i):
        if self.p[i] == i: return i
        self.p[i] = self.find_set(self.p[i])
        return self.p[i]
    def is_same_set(self, i, j):
        return self.find_set(i) == self.find_set(j)
    def union(self, i, j): # assumes not same set
        self.n -= 1
        x, y = self.find_set(i), self.find_set(j)
        if self.rank[x] > self.rank[y]: self.p[y] = x
        else:
            self.p[x] = y
            if self.rank[x] == self.rank[y]: self.rank[y] += 1

N, MAX, K, E = int(input()), 1000, ((0, 1), (0, -1), (-1, 0), (1, 0)), {}
pts = set()
for l in sys.stdin:
    x, y = map(int, l.split())
    pts.add(MAX*x+y)
mst, uf, q, D = 0, UFDS(len(pts)), deque(pts), [(None, None) for _ in range(MAX**2)]
for i, n in enumerate(pts): D[n] = (0, i)
while q:
    xy = q.popleft()
    x, y = xy//MAX, xy%MAX
    for dx, dy in K:
        if 0 <= dx+x < MAX and 0 <= dy+y < MAX:
            nxt = MAX*(dx+x)+dy+y
            if D[nxt][0] != None:
                d = D[xy][0]+D[nxt][0]+1
                if d not in E: E[d] = []
                E[d].append((D[xy][1], D[nxt][1]))
                continue
            D[nxt] = (D[xy][0]+1, D[xy][1])
            q.append(nxt)
for d in sorted(E):
    for u, v in E[d]:
        if not uf.is_same_set(u, v):
            uf.union(u, v)
            mst += d
        if uf.n == 1: break
    if uf.n == 1: break
print(mst)