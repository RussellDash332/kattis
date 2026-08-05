import sys; input = sys.stdin.readline
N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M): a, b = map(int, input().split()); a -= 1; b -= 1; G[a] += [b]; G[b] += [a]
T = 0; V = [0]*N; D = [-1]*N; L = [-1]*N; bridges = []; new = []; S = [(0, -1)]
while S:
    vs, p = S.pop(); v, s = divmod(vs, 2)
    if s&1:
        L[v] = min(L[v], L[p])
        if L[p] > D[v]: bridges.append((v, p))
    else:
        if V[v]: S.pop(); continue
        V[v] = 1; D[v] = L[v] = T; T += 1
        if p != -1: new += [(p, v)]
        for to in G[v]:
            if to == p: continue
            if V[to]: L[v] = min(L[v], D[to]); new += [(v, to)]*(D[v] > D[to])
            else: S.append((vs^1, to)); S.append((2*to, v))
if bridges or min(D)<0: print('Ekki haegt'); exit()
for i, j in new: print(i+1, j+1)