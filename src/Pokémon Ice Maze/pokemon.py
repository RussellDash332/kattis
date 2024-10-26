import sys; from array import *
C, R = map(int, sys.stdin.readline().split()); S = array('h')
M = [*sys.stdin]; G = [array('i') for _ in range(R*C)]; K = (1, -1)
for i in range(R*C):
    if M[i//C][i%C] == 'M': X = i
for i in range(1, R-1):
    for t in K:
        for j in range(C)[::t]:
            if M[i][j] != '_':
                nx = j-t*(M[i][j]=='#')
                while S: G[C*i+nx].append(C*i+S.pop())
            if M[i][j] != '#': S.append(j)
for j in range(1, C-1):
    for t in K:
        for i in range(R)[::t]:
            if M[i][j] != '_':
                nx = i-t*(M[i][j]=='#')
                while S: G[C*nx+j].append(C*S.pop()+j)
            if M[i][j] != '#': S.append(i)
D = array('i', [-1]*R*C); D[X] = 0; Q = array('i', [X])
for u in Q:
    for v in G[u]:
        if D[v] == -1: D[v] = D[u]+1; Q.append(v)
for i in D: print(i)