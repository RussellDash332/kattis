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
N, S, B = map(int, input().split()); U = UFDS(N); E = []; Z = 0
for _ in range(S): a, b = map(int, input().split()); U.union(a-1, b-1)
for _ in range(B): a, b, w = map(int, input().split()); E.append((w, a-1, b-1))
for w, a, b in sorted(E):
    if U.find(a) != U.find(b): U.union(a, b); Z += w
print([Z, 'more boardwalks needed!'][U.n>1])