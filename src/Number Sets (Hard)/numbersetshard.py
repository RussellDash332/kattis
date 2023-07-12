class UFDS:
    def __init__(self, N):
        self.p = [*range(N)]
        self.rank = [0]*N
        self.n = N
    def find_set(self, i):
        if self.p[i] == i: return i
        self.p[i] = self.find_set(self.p[i])
        return self.p[i]
    def is_same_set(self, i, j):
        return self.find_set(i) == self.find_set(j)
    def union(self, i, j):
        if not self.is_same_set(i, j):
            self.n -= 1
            x, y = self.find_set(i), self.find_set(j)
            if self.rank[x] > self.rank[y]: self.p[y] = x
            else:
                self.p[x] = y
                if self.rank[x] == self.rank[y]: self.rank[y] += 1

LIMIT = 10**6
spf = list(range(LIMIT+1))
primes = [2]
p = 3
while p <= LIMIT:
    if spf[p] == p:
        primes.append(p)
        for i in range(p*p, LIMIT+1, 2*p):
            if spf[i] == i: spf[i] = p
    p += 2
primes = primes[::-1]

input()
import sys; t = 1
for l in sys.stdin:
    a, b, p = map(int, l.split())
    u = UFDS(b-a+1)
    for pp in primes:
        if pp < p: break
        lo = (a+pp-1)//pp*pp
        for c in range(lo+pp, b+1, pp): u.union(lo-a, c-a)
    print(f'Case #{t}:', u.n); t += 1