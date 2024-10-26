import sys
from bisect import *
from array import *
C, R = map(int, sys.stdin.readline().split())
M = [*sys.stdin]; G = [array('i') for _ in range(R*C)]

for i in range(1, R-1):
    A = array('i')
    for j in range(C):
        if M[i][j] == 'M': X = C*i+j
        if M[i][j] != '_': A.append(j)
    for j in range(1, C-1):
        if M[i][j] != '#': nx = A[bisect(A, j)]; G[C*i+nx-(M[i][nx]=='#')].append(C*i+j)
    A = array('i')
    for j in range(C, -1, -1):
        if M[i][j] != '_': A.append(-j)
    for j in range(C-2, 0, -1):
        if M[i][j] != '#': nx = -A[bisect(A, -j)]; G[C*i+nx+(M[i][nx]=='#')].append(C*i+j)
for j in range(1, C-1):
    A = array('i')
    for i in range(R):
        if M[i][j] != '_': A.append(i)
    for i in range(1, R-1):
        if M[i][j] != '#': nx = A[bisect(A, i)]; G[C*(nx-(M[nx][j]=='#'))+j].append(C*i+j)
    A = array('i')
    for i in range(R-1, -1, -1):
        if M[i][j] != '_': A.append(-i)
    for i in range(R-2, 0, -1):
        if M[i][j] != '#': nx = -A[bisect(A, -i)]; G[C*(nx+(M[nx][j]=='#'))+j].append(C*i+j)

D = array('i', [-1]*R*C); D[X] = 0; Q = array('i', [X])
for u in Q:
    for v in G[u]:
        if D[v] == -1: D[v] = D[u]+1; Q.append(v)
print(*D)