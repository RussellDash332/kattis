import sys, os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

# convex hull
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

# polygon area
def cross(a, b):
    return a[0]*b[1]-a[1]*b[0]
def area(p):
    a, n = 0, len(p)
    for i in range(n): a += cross(p[i], p[(i+1)%n])
    return abs(a)

# maximum flow - minimum cut
from collections import deque; INF = 10**13
def BFS(s, t):
    d[s] = 0; q = deque([s])
    while q:
        u = q.popleft()
        if u == t: break
        for idx in AL[u]:
            v, cap, flow = EL[idx]
            if cap > flow and d[v] == -1: d[v] = d[u]+1; q.append(v)
    return d[t] != -1
def DFS(u, t, f=INF):
    if u == t or f == 0: return f
    for i in range(last[u], len(AL[u])):
        last[u] = i; v, cap, flow = EL[AL[u][i]]
        if d[v] != d[u]+1: continue
        pushed = DFS(v, t, min(f, cap-flow))
        if pushed: EL[AL[u][i]][2] += pushed; EL[AL[u][i]^1][2] -= pushed; return pushed
    return 0
def add(u, v, c):
    AL[u].append(len(EL)); EL.append([v, c, 0]); AL[v].append(len(EL)); EL.append([u, 0, 0])

h, n = map(int, input().split()); P = []; OX = []; OY = []
V = 2*n+2; source, sink = V-2, V-1; EL, AL = [], [[] for _ in range(V)]

for i in range(n):
    k, c = map(int, input().split())
    ox, oy = map(int, input().split())
    v = [*map(int, input().split())]
    p = [(v[2*i], v[2*i+1]) for i in range(k)]; p.append((0, 0))
    P.append(chull(p))
    OX.append(ox); OY.append(oy)
    add(i, i+n, area(P[i])*c//2)
m = int(input()); M = 10**10+3233; E = [[] for _ in range(m+2)]; F = [0]
for q in map(int, input().split()): F.append(F[-1]+q)

# for BSTA, minowski sum of polygon
H = [p.index(max(p)) for p in P]
def its(t, i, j):
    A = [(OX[i]+x*t, OY[i]+y*t) for x, y in P[i]]; B = [(-OX[j]-x*t, -OY[j]-y*t) for x, y in P[j]]
    q = H[j]; a = len(A); b = len(B); R = [(A[0][0]+B[q][0], A[0][1]+B[q][1])]; i = 0; j = q
    while i < a or j < q+b:
        if i == a: j += 1
        elif j == q+b: i += 1
        else:
            if (c:=(A[(i+1)%a][0]-A[i][0])*(B[(j+1)%b][1]-B[j%b][1])-(A[(i+1)%a][1]-A[i][1])*(B[(j+1)%b][0]-B[j%b][0])) >= 0: i += 1
            if c <= 0: j += 1
        R.append((A[i%a][0]+B[j%b][0], A[i%a][1]+B[j%b][1]))
    N = len(R)
    for i in range(N):
        if cross(R[i], R[(i+1)%N]) < 0: return 0
    return 1
def wall(t, i, h):
    b = 0
    for _, y in P[i]:
        y2 = OY[i]+y*t; b |= (y2<=h)+2*(y2>=h)
        if b == 3: return 1
    return 0

# BSTA on time bounds instead of the entire [0, LARGE)
for i in range(n):
    # minimum time to hit upper boundary
    lo, hi = 0, m+1
    while lo+1 < hi:
        if wall(F[mi:=(lo+hi)//2], i, h): hi = mi
        else: lo = mi
    E[hi].append((i, n+1))
    # minimum time to hit lower boundary
    lo, hi = 0, m+1
    while lo+1 < hi:
        if wall(F[mi:=(lo+hi)//2], i, -h): hi = mi
        else: lo = mi
    E[hi].append((i, n))
    # deal with the rest
    for j in range(i):
        lo, hi = 0, m+1
        while lo+1 < hi:
            if its(F[mi:=(lo+hi)//2], i, j): hi = mi
            else: lo = mi
        E[hi].append((i, j))

# run max flow to get min cut over and over
mf = 0
for p in range(m+1):
    for i, j in E[p]:
        if j == n: add(source, i, INF)
        elif j == n+1: add(i+n, sink, INF)
        else: add(i+n, j, INF); add(j+n, i, INF)
    if E[p]:
        d = [-1]*V
        while BFS(source, sink):
            last = [0]*V; f = DFS(source, sink)
            while f: mf += f; f = DFS(source, sink); mf %= M
            d = [-1]*V
    if p: sys.stdout.write(str(mf*F[p]*F[p]%M)); sys.stdout.write(' ')