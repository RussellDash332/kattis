class XORFT:
    def __init__(self, arr):
        self.ft = [0]*(len(arr)+1); self.n = len(arr)
        for i, e in enumerate(arr): self.update(i, e)
    def update(self, idx, e):
        idx += 1
        while idx <= self.n: self.ft[idx] ^= e; idx += idx & (-idx)
    def get(self, idx):
        s, idx = 0, min(idx, self.n)
        while idx > 0: s, idx = s^self.ft[idx], idx-(idx&(-idx))
        return s

import sys; input = sys.stdin.readline
k = int(input()); a = [*map(int, input().split())]; xor = 0; k += 1
for i in a: xor ^= i
a.append(xor); f = XORFT(a)
for _ in range(int(input())): l, r = map(int, input().split()); l -= 1; print(f.get(r%k)^f.get(l%k))