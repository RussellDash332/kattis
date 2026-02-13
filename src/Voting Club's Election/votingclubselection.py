n = int(input())
m = int(input())
V = input().split()
r = {e:i for i,e in enumerate(V)}
B = []; S = {*range(m)}
for _ in range(n):
    b = [0]*m
    for c in input().split(): b[r[c[0]]] = int(c[1:])
    B.append(b)
for _ in range(m):
    H = {}; I = (10**9, []); J = (-10**9, [])
    for i in S: H[i] = 0
    for i in range(n):
        h = {}; d = 0
        for j in range(m):
            if j in S:
                if B[i][j] not in h: h[B[i][j]] = []
                h[B[i][j]].append(j)
            else: d += B[i][j]
        t = max(h); u = len(h[t])
        for k in h:
            for v in h[k]: H[v] += k
        for v in h[t]: H[v] += d/u
    for i in H:
        if H[i] == I[0]: I[1].append(i)
        elif H[i] < I[0]: I = (H[i], [i])
        if H[i] == J[0]: J[1].append(i)
        elif H[i] > J[0]: J = (H[i], [i])
    if 2*J[0] > sum(H.values()): print(V[J[1][0]]); exit()
    for v in I[1]: S.discard(v)
    if len({*H.values()}) == 1: print('VOID'); exit()