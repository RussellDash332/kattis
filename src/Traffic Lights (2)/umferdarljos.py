import sys, os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
from heapq import *
from random import *
from math import *
from array import *
class QK:
    def __init__(s, v, u, d=1):
        if d < 0: v = -v; u = -u; d = -d
        s.v = v; s.u = u; s.d = d
    def __lt__(s, o):
        q = s.v*o.d-o.v*s.d
        if q: return q < 0
        return s.u*o.d < o.u*s.d
    def __eq__(s, o):
        return s.v*o.d == o.v*s.d and s.u*o.d == o.u*s.d
S = []; N = int(input()); B0 = 2_000_001
U1 = [0]*N; V1 = [0]*N; U2 = [0]*N; V2 = [0]*N; DU = [0]*N; DV = [0]*N; C = [0]*N
for i in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    if y1 > y2 or (y1 == y2 and x1 > x2): x1, y1, x2, y2 = x2, y2, x1, y1
    S += [(x1, y1, x2, y2, i)]
    u1 = B0*x1-y1; v1 = B0*y1+x1; u2 = B0*x2-y2; v2 = B0*y2+x2
    if v1 > v2: u1, v1, u2, v2 = u2, v2, u1, v1
    U1[i] = u1; V1[i] = v1; U2[i] = u2; V2[i] = v2; du = u2-u1; dv = v2-v1; DU[i] = du; DV[i] = dv; C[i] = dv*u1-du*v1
L = array('i', [-1]*N); R = array('i', [-1]*N); P = array('i', [-1]*N); SZ = array('I', [1]*N); AC = array('B', [0]*N); prio = array('I', (randint(1, 10**9) for _ in range(N))); root = -1
def sz(x):
    return 0 if x < 0 else SZ[x]
def pull(x):
    SZ[x] = 1+sz(L[x])+sz(R[x])
    if L[x] >= 0: P[L[x]] = x
    if R[x] >= 0: P[R[x]] = x
def merge(a, b):
    if a < 0:
        if b >= 0: P[b] = -1
        return b
    if b < 0: P[a] = -1; return a
    if prio[a] < prio[b]: R[a] = merge(R[a], b); pull(a); P[a] = -1; return a
    L[b] = merge(a, L[b]); pull(b); P[b] = -1; return b
def split(t, k):
    if t < 0: return -1, -1
    z = sz(L[t])
    if k <= z:
        a, b = split(L[t], k); L[t] = b; pull(t); P[t] = -1
        if a >= 0: P[a] = -1
        return a, t
    a, b = split(R[t], k-z-1); R[t] = a; pull(t); P[t] = -1
    if b >= 0: P[b] = -1
    return t, b
def rank(i):
    z = sz(L[i])
    while P[i] >= 0:
        if R[q:=P[i]] == i: z += sz(L[q])+1
        i = q
    return z
def cmp(i, j, n, d):
    q = (DU[i]*n+C[i]*d)*DV[j]-(DU[j]*n+C[j]*d)*DV[i]
    if q < 0: return -1
    if q > 0: return 1
    q = DU[i]*DV[j]-DU[j]*DV[i]
    if q < 0: return -1
    if q > 0: return 1
    return -1 if i < j else 1 if i > j else 0
def insert(i):
    global root
    AC[i] = 1; L[i] = R[i] = P[i] = -1; SZ[i] = 1; q = root; pos = 0
    while q >= 0:
        if cmp(i, q, cur.v, cur.d) < 0: q = L[q]
        else: pos += sz(L[q])+1; q = R[q]
    a, b = split(root, pos); root = merge(merge(a, i), b)
def erase(i):
    global root
    k = rank(i); a, b = split(root, k); _, b = split(b, 1); root = merge(a, b)
    AC[i] = 0; L[i] = R[i] = P[i] = -1; SZ[i] = 1
def nxt(i, f):
    k = rank(i)
    if k+f < 0 or k+f >= sz(root): return -1
    q = root; k += f
    while 1:
        if k < (z:=sz(L[q])): q = L[q]
        elif k == z: return q
        else: k -= z+1; q = R[q]
