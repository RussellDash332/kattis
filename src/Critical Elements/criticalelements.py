import sys, os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
from array import *
def lis(A):
    B = []; P = []
    for e in A:
        lo, hi = 0, len(B)
        while lo < hi:
            if e-1 < B[mi:=(lo+hi)//2][-1][0]: hi = mi
            else: lo = mi+1
        p = lo
        if p == len(B): P.append([0]); B.append([])
        lo, hi = 0, len(B[p-1])
        while lo < hi:
            if e > B[p-1][mi:=(lo+hi)//2][0]: hi = mi
            else: lo = mi+1
        u = P[p-1][-1]-P[p-1][lo] if p else 1
        if B[p] and B[p][-1][0] == e: B[p][-1] = (e, u); P[p][-1] = P[p][-2]+u
        else: B[p].append((e, u)); P[p].append(P[p][-1]+u)
    return B
N = int(input())
A = array('i', map(int, input().split()))
L = lis(A)
R = lis(-i for i in A[::-1])
Z = array('i')
C = sum(b[-1] for b in L[-1]) # C can be very big
for i in range(len(L)):
    l = dict(L[i]); r = dict(R[~i])
    for u in l:
        if -u in r and l[u]*r[-u] == C: Z.append(u)
for i in sorted(Z) or [-1]: sys.stdout.write(str(i)); sys.stdout.write(' ')