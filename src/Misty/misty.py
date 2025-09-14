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
n, m = map(int, input().split())
el = []; mst = []; u = UFDS(n)
for i in range(m): a, b, d = map(int, input().split()); el += [(d, i+1, a-1, b-1)]
for w, i, a, b in sorted(el):
    if u.find(a) != u.find(b): u.union(a, b); mst += [i]
print(len(mst), *mst, sep='\n')