import sys; input = sys.stdin.readline; from array import *
n, q = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split()); a -= 1; b -= 1
    g[a].append(b), g[b].append(a)

# Tarjan's OLCA
Q = [[] for _ in range(n)]; R = []; d = array('i', [0]*n); par = array('i', range(n)); d[0] = 1; s = [(0, 0)]
for i in range(q):
    a, b = map(int, input().split()); a -= 1; b -= 1
    R.append([a, b, 0]), Q[a].append(i), Q[b].append(i)

def find(i):
    if par[i] == i: return i
    par[i] = find(par[i]); return par[i]

while s:
    ub, p = s.pop(); u = ub//2
    if ub%2:
        for x in Q[u]:
            if R[x][1] == u: R[x][0], R[x][1] = R[x][1], R[x][0]
            R[x][2] = n+(L:=d[R[x][0]]+d[R[x][1]]-2*d[find(R[x][1])])*(L+1)//2
        par[u] = p
    else:
        s.append((ub+1, p))
        for t in g[u]:
            if t != p: d[t] = d[u]+1; s.append((2*t, u))
for i in R: print(i[2])