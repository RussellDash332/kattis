import sys; input = sys.stdin.readline
from collections import *
def lapjv(mat):
    if len(mat) > len(mat[0]): mat = [*map(list, zip(*mat))]
    n, m = len(mat), len(mat[0]); D = [0]*m; P = [0]*m; mtc = [-1]*n; cm = [-1]*m; C = [*range(m)]; pr = [0]*m; d = 0
    for i in range(n):
        for c in range(m): D[c] = mat[i][c]-P[c]; pr[c] = i
        s = t = x = z = 0
        while z^1:
            if s == t:
                x = s; d = D[C[t]]; t += 1
                for j in range(t, m):
                    if d < D[c:=C[j]]: continue
                    if d > D[c]: d = D[c]; t = s
                    C[j], C[t] = C[t], C[j]; t += 1
                for j in range(s, t):
                    if cm[c:=C[j]] < 0: z = 1; break
                if z: break
            r = cm[e:=C[s]]; s += 1
            for j in range(t, m):
                if D[c:=C[j]] <= (v:=mat[r][c]-mat[r][e]+P[e]-P[c]+d): continue
                D[c] = v; pr[c] = r
                if v == d:
                    if cm[c] < 0: z = 1; break
                    C[j], C[t] = C[t], C[j]; t += 1
            if z: break
        for j in range(x): P[C[j]] += D[C[j]]-d
        r = -1
        while r != i: r = cm[c] = pr[c]; c, mtc[r] = mtc[r], c
    return sum(mat[i][mtc[i]] for i in range(n))
for tc in range(1, int(input())+1):
    p = [*map(int, input().split())]; v = [*map(int, input().split())]; s = len(p)
    mat1 = [[1000]*s for _ in range(s)]; mat2 = [[1000]*s for _ in range(s)]; mat3 = [[1000]*s for _ in range(s)]
    hexa = [[*range(1, (s+1)//2+1)]]
    for i in range((s-1)//2): hexa.append([*range(hexa[-1][-1]+1, hexa[-1][-1]+len(hexa[-1])+2)])
    for i in range((s-1)//2): hexa.append([*range(hexa[-1][-1]+1, hexa[-1][-1]+len(hexa[-1]))])
    g = [[] for _ in range((3*s*s+1)//4+1)]
    for i in range((s-1)//2):
        for j in range(len(hexa[i])-1): g[hexa[i][j]].append(hexa[i][j+1]), g[hexa[i][j+1]].append(hexa[i][j])
        for j in range(len(hexa[i])): g[hexa[i][j]].append(hexa[i+1][j]), g[hexa[i+1][j]].append(hexa[i][j]), g[hexa[i][j]].append(hexa[i+1][j+1]), g[hexa[i+1][j+1]].append(hexa[i][j])
    for i in range(s-1, (s-1)//2, -1):
        for j in range(len(hexa[i])-1): g[hexa[i][j]].append(hexa[i][j+1]), g[hexa[i][j+1]].append(hexa[i][j])
        for j in range(len(hexa[i])): g[hexa[i][j]].append(hexa[i-1][j]), g[hexa[i-1][j]].append(hexa[i][j]), g[hexa[i][j]].append(hexa[i-1][j+1]), g[hexa[i-1][j+1]].append(hexa[i][j])
    for i in range(s-1): g[hexa[(s-1)//2][i]].append(hexa[(s-1)//2][i+1]), g[hexa[(s-1)//2][i+1]].append(hexa[(s-1)//2][i])
    for i in range(s):
        D = [-1]*len(g); q = deque([(p[i], 0)])
        while q:
            u, par = q.popleft()
            if D[u] != -1: continue
            D[u] = D[par] + 1
            for nxt in g[u]: q.append((nxt, u))
        for j in range(s):
            mat1[i][j] = v[i]*D[hexa[(s-1)//2][j]]
            mat2[i][j] = v[i]*D[hexa[j][min((s-1)//2, j)]]
            mat3[i][j] = v[i]*D[hexa[j][len(hexa[j])-1-min((s-1)//2, j)]]
    print(f'Case #{tc}:', min(map(lapjv, (mat1, mat2, mat3))))