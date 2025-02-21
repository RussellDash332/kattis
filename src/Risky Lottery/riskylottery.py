from math import *; from itertools import *; from collections import *
N, M = map(int, input().split()); P = [1/M]*M; E = 6e-4; Z = {}
for p in product(*[range(M) for _ in range(N)]):
    h = Counter(p); u = [i for i in p if h[i]==1]
    if u and min(u) == p[0]:
        L = Counter(i for i in p if i < p[0]); q = tuple(sorted(L.items()))
        if (p[0], q) not in Z:
            K = N-1; C = 1
            for v in L.values(): C *= comb(K, v); K -= v
            Z[(p[0], q)] = (N-1-sum(v for k, v in q), C)
while 1:
    Q = [0]*M; R = [sum(P[p+1:]) for p in range(M)]
    for (p, q), (l, r) in Z.items():
        z = R[p]**l
        for k, v in q: z *= P[k]**v
        Q[p] += z*r
    s = sum(Q)/M
    for i in range(M):
        if Q[i] > s: P[i] = min(1, P[i]+E)
        else:        P[i] = max(0, P[i]-E)
    s = sum(P)
    for i in range(M): P[i] /= s
    if max(Q)-min(Q) < 2*E: break
print(*P)