import sys; input = sys.stdin.readline; from array import *

class Node:
    z = 0
    def __init__(self, c, l): self.id = self.z; Node.z += 1; X.append(self); self.ch = {}; self.c = c; self.l = l

# Construct trie
V, N = input().split(); V = ord(V)-96; N = int(N); W = [[ord(x)-97 for x in input().strip()] for _ in range(N)]; G = [set() for _ in range(V)]; indeg, top = [0]*V, []; X = []; T = Node(-1, -1)
for n in range(N):
    w = W[n]; t = T
    for k, i in enumerate(w):
        if i not in t.ch: t.ch[i] = Node(i, k)
        t = t.ch[i]
vg = Node.z; g = [set() for _ in range(vg)]; p = []; q = {}
for n in range(N):
    w = W[n]; t = T
    for i in w: g[t.id].add(t.ch[i].id); g[t.ch[i].id].add(t.id); t = t.ch[i]
    p.append(t.id); q[t.id] = n
for i in range(vg): g[i] = [*g[i]]

# Tarjan's OLCA
Q = [[] for _ in range(vg)]; R = []; d = array('i', [0]*vg); par = array('i', range(vg)); d[0] = 1; s = [(0, 0)]; Z = 0
for i in range(N):
    for j in range(i): R.append([p[i], p[j], None]), Q[p[i]].append(Z), Q[p[j]].append(Z); Z += 1
def find(i):
    if par[i] == i: return i
    par[i] = find(par[i]); return par[i]
while s:
    ub, p = s.pop(); u = ub//2
    if ub%2:
        for x in Q[u]:
            if R[x][1] == u: R[x][0], R[x][1] = R[x][1], R[x][0]
            R[x][2] = find(R[x][1])
        par[u] = p
    else:
        s.append((ub+1, p))
        for t in g[u]:
            if t != p: d[t] = d[u]+1; s.append((2*t, u))
for a, b, lca in R:
    lcp = X[lca].l+1 if lca != vg-1 else 0
    if lcp < len(W[q[a]]) and lcp < len(W[q[b]]): G[W[min(q[a], q[b])][lcp]].add(W[max(q[a], q[b])][lcp])
    elif lcp == len(W[max(q[a], q[b])]): print('IMPOSSIBLE'), exit(0)

# Topological sort
for v in range(V):
    for w in G[v]: indeg[w] += 1
q = [i for i in range(V) if indeg[i] == 0]; r = [set() for _ in range(2*V)]; z = 0
for i in range(V): r[indeg[i]].add(i)
for u in q:
    if len(r[0]) > 1: z = 1
    top.append(u); r[0].discard(u)
    for v in G[u]:
        r[indeg[v]].discard(v)
        indeg[v] -= 1
        r[indeg[v]].add(v)
        if indeg[v] == 0: q.append(v)
if len(top) != V: print('IMPOSSIBLE')
elif z: print('AMBIGUOUS')
else: print(''.join(chr(i+97) for i in top))