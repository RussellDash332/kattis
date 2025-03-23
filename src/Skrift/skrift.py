import sys; input = sys.stdin.readline
n, m, q = map(int, input().split())
R = []; p = s = t = 0; F = {}; E = []
for _ in range(m): a, b = map(int, input().split()); R.append((b, a))
for _ in range(q):
    x, y = map(int, input().split())
    if x%2:
        if p not in F: F[p] = 0
        if p+y not in F: F[p+y] = 0
        F[p] += 1; F[p:=p+y] -= 1
    else: p -= y
for k, v in sorted(F.items()):
    if k-t: E.append((s-1, k-t))
    t = k; s += v
l = r = x = y = z = 0; E.sort(); R.sort()
while l < len(E) and r < len(R):
    e, f = E[l]; u, v = R[r]
    wl = max(x, y); wr = min(x+f, y+v); z += (wr-wl)*e*u
    if x+f < y+v: x += f; l += 1
    else: y += v; r += 1
print(z)