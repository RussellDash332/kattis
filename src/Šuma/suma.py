import os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
from math import *
from collections import *
class UFDS:
    ans = 1; records = []
    def __init__(s, N):
        s.p = [-1]*N # at representative: size of set, otherwise: ptr to parent
    def find(s, i, to_undo=0):
        if s.p[i] < 0: return i
        if to_undo: s.records.append((i, s.p[i]))
        s.p[i] = s.find(s.p[i], to_undo)
        return s.p[i]
    def union(s, i, j, to_undo=0):
        if (x:=s.find(i, to_undo)) != (y:=s.find(j, to_undo)):
            if s.p[x] > s.p[y]: x, y = y, x
            if to_undo: s.records.append((x, s.p[x])), s.records.append((y, s.p[y]))
            s.p[x] += s.p[y]; s.p[y] = x; s.ans = max(s.ans, -s.p[x])
def norm(dh, dv):
    if dh*dv < 0: return -1
    return dh/dv
N = int(input()); U = UFDS(N*N); T = defaultdict(list)
H = [[*map(int, input().split())] for _ in range(N)]
V = [[*map(int, input().split())] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i < N-1: # down
            if H[i][j] == H[i+1][j] and V[i][j] == V[i+1][j]: U.union(i*N+j, i*N+j+N)
            elif V[i][j] != V[i+1][j] and (t:=norm(H[i][j]-H[i+1][j], V[i+1][j]-V[i][j])) != -1: T[t].append((i*N+j, i*N+j+N))
        if j < N-1: # right
            if H[i][j] == H[i][j+1] and V[i][j] == V[i][j+1]: U.union(i*N+j, i*N+j+1)
            elif V[i][j] != V[i][j+1] and (t:=norm(H[i][j]-H[i][j+1], V[i][j+1]-V[i][j])) != -1: T[t].append((i*N+j, i*N+j+1))
for t in T:
    for src, dst in T[t]: U.union(src, dst, 1)
    while U.records: a, b = U.records.pop(); U.p[a] = b
print(U.ans)