import sys; input = sys.stdin.readline

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

def is_lattice(p):
    return abs(p[0]-round(p[0]))<1e-9>abs(p[1]-round(p[1]))

n = int(input()); d = []
for _ in range(n): x, y, r = map(int, input().split()); d.append((x, y, r))
if n == 1:
    if r == 0: print(x, y)
    else: print('uncertain')
    exit(0)
candidates = set()
x1, y1, r1 = d[0]
p1 = [(x1, y1+r1), (x1+r1, y1), (x1, y1-r1), (x1-r1, y1)]
s1 = [(p1[k], p1[(k+1)%4]) for k in range(4)]
x2, y2, r2 = d[1]
p2 = [(x2, y2+r2), (x2+r2, y2), (x2, y2-r2), (x2-r2, y2)]
s2 = [(p2[k], p2[(k+1)%4]) for k in range(4)]
for a in s1:
    for b in s2:
        c = intersect(a, b)
        if c: candidates.add(c)
for i in range(2, n):
    x1, y1, r1 = d[i]
    p1 = [(x1, y1+r1), (x1+r1, y1), (x1, y1-r1), (x1-r1, y1)]
    s1 = [(p1[k], p1[(k+1)%4]) for k in range(4)]
    new_candidates = set()
    for cand in candidates:
        if type(cand[0]) != tuple: # point
            if abs(abs(x1-cand[0])+abs(y1-cand[1])-r1)<1e-9: new_candidates.add(cand)
        else: # segment
            for a in s1:
                b = intersect(cand, a)
                if b: new_candidates.add(b)
    candidates = new_candidates
candidates = {(a, b) for a, b in candidates if (type(a)!=tuple and is_lattice((a, b))) or (type(a)==tuple and is_lattice(a) and is_lattice(b))}
if len(candidates) == 1: print(*map(round, candidates.pop()))
elif len(candidates) > 1: print('uncertain')
else: print('impossible')