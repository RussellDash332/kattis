import os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline; from heapq import *; from array import *
class F:
    def __init__(s, a, b, c, d):
        if b < 0: a, b = -a, -b
        s.a, s.b, s.c, s.d = a, b, c, d
    def __lt__(s, o): return s.a*o.b < s.b*o.a
N = int(input()); P = array('i'); V = array('i'); L = array('i', [-1]+[*range(N-1)]); R = array('i', [*range(1, N)]+[-1]); Q = []; Z = array('b', [1]*N)
for _ in range(N): p, v = map(int, input().split()); P.append(p); V.append(v)
for i in range(N-1): V[i]-V[i+1] and (t:=F(P[i+1]-P[i], V[i]-V[i+1], i, i+1)).a > 0 and Q.append(t)
heapify(Q)
while Q:
    _ = heappop(Q); i, j = _.c, _.d
    if Z[i] == 0 or Z[j] == 0: continue
    Z[i] = Z[j] = 0; p = L[i]; q = R[j]
    if p == q == -1: continue
    if p != -1: R[p] = q
    if q != -1: L[q] = p
    if p != -1 != q: V[p]-V[q] and (t:=F(P[q]-P[p], V[p]-V[q], p, q)).a > 0 and heappush(Q, t)
print(sum(Z), *(i+1 for i in range(N) if Z[i]))