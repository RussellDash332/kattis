import sys; input = sys.stdin.readline
T = {}; P = []; S = 0; R = int(input())
for _ in range(R):
    p = input().strip().split('/'); c = T; P.append(p); S += len(p)
    for i in p:
        if i not in c: c[i] = {}
        c = c[i]
    if '.' not in c: c['.'] = 0
    c['.'] += 1
Q = [T]; G = [[]]; x = 0
for t in Q:
    for i in t:
        if type(t[i]) != int: G[x].append(len(G)); Q.append(t[i]); G.append([])
    x += 1
N = len(G); V = [0]*N; Z = [(S, 1)]
for i in range(N):
    if not G[i]: V[i] = Q[i]['.']
for i in range(N-1, -1, -1):
    if not V[i]: V[i] = sum(V[j] for j in G[i])
while Z:
    x, u = Z.pop(); S = min(S, x)
    for v in G[u]: Z.append((x+R-2*V[u], v))
print(S)