class UFDS:
    def __init__(s, N): s.p = [*range(N)]; s.c = [[] for _ in range(N)]
    def find(s, i):
        if s.p[i] == i: return i
        s.p[i] = s.find(s.p[i]); return s.p[i]
    def union(s, i, j): s.p[j:=s.find(j)] = (i:=s.find(i)); s.c[i].append(j)
    def balkan(s, i):
        while s.c[i]: s.balkan(s.c[i].pop())
        s.p[i] = i
import sys; input = sys.stdin.readline
n, q = map(int, input().split()); U = UFDS(n+1)
for _ in range(q):
    c, *x = input().split()
    if c == 'c': print(U.find(int(x[0])))
    elif c == 'a': U.union(*map(int, x))
    else: U.balkan(U.find(int(x[0])))