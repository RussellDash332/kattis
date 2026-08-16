import sys; input = sys.stdin.readline; from array import *
R, C = map(int, input().split())
M = array('I', [i*C+j for i in range(R) for j, x in enumerate(input()) if x == '#'])
H = array('i', [-1]*R*C)
for i in range(N:=len(M)): H[M[i]] = i
for k in range(int(N**.5)+1, 1, -1):
    if N%(k*k) < 1:
        Z = 0; T = array('B', [0]*N)
        for x in M:
            if T[H[x]] or x//C > R-k or x%C > C-k: continue
            for i in range(k):
                for j in range(k):
                    u = H[x+i*C+j]
                    if u < 0 or T[u]: Z = 1; break
                    T[u] = 1
                if Z: break
        if 1-Z and all(T): print(k); exit()
print(1)