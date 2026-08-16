import sys; input = sys.stdin.readline
N, K = map(int, input().split()); C = []; G = {}; D = {}
for t in range(K):
    k, *v = input().strip().split(); C += [{*v}]
    for u in v:
        if u not in G: G[u] = []; D[u] = 10**9
        G[u] += [t]
Q = ['ERDOS']; D['ERDOS'] = 0; V = [0]*K
for u in Q:
    for t in G[u]:
        if V[t]: continue
        V[t] = 1; C[t].discard(u)
        for v in C[t]:
            if D[v] == 10**9: D[v] = D[u]+1; Q += [v]
for i in sorted(D.items()): print(*i)