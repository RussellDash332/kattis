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
N, M = map(int, input().split()); T = 0; K = FenwickTree(N); A = FenwickTree(N)
for i in range(N): k, *s = map(int, input().split()); K.add(i, k); A.add(i, sum(s))
for _ in range(M):
    c, *v = map(int, input().split())
    if c < 2: a, b = v; a -= 1; K.add(a, 1); A.add(a, b-T)
    elif c < 3: T += v[0]
    else: a, b = v; a -= 1; print((A.get(b)-A.get(a))/(K.get(b)-K.get(a))+T)