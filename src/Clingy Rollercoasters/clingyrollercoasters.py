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
N, *C = map(int, open(0).read().split()); U = UFDS(N)
for i in range(N): U.union(i, C[i]-1)
D = {0}
for i in {*map(U.find, range(N))}: k = U.s[i]; D |= {x+k for x in D}
print(len(D), *sorted(D))