from array import *; v, m = map(int, input().split()); v += 2; Z = INF = 10**9; L = 10**6; g = [{} for _ in range(v)]; M = array('i', [-1]*(v<<v)); A = 1<<v-1; P = [1<<i for i in range(17)]; R = {1<<i:i for i in range(17)}; H = array('i', [-1]*A); B = array('i', [-1]*A); U = [[] for i in range(6)]
for _ in range(m):
    a, b, w = map(int, input().split())
    if b not in g[a]: g[a][b] = g[b][a] = w
    g[a][b] = g[b][a] = min(g[a][b], w)

# Part 1: APSP
D = [[g[i][j] if j in g[i] else INF for j in range(v)] for i in range(v)]
for i in range(v): D[i][i] = 0
for k in range(v):
    for i in range(v):
        for j in range(v): D[i][j] = min(D[i][j], D[i][k]+D[k][j])

# Part 2: DP bitmask (like TSP)
def dp(i, bm):
    # i: last vertex of the tour; bm: mask of unvisited vertices
    if bm == 0: return D[0][i]+D[i][-1]+5
    if M[bm*v+i] != -1: return M[bm*v+i]
    z = INF; bm2 = bm
    while bm2:
        nxt = bm2&-bm2; bm2 ^= nxt; t = dp(R[nxt], bm^nxt)-D[R[nxt]][-1]+D[R[nxt]][i]+D[i][-1]+5
        if t < z: z = t
    M[bm*v+i] = z; return z

# Part 3: Bruteforce all divisions
def best(p):
    if B[p] != -1: return B[p]
    t = p; u = INF
    while t:
        x = t&-t; t -= x; z = dp(R[x], p^x)
        if z < u: u = z
    B[p] = u; return u

for bm in range(0, A, 2):
    if (bc:=bin(bm).count('1')) < 6: U[bc].append(bm)
if v < 8: Z = best(A-2)
elif v < 13:
    for a in range(1, min(6, v//2)):
        if 2 < v-a < 8:
            for bm in U[a]:
                if (z:=max(best(bm), best(A-2-bm))) < Z: Z = z
elif v < 18:
    for a in range(1, min(6, v//2)):
        for b in range(1, min(6, (v-a)//2)):
            if 2 < v-a-b < 8:
                for bm in U[a]:
                    for bm2 in U[b]:
                        if bm&bm2 == 0 and (z:=max(best(bm), best(bm2), best(A-2-bm-bm2))) < Z: Z = z
print(Z)