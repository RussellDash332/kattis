# Only got 77/100 partial :)

def intersect(s1, s2):
    (p1, p2), (p3, p4) = s1, s2
    (x1, y1), (x2, y2), (x3, y3), (x4, y4) = p1, p2, p3, p4
    a, b, c = y2-y1, x1-x2, (y2-y1)*x1 - (x2-x1)*y1
    d, e, f = y4-y3, x3-x4, (y4-y3)*x3 - (x4-x3)*y3
    if a == b == 0: return ((x1, y1) if (x1, y1) == (x3, y3) else None) if d == e == 0 else ((x1, y1) if d*x1 + e*y1 == f and min(x3, x4) <= x1 <= max(x3, x4) and min(y3, y4) <= y1 <= max(y3, y4) else None)
    elif d == e == 0: return (x3, y3) if a*x3 + b*y3 == c and min(x1, x2) <= x3 <= max(x1, x2) and min(y1, y2) <= y3 <= max(y1, y2) else None
    else:
        det = b*d-a*e
        if det:
            x, y = (b*f-c*e)//det, (c*d-a*f)//det
            return (x, y) if min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2) and min(x3, x4) <= x <= max(x3, x4) and min(y3, y4) <= y <= max(y3, y4) else None
        else:
            if a*f != c*d or b*f != c*e: return None
            else:
                p, q = min((x1, y1), (x2, y2)), max((x1, y1), (x2, y2))
                r, s = min((x3, y3), (x4, y4)), max((x3, y3), (x4, y4))
                if (p, q) == (r, s):    i1, i2 = p, q
                elif p <= r <= q:       i1, i2 = r, min(q, s)
                elif r <= p <= s:       i1, i2 = p, min(s, q)
                else:                   i1 = i2 = None
                if i1 == i2 and i1 != None: return i1
                elif i1:                    return (i1, i2)
                else:                       return None

def merge(intervals): h=lambda a,b:0 if a[1]<b[0]or b[1]<a[0]else[min(a[0],b[0]),max(a[1],b[1])]; return [r:=[],[[r.pop(),r.append(k)]if r and(k:=h(r[-1],j))else r.append(j)for j in sorted(intervals)]][0]

n, *c = open(0).read().split(); x = y = 0; V = []; H = []; dx, dy = 0, 1; K = ((0, -1), (1, 0), (-1, 0), (0, 1)); P = {}
sgn = lambda x: 0 if x == 0 else 1-2*(x<0); A = 0
for i in c:
    if i.isdigit(): (V, H)[A].append(((x, y), (x:=x+int(i)*dx, y:=y+int(i)*dy)))
    elif i == 'U': dx, dy = -dx, -dy
    elif i == '<': dx, dy = -dy, dx; A ^= 1
    else: dx, dy = dy, -dx; A ^= 1
V2 = {}; H2 = {}
for (x1, y1), (x2, y2) in sorted(V):
    if y1 > y2: y1, y2 = y2, y1
    if x1 not in V2: V2[x1] = []
    V2[x1].append((y1, y2))
V2 = sorted(V2.items(), key=lambda c: c[0])
for (x1, y1), (x2, y2) in sorted(H, key=lambda c: c[1]):
    if x1 > x2: x1, x2 = x2, x1
    if y1 not in H2: H2[y1] = []
    H2[y1].append((x1, x2))
H2 = sorted(H2.items(), key=lambda c: c[0])

V3 = {}; H3 = {}
for v, u in V2:
    V3[v] = set()
    for a, b in u: V3[v].add(a); V3[v].add(b)
for v, u in H2:
    H3[v] = set()
    for a, b in u: H3[v].add(a); H3[v].add(b)

# resolve segment endpoints
for h in H+V:
    if h[0] not in P: P[h[0]] = set()
    if h[1] not in P: P[h[1]] = set()
    P[h[0]].add(h[1]); P[h[1]].add(h[0])

# resolve intersections between horizontal and vertical
for h in H:
    for v in V:
        k = intersect(h, v)
        if not k: continue
        if k not in P: P[k] = set()
        for p in (h[0], h[1], v[0], v[1]): P[p].add(k); P[k].add(p)
        H3[h[0][1]].add(k[0]); H3[h[1][1]].add(k[0])
        V3[v[0][0]].add(k[1]); V3[v[1][0]].add(k[1])

