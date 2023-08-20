import sys; input = sys.stdin.readline
class UFDS:
    def __init__(self, N):
        self.p = [*range(N)]
        self.rank = [0]*N
        self.n = N
    def find_set(self, i):
        if self.p[i] == i: return i
        self.p[i] = self.find_set(self.p[i])
        return self.p[i]
    def union(self, i, j):
        if (x:=self.find_set(i)) != (y:=self.find_set(j)):
            self.n -= 1
            if self.rank[x] > self.rank[y]: self.p[y] = x
            else: self.p[x] = y; self.rank[y] += self.rank[x] == self.rank[y]
n, m, p = map(int, input().split())
if n == 1: print(0), exit(0)
safe = [1]*n; el = []; lo = [float('inf')]*n
for c in [*map(int, input().split())]: safe[c-1] = 0
if n == 2: print('impossible' if m == 0 else [*map(int, input().split())][2]), exit(0)
for _ in range(m):
    a, b, w = map(int, input().split()); a -= 1; b -= 1
    if safe[a] and safe[b]: el.append((w, a, b))
    elif not safe[a] and not safe[b]: continue
    elif safe[a]: lo[b] = min(lo[b], w)
    else: lo[a] = min(lo[a], w)
el.sort(); u = UFDS(n); tc = 0
for w, a, b in el:
    if u.find_set(a) == u.find_set(b): continue
    u.union(a, b); tc += w
if u.n != n-sum(safe)+1: print('impossible'), exit(0)
for i in range(n):
    if not safe[i]: tc += lo[i]
print(tc if tc < 1e18 else 'impossible')