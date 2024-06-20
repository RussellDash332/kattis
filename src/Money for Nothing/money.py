import os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline; from bisect import *; from array import *
X = 10**9+7; m, n = map(int, input().split()); Mx = array('i'); My = array('i'); Nx = array('i'); Ny = array('i'); M0 = []; N0 = []
for _ in range(m): x, y = map(int, input().split()); M0.append(x*X+y)
for _ in range(n): x, y = map(int, input().split()); N0.append(x*X+y)
M0.sort(); N0.sort()
for i in range(m):
    if not Mx or My[-1] > M0[i]%X: Mx.append(M0[i]//X); My.append(M0[i]%X)
if len(Mx) == 0: print(0), exit(0)
for i in range(n-1, -1, -1):
    if (N0[i]//X >= Mx[0] and N0[i]%X >= My[-1]) and (not Nx or Ny[-1] < N0[i]%X): Nx.append(N0[i]//X); Ny.append(N0[i]%X)
Nx = Nx[::-1]; Ny = Ny[::-1]; m = len(Mx); n = len(Nx); Z = [0]
def f(k): return (Nx[k]-Mx[i])*(Ny[k]-My[i])>(Nx[k]-Mx[z:=Z[bisect(Z, k*X+m)-1]%X])*(Ny[k]-My[z])
for i in range(1, m):
    lo, hi = 0, n
    while lo < hi:
        if f(mi:=(lo+hi)//2): hi = mi
        else: lo = mi+1
    p = bisect_left(Z, lo*X)
    while len(Z) != p: Z.pop()
    Z.append(lo*X+i)
try: print(max((Nx[i]-Mx[z])*(Ny[i]-My[z]) for i in range(n) if Nx[i] >= Mx[z:=Z[bisect(Z, i*X+m)-1]%X] and Ny[i] >= My[z]))
except: print(0)