def intersect(a, b):
    x1, y1, x2, y2, _ = S[a]; x3, y3, x4, y4, _ = S[b]
    A = y2-y1; B = x1-x2; C0 = A*x1-(x2-x1)*y1; D = y4-y3; E = x3-x4; F = D*x3-(x4-x3)*y3; det = A*E-B*D
    if det == 0:
        pts = []
        for x, y in ((x1, y1), (x2, y2), (x3, y3), (x4, y4)):
            if min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2) and min(x3, x4) <= x <= max(x3, x4) and min(y3, y4) <= y <= max(y3, y4):
                if not pts or pts[-1] != (x, y): pts.append((x, y))
        if len(pts) == 1: x, y = pts[0]; return x, y, 1
        return
    xn = C0*E-B*F; yn = A*F-C0*D
    if det < 0: det = -det; xn = -xn; yn = -yn
    if min(x1, x2)*det <= xn <= max(x1, x2)*det and min(y1, y2)*det <= yn <= max(y1, y2)*det and min(x3, x4)*det <= xn <= max(x3, x4)*det and min(y3, y4)*det <= yn <= max(y3, y4)*det: return xn, yn, det
def addz(a, b, z=None):
    if a > b: a, b = b, a
    pr = (a, b)
    if pr in RP: return
    z = z or intersect(a, b)
    if z is None: return
    RP.add(pr); x, y, d = z; Z.append(((round(x/d, 8), round(y/d, 8)), [a, b]))
def find(a, b):
    if a < 0 or b < 0: return
    if a == b or not AC[a] or not AC[b]: return
    if a > b: pr = (b, a)
    else: pr = (a, b)
    if pr in SN or pr in RP: return
    z = intersect(a, b)
    if z is None: return SN.add(pr)
    x, y, d = z; qk = QK(B0*y+x, B0*x-y, d)
    SN.add(pr)
    if qk < cur: return
    if qk == cur: addz(a, b, z); return
    heappush(Q, (qk, 1, pr[0], pr[1]))
Q = []; Z = []
for i in range(N): Q.append((QK(V1[i], U1[i]), 0, i, -1)); Q.append((QK(V2[i], U2[i]), 2, i, -1))
heapify(Q); SN = set(); RP = set()
while Q:
    cur, ty, a, b = heappop(Q); ev = [(ty, a, b)]
    while Q and Q[0][0] == cur: _, t, aa, bb = heappop(Q); ev.append((t, aa, bb))
    ss = set(); ee = set(); cc = set()
    for t, a, b in ev:
        if t == 0: ss.add(a)
        elif t == 2: ee.add(a)
        elif AC[a] and AC[b]: cc.add(a); cc.add(b)
    if len(zz:=ss|ee|cc) > 1: addz(*sorted(zz))
    rr = ee|cc; bb = set()
    for i in rr:
        if not AC[i]: continue
        p = nxt(i, -1); s = nxt(i, 1)
        if p >= 0 and p not in rr: bb.add(p)
        if s >= 0 and s not in rr: bb.add(s)
    for i in rr:
        if AC[i]: erase(i)
    for i in (add:=(cc-ee)|ss): insert(i)
    for i in bb|add:
        if AC[i]: find(i, nxt(i, -1)); find(i, nxt(i, 1))
Z.sort(key=lambda z: z[0]); print(M:=len(Z))
K = [[] for _ in range(N)]
for i, (_, z) in enumerate(Z): K[z[0]] += [i]; K[z[1]] += [i]
B = [[-1]*4 for _ in range(M)]; X = [-1]*N
for i in range(N):
    for j in range(len(K[i])-1): a, b = Z[k:=K[i][j]][1]; B[k][i==a] = K[i][j+1]
for i in range(M):
    a, b = Z[i][1]; ca = X[a]; cb = X[b]
    if ca == cb:
        if ca in (-1, 2): ca, cb = 0, 1
        else: ca = cb = 2
    elif ca == 0 or cb == 1: ca, cb = 1, 0
    else: ca, cb = 0, 1
    X[a] = ca; X[b] = cb; B[i][2] = ca; B[i][3] = cb
for i in range(M): a, b = Z[i][1]; ca, cb = 'rgy'[B[i][2]], 'rgy'[B[i][3]]; sys.stdout.write(f'{a+1} {b+1} {ca} {cb}\n')