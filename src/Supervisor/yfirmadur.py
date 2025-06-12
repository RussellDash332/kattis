import sys; input = sys.stdin.readline; from heapq import *; from array import *
class UFDS:
    def __init__(s, N): s.p = [*range(N)]
    def find(s, i):
        if s.p[i] == i: return i
        s.p[i] = s.find(s.p[i]); return s.p[i]
    def union(s, i, j): s.p[s.find(i)] = s.find(j)
n, q = map(int, input().split()); v = []; M = array('i', [-1]*(L:=n+q+3)); R = array('i', M); S = array('i', M); U = UFDS(L); P = n
for i, e in enumerate(map(int, input().split())): M[i+1] = R[i+1] = i+1; S[i+1] = e
for l in sys.stdin:
    c, x = l.split(); x = int(x)
    if c == '+': S[P:=P+1] = M[x]; M[u:=(heappop(v) if v else (n:=n+1))] = P; R[P] = u
    elif c == '-': heappush(v, x); U.union(M[x], S[M[x]])
    else: print(R[U.find(S[M[x]])])