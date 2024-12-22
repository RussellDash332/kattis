from heapq import *
N, *H = map(int, open(0).read().split()); H = sorted(H)[::-1]

def f(x, n):
    Q = [(0, 1)]*n; z = w = 0
    for h in H:
        if not Q or h+Q[0][0] > x: return 10**18
        u, d = heappop(Q); z = max(z, u+h); w += d
        if d: heappush(Q, (u+h, 0))
    return z*w

Z = 10**18
for n in range(N//2, N+1):
    a, b = H[0], 2*H[0]
    while b-a>2:
        if f(μ:=b-(b-a)//3, n) > f(λ:=a+(b-a)//3, n): b = μ
        else: a = λ
    Z = min(Z, min(f(x, n) for x in range(a-2, b+3)))
print(66*Z) # N ternary searches better than 2-layered ternary search