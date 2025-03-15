import sys, os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline; from array import *
N, M = map(int, input().split()); G = [[] for _ in range(N)]; Z = array('b', [0]*M); V = array('i', [0]*N); A = array('i'); B = array('i'); T = 0
for i in range(M): a, b = map(int, input().split()); G[a-1].append(i); G[b-1].append(i); A.append(a-1); B.append(a+b-2)
for i in range(N):
    if V[i]: continue
    S = [(2*i+1, -1)]
    while S:
        ub, p = S.pop(); u = ub>>1
        if ub%2:
            if V[u]: continue
            V[u] = (T:=T+1)
            for t in G[u]:
                if t==p: continue
                if V[v:=B[t]-u] < 1: S.append((2*v+1, t))
                if V[v] < V[u]: S.append((2*t, u))
        elif V[B[u]-p] < V[p]: Z[u] = A[u]!=p
for i in Z: sys.stdout.write(str(i))