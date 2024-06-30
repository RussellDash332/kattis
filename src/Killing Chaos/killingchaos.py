class UFDS:
    def __init__(self, N):
        self.p = [*range(N)]; self.rank = [0]*N; self.s = [0]*N; self.n = self.S = 0
    def find(self, i):
        if self.p[i] == i: return i
        self.p[i] = self.find(self.p[i])
        return self.p[i]
    def union(self, i, j):
        if (x:=self.find(i)) != (y:=self.find(j)):
            self.n -= 1; self.S -= ((self.s[x]+9)//10+(self.s[y]+9)//10)*10
            if self.rank[x] > self.rank[y]: self.p[y] = x; self.s[x] += self.s[y]; self.S += (self.s[x]+9)//10*10
            else: self.p[x] = y; self.rank[y] += self.rank[x] == self.rank[y]; self.s[y] += self.s[x]; self.S += (self.s[y]+9)//10*10

import sys; input = sys.stdin.readline
N = int(input()); A = [*map(int, input().split())]; P = [*map(int, input().split())]; Z = 0; U = UFDS(N)
while P:
    p = P.pop()-1; U.s[p] = A[p]; U.S += (A[p]+9)//10*10; U.n += 1
    if p > 0 and U.s[p-1]: U.union(p, p-1)
    if p < N-1 and U.s[p+1]: U.union(p, p+1)
    Z = max(Z, U.S*U.n)
print(Z)