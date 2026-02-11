class FenwickTree:
    def __init__(self, arr):
        self.ft = [0]*(len(arr)+1)
        self.n = len(arr)
        for i in range(self.n): self.add(i, i+1, arr[i])
    def _add(self, idx, e):
        idx += 1
        while idx <= self.n: self.ft[idx] += e; idx += idx&(-idx)
    def add(self, l, r, e): # a[l:r] += e
        self._add(l, e); self._add(min(r, self.n), -e)
    def get(self, idx): # a[idx]
        s, idx = 0, min(idx+1, self.n)
        while idx > 0: s += self.ft[idx]; idx -= idx&(-idx)
        return s

import sys; input = sys.stdin.readline
N = int(input())
A = FenwickTree(sorted(map(int, input().split()), reverse=True))
M = int(input())
for b in map(int, input().split()):
    lo, hi = 0, N
    while lo < hi:
        if A.get(mi:=(lo+hi)//2) < b: hi = mi
        else: lo = mi+1
    print(lo); A.add(0, lo, -1)