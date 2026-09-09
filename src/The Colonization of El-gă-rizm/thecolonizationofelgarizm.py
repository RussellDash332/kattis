import os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline; from array import *
M, N = map(int, input().split())
G = [[] for _ in range(M)]
E = [[] for _ in range(N+1)]
for i in range(M):
    for u in map(int, input().split()): E[u-1] += [i]
E.pop()
for a, b in E: G[a] += [b]; G[b] += [a]
C = array('B', [0]*M)
for i in range(M):
    if C[i]<1:
        C[i] = 1; Q = [i]
        for u in Q:
            for v in G[u]:
                if C[u]==C[v]>0: print('NO'); exit()
                if C[v]<1: C[v] = 3-C[u]; Q += [v]
print('YES')