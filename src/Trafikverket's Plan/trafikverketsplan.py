n = int(input()); g = [[] for _ in range(n)]; e = [set() for _ in range(n)]
for _ in range(n-1): a, b = map(int, input().split()); a -= 1; b -= 1; g[a] += [b]; g[b] += [a]; e[a].add(b)
Q = [[] for _ in range(n)]; R = []; d = [0]*n; par = [*range(n)]; d[0] = 1; U = [0]*n; D = [0]*n; s = [(0, 0)]
for i in range(int(input())): a, b = map(int, input().split()); a -= 1; b -= 1; R += [[a, b, -1]]; Q[a] += [i]; Q[b] += [i]
def find(i):
    v = [i]
    while par[i] != i: i = par[i]; v += [i]
    for u in v: par[u] = i
    return i
while s:
    ub, p = s.pop(); u = ub//2
    if ub%2:
        for x in Q[u]: a, b, _ = R[x]; R[x][2] = find(b if a == u else a)
        par[u] = p
    else:
        s += [(ub+1, p)]
        for t in g[u]:
            if t == p: continue
            if t in e[u]: U[t] = t; D[t] = D[u]
            else: U[t] = U[u]; D[t] = t
            d[t] = d[u]+1; s += [(2*t, u)]
for a, b, lca in R: print('njeaj'[d[lca]>=max(d[U[a]], d[D[b]])::2])