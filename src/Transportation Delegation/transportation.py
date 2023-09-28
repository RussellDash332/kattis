import sys; input = sys.stdin.readline
from collections import deque
INF = float('inf')
s, r, f, t = map(int, input().split())
rr = input().strip().split()
ff = input().strip().split()
rev = {}
for i in rr:
    if i not in rev: rev[i] = len(rev)
for i in ff:
    if i not in rev: rev[i] = len(rev)
rr = [rev[i] for i in rr]; ff = [rev[i] for i in ff]

def BFS(s, t):
    d[s] = 0
    q = deque([s])
    while q:
        u = q.popleft()
        if u == t: break
        for idx in AL[u]:
            v, cap, flow = EL[idx]
            if cap > flow and d[v] == -1:
                d[v] = d[u]+1
                q.append(v)
    return d[t] != -1

def DFS(u, t, f=INF):
    if u == t or f == 0: return f
    for i in range(last[u], len(AL[u])):
        last[u] = i
        v, cap, flow = EL[AL[u][i]]
        if d[v] != d[u]+1: continue
        pushed = DFS(v, t, min(f, cap - flow))
        if pushed:
            EL[AL[u][i]][2] += pushed
            EL[AL[u][i]^1][2] -= pushed
            return pushed
    return 0

V, E = s+2*t+2, 0
source, sink = V-2, V-1
EL, AL = [], [[] for _ in range(V)]
def add(u, v, capacity):
    EL.append([v, capacity, 0]), AL[u].append(len(EL)-1), EL.append([u, 0, 0]), AL[v].append(len(EL)-1)

for i in rr: add(source, i, 1)
for i in ff: add(i, sink, 1)
for u in range(t):
    n, *a = input().strip().split(); v = s+2*u
    add(v, v+1, 1)
    for i in a:
        if i not in rev: rev[i] = len(rev)
        b = rev[i]
        if b < r: add(b, v, 1)
        elif b < r+f: add(v+1, b, 1)
        else: add(b, v, 1), add(v+1, b, 1)

mf = 0; d = [-1]*V
while BFS(source, sink):
    last = [0]*V
    f = DFS(source, sink)
    while f: mf += f; f = DFS(source, sink)
    d = [-1]*V
print(mf)