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
            if self.rank[x] > self.rank[y]:
                self.p[y] = x
            else:
                self.p[x] = y
                if self.rank[x] == self.rank[y]:
                    self.rank[y] += 1

import sys

n = int(input())
ufds = UFDS(2*n)
check = []
t = {}
w = {}
for line in sys.stdin:
    w1, e, w2 = line.strip().split()
    if w1 not in w:
        w[w1] = len(w)
    if w2 not in w:
        w[w2] = len(w)

    for word in [w1, w2]:
        idx = w[word]
        ptr = t
        for c in word[:-4:-1]:
            c = ord(c)
            if c not in ptr:
                ptr[c] = {}
            ptr = ptr[c]
            if 0 in ptr:
                ufds.union(ptr[0], idx)
        if 0 not in ptr:
            ptr[0] = idx
        for k in ptr:
            if k != 0:
                ufds.union(idx, ptr[k][0])
                for l in ptr[k]:
                    if l != 0:
                        ufds.union(idx, ptr[k][l][0])

    if e == 'is':
        ufds.union(w[w1], w[w2])
    else:
        check.append(w[w1]*2*n + w[w2])

for h in check:
    if ufds.is_same_set(h // (2*n), h % (2*n)):
        print('wait what?')
        sys.exit(0)
print('yes')