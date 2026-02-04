import os, subprocess; from collections import *; from random import *; from bisect import *
def div(n):
    D = [1]
    for k, v in Counter(map(int, subprocess.check_output(f"factor {n}|cut -d':' -f2",shell=True).split())).items():
        d = len(D); p = 1
        for _ in range(v):
            p *= k
            for j in range(d):
                if D[j]*p <= X: L.append([]); L[j].append(len(D)); D.append(D[j]*p)
    return D
def can(p):
    for s in range(bisect(U, d:=S//p)):
        ok = 1; u = U[s]
        for _ in range(p-1):
            if (u:=u+d) not in R: ok = 0; break
        if ok: return 1
c = r = 0; W = []; F = W.append; U = [0]
for i in os.read(0, 1<<22):
    if i > 45: c = c*10+i-48; r = 1
    elif r: F(c); c = r = 0
N, *W = W; M = max(W); S = sum(W); X = min(N, S//M); Z = 0; L = [[]]; V = [1]*(K:=len(P:=div(S)))
for _ in '..':
    for i in W: U.append(U[-1]+i)
R = {*U}
for i in sample(range(K), K):
    if V[i] < 1 or P[i] < Z: continue
    if can(P[i]): Z = max(Z, P[i])
    else:
        Q = [i]; V[i] = 0
        while Q:
            u = Q.pop()
            for v in L[u]:
                if V[v]: V[v] = 0; Q.append(v)
print(N-Z)