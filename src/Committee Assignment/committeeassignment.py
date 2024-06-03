import sys; input = sys.stdin.readline

def bt(cl, v, z):
    if v < n:
        for i in range(1, v+2):
            cl[v] = i; d[i].append(v); ok = 1
            for j in range(len(d[i])-1):
                if am[d[i][j]][v] < 1: ok = 0; break
            if ok and max(cl) < z: z = bt(cl, v+1, z)
            cl[v] = 0; d[i].pop()
    elif (m:=max(cl)) < z: z = m
    return z

while True:
    n, m = map(int, input().split())
    if n == m == 0: break
    am = [[1]*n for _ in range(n)]; r = {}
    for _ in range(m):
        a, b = input().strip().split()
        if a not in r: r[a] = len(r)
        if b not in r: r[b] = len(r)
        am[r[a]][r[b]] = am[r[b]][r[a]] = 0
    d = {i:[] for i in range(1, n+1)}; d[1].append(0)
    print(bt([1]+[0]*(n-1), 1, n))