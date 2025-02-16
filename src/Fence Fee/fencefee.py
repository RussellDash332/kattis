import sys; input = sys.stdin.readline; from math import *
N = int(input()); G = {}; R = {}; S = set(); Z = 0
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    if (x1, y1) not in G: G[(x1, y1)] = []
    if (x2, y2) not in G: G[(x2, y2)] = []
    G[(x1, y1)].append((x2, y2)); G[(x2, y2)].append((x1, y1))
for p in G: G[p].sort(key=lambda x: atan2(x[1]-p[1], x[0]-p[0])); R[p] = {e:i for i,e in enumerate(G[p])}
for x1, y1 in G:
    for x2, y2 in G[(x1, y1)]:
        if (x1, y1, x2, y2) not in S:
            P = [(x1, y1), (x2, y2)]
            while P[0] != P[-1]: g = G[P[-1]]; p = G[P[-1]][(R[P[-1]][P[-2]]-1)%len(g)]; P.append(p)
            A = 0; N = len(P)
            for i in range(N-1): A += P[i][0]*P[i+1][1]-P[i][1]*P[i+1][0]; S.add((*P[i], *P[i+1]))
            Z += max(A, 0)**2
print(Z/4)