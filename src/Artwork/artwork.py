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
n, m, q = map(int, input().split()); u = UFDS(n*m); Q = []; R = []; K = ((-1, 0), (1, 0), (0, 1), (0, -1)); M = [0]*n*m
for _ in range(q):
    x1, y1, x2, y2 = (i-1 for i in map(int, input().split())); Q.append((x1, y1, x2, y2))
    for x in range(x1, x2+1):
        for y in range(y1, y2+1): M[x*m+y] += 1
for i in range(n):
    for j in range(m):
        if M[i*m+j] == 0:
            for di, dj in K:
                if n>i+di>-1<j+dj<m and M[(i+di)*m+j+dj] == 0: u.union(i*m+j, (i+di)*m+j+dj)
S = sum(map(bool, M))
while Q:
    R.append(u.n-S); x1, y1, x2, y2 = Q.pop()
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            M[x*m+y] -= 1
            if M[x*m+y] == 0:
                S -= 1
                for dx, dy in K:
                    if n>x+dx>-1<y+dy<m and M[(x+dx)*m+y+dy] == 0: u.union(x*m+y, (x+dx)*m+y+dy)
print(*R[::-1])