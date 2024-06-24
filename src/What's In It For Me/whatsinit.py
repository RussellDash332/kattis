import sys; input = sys.stdin.readline; from array import *

def dp(i, p, s):
    if s > 100: return 0
    if i == N: return s == 100
    if D[(x:=10201*i+101*p+s)] != -1: return D[x]
    D[x] = 0; lo, hi = divmod(S[i], 101)
    for v in range(lo, min(hi, p)+1):
        if dp(i+1, v, s+v): D[x] = 1; M[i] = 101*min(M[i]//101, v)+max(M[i]%101, v)
    return D[x]

S = []; M = []; E = []; N = int(input()); D = array('b', [-1]*N*101*101)
for i in range(N):
    s, p = input().strip().split(); E.append(s)
    if p != '?': S.append(102*int(p))
    else: S.append(100)
    M.append(10100)
dp(0, 100, 0)
for i in range(N): print(E[i], *divmod(M[i], 101))