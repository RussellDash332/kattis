N, T = map(int, input().split())
P = [[*map(float, input().split())] for _ in range(N)]; Z = 0
def f(z): return sum(max(0, (z-b)/2/a) for a, b, c in P) <= T
lo, hi = -1e4, max(b for a, b, c in P)
while abs(lo-hi)>1e-8:
    if f(mi:=(lo+hi)/2): hi = mi
    else: lo = mi
for a, b, c in P: t = max(0, (mi-b)/2/a); Z += a*t*t+b*t+c
print(Z/N)