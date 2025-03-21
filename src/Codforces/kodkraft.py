import sys; input = sys.stdin.readline; from array import *
N, K = map(int, input().split())
A = array('i', map(int, input().split()))
T = [array('i') for _ in range(K)]
for i in range(N): T[A[i]-1].append(i)
G = [-1]*N
for i in range(K-1):
    p = 0; q = len(T[i+1])
    for t in T[i]:
        while p < 2*q and T[i+1][p%q]+N*(p>=q) < t: p += 1
        G[t] = T[i+1][p%q]*N+(T[i+1][p%q]-t)%N
D = [10**18]*N; Q = array('i', T[0])
for i in T[0]: D[i] = 1
for u in Q:
    if G[u] != -1: v = G[u]//N; D[v] = min(D[v], D[u]+G[u]%N); Q.append(v)
print(min(D[i] for i in T[-1]))