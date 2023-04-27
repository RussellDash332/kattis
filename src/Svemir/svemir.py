class UFDS:
    def __init__(self, N):
        self.p = [i for i in range(N)]
        self.rank = [0 for _ in range(N)]
    def find_set(self, i):
        if self.p[i] == i: return i
        self.p[i] = self.find_set(self.p[i])
        return self.p[i]
    def is_same_set(self, i, j):
        return self.find_set(i) == self.find_set(j)
    def union(self, i, j):
        if not self.is_same_set(i, j):
            x, y = self.find_set(i), self.find_set(j)
            if self.rank[x] > self.rank[y]: self.p[y] = x
            else:
                self.p[x] = y
                self.rank[y] += self.rank[x] == self.rank[y]

p = []
for _ in range(int(input())): p.append([*map(int, input().split())])
p, v, u = list(enumerate(p)), len(p), UFDS(len(p))
px, py, pz = [sorted(p, key=lambda x: x[1][i]) for i in range(3)]
el = set()
for pp in [px, py, pz]:
    for i in range(1, v): el.add((pp[i-1][0], pp[i][0], min(abs(a-b) for a,b in zip(pp[i-1][1], pp[i][1]))))
m = 0
for i, j, k in sorted(el, key=lambda x: x[2]):
    if u.is_same_set(i, j): continue
    u.union(i, j)
    m += k
print(m)