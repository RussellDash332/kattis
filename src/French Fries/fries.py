import os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline; from math import *; from array import *
W = 27500
P, T, L = map(float, input().split()); P = round(P); T = round(T); X = array('I', map(int, input().split()))
Z = array('f', [0]*(10**7+2*W+5)); D = array('f', [0]*(W//2+3))
for i in range(min((T+1)//2, W//2)+1): D[i] = exp(lgamma(T+1)-lgamma(T//2+i+1)-lgamma((T+1)//2-i+1)-T*log(2))
K = tuple((w, D[(abs(w)+1)//2]) for w in range(-W-T%2, W+1, 2) if D[(abs(w)+1)//2]); M = 5/4; Gp = array('f'); Go = array('I')
for k in range(len(D)):
    if 4*M/5 > D[k]: Gp.append(M:=D[k]); Go.append(k)
if len(K) < 2*len(Gp):
    for x in X:
        for w, v in K: Z[x+w] += v
    print(sum(i>=L for i in Z))
else:
    G = array('f', (Gp[i]-Gp[i-1] for i in range(len(Gp))))
    for i in range(P): X[i] += W
    for x in X:
        for i in range(len(Gp)): Z[x-2*Go[~i+1]] -= G[-i]; Z[x+2*Go[i]-2] += G[i]
        Z[x+2*Go[-1]] -= Gp[-1]
    O = E = z = 0
    for i in range(0, len(Z)-1, 2): z += (E>=L)+(O>=L); E += Z[i]; O += Z[i+1]
    print(z)