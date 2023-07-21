class UFDS:
    def __init__(self, N):
        self.p = [*range(N)]
        self.rank = [0]*N
    def find_set(self, i):
        if self.p[i] == i: return i
        self.p[i] = self.find_set(self.p[i])
        return self.p[i]
    def union(self, i, j):
        if (x:=self.find_set(i)) != (y:=self.find_set(j)):
            if self.rank[x] > self.rank[y]: self.p[y] = x
            else: self.p[x] = y; self.rank[y] += self.rank[x] == self.rank[y]

import sys; input = sys.stdin.readline
from collections import deque
V, E = map(int, input().split())
G = [[] for _ in range(V)]
D, S, T = [0]*V, [0]*V, [0]*V
U = UFDS(V)
t = 1; q = deque()
for _ in range(E): a, b = map(int, input().split()); G[a].append(b), G[b].append(a), U.union(a, b)
for _ in range(int(input())):
    a, b = map(int, input().split())
    if U.find_set(a) != U.find_set(b): print(-1); continue
    q.append(a), q.append(b)
    D[a] = D[b] = 0; S[a] = S[b] = t; T[a], T[b] = 0, 1 # T[x]: coming from a or b?
    while q:
        u = q.popleft()
        for v in G[u]:
            if S[v] == t and T[u] != T[v]: print(D[u] + D[v] + 1); q = deque(); t += 1; break # meet in the middle
            if S[v] != t: D[v] = D[u] + 1; T[v] = T[u]; S[v] = t; q.append(v)