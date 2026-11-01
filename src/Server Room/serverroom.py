from array import *
R, C = map(int, input().split()); MOD = 998244353
M = [[*map(int, input())] for _ in range(R)]
if R < C: R, C = C, R; M = [*map(list, zip(*M))]
M = array('B', sum(M, []))
D = array('i', [-1])*2**C; D[0] = 0
W = array('i', [-1])*2**C; W[0] = 1
E = array('i', [-1])*2**C; D[0] = 0
X = array('i', [-1])*2**C; W[0] = 1
for r in range(R):
    for c in range(C):
        B = 1<<c; u = r*C+c
        for i in range(1<<C): E[i] = X[i] = -1
        for bm in range(1<<C):
            if D[bm]<0: continue
            v = D[bm]; w = W[bm]
            if M[u] < 2:
                if v > E[nm:=bm&~B]: E[nm] = v; X[nm] = w
                elif v == E[nm]: X[nm] = (X[nm]+w)%MOD
            if M[u]:
                if (c>0)*(bm&(B>>1))<1>bm&B:
                    nm = bm|B; v2 = v+2-M[u]
                    if v2 > E[nm:=bm|B]: E[nm] = v2; X[nm] = w
                    elif v2 == E[nm]: X[nm] = (X[nm]+w)%MOD
        for i in range(1<<C): D[i] = E[i]; W[i] = X[i]
Y = Z = 0
for v, w in zip(D, W):
    if v > Y: Y = v; Z = w
    elif v == Y: Z = (Z+w)%MOD
print(Y, Z)