from collections import *
N, E, Sx, Sy, C = map(int, input().split())
T = defaultdict(lambda: [0, 0]); T[(0, Sx, Sy)] = [0, 0]
K = ((0, 1), (1, 0), (-1, 0), (0, -1))
for _ in range(C):
    x, y, t = map(int, input().split())
    for dx, dy in K:
        if N>x+dx>-1<y+dy<N: T[(t, x+dx, y+dy)][0] += 1
    T[(t, x, y)][1] += 1
T = sorted((t, x, y, s, e) for (t, x, y), (s, e) in T.items()); L = len(T)
D = [[] for _ in range(L)]; D[0] = [(E, 0)]
for i in range(L):
    if not D[i]: continue
    ti, xi, yi, *_ = T[i]
    for j in range(i+1, L):
        tj, xj, yj, de, ds = T[j]; d = abs(xi-xj)+abs(yi-yj)
        if tj-ti<d: continue
        for e, cs in D[i]:
            if e<d: continue
            e2, s2 = e-d+de, cs+ds
            if any(pe>=e2 and ps>=s2 for pe, ps in D[j]): continue
            D[j] = [p for p in D[j] if p[0]>e2 or p[1]>s2]; D[j] += [(e2, s2)]
print(max(p[1] for u in D for p in u))