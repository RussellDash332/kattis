N, V = map(int, input().split()); T = [[] for _ in range(N)]; g = [[] for _ in range(V)]
for i in range(V): a, b = map(int, input().split()); T[a].append(i); T[b].append(i)
for v in T:
    for i in range(len(v)):
        for j in range(i+1, len(v)): g[v[i]].append(v[j]); g[v[j]].append(v[i])

def aug(s):
    bs = [*range(V)]; nq = [0]*V; qh = qt = 0; q[0] = s; nq[s] = 1
    while qh <= qt:
        au = q[qh]; qh += 1
        for av in g[au]:
            if bs[au] != bs[av] and mtc[au] != av:
                if av == s or (mtc[av] != -1 and par[mtc[av]] != -1):
                    u, v = au, av; np = [0]*V; nb = [0]*V; uu, vv = u, v
                    while 1:
                        np[(uu:=bs[uu])] = 1
                        if uu == s: break
                        uu = par[mtc[uu]]
                    while 1:
                        if np[(vv:=bs[vv])]: lca = vv; break
                        vv = par[mtc[vv]]
                    for uu in (u, v):
                        while bs[uu] != lca:
                            vv = mtc[uu]; nb[bs[uu]] = nb[bs[vv]] = 1; uu = par[vv]
                            if bs[uu] != lca: par[uu] = vv
                    if bs[u] != lca: par[u] = v
                    if bs[v] != lca: par[v] = u
                    for u in range(V):
                        if nb[bs[u]]:
                            bs[u] = lca
                            if not nq[u]: nq[u] = 1; qt += 1; q[qt] = u
                elif par[av] == -1:
                    par[av] = au
                    if mtc[av] == -1: return av
                    elif not nq[mtc[av]]: nq[mtc[av]] = 1; qt += 1; q[qt] = mtc[av]
    return -1

mcm = 0; mtc = [-1]*V; q = [0]*V
for u in range(V):
    if mtc[u] == -1:
        par = [-1]*V; mcm += (t:=aug(u)) != -1
        while t != -1: v = par[t]; w = mtc[v]; mtc[t], mtc[v] = v, t; t = w; s = [0]*V
if 2*mcm != V: print('impossible'), exit(0)
for i in range(V):
    if s[i]: continue
    print(i, mtc[i]); s[i] = s[mtc[i]] = 1