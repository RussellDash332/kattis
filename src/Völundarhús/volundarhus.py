import sys; input = sys.stdin.readline
N = int(input()); G = [{} for _ in range(N)]; E = []; Z = [0]*N
for _ in range(N-1):
    u, v, w = map(int, input().split()); u -= 1; v -= 1
    if u > v: u, v = v, u
    G[u][v] = G[v][u] = w
    E.append((u, v))
S = [(0, -1, 0)]; tin = [0]*N; tout = [0]*N; T = 0; P = [-1]*N; B = set(); z = N-1
while S:
    u, p, b = S.pop()
    if b:
        tout[u] = T; T += 1
        for v in G[u]:
            if v != p: Z[u] += Z[v]+G[u][v]
    else:
        tin[u] = T; T += 1
        S.append((u, p, 1))
        for v in G[u]:
            if v != p: S.append((v, u, 0)); P[v] = u
while 1:
    p = P[z]
    if p < 0: break
    B.add((min(z, p), max(z, p))); z = p
for _ in range(int(input())):
    u, v = E[int(input())-1]
    if (u, v) in B: print('Kemst ekki'); continue
    if P[u] == v: u, v = v, u
    print(Z[0]-Z[-1]-(Z[v]+G[u][v])*(1-(tin[-1] < tin[v] <= tout[v] < tout[-1])))