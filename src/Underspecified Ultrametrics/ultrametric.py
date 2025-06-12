import sys; input = sys.stdin.readline
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
N, M = map(int, input().split()); E = {}; U = UFDS(N)
for _ in range(M):
    a, b, w = map(int, input().split())
    if w not in E: E[w] = []
    E[w].append((a, b))
for w in sorted(E):
    for a, b in E[w]:
        if U.find(a) == U.find(b): print('not ultrametric'); exit()
    for a, b in E[w]: U.union(a, b)
print('possibly ultrametric')