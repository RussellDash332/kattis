import os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline; from array import *
N = int(input()); M = [[int(x>32) for x in input()] for _ in range(N)]; Z = array('I', [0]*(N+1)*(N+1)); E = (-1, N, N)
for i in range(N):
    for j in range(N): u = i*-~N+j; Z[u+N+2] = Z[u+1]+Z[u-~N]-Z[u]+M[i][j]
for i in range(N):
    for j in range(N):
        if M[i][j]<1: continue
        lo, hi = -E[0], N-max(i,j)+1; u = i*-~N+j
        while lo < hi:
            mi = (lo+hi)//2
            if Z[u+mi*(N+2)]-Z[u+mi*-~N]-Z[u+mi]+Z[u] < mi*mi: hi = mi
            else: lo = mi+1
        E = min(E, (1-lo, i, j))
a, b, c = E; print(b, c, -a)