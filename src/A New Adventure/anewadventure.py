import sys; input = sys.stdin.readline; K = ((-1, -1), (0, -2), (0, -1), (1, -1)); from collections import *; from array import *; R, C = map(int, input().split()); M = [input().strip() for _ in range(R)]; D = array('i', [-1]*R*C); Q = deque([0]); D[0] = 0
while Q:
    rc = Q.popleft(); r, c = divmod(rc, C)
    if r == R-1: print(D[rc]+1), exit(0)
    for dr, dc in K:
        if r+dr>-1 and M[r+dr][(c+dc)%C]<'M'>M[r+dr][(c+dc+1)%C] and D[p:=(r+dr)*C+(c+dc)%C] < 0: Q.append(p); D[p] = D[rc]+1
print(-1)