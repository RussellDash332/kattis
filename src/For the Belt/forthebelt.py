for _ in range(int(input())):
    R, C = map(int, input().split()); O = []
    while 1:
        v, *r = map(int, input().split())
        if v<1 and not r: break
        if len(r) == 2: z, (x, y) = v, r; O += [(x, y)]
        else:
            z, (x, y, dx, dy) = v, r
            for i in range(z): O += [(x+dx*i, y+dy*i)]
    D = {}; T = {0}
    for r, c in O:
        if r < R: T.add(r)
        if c < C:
            if c not in D: D[c] = []
            D[c].append(r)
    X = sorted(D); P = [0]+X+[C]; T = sorted(T); U = [0]*len(X); Z = 0
    for c in X: D[c].sort()
    for r in T:
        H = R-r; h = []; S = []
        for j, c in enumerate(X):
            while U[j] < len(a:=D[c]) and a[U[j]] <= r: U[j] += 1
            h.append((a[U[j]] if U[j] < len(a) else R)-r)
        for i in range(len(X)+1):
            v = h[i] if i < len(X) else 0
            while S and h[S[-1]] > v: Z = max(Z, h[j:=S.pop()]*((X[i] if i < len(X) else C)-(X[S[-1]] if S else 0)))
            S.append(i)
    for a, b in zip(P, P[1:]): Z = max(Z, R*(b-a))
    print(Z)