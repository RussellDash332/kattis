import sys; input = sys.stdin.readline
from collections import *
K = ((0, -1), (0, 1), (1, 0), (-1, 0), (1, -1), (-1, 1), (-1, -1), (1, 1))
# . @
while 1:
    R, C = map(int, input().split())
    if R*C < 1: break
    M = [input() for _ in range(R)]
    D = [10**9]*R*C; Q = deque()
    for i in range(R):
        if M[i][0]<'@': (Q.appendleft, Q.append)[v:=M[i][0]>'#'](i*C); D[i*C] = int(v)
    for i in range(1, C):
        if M[R-1][i]<'@': (Q.appendleft, Q.append)[v:=M[R-1][i]>'#']((R-1)*C+i); D[(R-1)*C+i] = int(v)
    while Q:
        r, c = divmod(p:=Q.popleft(), C)
        for dr, dc in K:
            if R>r+dr>-1<c+dc<C and M[r+dr][c+dc]<'@' and D[u:=(r+dr)*C+c+dc] > 10**8: (Q.appendleft, Q.append)[v:=M[r+dr][c+dc]>'#'](u); D[u] = D[p]+v
    Z = min(min(D[:C]), min(D[C-1::C])); print(Z if Z < 10**8 else -1)