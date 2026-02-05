import sys, os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
N, K = map(int, input().split()); Z = [-1]*N; G = [{} for _ in range(N)]
for _ in range(K):
    a, b, w = map(int, input().split()); a -= 1; b -= 1
    if a == b and w%2: print(-1); exit()
    elif b not in G[a]: G[a][b] = G[b][a] = w
    elif G[a][b] != w: print(-1); exit()
for i in range(N):
    if Z[i] != -1: continue
    # (0, c) -> x+c; (1, c) -> -x+c
    Q = [i]; Z[i] = (0, 0); L = 0; R = 10**9
    for u in Q:
        m, c = Z[u]
        if m: R = min(R, c)
        else: L = max(L, -c)
        for v in G[u]:
            x = G[u][v]
            if Z[v] != -1:
                if Z[v][0]^m:
                    if c+Z[v][1] != G[u][v]: print(-1); exit()
                else:
                    d = G[u][v]-c-Z[v][1]
                    if d%2: print(-1); exit()
                    else: d //= 2*(1-2*m); L = max(L, d); R = min(R, d)
            else: Z[v] = (m^1, x-c); Q.append(v)
    if L > R: print(-1); exit()
    for i in Q: m, c = Z[i]; Z[i] = L*(1-2*m)+c
sys.stdout.write(' '.join(map(str, Z)))