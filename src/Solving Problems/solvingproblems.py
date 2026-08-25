import sys; input = sys.stdin.readline; from heapq import *
class UFDS:
    def __init__(s, N):
        s.p = [*range(N)]; s.e = [0]*N; s.q = [1]*N
    def find(s, i):
        if s.p[i] == i: return i
        s.p[i] = s.find(s.p[i])
        return s.p[i]
    def union(s, i, j):
        if (x:=s.find(i)) != (y:=s.find(j)): s.p[y] = x; s.e[x] += s.q[x]*s.e[y]; s.q[x] *= s.q[y]; return x
N = int(input()); Q = []; R = []; P = [0]; U = UFDS(N+1); V = UFDS(N+1)
for i in range(1, N+1):
    s, p, a, b = map(int, input().split()); a = 1-a/100; b = 1-b/100
    U.e[i] = s*a; V.e[i] = s*b; U.q[i] = a; V.q[i] = b
    P += [p]; heappush(Q, (-U.e[i]/(1-U.q[i]), i)); heappush(R, (-V.e[i]/(1-V.q[i]), i))
while Q:
    _, i = heappop(Q)
    if U.find(i) == i and P[i] != i:
        r = U.union(P[i], i)
        if r: heappush(Q, (-U.e[r]/(1-U.q[r]), r))
while R:
    _, i = heappop(R)
    if V.find(i) == i and P[i] != i:
        r = V.union(P[i], i)
        if r: heappush(R, (-V.e[r]/(1-V.q[r]), r))
u, v = U.e[0], V.e[0]
print(['Tie', 'Rasmus', 'Ryan'][(u>v)-(u<v)])