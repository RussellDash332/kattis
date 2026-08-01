import sys; input = sys.stdin.readline
N, T = map(int, input().split())
B = [[] for _ in range(6)]
for _ in range(N): l, g = map(int, input().split()); B[l].append(g)
for b in B: b.sort()
for i in range(6): B[i] = [p:=0]+[p:=p+v for v in B[i]]
from collections import *
INF = 10**18; D = [0]; G = 0
for v in range(1, 6): # 1D1D
    C = B[v]; K = len(C)-1
    if K<1: continue
    H = G+K*v; E = [INF]*-~H
    for r in range(v):
        U = max((G-r)//v, -1); V = max((H-r)//v, -1)
        if V < 0: continue
        def f(m, k):
            return D[k*v+r]+C[m-k] if 0<=m-k<=K else INF
        def turn(j, k):
            l, r = k, V+1
            while l < r:
                if f(m:=(l+r)//2,k) <= f(m,j): r = m
                else: l = m+1
            return l
        Q = deque()
        for i in range(V+1):
            if i <= U and D[i*v+r] < INF:
                while len(Q) > 1 and turn(Q[-2], Q[-1]) >= turn(Q[-1], i): Q.pop()
                Q.append(i)
            while len(Q) > 1 and turn(Q[0], Q[1]) <= i: Q.popleft()
            if Q: E[i*v+r] = f(i, Q[0])
    D = E; G = H
print(max(i for i in range(len(D)) if D[i] <= T))