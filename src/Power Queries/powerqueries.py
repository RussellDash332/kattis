import sys, os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
class FenwickTree:
    def __init__(self, N):
        self.ft1 = [0]*(N+1); self.ft2 = [0]*(N+1); self.n = N
    def add(self, l, r, v):
        if v == 0: return
        p1 = l+1; p2 = r+1
        while p1 <= self.n: self.ft1[p1] += v; self.ft2[p1] += v*l; p1 += p1&(-p1)
        while p2 <= self.n: self.ft1[p2] -= v; self.ft2[p2] -= v*r; p2 += p2&(-p2)
    def get(self, r):
        s1 = s2 = s4 = 0; p1 = r; p2 = 0
        while p1 > 0: s1 += self.ft1[p1]; s2 += self.ft2[p1]; p1 -= p1&(-p1)
        while p2 > 0: s4 += self.ft2[p2]; p2 -= p2&(-p2)
        return s1*r-s2-s4
N, Q = map(int, input().split()); F = FenwickTree(N); R = N; S = [0]; G = F.add; T = [[] for _ in range(N)]; P = [*map(int, input().split())]; V = [[] for _ in range(N)]; Z = [0]*N
for i in range(N-1): T[P[i]-1].append(2*i+2)
for _ in range(Q): v, p = map(int, input().split()); V[v-1].append(p)
while S:
    ub = S.pop(); u = ub>>1
    if ub&1:
        R += 1
        for p in V[u]: G(max(R-p, 0), R, -1); G(0, 1, min(R-p, 0))
    else:
        S.append(ub^1); S.extend(T[u])
        for p in V[u]: G(max(R-p, 0), R, 1); G(0, 1, max(p-R, 0))
        Z[u] = F.get(R); R -= 1
sys.stdout.write(' '.join(map(str, Z)))