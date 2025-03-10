M = 10**15+37
def det(a):
    z = 1; n = len(a)
    for i in range(n):
        k = i
        for j in range(i+1, n):
            if a[j][i] > a[k][i]: k = j
        if a[k][i] == 0: return 0
        a[i], a[k] = a[k], a[i]
        if i != k: z = -z
        z *= a[i][i]; z %= M
        for j in range(i+1, n): a[i][j] *= pow(a[i][i], -1, M); a[i][j] %= M
        for j in range(n):
            if j != i and a[j][i]:
                for k in range(i+1, n): a[j][k] -= a[i][k]*a[j][i]; a[j][k] %= M
    return z

def st(g):
    n = len(g); A = [[0]*n for _ in range(n)]
    for i in range(n):
        A[i][i] = len(g[i])
        for j in g[i]: A[i][j] -= 1
    return det([r[1:] for r in A[1:]])

import sys; input = sys.stdin.readline
while True:
    try: n, k, m = map(int, input().split())
    except: break
    G = [{*range(n)}-{i} for i in range(n)]
    for _ in range(k): a, b = map(int, input().split()); G[a:=a-1].discard(b:=b-1); G[b].discard(a)
    print(st(G))