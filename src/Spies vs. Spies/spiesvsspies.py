N, Q = map(int, input().split())
P = []; V = [0]*N
U = {}; L = {}; R = {}; D = {}
for i in range(N):
    x, y = map(int, input().split())
    P += [(x, y)]
    if x not in U: U[x] = []; D[x] = []
    if y not in L: L[y] = []; R[y] = []
    U[x] += [(y, i)]; D[x] += [(-y, i)]; L[y] += [(-x, i)]; R[y] += [(x, i)]
for x in U: U[x].sort(); D[x].sort()
for y in L: L[y].sort(); R[y].sort()
K = (U, D, L, R)
from bisect import *
for _ in range(Q):
    c, d = input().split()
    c = int(c)-1; d = 'NSWE'.index(d)
    if V[c]: print('ignore'); continue
    x, y = P[c]; t = bisect(v:=K[d][(y, x)[d<2]], (y, -y, -x, x)[d], key=lambda x: x[0]); z = []
    while len(v) > t:
        _, k = v.pop()
        if V[k]<1: V[k] = 1; z += [k+1]
    print(len(z), *z[::-1])