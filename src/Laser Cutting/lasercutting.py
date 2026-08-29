def pip(p, P):
    z = False; n = len(P)
    for i in range(n):
        a = (P[i][0]-p[0], P[i][1]-p[1]); b = (P[(i+1)%n][0]-p[0], P[(i+1)%n][1]-p[1])
        if a[1] > b[1]: a, b = b, a
        if a[1] <= 0 and b[1] > 0 and a[0]*b[1] < a[1]*b[0]: z = not z
        if a[0]*b[1] == a[1]*b[0] and a[0]*b[0]+a[1]*b[1] <= 0: return True
    return z
def intersect(s1, s2):
    (x1, y1), (x2, y2) = s1; (x3, y3), (x4, y4) = s2
    if x1 == x2 and x3 == x4: return x1 == x3 and max(min(y1, y2), min(y3, y4)) <= min(max(y1, y2), max(y3, y4))
    if y1 == y2 and y3 == y4: return y1 == y3 and max(min(x1, x2), min(x3, x4)) <= min(max(x1, x2), max(x3, x4))
    if x1 == x2 and y3 == y4: return min(x3, x4) <= x1 <= max(x3, x4) and min(y1, y2) <= y3 <= max(y1, y2)
    if y1 == y2 and x3 == x4: return min(x1, x2) <= x3 <= max(x1, x2) and min(y3, y4) <= y1 <= max(y3, y4)
    return 0
for _ in range(int(input())):
    P = []; N = int(input()); inv = 0; its = 0
    for _ in range(N):
        n = int(input()); p = []
        v = [*map(int, input().split())]
        for i in range(n): p += [(v[2*i], v[2*i+1])]
        if p[0] != p.pop(): inv = 1
        P += [p]; n -= 1
        for i in range(n):
            for j in range(n):
                if j not in [i, (i-1)%n, (i+1)%n]:
                    if intersect((p[i], p[i-1]), (p[j], p[j-1])): inv = 1
    if inv: print('INVALID POLYGON'); continue
    G = [[] for _ in range(N)]
    for i in range(N):
        for j in range(i):
            p1 = P[i]; p2 = P[j]
            if all(pip(p, p2) for p in p1): G[j] += [i]
            if all(pip(p, p1) for p in p2): G[i] += [j]
            for k in range(len(p1)):
                s = (p1[k], p1[k-1])
                for l in range(len(p2)):
                    if intersect(s, (p2[l], p2[l-1])): its = 1
    if its: print('INTERSECTING POLYGONS'); continue
    if any(G[j] for i in range(N) for j in G[i]): print('INVALID NESTING')
    else: print('CORRECT')