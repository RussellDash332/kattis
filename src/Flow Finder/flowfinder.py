import sys; input = sys.stdin.readline; sys.setrecursionlimit(300_000)
N = int(input()); G = [[] for _ in range(N)]
P = [*map(int, input().split())]
F = [*map(int, input().split())]
L = [*F]
for i in range(N-1): G[P[i]-1].append(i+1)

def derive(v):
    for u in G[v]: derive(u)
    s = 0; k = len(G[v])
    for u in G[v]:
        if F[u]: s += F[u]; k -= 1
    if k == 0:
        if F[v]:
            if G[v] and F[v] != s: print('impossible'), exit(0)
        else: F[v] = L[v] = s
    if not F[v]:
        L[v] = max(1, sum(max(1, L[u]) for u in G[v]))

def distribute(v):
    s = 0; k = []
    for u in G[v]:
        if F[u]: s += F[u]
        else: k.append(u)
    rem = F[v]-s
    if len(k) == 1:
        F[k[0]] = rem
    elif rem == sum(L[u] for u in k):
        for u in k: F[u] = L[u]
    for u in G[v]: distribute(u)

derive(0)
distribute(0)
if min(F) < 1: print('impossible'), exit(0)
print(*F)