class FenwickTree:
    def __init__(self, n):
        self.ft = [0]*(n+1); self.n = n
    def add(self, idx, e):
        idx += 1
        while idx <= self.n: self.ft[idx] += e; idx += idx&(-idx)
    def get(self, idx):
        s, idx = 0, min(idx, self.n)
        while idx > 0: s += self.ft[idx]; idx -= idx&(-idx)
        return s

import sys; input = sys.stdin.readline
n, q = map(int, input().split()); O = 0; F = FenwickTree(n)
for _ in range(q):
    c, *x = map(int, input().split())
    if c == 1: i = x[0]-1; v = F.get(i+1)-F.get(i); F.add(i, 1-2*v)
    elif c == 2: O = 1-O
    elif c == 3: v = F.get(n); print([v, n-v][O])
    elif c == 4: l, r = x; v = F.get(r)-F.get(l-1); print([v, r-l+1-v][O])