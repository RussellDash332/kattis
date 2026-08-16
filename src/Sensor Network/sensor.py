from random import *
def aug(l):
    if vis[l]: return 0
    vis[l] = 1
    for r in g[l]:
        if match[r] == -1 or aug(match[r]): match[r] = l; return 1
    return 0
N, D = map(int, input().split())
P = [tuple(map(int, input().split())) for _ in range(N)]
Z = [0]
for i in range(N):
    xi, yi = P[i]
    for j in range(i):
        xj, yj = P[j]; dx, dy = xj-xi, yj-yi; d2 = dx*dx+dy*dy
        if d2 > D*D: continue
        A, B = [], []
        for k in range(N):
            xk, yk = P[k]
            if (xk-xi)**2+(yk-yi)**2 <= d2 >= (xk-xj)**2+(yk-yj)**2:
                if (xk-xi)*dy < (yk-yi)*dx: A.append(k)
                else: B.append(k)
        nA = len(A); nB = len(B); V = nA+nB
        g = [[] for _ in range(V)]
        for a in range(nA):
            xa, ya = P[A[a]]
            for b in range(nB):
                xb, yb = P[B[b]]
                if (xa-xb)**2+(ya-yb)**2 > d2: g[a] += [b+nA]; g[b+nA] += [a]
        match = [-1]*V; free = {*range(nA)}
        for l in [*free]:
            if (candidates:=[r for r in g[l] if match[r] == -1]): free.discard(l); match[c:=choice(candidates)] = l; match[l] = c
        for f in free: vis = [0]*nA; aug(f)
        z = [0]*V; Q = [a for a in range(nA) if match[a] < 0]
        for u in Q: z[u] = 1
        for u in Q:
            for v in g[u]:
                if not z[v] and v != match[u]:
                    z[v] = 1; w = match[v]
                    if w >= 0 and not z[w]: z[w] = 1; Q += [w]
        z = [A[a] for a in range(nA) if z[a]]+[B[b-nA] for b in range(nA, V) if not z[b]]
        if len(z) > len(Z): Z = z
print(len(Z))
print(*(i+1 for i in Z))