import sys; input = sys.stdin.readline; from collections import *; from array import *
K = ((-1, 0, 0), (0, -1, 1), (1, 0, 2), (0, 1, 3)); S = [array('i', [0]*(10**6)) for _ in range(12)]
for _ in range(int(input())):
    input(); R, C = map(int, input().split()); M = [[*input().strip()] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if M[i][j] == 'R': s = i*C+j
            if M[i][j] == 'D': e = i*C+j
            M[i][j] = M[i][j] != 'B'
        M[i] = array('b', M[i])
    q = deque((s, i, 0) for i in range(4)); z = -1
    for w in range(12):
        for x in range(R*C): S[w][x] = 0
    while q:
        rc, p, v = q.popleft(); r, c = divmod(rc, C)
        for dr, dc, t in K:
            if t!=(p+2)%4 and (t!=p)+(v!=1) and 0<=(a:=r+dr)<R and 0<=(b:=c+dc)<C and M[a][b]:
                if (n:=a*C+b) == e: z = S[4*v+p][rc] + 1; break
                if S[4*(u:=(v+1)*(p==t))+t][n] == 0: S[4*u+t][n] = S[4*v+p][rc] + 1; q.append((n, t, u))
        if z != -1: break
    print(z)