import sys, os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline; from array import *; from heapq import *

def find(i):
    if p[i] == i: return i
    p[i] = find(p[i]); return p[i]
def union(i, j):
    if (x:=find(i)) != (y:=find(j)):
        if rank[x] > rank[y]: p[y] = x
        else: p[x] = y; rank[y] += rank[x] == rank[y]

N, M, U = map(int, input().split()); E = []; Q = []; R = array('b', [0]*U); p = array('i', range(N+1)); rank = array('h', [0]*(N+1)); A = array('i', [0]*M); B = array('i', [0]*M); C = array('i', [0]*U); D = array('i', [0]*U)
for i in range(M): a, b, w = map(int, input().split()); E.append(w*M+i); A[i] = a; B[i] = b
for i in range(U): a, b, w = map(int, input().split()); Q.append(w*U+i); C[i] = a; D[i] = b
heapify(E); V = ('NE\n', 'TAIP\n')
for x in sorted(Q):
    while E and E[0]//M <= x//U: e = heappop(E)%M; union(A[e], B[e])
    R[x%U] = find(C[x%U]) == find(D[x%U])
for v in R: sys.stdout.write(V[v])