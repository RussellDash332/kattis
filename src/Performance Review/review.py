class FenwickTree:
    def __init__(self, N):
        self.ft = [0]*(N+1); self.n = N
    def add(self, idx, e):
        idx += 1
        while idx <= self.n: self.ft[idx] += e; idx += idx&(-idx)
    def get(self, idx):
        s = 0
        while idx > 0: s += self.ft[idx]; idx -= idx&(-idx)
        return s
import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**5+10)
N = int(input()); G = [[] for _ in range(N)]; R = []; T = []; C = -1; F = FenwickTree(10**5); Z = [-1]*N
for i in range(N): m, r, t = map(int, input().split()); m == -1 or G[m-1].append(i); R.append(r); T.append(t); C = [C, i][m < 0]
def trav(u):
    p = F.get(R[u])
    for v in G[u]: trav(v)
    Z[u] = F.get(R[u])-p; F.add(R[u], T[u])
trav(C); print(*Z)