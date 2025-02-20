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
                elif i1:                    return None # was (i1, i2)
                else:                       return None
import sys; input = sys.stdin.readline
def f(p, t): return p[0]*t+p[1]
N = int(input()); P = []; H = []
for _ in range(N): x, y = map(int, input().split()); P.append((x-y, y))
S = ((0, f(P[0], 0)), (1, f(P[0], 1))); U = T = E = 0; K = {}; H = N-1; L = 0
for i in range(1, N):
    k = intersect(((0, f(P[i], 0)), (1, f(P[i], 1))), S)
    if k == None:
        if P[i][1] > P[0][1]: U += 1
        elif P[i][1] == P[0][1]: T += 1
        continue
    E += f(P[i], -1e-8)>f(P[0], -1e-8)
    if k[0] not in K: K[k[0]] = [0, 0]
    K[k[0]][f(P[i], k[0]-1e-8)>f(P[0], k[0]-1e-8)] += 1
for x in sorted(K): H = min(H, E-K[x][1]+U); L = max(L, E+U+T+K[x][0]); E += K[x][0]-K[x][1]
H = min(H, E+U); L = max(L, E+U+T); print(max(H, 0)+1, min(L+1, N))