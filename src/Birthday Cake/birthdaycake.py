def its(a, b, c, d, e, f):
    det = b*d-a*e
    if det: return (b*f-c*e)/det, (c*d-a*f)/det
n, m, r = map(int, input().split()); p = []; l = []; v = set()
for _ in range(n): x, y = map(int, input().split()); p.append((x, y))
for _ in range(m): a, b, c = map(int, input().split()); l.append((a, b, -c))
for a, b, c in l:
    for d, e, f in l:
        k = its(a, b, c, d, e, f)
        if k:
            x, y = k
            if x*x+y*y < r*r: v.add(k)
if n != m+len(v)+1: print('no'); exit()
for x1, y1 in p:
    for x2, y2 in p:
        if (x1, y1) <= (x2, y2): continue
        ok = 0
        for a, b, c in l:
            if (a*x1+b*y1-c)*(a*x2+b*y2-c) < 0: ok = 1; break
        ok or print('no')<exit()
print('yes')