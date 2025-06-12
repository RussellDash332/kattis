n, m = map(int, input().split())
l = float(input())
if l <= n+m:
    hi, lo = 1, 0
    while abs(hi-lo)>1e-7:
        mi = (hi+lo)/2; x, y = n/2*mi+n*(1-mi), m/2*mi
        if (x*x+y*y)**.5 + ((n-x)**2+(m-y)**2)**.5 > l: lo = mi
        else: hi = mi
    print(3); print(0, 0); print(x, y); print(n, m); exit()
p = [(0, 0), (n, 0)]; l -= n+m
while l > 0:
    x, y = p[-1]; t = min(l, 2*x); l -= t
    p.append((x, y+1)); p.append((x-t/2, y+1)); p.append((x-t/2, y+2)); p.append((x, y+2))
if p[-1] != (n, m): p.append((n, m))
print(len(p))
for i in p: print(*i)