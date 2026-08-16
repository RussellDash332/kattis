import sys; input = sys.stdin.readline
class DT:
    def __init__(s, q):
        s.p = [*range(N:=len(q))]; s.q = [*q]
    def find(s, i):
        if i < 0 or i >= len(s.p): return -1
        v = [i]
        while s.p[b:=v[-1]] != b and ~s.p[b]: v += [s.p[b]]
        x = s.p[b]
        for i in v: s.p[i] = x
        return x
    def free(s, x):
        s.p[x] = s.q[x]
N, Q = map(int, input().split()); K = [-1]*N
S = [*map(int, input().split())]
R = DT([*range(1,N)]+[-1])
L = DT([-1]+[*range(N-1)])
for _ in range(Q):
    x, d = input().split(); c = x = int(x)
    while 1:
        c = R.find(c+1) if d > '<' else L.find(c-1)
        if c < 0 or S[c] > S[x]: break
        K[c] = x; R.free(c); L.free(c)
print(*K)