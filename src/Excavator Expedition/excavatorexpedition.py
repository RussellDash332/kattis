import sys; input = sys.stdin.readline; from array import *
V, E = map(int, input().split()); G = [[] for _ in range(V)]; H = [[] for _ in range(V)]; T = []; I = array('i', [0]*V); P = input().strip(); A = array('b', [0]*V)
for _ in range(E): a, b = map(int, input().split()); G[a].append(b); H[b].append(a)
s = [0]
while s:
    u = s.pop()
    if A[u] < 1: A[u] |= 1; s.extend(G[u])
s = [V-1]
while s:
    u = s.pop()
    if A[u] < 2: A[u] |= 2; s.extend(H[u])
H = [[] for _ in range(V)]
for i in range(V):
    for j in G[i]:
        if A[j] == 3: H[i].append(j); I[j] += 1
Q = [i for i in range(V) if I[i] == 0]
for u in Q:
    T.append(u)
    for v in H[u]:
        I[v] -= 1
        if I[v] == 0: Q.append(v)
dp = array('i', [-10**9]*V); dp[-1] = 0
for u in T[::-1]:
    w = -10**9
    for v in H[u]:
        if w < dp[v]: w = dp[v]
    if H[u]: dp[u] = 2*(P[u]=='X')-1+w
print(dp[0]+1)