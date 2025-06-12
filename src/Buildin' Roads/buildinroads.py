import os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline; from math import gcd
def find(i):
    if Up[i] == i: return i
    Up[i] = find(Up[i]); return Up[i]
def union(i, j):
    if (x:=find(i)) != (y:=find(j)):
        if Ur[x] > Ur[y]: Up[y] = x
        else: Up[x] = y; Ur[y] += Ur[x] == Ur[y]
N, M = map(int, input().split()); E = []; Up = [*range(N)]; Ur = [0]*N; n = N; P = G = 0
for _ in range(M): u, v, p, g = map(int, input().split()); E.append((u-1, v-1, p, g))
for u, v, p, g in E:
    if n == 1: break
    if find(u) != find(v): P += p; G += g; union(u, v); n -= 1
lo = 0; hi = P/G; Z = (P, G)
while abs(lo-hi) > 1e-5:
    X = (lo+hi)/2; Up = [*range(N)]; Ur = [0]*N; n = N; P = G = 0
    for u, v, p, g in sorted(E, key=lambda x: x[2]-X*x[3]):
        if n == 1: break
        if find(u) != find(v): P += p; G += g; union(u, v); n -= 1
    if P >= X*G: lo = X; Z = (P, G)
    else: hi = X
x, y = Z; d = gcd(x, y); print(f'{x//d}/{y//d}')