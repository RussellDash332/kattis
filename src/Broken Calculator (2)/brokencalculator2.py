INF = 10**36
def hungarian(mat):
    n = len(mat)+1; ans = 0; ii = [0]*n; mtc = [*ii]; u = [*ii]; v = [*ii]; w = [*ii]; c = 0; mat = [[*ii], *([0]+r for r in mat)]
    for i in range(1, n):
        mtc[0] = i; mi = [INF]*n; vis = [*ii]
        while 1:
            vis[c] = 1; d = INF; c2 = 0
            for j in range(1, n):
                if vis[j]: continue
                if (cur:=mat[mtc[c]][j]-u[mtc[c]]-v[j]) < mi[j]: mi[j] = cur; w[j] = c
                if mi[j] < d: d = mi[j]; c2 = j
            for j in range(n):
                if vis[j]: u[mtc[j]] += d; v[j] -= d
                else: mi[j] -= d
            if mtc[(c:=c2)] == 0: break
        while 1:
            mtc[c] = mtc[w[c]]
            if (c:=w[c]) == 0: break
    for i in range(1, n):
        if mtc[i]: ans += mat[mtc[i]][i]
    return ans
n = int(input())
A, B, C = map(int, input().split())
x = [*map(int, input().split())]
M = [[INF]*n for _ in range(n)]
def f(X, Y):
    b = 0; r = INF
    while max(X, 1)<<b <= Y:
        D = Y-(X<<b); a = 0
        for c in range(b, -1, -1): a += D>>c; D -= (D>>c)<<c
        r = min(r, A*a+B*b); b += 1
    return r
for i in range(n):
    for j in range(n): M[i][j] = C+f(0, x[j]) if i >= j else min(C+f(0, x[j]), f(x[i], x[j]))
print(hungarian(M)-C)