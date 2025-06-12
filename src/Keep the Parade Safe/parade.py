def ccw(p, q, r):
    return (q[0]-p[0])*(r[1]-p[1]) > (r[0]-p[0])*(q[1]-p[1])

def chull(pts):
    if len(pts) < 3: return pts
    pts, n = sorted(pts), len(pts)
    upper, lower = pts[:2], pts[-1:-3:-1]
    for i in range(2, n):
        while len(upper) > 1 and not ccw(upper[-2], upper[-1], pts[i]): upper.pop()
        upper.append(pts[i])
    for i in range(n-2, -1, -1):
        while len(lower) > 1 and not ccw(lower[-2], lower[-1], pts[i]): lower.pop()
        lower.append(pts[i])
    return upper[:-1] + lower[:-1]

def pip(p, P):
    z = 0; N = len(P)
    for i in range(N):
        a = (P[i][0]-p[0], P[i][1]-p[1]); b = (P[(i+1)%N][0]-p[0], P[(i+1)%N][1]-p[1])
        if a[1] > b[1]: a, b = b, a
        if a[1] <= 0 and b[1] > 0 and a[0]*b[1] < a[1]*b[0]: z = 1-z
        if a[0]*b[1] == a[1]*b[0] and a[0]*b[0]+a[1]*b[1] <= 0: return ~i
    return z

N = int(input())
P = [[*map(int, input().split())] for _ in range(N)]
C = chull(P)
if len(C) < 3: print(0); exit()
elif len(C) == 3:
    a, b, c = C; H = [[], [], []]; z = 0
    for p in P:
        if p == a or p == b or p == c: continue
        t = pip(p, C)
        if t > 0: z = 1; break
        H[t].append(p)
    s = sum(h!=[] for h in H)
    if z: pass
    elif s < 2: print(0); exit()
    elif s == 2:
        for i in range(3):
            if not H[i]: x = C[1-i]
        P.remove(x); C = chull(P)
S = int(input()); Z = 0
for _ in range(S): x, y = map(int, input().split()); Z += pip((x, y), C) != 0
print(Z)