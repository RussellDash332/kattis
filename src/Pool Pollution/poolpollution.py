class UFDS:
    def __init__(s, N, c):
        s.p = [*range(N)]; s.r = [0]*N; s.c = c
    def find(s, i):
        if s.p[i] == i: return i
        s.p[i] = s.find(s.p[i])
        return s.p[i]
    def union(s, i, j):
        if (x:=s.find(i)) != (y:=s.find(j)):
            if s.r[x] > s.r[y]: s.p[y] = x; s.c[x] += s.c[y]
            else: s.p[x] = y; s.r[y] += s.r[x] == s.r[y]; s.c[y] += s.c[x]
import sys; input = sys.stdin.readline
n, m, k = map(int, input().split()); U = UFDS(n, c:=[*map(int, input().split())])
for _ in range(m): a, b = map(int, input().split()); U.union(a-1, b-1)
for i in map(int, input().split()): c[U.find(i-1)] = 0
print(sum(c[x] for x in {U.find(i) for i in range(n)}))