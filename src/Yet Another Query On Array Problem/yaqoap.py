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
import sys; input = sys.stdin.readline
N = int(input())
A = [*map(int, input().split())]
U = UFDS(N)
H = {}
for i in range(N): H.setdefault(A[i], []).append(i)
for a, *v in H.values():
    for i in v: U.union(a, i)
for _ in range(int(input())): a, b = map(int, input().split()); print(U.s[a:=U.find(a-1)], U.union(a, b-1) or U.s[U.find(a)])