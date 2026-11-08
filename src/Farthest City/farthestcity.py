import sys; input = sys.stdin.readline
from collections import *
N = int(input()); G = [{} for _ in range(N)]; D = [0]*N
for _ in range(N):
    a, b, w = map(int, input().split())
    G[a-1][b-1] = G[b-1][a-1] = w; D[a-1] += 1; D[b-1] += 1
Q = [i for i in range(N) if len(G[i])<2]; T = [{} for _ in range(N)]; M = [0]*N
for u in Q:
    d = G[p:=min(G[u])].pop(u); T[p][u] = T[u][p] = d; M[p] = max(M[p], M[u]+d)
    if len(G[p]) == 1: Q += [p]
c = next(i for i in range(N) if len(G[i])>1); C = []; u = c; p = -1
while 1:
    C += [u]; v = next(v for v in G[u] if v!=p); p, u = u, v
    if u == c: break
K = len(C); W = [G[C[i]][C[(i+1)%K]] for i in range(K)]; S = [0]
for i in range(2*K): S += [S[-1]+W[i%K]]
s = S[K]; A = deque(); B = deque(); Z = [0]*K; p = a = b = 0
for i in range(K):
    h = p = max(p, i)
    while p+1<i+K and 2*(S[p+1]-S[i])<=s: p += 1; h += 1
    while a < h:
        a += 1; x = M[C[a%K]]+S[a]
        while A and M[C[A[-1]%K]]+S[A[-1]]<=x: A.pop()
        A.append(a)
    while b < i+K-1:
        b += 1; x = M[C[b%K]]-S[b]
        while B and M[C[B[-1]%K]]-S[B[-1]]<=x: B.pop()
        B.append(b)
    while A and A[0]<i+1: A.popleft()
    while B and B[0]<h+1: B.popleft()
    if A: Z[i] = M[C[A[0]%K]]+S[A[0]]-S[i]
    if B: Z[i] = max(Z[i], M[C[B[0]%K]]-S[B[0]]+S[i]+s)
P = [-1]*N; Q = [*C]; U = [0]*N
for u in C: P[u] = u
for u in Q:
    for v, _ in T[u].items():
        if v != P[u]: P[v] = u; Q += [v]
for i in range(K): U[C[i]] = Z[i]
for u in Q:
    a = b = 0; t = -1
    for v, w in T[u].items():
        if P[v] == u:
            x = M[v]+w
            if x > a: b, a, t = a, x, v
            elif x > b: b = x
    for v, w in T[u].items():
        if P[v] == u: U[v] = w+max(0, U[u], (a, b)[v==t])
print(*[max(M[i], U[i]) for i in range(N)])