import sys; input = sys.stdin.readline
from array import *
from collections import *
def hungarian(mat):
    INF = 10**9; n = len(mat)+1; m = len(mat[0])+1; ans = 0; ii = [0]*max(m, n)
    mtc = array('i', ii); u = array('i', ii); v = array('i', ii); w = array('i', ii); c = 0
    mat = [array('i', ii), *(array('i', [0]+r) for r in mat)]
    for i in range(1, n):
        mtc[0] = i; mi = array('i', [INF]*m); vis = array('i', ii)
        while 1:
            vis[c] = 1; d = INF; c2 = 0
            for j in range(1, m):
                if vis[j]: continue
                if (cur:=mat[mtc[c]][j]-u[mtc[c]]-v[j]) < mi[j]: mi[j] = cur; w[j] = c
                if mi[j] < d: d = mi[j]; c2 = j
            for j in range(m):
                if vis[j]: u[mtc[j]] += d; v[j] -= d
                else: mi[j] -= d
            if mtc[(c:=c2)] == 0: break
        while 1:
            mtc[c] = mtc[w[c]]
            if (c:=w[c]) == 0: break
    for i in range(1, m):
        if mtc[i]: ans += mat[mtc[i]][i]
    return ans

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
    print(f'Case #{tc}:', min(map(hungarian, (mat1, mat2, mat3))))