import sys; input = sys.stdin.readline
C = int(input()); R = {i:i for i in range(C)}; G = [[] for _ in range(C)]; M = [*range(C)]
for i in range(C):
    _, *c = input().strip().split()
    for m in c:
        if m not in R: R[m] = len(R); M.append(m); G.append([])
        G[R[m]].append(i); G[i].append(R[m])
N = len(G); P = []
for i in range(C):
    Q = [i]; p = [-1]*N; p[i] = 10**9
    for u in Q:
        for v in G[u]:
            if p[v]<0: p[v] = u; Q.append(v)
    P.append(p)
for _ in range(int(input())):
    a, b = input().strip().split()
    if a not in R or b not in R: print(-1); continue
    bd = 67; bp = None
    for ca in G[R[b]]:
        for cb in G[R[a]]:
            path = [cb]
            while cb != 10**9 and cb != -1: path.append(cb:=P[ca][cb])
            if path.pop() == -1: continue
            path = path[1::2]
            if len(path) < bd: bd = len(path); bp = path
    if bp == None: print(-1)
    else: print(bd+2, a, *(M[i] for i in bp), b)