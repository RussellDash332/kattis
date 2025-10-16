from bisect import *; from array import *
def lds(A):
    B = []; D = []
    for e in A:
        e = -e; p = bisect(B, e-1)
        if p == len(B): B.append(e)
        else: B[p] = e
        D.append(len(B))
    return D
m = int(input()); a = [*map(int, input().split())]; b = [*map(int, input().split())]; n = m+1
M = array('i', [-1]*n*n); M[-1] = 0; D = []
for i in range(m): M[m*n+i] = b[i]; M[i*n+m] = a[i]
for i in range(m-1, -1, -1): D.append((m-1, i))
for i in range(m-2, -1, -1): D.append((i, 0))
for r, c in D:
    L = []; p, q = r, c+1
    while 0<=p<=m and 0<=q<=m: L.append(M[p*n+q]); p -= 1; q += 1
    D = lds(A:=L[::-1]+[M[(r+1)*n+c]]); E = lds(A[::-1]); x = 0
    for _ in range(len(L)): M[r*n+c] = max(D[-x-2], E[x])+M[(r+1)*n+c+1]; r -= 1; c += 1; x += 1
print(M[0])