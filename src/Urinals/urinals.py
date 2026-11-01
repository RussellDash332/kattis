import sys; input = sys.stdin.readline; from heapq import *; from collections import *
class FenwickTree:
    def __init__(self, n):
        self.n = n; self.ft = [0]*(n+1)
    def add(self, idx, v):
        idx += 1
        while idx <= self.n: self.ft[idx] += v; idx += idx&(-idx)
    def get(self, idx):
        s = 0
        while idx: s += self.ft[idx]; idx -= idx&(-idx)
        return s
    def kth(self, k):
        x = idx = 0
        for i in range(10, -1, -1):
            if (t:=idx|(1<<i)) <= self.n and self.ft[t] < k: k -= self.ft[idx:=t]
        return idx
n, m = map(int, input().split())
V = set(); Q = []; W = deque(); F = FenwickTree(m); H = []
def vadd(l, r):
    V.add((l, r)); p = (l+r)//2
    if l<p<r: heappush(H, (l-r, p, l, r))
def leave(p):
    F.add(p, -1); k = F.get(p); V.remove(((l:=F.kth(k) if k else -1), p)); V.remove((p, (r:=F.kth(k+1) if k < F.get(m) else m))); vadd(l, r)
def enter(a, d, t):
    while 1:
        _, p, l, r = heappop(H)
        if (l, r) in V: break
    V.remove((l, r)); F.add(p, 1); vadd(l, p); vadd(p, r); s = max(a, t); heappush(Q, (s+d, p)); print(p+1, s)
vadd(-1, m)
for i in range(n):
    a, d = map(int, input().split())
    while Q and Q[0][0] <= a:
        t = Q[0][0]
        while Q and Q[0][0] == t: _, p = heappop(Q); leave(p)
        while W and len(V) < m+1: enter(*W.popleft(), t)
    W.append((a, d))
    while W and len(V) < m+1: enter(*W.popleft(), a)
while W:
    t = Q[0][0] if Q else -1
    while Q and Q[0][0] == t: _, p = heappop(Q); leave(p)
    while W and len(V) < m+1: enter(*W.popleft(), t)