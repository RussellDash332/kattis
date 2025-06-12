import os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline; from array import *
class UFDS:
    def __init__(s, c): s.p = [*range(len(c))]; s.r = [0]*len(c); s.c = c
    def find(s, i):
        if s.p[i] == i: return i
        s.p[i] = s.find(s.p[i]); return s.p[i]
    def union(s, i, j):
        if (x:=s.find(i)) == (y:=s.find(j)): return y
        if s.r[x] > s.r[y]: s.p[y] = x; s.c[x] |= s.c[y]; return x
        else: s.p[x] = y; s.r[y] += s.r[x] == s.r[y]; s.c[y] |= s.c[x]; return y
q = int(input()); n, m = map(int, input().split()); Q = []; H = {}; C = array('b'); M = 10**9+7
for _ in range(q):
    x1, y1, x2, y2 = map(int, input().split())
    if (x1, y1) > (x2, y2): x1, y1, x2, y2 = x2, y2, x1, y1
    if y1 == y2 and x1*M+y1-1 not in H: H[x1*M+y1-1] = len(H); C.append((y1==m)+2*(y1==0))
    elif x1 == x2 and (x1-1)*M+y1 not in H: H[(x1-1)*M+y1] = len(H); C.append((x1==0)+2*(x1==n))
    if x1*M+y1 not in H: H[x1*M+y1] = len(H); C.append((y1==y2==m)+2*(x1==x2==n))
    Q.append((H[(x1-(x1==x2))*M+y1-(y1==y2)], H[x1*M+y1]))
U = UFDS(C); T = 0
for u, v in Q:
    T += 1
    if U.c[U.union(u, v)] == 3: print(T); exit()
print(-1)