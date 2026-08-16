def union(R):
    X = set(); Q = []; T = 1; Z = []
    for x1, y1, x2, y2 in R: X.add(x1); X.add(x2); Q.append((y2, -1, x1, x2)); Q.append((y1, 1, x1, x2))
    i2x = sorted(X); x2i = {i2x[i]: i for i in range(len(i2x))}; L = [i2x[i+1]-i2x[i] for i in range(len(i2x)-1)]
    while T < len(L): T *= 2
    C = [0]*2*T; S = [0]*2*T; W = [0]*2*T; A = {}; Q.sort()
    for i in range(len(L)): W[T+i] = L[i]
    for p in range(T-1, 0, -1): W[p] = W[2*p]+W[2*p+1]
    i = 0; P = Q[0][0]
    while i < len(Q):
        y = Q[i][0]
        while i < len(Q) and Q[i][0] == y:
            _, v, x1, x2 = Q[i]
            D = x2i[x1]; E = x2i[x2]; U = [(1, 0, T, 0)]
            while U:
                p, s, l, b = U.pop()
                if b:
                    if C[p]:    S[p] = W[p]
                    elif p < T: S[p] = S[2*p]+S[2*p+1]
                    else:       S[p] = 0
                else:
                    U.append((p, s, l, 1))
                    if D <= s <= E-l: C[p] += v
                    else:
                        if E > s > D-l//2: U.append((2*p, s, l//2, 0))
                        if E+l//2 > s+l > D: U.append((2*p+1, s+l//2, l//2, 0))
            i += 1
        K = []; U = [(1, 0, T)]
        while U:
            p, s, l = U.pop()
            if C[p]: K.append((i2x[s], i2x[min(s+l, len(i2x)-1)]))
            elif p < T: U.append((2*p, s, l//2)); U.append((2*p+1, s+l//2, l//2))
        B = set(K)
        for x in A.keys()-B: Z.append((x[0], A[x], x[1], y)); del A[x]
        for x in B-A.keys(): A[x] = y
        P = y
    for x, y0 in A.items(): Z.append((x[0], y0, x[1], P))
    return Z

from math import *
R = [[] for _ in range(4)]; I = []
for _ in range(int(input())):
    x1, y1, w, h = map(int, input().split()); x2, y2 = x1+w, y1+h
    if x1 <= 0 <= x2: xm = 0
    else: xm = min(abs(x1), abs(x2))
    if y1 <= 0 <= y2: ym = 0
    else: ym = min(abs(y1), abs(y2))
    tm = xm*xm+ym*ym; tM = max(abs(x1), abs(x2))**2+max(abs(y1), abs(y2))**2
    I += [(tm, tM)]; x = 0
    for f in (max, min):
        for g in (max, min):
            a1, b1, a2, b2 = f(x1, 0), g(y1, 0), f(x2, 0), g(y2, 0)
            if (a2-a1)*(b2-b1): R[x] += [(a1, b1, a2, b2)]
            x += 1
r = {}; z = S = t = 0
for a, b in I:
    if a not in r: r[a] = 0
    if b not in r: r[b] = 0
    r[a] += 1; r[b] -= 1
for i in sorted(r):
    z += r[i]
    if 1-t and z>0: S -= i; t ^= 1
    elif t and z<1: S += i; t ^= 1
if not all(R): print(0, S*pi); exit()
T = {0}; E = {}; R = [*map(union, R)]
for rr in R:
    for i in range(len(rr)):
        x1, y1, x2, y2 = rr[i]; T.update([x1*x1+y1*y1, x1*x1+y2*y2, x2*x2+y1*y1, x2*x2+y2*y2])
        hi = ((x1, x2, y1), (x1, x2, y2)); vi = ((x1, y1, y2), (x2, y1, y2))
        for j in range(i):
            x3, y3, x4, y4 = rr[j]
            if x2 < x3 or x4 < x1 or y2 < y3 or y4 < y1: continue
            hj = ((x3, x4, y3), (x3, x4, y4)); vj = ((x3, y3, y4), (x4, y3, y4))
            for xa, xb, y in hi:
                for x, yc, yd in vj:
                    if xa <= x <= xb and yc <= y <= yd: T.add(x*x+y*y)
            for x, ya, yb in vi:
                for xc, xd, y in hj:
                    if xc <= x <= xd and ya <= y <= yb: T.add(x*x+y*y)
T = sorted(T)
for rr in R:
    ev, A, U = [], set(), []
    for x1, y1, x2, y2 in rr:
        if x1*x1 > x2*x2: x1, x2 = x2, x1
        if y1*y1 > y2*y2: y1, y2 = y2, y1
        U.append((2*x1*x1, 2*y1*y1, 2*x2*x2, 2*y2*y2))
    for i, (x, y, X, Y) in enumerate(U): ev.append(((x+y)>>1, 1, i)); ev.append(((X+Y)>>1, -1, i))
    ev.sort(key=lambda e: e[0]); p = 0; q = len(ev)
    for i in range(len(T)-1):
        t0 = T[i]; t1 = T[i+1]; t = t0+t1
        while p < q and ev[p][0] <= t0:
            _, l, j = ev[p]
            if l<0: A.discard(j)
            else: A.add(j)
            p += 1
        if not A: continue
        K = []; z = 0
        for j in A:
            x, y, X, Y = U[j]; lk = t-X if t-X>y else y; rk = t-x if t-x<Y else Y
            if lk < rk: K.append((lk, rk))
        for lk, rk in sorted(K):
            if lk > z: break
            if rk > z:
                z = rk
                if z >= t: break
        if z >= t:
            if t0 not in E: E[t0] = 0
            if t1 not in E: E[t1] = 0
            E[t0] += 1; E[t1] -= 1
U = sorted(i for i in E if E[i]); z = Z = 0
for i in range(len(U)-1):
    z += E[U[i]]
    if z == 4: Z += U[i+1]-U[i]
print(Z*pi, (S-Z)*pi)