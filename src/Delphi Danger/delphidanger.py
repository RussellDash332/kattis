import sys; input = sys.stdin.readline
class UFDS:
    def __init__(s, N):
        s.p = [*range(N)]; s.r = [0]*N; s.s = [1]*N
    def find(s, i):
        if s.p[i] == i: return i
        s.p[i] = s.find(s.p[i])
        return s.p[i]
    def union(s, i, j):
        if (x:=s.find(i)) != (y:=s.find(j)):
            if s.r[x] > s.r[y]: s.p[y] = x; s.s[x] += s.s[y]
            else: s.p[x] = y; s.r[y] += s.r[x] == s.r[y]; s.s[y] += s.s[x]
N, M = map(int, input().split()); Q = {}; Z = 0; U = UFDS(N+1)
for _ in range(M): a, b, t = map(int, input().split()); Q.setdefault(-t, []).append((a, b))
for t in sorted(Q):
    M = {}; C = {}
    for a, b in Q[t]:
        if (a:=U.find(a)) == (b:=U.find(b)): print('impossible'); exit()
        if a not in M: M[a] = []
        if b not in M: M[b] = []
        M[a] += [b]; M[b] += [a]
    for i in M:
        if i not in C:
            q = [i]; C[i] = 0
            for u in q:
                for v in M[u]:
                    if v not in C: C[v] = C[u]^1; q += [v]
                    elif C[v]==C[u]: print('impossible'); exit()
            Z += min(x:=sum(U.s[j] for j in q if C[j]), sum(U.s[j] for j in q)-x)
    for a, b in Q[t]: U.union(a, b)
print('possible', Z)