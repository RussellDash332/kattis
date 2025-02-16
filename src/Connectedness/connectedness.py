class UFDS:
    def __init__(self, N):
        self.p = [*range(N)]; self.rank = [0]*N; self.n = N
    def find(self, i):
        if self.p[i] == i: return i
        self.p[i] = self.find(self.p[i])
        return self.p[i]
    def union(self, i, j):
        if (x:=self.find(i)) != (y:=self.find(j)):
            self.n -= 1
            if self.rank[x] > self.rank[y]: self.p[y] = x
            else: self.p[x] = y; self.rank[y] += self.rank[x] == self.rank[y]
import sys; input = sys.stdin.readline
N, M = map(int, input().split()); U = UFDS(N)
if N == 1: print(0), exit()
for i in range(M):
    a, b = map(int, input().split()); U.union(a-1, b-1)
    if U.n == 1: print(i+1), exit()
print(-1)