def add(x, y):
    if x not in P: P[x] = set()
    if y not in P: P[y] = set()
    P[x].add(y); P[y].add(x)

# resolve between horizontal-horizontal or vertical-vertical
for A2, A3 in ((V2, V3), (H2, H3)):
    for v, z in A2:
        mz = merge(z)
        dz = sorted(A3[v]); mz = mz[::-1]
        new = []
        for i in range(len(dz)-1):
            while mz and dz[i]>mz[-1][1]: mz.pop()
            if not mz: continue
            if mz[-1][0]<=dz[i]<=dz[i+1]<=mz[-1][1]: new.append(dz[i:i+2])
            else: mz.pop()
        z.clear(); z.extend(new)

# resolve adjacent horizontal lines and adjacent vertical lines
for A2, A3 in ((V2, V3), (H2, H3)):
    for t in (1, -1):
        for i in range(len(A2)-1):
            if A2[i][0] != A2[i+1][0]-t: continue
            B = set()
            dz = sorted(A3[A2[i][0]]|A3[A2[i+1][0]]); mz = A2[i+1][1][::-1]; new = []
            for j in range(len(dz)-1):
                while mz and dz[j]>mz[-1][1]: mz.pop()
                if not mz: continue
                if mz[-1][0]<=dz[j]<=dz[j+1]<=mz[-1][1]: new.append((dz[j], dz[j+1]))
                elif dz[j]>mz[-1][0]: mz.pop()
            for a, b in new: A3[A2[i+1][0]].add(a); A3[A2[i+1][0]].add(b)
            A2[i+1] = (A2[i+1][0], new)
        A2.reverse()
for i in range(len(V2)-1):
    if V2[i][0] != V2[i+1][0]-1: continue
    for j in V3[V2[i][0]]&V3[V2[i+1][0]]: add((V2[i][0], j), (V2[i+1][0], j))
for i in range(len(H2)-1):
    if H2[i][0] != H2[i+1][0]-1: continue
    for j in H3[H2[i][0]]&H3[H2[i+1][0]]: add((j, H2[i][0]), (j, H2[i+1][0]))

# do H-H and V-V again
for v, mz in H2:
    for a, b in mz: add((a, v), (b, v))
for v, mz in V2:
    for a, b in mz: add((v, a), (v, b))

if any(int(u)%2 for u in c if u.isdigit()): # TODO: resolve last TC group??
    S = V+H
    for _ in range(2):
        for a, b in [*P]:
            for p, q in K:
                for s in S:
                    k = intersect(s, ((a, b), (a+p, b+q)))
                    if k:
                        if type(k[0]) != tuple and k == (a+p, b+q): add(k, (a, b))
                        elif type(k[0]) == tuple: add(k[0], (a, b)); add(k[1], (a, b))
        for i in P: P[i].discard(i)
for i in P: P[i].discard(i)

from heapq import *
F = {e:i for i,e in enumerate(K)}
D = {(x, y, F[(dx, dy)]): (0, 0, None, None, None)}; Q = [(0, 0, -1, -1, x, y, F[(dx, dy)])]
while Q:
    d, t, px, py, x, y, dd = heappop(Q)
    if x==y==0: break
    for x2, y2 in P[(x, y)]:
        p = F[(sgn(x2-x), sgn(y2-y))]
        new = (d+abs(x2-x)+abs(y2-y), t+(p!=dd))
        if (tt:=(x2, y2, p)) not in D or D[tt][:2] > new: D[tt] = (*new, x, y, dd); heappush(Q, (*new, x, y, *tt))
Z = []; x = y = 0; W = []
i = min((D[(x, y, i)], i) for i in range(4) if (x, y, i) in D)[1]
while x != None: Z.append((x, y)); _, _, x, y, i = D[(x, y, i)]
x, y = Z.pop()
while Z:
    x2, y2 = Z.pop()
    ddx, ddy = sgn(x2-x), sgn(y2-y)
    if (ddx-dx)*(ddy-dy) == 0:
        if ddx-dx != ddy-dy: W.append('U')
    elif (ddx, ddy) == (-dy, dx): W.append('<')
    else: W.append('>')
    W.append(abs(x2-x)+abs(y2-y))
    x, y = x2, y2; dx, dy = ddx, ddy
W.append('exit'); X = []
for i in W:
    if X and type(X[-1]) == int and type(i) == int: X[-1] += i
    else: X.append(i)
print(' '.join(map(str, X)))