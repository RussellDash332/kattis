import sys; input = sys.stdin.readline
class UFDS:
    def __init__(s, N):
        s.p = [*range(N)]; s.r = [0]*N; s.s = 0
    def find(s, i):
        if s.p[i] == i: return i
        s.p[i] = s.find(s.p[i])
        return s.p[i]
    def union(s, i, j, w):
        if (x:=s.find(i)) != (y:=s.find(j)):
            if min(s.s[x], s.s[y]) < w: return -1
            if s.r[x] > s.r[y]: s.p[y] = x; s.s[x] += s.s[y]-2*w
            else: s.p[x] = y; s.r[y] += s.r[x] == s.r[y]; s.s[y] += s.s[x]-2*w
            return 1
        return 0
N, M = map(int, input().split()); U = UFDS(N+1)
U.s = [0, *map(int, input().split())]
for _ in range(M): print(['UNNECESSARY', 'BUILT', 'IMPOSSIBLE'][U.union(*map(int, input().split()))])