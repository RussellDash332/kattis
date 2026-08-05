# purposely avoiding kruskal
N, M = map(int, input().split())
INF = 10**9; G = [set() for _ in range(N)]; Z = 0
for _ in range(M): a, b, w = map(int, input().split()); G[a].add((b, w)); G[b].add((a, w))
mst = []; A = [(INF, INF)]*N; B = [0]*N; A[0] = (0, 0)
while len(mst) != N:
    best = (0, A[0])
    for i in range(1, N):
        if A[i][0] < best[1][0]: best = (i, A[i])
    mst.append(best); Z += best[1][0]; z = best[0]
    A[z], B[z] = (INF, 0), 1
    for v, w in G[z]:
        if not B[v] and A[v][0] > w: A[v] = (w, z)
for b, (w, a) in mst:
    if a == b: continue
    mst2 = []; A = [INF]*N; B = [0]*N; A[0] = 0; C = 0
    G[a].discard((b, w)); G[b].discard((a, w))
    for b2, (w2, a2) in mst:
        if (b, w, a) == (b2, w2, a2): continue
        C += w2; G[a2].add((b2, 0)); G[b2].add((a2, 0))
    while len(mst2) != N:
        best = (0, A[0])
        for i in range(1, N):
            if A[i] < best[1]: best = (i, A[i])
        mst2.append(best); C += best[1]; z = best[0]
        A[z], B[z] = INF, 1
        for v, w2 in G[z]:
            if not B[v] and A[v] > w2: A[v] = w2
    if C < INF: Z = max(Z, C)
    G[a].add((b, w)); G[b].add((a, w))
    for b2, (w2, a2) in mst:
        if (b, w, a) == (b2, w2, a2): continue
        G[a2].discard((b2, 0)); G[b2].discard((a2, 0))
print(Z)