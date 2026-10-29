def f(x):
    l, z = -1e9, 0
    for lo, hi in sorted((cy-(r*r-(cx-x)**2)**.5, cy+(r*r-(cx-x)**2)**.5) for r, cx, cy in C if abs(x-cx)<r): l = max(l, lo); z += max(0, hi-l); l = max(l, hi)
    return z
def g(l, r, fl, fm, fr):
    return (fl+4*fm+fr)/6*(r-l)
def simpson(l, r):
    fl = f(l); fm = f(m:=(l+r)/2); fr = f(r)
    s, sl, sr = g(l, r, fl, fm, fr), g(l, m, fl, f((l+m)/2), fm), g(m, r, fm, f((m+r)/2), fr)
    if abs(s-sl-sr) < EPS: return sl+sr
    return simpson(l, m)+simpson(m, r)
C = []; EPS = 1e-9
for _ in range(int(input())): r, x, y = map(float, input().split()); C += [(r, x, y)]
z = sorted({v for r, x, y in C for v in (x-r, x+r)})
print(sum(simpson(*p) for p in zip(z, z[1:])))