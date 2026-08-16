import sys; input = sys.stdin.readline
class FenwickTree:
    def __init__(self, N):
        self.ft = [0]*(N+1); self.n = N
    def add(self, idx, e):
        idx += 1
        while idx <= self.n: self.ft[idx] += e; idx += idx&(-idx)
    def get(self, idx):
        s, idx = 0, min(idx, self.n)
        while idx > 0: s += self.ft[idx]; idx -= idx&(-idx)
        return s
N, K = map(int, input().split()); P = [N]; Z = 0
for i, e in enumerate(input().strip()): P += [P[-1]+2*(e<'L')-1]
F = FenwickTree(2*N+1)
for i in range(N+1): Z += F.get(P[i]+1); F.add(P[i], 1)
F = FenwickTree(2*N+1)
for i in range(2*K, N+1): Z -= F.get(P[i]+1); F.add(P[i-2*K], 1)
print(Z)