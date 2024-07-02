import sys; input = sys.stdin.readline
while 1:
    k, n, e = map(int, input().split())
    if k == 0: break
    p = [1<<i for i in range(n)]; n = 1<<n; g = [[] for _ in range(n)]; P = [0]*n*k; ok = 1
    for _ in range(e): a, b = map(int, input().split()); g[a].append(b); g[b].append(a)
    for i in range(n): P[i] = 1/n
    for i in range(1, k):
        for j in range(n):
            for v in g[j]: P[i*n+j] += P[(i-1)*n+v]/len(g[v])
    for r in range(k):
        for i in p:
            s = 0
            for j in range(n):
                if j&i: s += P[r*n+j]
            if 0.25 < s < 0.75: continue
            ok = 0; break
        if not ok: break
    print('YNeos'[1-ok::2])