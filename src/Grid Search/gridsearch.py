from collections import *
import sys; input = sys.stdin.readline
ri, ci = map(int, input().split())
pp = [input().strip() for _ in range(ri)]
R, C = map(int, input().split())
s = '`'.join(input().strip() for _ in range(R))
H = []; M = 10**9+7; P = []
for i in range(ri):
    p = 0
    for j in pp[i]: p = (31*p+ord(j))%M
    P.append(p)
X = 0; I = pow(31, ci, M); J = pow(I, ri, M)
for x in P: X = (I*X+x)%M
for i in range(R):
    h = [0]
    for j in range(C): h += [(31*h[-1]+ord(s[i*(C+1)+j]))%M]
    H.append([(h[j+ci]-h[j]*I)%M for j in range(C-ci+1)])
S = [[0]*(C-ci+1) for _ in range(R+1)]
for i in range(R):
    for j in range(C-ci+1): S[i+1][j] = (S[i][j]*I+H[i][j])%M
T = [[(S[i+ri][j]-S[i][j]*J)%M for j in range(C-ci+1)] for i in range(R-ri+1)]; Z = []
for i in range(R-ri+1):
    for j in range(C-ci+1):
        if T[i][j] == X: Z.append((i, j))
F = [[0]*(C+1) for _ in range(R+1)]
for rr, cc in Z: F[rr][cc] += 1; F[rr+ri][cc] -= 1; F[rr][cc+ci] -= 1; F[rr+ri][cc+ci] += 1
print = sys.stdout.write
S = [0]*C
for i in range(R):
    p = 0; rz = []
    for j in range(C): S[j] += F[i][j]
    for j in range(C): rz.append(s[i*-~C+j] if S[j]+p else '.'); p += S[j]
    print(''.join(rz)+'\n')