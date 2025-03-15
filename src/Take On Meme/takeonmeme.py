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
def minkowski(P, Q):
    p = P.index(min(P)); q = Q.index(min(Q)); a = len(P); b = len(Q); R = [(P[p][0]+Q[q][0], P[p][1]+Q[q][1])]; i = p; j = q
    while i < p+a or j < q+b:
        if i == p+a: j += 1
        elif j == q+b: i += 1
        else:
            if (c:=(P[(i+1)%a][0]-P[i%a][0])*(Q[(j+1)%b][1]-Q[j%b][1])-(P[(i+1)%a][1]-P[i%a][1])*(Q[(j+1)%b][0]-Q[j%b][0])) >= 0: i += 1
            if c <= 0: j += 1
        R.append((P[i%a][0]+Q[j%b][0], P[i%a][1]+Q[j%b][1]))
    return R
import sys; input = sys.stdin.readline
N = int(input())
G = [None]*N
H = [None]*N
for i in range(N):
    k, *r = map(int, input().split())
    if k: G[i] = [j-1 for j in r]
    else: H[i] = [(r[0], r[1])]
for i in range(N-1, -1, -1):
    if not G[i]: continue
    I = [[(-x,-y) for x,y in H[j]] for j in G[i]]; R = []
    for j in range(len(G[i])):
        v = G[i][j]; S = H[v]
        for m in range(len(G[i])):
            if m != j: S = minkowski(S, I[m])
        R.extend(S)
    H[i] = chull(R)
print(max(x*x+y*y for x,y in H[0]))