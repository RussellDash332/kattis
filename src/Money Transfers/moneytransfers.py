import sys; input = sys.stdin.readline
from heapq import *

# linesegmentintersection
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
            x, y = (b*f-c*e)/det, (c*d-a*f)/det
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

INF = 10**14
n, p, s, t = map(int, input().split())
s -= 1; t -= 1
g = [{} for _ in range(n)]
for _ in range(p):
    u, v, w = map(int, input().split())
    u -= 1; v -= 1
    for _ in range(2):
        if v not in g[u]: g[u][v] = w
        g[u][v] = min(g[u][v], w); u, v = v, u
b = [0]*n; _ = int(input())
for i in map(int, input().split()): b[i-1] = 1

# Prioritize base cost, what's the maximum step needed
D1 = [[(INF, INF), (INF, INF)] for _ in range(n)]
D1[s] = [(INF, INF), (0, 0)]
pq = [(D1[s][1], s, 1)]
while pq:
    de, vv, bb = heappop(pq)
    if de == D1[vv][bb]:
        dd, ee = de
        for nn in g[vv]:
            bb2 = bb*b[nn]
            if D1[nn][bb2] > (new:=(dd+g[vv][nn], ee+1)):
                D1[nn][bb2] = new
                heappush(pq, (D1[nn][bb2], nn, bb2))

# Dijkstra to find the SP that uses n edges for n = 1, 2, ..., LIM
# Now prioritize edges used
LIM = max(D1[t][0][1], D1[t][1][1])
if LIM == INF: LIM = 1
D2 = [[[INF]*(LIM+1) for _ in range(2)] for _ in range(n)]
D2[s][1][0] = 0
pq = [(0, D2[s][1][0], s, 1)]
while pq:
    ee, dd, vv, bb = heappop(pq)
    if ee >= LIM: break
    if dd == D2[vv][bb][ee]:
        for nn in g[vv]:
            bb2 = bb*b[nn]
            if D2[nn][bb2][ee+1] > (new:=dd+g[vv][nn]):
                D2[nn][bb2][ee+1] = new
                heappush(pq, (ee+1, new, nn, bb2))
wn1, wn2 = [], []
for i in range(LIM+1):
    if D2[t][0][i] != INF: wn1.append((D2[t][0][i], i))
    if D2[t][1][i] != INF: wn2.append((D2[t][1][i], i))

#print(f'min({", ".join([str(w)+"+"+str(n)+"x" for w,n in wn1])}) > min({", ".join([str(w)+"+"+str(n)+"x" for w,n in wn2])})')

# Somehow somewhat destination is not reachable
if not wn1 or not wn2: print('Impossible'), exit(0)

# Obvious case
if wn2[0][1] < wn1[0][1] or (wn2[0][1] == wn1[0][1] and wn2[0][0] < wn1[0][0]): print('Infinity'), exit(0)

# Find intersection of piecewise functions
cuts1, cuts2 = {-INF, INF}, {-INF, INF}
for i in range(len(wn1)-1):
    w1, n1 = wn1[i]
    for j in range(i+1, len(wn1)):
        w2, n2 = wn1[j]
        cuts1.add((w1-w2)/(n2-n1))
for i in range(len(wn2)-1):
    w1, n1 = wn2[i]
    for j in range(i+1, len(wn2)):
        w2, n2 = wn2[j]
        cuts2.add((w1-w2)/(n2-n1))
cuts1, cuts2 = sorted(cuts1), sorted(cuts2)
segments1 = [((cuts1[i-1], min(w+n*cuts1[i-1] for w,n in wn1)), (cuts1[i], min(w+n*cuts1[i] for w,n in wn1))) for i in range(1, len(cuts1))]
segments2 = [((cuts2[i-1], min(w+n*cuts2[i-1] for w,n in wn2)), (cuts2[i], min(w+n*cuts2[i] for w,n in wn2))) for i in range(1, len(cuts2))]
best = 0
for s1 in segments1:
    for s2 in segments2:
        its = intersect(s1, s2)
        if its == None: continue
        v, v2 = its
        if type(v) == tuple: v = v2[0]
        for C in range(round(v)-1, round(v)+1):
            if min(w+n*C for w,n in wn1) > min(w+n*C for w,n in wn2): best = max(best, C)
print(best if best else 'Impossible')