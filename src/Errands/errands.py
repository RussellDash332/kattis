import sys; input = sys.stdin.readline

INF = 1e18
def tsp(G):
    n = len(G); C = [[INF for _ in range(n)] for _ in range(1<<n)]; C[1][0] = 0
    p = [[0 for _ in range(n)] for _ in range(1<<n)]
    for s in range(1<<n):
        for i in range(n):
            for j in range(n):
                if s&(1<<j) == 0: s2 = s+(1<<j); C[s2][j], p[s2][j] = min((C[s][i]+G[i][j], i), (C[s2][j], p[s2][j]))
    tour = []; pos = n-1; k = (1<<n)-1
    while pos: nxt = p[k][pos]; k -= 1<<pos; pos = nxt; tour.append(pos)
    return tour[-2::-1]

locs = {}
for _ in range(int(input())): l, x, y = input().split(); locs[l] = complex(round(float(x)*1e5), round(float(y)*1e5))
for l in sys.stdin:
    m = {'work': 0, **{e:i+1 for i,e in enumerate(l.strip().split())}}; l = [*m]; m['home'] = len(m); l.append('home')
    G = [[INF]*len(m) for _ in range(len(m))]
    for a in m:
        for b in m:
            if a < b: G[m[a]][m[b]] = G[m[b]][m[a]] = abs(locs[a]-locs[b])
    print(' '.join(l[i] for i in tsp(G)))