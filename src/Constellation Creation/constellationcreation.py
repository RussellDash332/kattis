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
r, c, n = map(int, input().split())
m = [[*input().strip()] for _ in range(r)]
s = []
for i in range(r):
    for j in range(c):
        if m[i][j] == '*': s.append((i, j))
        else: m[i][j] = 0
h = {e:i for i,e in enumerate(s)}
u = UFDS(len(s))
el = set()
for i in range(r):
    prev = None
    for j in range(c):
        if (i, j) in h:
            if prev != None: el.add(tuple(sorted([h[(i, j)], h[prev]])))
            prev = (i, j)
for j in range(c):
    prev = None
    for i in range(r):
        if (i, j) in h:
            if prev != None: el.add(tuple(sorted([h[(i, j)], h[prev]])))
            prev = (i, j)
for a, b in el:
    if u.n == n: break
    u.union(a, b)
    if s[a][0] == s[b][0]:
        for i in range(s[a][1]+1, s[b][1]): m[s[a][0]][i] += 1
    else:
        for i in range(s[a][0]+1, s[b][0]): m[i][s[a][1]] += 2
for i in range(r):
    for j in range(c):
        if m[i][j] != '*': m[i][j] = ' -|+'[m[i][j]]
for x in m: print(''.join(x))