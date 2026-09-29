import sys; input = sys.stdin.readline
for _ in range(int(input())):
    N, M = map(int, input().split())
    L = [[*map(int, input().split())] for _ in range(N)]
    P = [[*map(int, input().split())] for _ in range(M)]
    R = [[*range(M)]]; K = N+1
    for i in range(N):
        a, b, c = L[i]
        for j in range(i): d, e, f = L[j]; K += a*e != b*d
        for r in R:
            p = []; q = []
            for k in r: x, y = P[k]; (p if a*x+b*y+c>0 else q).append(k)
            if q and not p: p, q = q, p
            r.clear(); r.extend(p)
            if q: R.append(q)
    print('VPURLONTEERCATBELDE'[len(R)==K::2])