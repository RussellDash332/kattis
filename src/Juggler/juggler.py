import sys; input = sys.stdin.readline
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
N = int(input())
F = FenwickTree(N)
for i in range(N): F.add(i, 1)
R = {e:i for i,e in enumerate(int(input())-1 for _ in range(N))}
p = Z = 0
for i in range(N):
    Z += min(z:=(F.get(k:=R[i])-F.get(p))%N, N-z)+1
    p = k; N -= 1; F.add(k, -1)
print(Z)