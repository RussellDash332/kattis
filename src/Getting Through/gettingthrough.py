import sys; input = sys.stdin.readline
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
def ok(r, n):
    u = UFDS(n+2)
    for i in range(n):
        if c[i][0]-c[i][2] <= r: u.union(i, n)
        if c[i][0]+c[i][2] >= w-r: u.union(i, n+1)
        for j in range(i+1, n):
            if d[i][j] <= r: u.union(i, j)
    return u.find(n) != u.find(n+1)
d = [[0]*1000 for _ in range(1000)]
for _ in range(int(input())):
    w = int(input()); n = int(input()); c = [array('i', [*map(int, input().split())]) for _ in range(n)]; lo, hi = 0, w
    for i in range(n):
        x1, y1, r1 = c[i]
        for j in range(i+1, n): x2, y2, r2 = c[j]; d[i][j] = d[j][i] = ((x1-x2)**2 + (y1-y2)**2)**0.5 - r1 - r2
    while abs(lo-hi) > 1e-6:
        mi = (lo+hi)/2
        if ok(mi, n): lo = mi
        else: hi = mi
    print(mi/2)