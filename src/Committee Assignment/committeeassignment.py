import sys; input = sys.stdin.readline
def bt(v, cc):
    global Z
    if cc >= Z: return
    if v == n: Z = cc; return
    for i in range(1, cc+2):
        if cm[i]&am[v] == cm[i]: cm[i] |= 1<<v; bt(v+1, max(cc, i)); cm[i] ^= 1<<v
while True:
    n, m = map(int, input().split())
    if n == m == 0: break
    G = [[1]*n for _ in range(n)]; r = {}
    for _ in range(m):
        a, b = input().strip().split()
        if a not in r: r[a] = len(r)
        if b not in r: r[b] = len(r)
        G[r[a]][r[b]] = G[r[b]][r[a]] = 0
    am = [0]*n
    for i in range(n):
        for j in range(n):
            if G[i][j]: am[i] |= 1<<j
    Z = n+1; cm = [0]*(n+1); bt(0, 0); print(Z)