import sys, os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline; from array import *
N = int(input()); C = array('I', [1]); P = array('i', map(int, input().split())); L = array('I', (P[2*i+1]-P[2*i]+1 for i in range(N))); G = [(i^(i>>1)) for i in range(1<<N)]; H = {1<<i:i for i in range(N)}; X = array('I', (H[G[i]^G[i+1]]*2+(G[i]<G[i+1]) for i in range((1<<N)-1))); O = array('I')
for i in L: C.append(C[-1]*i)
D = array('I', [0]*C[-1])
for _ in range(int(input())):
    v = 0
    for i, x in enumerate(map(int, input().split())): v += C[i]*(x-P[2*i])
    D[v] += 1
for j in range(N):
    for i in range(C[j], C[-1]):
        if i//C[j]%L[j]: D[i] += D[i-C[j]]
    L[j] -= 1
for _ in range(int(input())):
    R = array('l', map(int, input().split())); A = array('l', (max(R[2*i]-P[2*i], 0)*C[i] for i in range(N))); B = array('l', (min(L[i], R[2*i+1]-P[2*i])*C[i] for i in range(N))); E = array('l', (A[i]-B[i]-C[i] for i in range(N)))
    if any(A[i]>B[i] for i in range(N)): O.append(0); continue
    Z = D[idx:=sum(B)]; z = m = 0
    for dx in X:
        m ^= 1; d = dx>>1
        if dx&1: idx += E[d]; z += A[d]==0
        else:    idx -= E[d]; z -= A[d]==0
        if z == 0: Z -= D[idx] if m else -D[idx]
    O.append(Z)
sys.stdout.write('\n'.join(map(str, O)))