class UFDS:
    def __init__(s, n):
        s.p = [-1]*n; s.o = []; s.c = [[] for i in range(n)]
    def find(s, u):
        while s.p[u] > -1: u = s.p[u]
        return u
    def union(s, u, v):
        if (u:=s.find(u)) != (v:=s.find(v)):
            if s.p[u] > s.p[v]: u, v = v, u
            s.o.append((v, s.p[v])); s.p[u] += s.p[v]; s.p[v] = u; s.c[u].append(v)
        else: s.o.append(None)
    def undo(s):
        if not s.o: return
        if s.o[-1]: v, x = s.o.pop(); s.c[s.p[v]].pop(); s.p[s.p[v]] -= x; s.p[v] = x
        else: s.o.pop()
    def child(s, p):
        q = [p]
        for u in q: sys.stdout.write(str(u)+' '); q.extend(s.c[u])
import sys; input = sys.stdin.readline
N, Q = map(int, input().split()); U = UFDS(N+1)
for _ in range(Q):
    c, *x = input().split()
    if c == 'j': U.union(*map(int, x))
    elif c == 'u': U.undo()
    else: U.child(U.find(int(x[0]))); sys.stdout.write('\n')