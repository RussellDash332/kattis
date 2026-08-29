class UFDS:
    def __init__(s, N):
        s.p = [*range(N)]; s.r = [0]*N; s.n = N
    def find(s, i):
        if s.p[i] == i: return i
        s.p[i] = s.find(s.p[i])
        return s.p[i]
    def union(s, i, j):
        if (x:=s.find(i)) != (y:=s.find(j)):
            s.n -= 1
            if s.r[x] > s.r[y]: s.p[y] = x
            else: s.p[x] = y; s.r[y] += s.r[x] == s.r[y]
import sys; input = sys.stdin.readline
n, m, l = map(int, input().split())
el = []; mst = W = 0; u = UFDS(n)
for _ in range(m): a, b, w = map(int, input().split()); el += [(w, a-1, b-1)]; W += w*(_<l)
for w, a, b in sorted(el):
    if u.find(a) != u.find(b): u.union(a, b); mst += w
print('im'*(mst>W or u.n>1)+'possible')