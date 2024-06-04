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

V, E = map(int, input().split()); U = UFDS(V); C = [*map(int, input().split())]; G = [[] for _ in range(V)]; T = [[] for _ in range(V)]; M = 500
for _ in range(E):
    a, b = map(int, input().split()); G[a-1].append(b-1); G[b-1].append(a-1)
    if C[a-1] == C[b-1]: U.union(a-1, b-1)
for i in range(V):
    for j in G[i]: T[U.find(i)].append(U.find(j))
for i in {U.find(i) for i in range(V)}:
    Q = [i]; D = [-1]*V; D[i] = 0
    for u in Q:
        for v in T[u]:
            if D[v] == -1: D[v] = D[u]+1; Q.append(v)
    M = min(M, max(D))
print(M)