import sys; input = sys.stdin.readline
N, Q = map(int, input().split()); M = 10**9+7
class FenwickTree:
    def __init__(self, n):
        self.ft1 = [0]*(n+1)
        self.ft2 = [0]*(n+1)
        self.n = n
    def add(self, l, r, v):
        r = min(r, self.n); p1 = l+1; p2 = r+1
        while p1 <= self.n: self.ft1[p1] += v; self.ft2[p1] += v*l; p1 += p1&(-p1)
        while p2 <= self.n: self.ft1[p2] -= v; self.ft2[p2] -= v*r; p2 += p2&(-p2)
    def get(self, l, r):
        r = min(r, self.n); s1 = s2 = s3 = s4 = 0; p1 = r; p2 = l
        while p1 > 0: s1 += self.ft1[p1]; s2 += self.ft2[p1]; p1 -= p1&(-p1)
        while p2 > 0: s3 += self.ft1[p2]; s4 += self.ft2[p2]; p2 -= p2&(-p2)
        return s1*r-s2-s3*l+s4
F = FenwickTree(N); Z = 0
for _ in range(Q):
    c, *v = map(int, input().split())
    if c == 2: print(Z)
    else: l, r = v; x = pow(r-l+1, -1, M); Z = (Z+1+2*x*F.get(l-1, r))%M; F.add(l-1, r, x)