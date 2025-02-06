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
n, m = map(int, input().split()); u = UFDS(n)
for _ in range(m): a, b = map(int, input().split()); u.union(a-1, b-1)
print(pow(2, m-n+u.n, 10**9+9))