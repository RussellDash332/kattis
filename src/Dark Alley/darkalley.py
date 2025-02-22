from array import *
MOD = 10**9+7
class FenwickTree:
    def __init__(self, N):
        self.ft = array('i', [0]*(N+1)); self.n = N
    def add(self, idx, e):
        idx += 1
        while idx <= self.n: self.ft[idx] += e; self.ft[idx] %= MOD; idx += idx&(-idx)
    def get(self, idx):
        s = 0
        while idx > 0: s += self.ft[idx]; s %= MOD; idx -= idx&(-idx)
        return s
import sys; input = sys.stdin.readline; from fractions import *
n, q, p = map(Fraction, input().split()); n = int(n); q = int(q); p = 1-p
p = p.numerator*pow(p.denominator, -1, MOD)%MOD; z = pow(p, -1, MOD)
P = array('i', [1]); I = array('i', [1])
for _ in range(n): P.append(P[-1]*p%MOD); I.append(I[-1]*z%MOD)
L = FenwickTree(n+1); R = FenwickTree(n+1)
for _ in range(q):
    c, *k = input().split()
    if c != '?':
        b, x = map(int, k); x -= 1; v = b*I[x]%MOD; w = b*P[x]%MOD
        if c == '-': v = -v; w = -w
        R.add(x, v); R.add(n, -v); L.add(0, w); L.add(x, -w)
    else: x = int(k[0])-1; print((L.get(x+1)*I[x]+R.get(x+1)*P[x])%MOD)