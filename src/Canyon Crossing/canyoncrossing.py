import sys; input = sys.stdin.readline; from collections import *; from array import *
R, C, B = map(int, input().split()); M = array('i'); K = ((-1, 0), (0, -1), (0, 1), (1, 0))
for _ in range(R): M.extend(map(int, input().split()))

def f(x):
    D = array('i', [-1]*R*C); Q = deque((R-1)*C+i for i in range(C-1, -1, -1) if M[-C+i] >= x)
    for i in Q: D[i] = 0
    for i in range(C-1, -1, -1):
        if M[-C+i] < x: Q.append((R-1)*C+i); D[-C+i] = 1
    while Q:
        rc = Q.popleft()
        if rc < C: return D[rc] <= B
        if D[rc] > B: return 0
        r = rc//C; c = rc%C
        for dr, dc in K:
            if R>r+dr>-1<c+dc<C:
                p = (r+dr)*C+c+dc
                if D[p] != -1: continue
                if M[p] >= x: Q.appendleft(p); D[p] = D[rc]
                else: Q.append(p); D[p] = D[rc]+1

lo, hi = min(M), max(M)
while hi-lo>1:
    mi = (lo+hi)//2
    if f(mi): lo = mi
    else: hi = mi-1
print(hi if f(hi) else hi-1)