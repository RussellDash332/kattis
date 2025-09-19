from heapq import *; INF = 10**18
for _ in range(int(input())):
    F, E = map(int, input().split()); V = [E, (F-1)*(E+2)+E+1]
    for i in range(E):
        R, M = map(int, input().split())
        for j in range(R, F, M): V.append(j*(E+2)+i)
    V.sort(); G = [{} for _ in range(E+2)]
    for i in range(len(V)-1):
        a, b = divmod(V[i], E+2); c, d = divmod(V[i+1], E+2)
        if d not in G[b]: G[b][d] = G[d][b] = INF
        G[b][d] = G[d][b] = min(G[b][d], c-a)
    D = [INF]*(E+2); D[E] = 0; pq = [E]; Z = (0, -INF)
    while pq:
        dd, vv = divmod(heappop(pq), E+2)
        if dd != D[vv]: continue
        for nn in G[vv]:
            if D[nn] > (new:=dd+G[vv][nn]): D[nn] = new; heappush(pq, new*(E+2)+nn)
    for i in range(len(V)-1): a, b = divmod(V[i], E+2); c, d = divmod(V[i+1], E+2); m = (a+c+D[d]-D[b])//2; k = m-a+D[b]; Z = max(Z, (k, -m))
    print(Z[0], -Z[1])