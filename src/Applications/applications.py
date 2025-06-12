from array import *
class UFDS:
    def __init__(s, N):
        s.p = array('I', range(N)); s.r = array('B', [0]*N); s.s = array('I', [1]*N); s.n = N
    def find(s, i):
        if s.p[i] == i: return i
        s.p[i] = s.find(s.p[i])
        return s.p[i]
    def union(s, i, j):
        if (x:=s.find(i)) != (y:=s.find(j)):
            s.n -= 1
            if s.r[x] > s.r[y]: s.p[y] = x; s.s[x] += s.s[y]
            else: s.p[x] = y; s.r[y] += s.r[x] == s.r[y]; s.s[y] += s.s[x]

import sys, os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
N, K = map(int, input().split()); U = UFDS(N)
for _ in range(K):
    a, b, c = map(lambda x: U.find(int(x)-1), input().split()); p, q, r = U.s[a], U.s[b], U.s[c]
    if p==q==r or (a==b and p>r) or (a==c and p>q) or (b==c and q>p): U.union(a, b); U.union(b, c)
    sys.stdout.write(str(U.n)+'\n')