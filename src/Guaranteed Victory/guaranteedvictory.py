import sys; input = sys.stdin.readline
N, M = map(int, input().split()); R = {}; E = []
for _ in range(N): s = input().strip(); R[s] = len(R)
for _ in range(M):
    k = int(input()); p = input().strip().split()
    for q in p:
        if q not in R: R[q] = len(R)
    for i in range(k-1): E.append((R[p[i+1]], R[p[0]]))
G = [[] for _ in range(len(R))]; I = [0]*len(R); T = []
for a, b in E: G[a].append(b); I[b] += 1
Q = [i for i in range(len(R)) if I[i] == 0]
for u in Q:
    T.append(u)
    for v in G[u]:
        I[v] -= 1
        if I[v] == 0: Q.append(v)
if len(T) == len(R): print('GUARANTEED VICTORY')
else: print(len(R)-len(T))