import sys, os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline; from math import *; from functools import *; from array import *

def c1(q, r): q = P[q]; r = P[r]; return (q//M-b)*(r%M)-(r//M-b)*(q%M)
def c2(q, r): q = P[q]; r = P[r]; return r//M*(q%M)-q//M*(r%M)

class FenwickTree:
    def __init__(self, n):
        self.ft = [0]*(n+1); self.n = n
    def add(self, idx, e):
        idx += 1
        while idx <= self.n: self.ft[idx] += e; idx += idx&(-idx)
    def get(self, idx):
        s = 0
        while idx > 0: s += self.ft[idx]; idx -= idx&(-idx)
        return s

n, b = map(int, input().split()); P = []; V = array('i'); A = [-1]*n; F = FenwickTree(n); M = 10**9+7
for _ in range(n): x, y, v = map(int, input().split()); P.append(x*M+y); V.append(v)
S = {e:i for i,e in enumerate(sorted(range(n), key=cmp_to_key(c1)))}
for i in sorted(range(n), key=cmp_to_key(c2)): A[i] = F.get(S[i]); F.add(S[i], V[i])
for i in A: sys.stdout.write(str(i)+' ')