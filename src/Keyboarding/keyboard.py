import sys; input = sys.stdin.readline; from array import *; from collections import *
R, C = map(int, input().split()); M = array('b')
for _ in range(R): M.extend(map(ord, input().strip()))
S = array('b', map(ord, input().strip()+'*')); N = len(S); D = array('i', [-1]*N*R*C); D[0] = 0; Q = deque([0]); K = ((1, 0), (0, 1), (-1, 0), (0, -1)); G = [set() for _ in range(R*C)]
for r in range(R):
    for c in range(C):
        for dr, dc in K:
            rr, cc = r, c
            while R>rr>-1<cc<C and M[rr*C+cc] == M[r*C+c]: rr += dr; cc += dc
            if R>rr>-1<cc<C: G[r*C+c].add((rr*C+cc)*N)
        G[r*C+c] = tuple(G[r*C+c])
while Q:
    u = Q.popleft(); t = u%N; rc = u//N
    if M[rc] == S[t]:
        if t == N-1: print(D[u]+1); break
        if D[u+1] == -1: D[u+1] = D[u]+1; Q.append(u+1); continue
    for nxt in G[rc]:
        if D[nxt+t] == -1: D[nxt+t] = D[u]+1; Q.append(nxt+t)