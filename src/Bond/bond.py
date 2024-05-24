from math import *; INF = 10**9

def hungarian(mat):
    if len(mat) > len(mat[0]): mat = [*map(list, zip(*mat))]
    n = len(mat)+1; m = len(mat[0])+1; ans = 0; ii = [0]*max(m, n)
    mtc = [*ii]; u = [*ii]; v = [*ii]; w = [*ii]; c = 0
    mat = [[*ii], *([0]+r for r in mat)]
    for i in range(1, n):
        mtc[0] = i; mi = [INF]*m; vis = [*ii]
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
    return 10**(2-ans) if ans < 5000 else 0

n = int(input()); p = [[*map(lambda x: 2-log10(int(x)) if int(x) else INF, input().split())] for _ in range(n)]
print(hungarian(p))