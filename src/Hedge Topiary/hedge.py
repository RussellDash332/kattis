def pip(p, P, s=False):
    px, py = p; z = False; n = len(P)
    for i in range(n):
        x1, y1 = P[i]; x2, y2 = P[i-1]; c = (x2-x1)*(py-y1)-(y2-y1)*(px-x1)
        if abs(c) < 1e-9 and min(x1, x2)-1e-9 <= px <= max(x1, x2)+1e-9 and min(y1, y2)-1e-9 <= py <= max(y1, y2)+1e-9: return not s
        if (y1 > py) != (y2 > py) and px < x1+(py-y1)*(x2-x1)/(y2-y1): z = not z
    return z
def check(s1, s2):
    (p1, p2), (p3, p4) = s1, s2; (x1, y1), (x2, y2), (x3, y3), (x4, y4) = p1, p2, p3, p4
    c1 = (x2-x1)*(y3-y1)-(y2-y1)*(x3-x1); c2 = (x2-x1)*(y4-y1)-(y2-y1)*(x4-x1)
    c3 = (x4-x3)*(y1-y3)-(y4-y3)*(x1-x3); c4 = (x4-x3)*(y2-y3)-(y4-y3)*(x2-x3)
    return ((c1 > 1e-9 and c2 < -1e-9) or (c1 < -1e-9 and c2 > 1e-9)) and ((c3 > 1e-9 and c4 < -1e-9) or (c3 < -1e-9 and c4 > 1e-9))
def f(k):
    if k > K+1e-9: return 0
    R = [(x*k, y*k) for x, y in P]
    if any(check((R[i], R[i-1]), (Q[j], Q[j-1])) for i in range(N) for j in range(M)): return 0
    if any(pip(q, R, True) for q in Q): return 0
    return all(pip(p, Q) for p in R)
def ray(x, y, x1, y1, x2, y2):
    vx, vy = x2-x1, y2-y1; d = x*vy-y*vx
    if abs(d) < 1e-9: return
    t = (x1*vy-y1*vx)/d; u = (x1*y-y1*x)/d
    if t >= -1e-9 and -1e-9 <= u <= 1+1e-9: return t
N = int(input())
P = [[*map(int, input().split())] for _ in range(N)]
M = int(input())
Q = [[*map(int, input().split())] for _ in range(M)]
C = [0]
mxp, Mxp = min(x for x, y in P), max(x for x, y in P)
myp, Myp = min(y for x, y in P), max(y for x, y in P)
mxq, Mxq = min(x for x, y in Q), max(x for x, y in Q)
myq, Myq = min(y for x, y in Q), max(y for x, y in Q)
K = 1e9
if Mxp > 0: K = min(K, Mxq/Mxp)
if mxp < 0: K = min(K, mxq/mxp)
if Myp > 0: K = min(K, Myq/Myp)
if myp < 0: K = min(K, myq/myp)
for p in P:
    for i in range(M):
        t = ray(*p, *Q[i], *Q[i-1])
        if t != None and t > 1e-9: C += [t]
for q in Q:
    for i in range(N):
        t = ray(*q, *P[i], *P[i-1])
        if t != None and t > 1e-9: C += [1/t]
C = sorted({*C})
for i in range(len(C)-1, -1, -1):
    a, b = C[i-1], C[i]
    if f(b): print(b); break
    if f((a+b)/2): print((a+b)/2); break