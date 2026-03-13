import sys, os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline; from array import *
N = int(input()); G = [0]*N; T = [[] for _ in range(N)]
for i in range(N): G[i] = [int(input())-1]; T[G[i][0]].append(i)
Z = int(input())

# create SCC graph first
top, vis, scc = [], array('b', [0]*N), 0; S = array('i', [-1]*N)
def DFS(s, t):
    stack = [2*s]; a = G if t else T
    while stack:
        ub = stack.pop()
        u, b = ub//2, ub%2
        if b and t: top.append(u)
        elif not vis[u]:
            vis[u] = 1; S[u] = scc
            stack.append(2*u+1)
            for v in a[u]:
                if not vis[v]: stack.append(2*v)
    return 1
for i in range(N):
    if not vis[i]: DFS(i, True)
vis = array('b', [0]*N)
for i in top[::-1]:
    if not vis[i]: scc += DFS(i, False)

# check if SCC of a can reach SCC of b
# the nature of the question forces the SCC graph to be a tree like 1->2->3<-0
# SC: {scc num: [vertices in this scc]}
# H: the scc graph
# K: transpose of the scc graph
# I: indegree of H for toposort of H
# P: the toposort of H
# F: store the cycle
# R: reverse mapping of F
# J: if this scc keeps going on, which part of the cycle does it meet
H = [set() for _ in range(scc)]; I = array('i', [0]*scc); SC = [[] for _ in range(scc)]; K = [[] for _ in range(scc)]; F = {}
for i in range(N): SC[S[i]].append(i)
for i in range(N):
    for j in G[i]: H[S[i]].add(S[j])
    if len(SC[S[i]]) > 1 or G[i][0] == i: F[S[i]] = i # {scc num: one endpoint of the cycle}
for i in range(scc): H[i].discard(i)
for i in range(scc):
    for j in H[i]: I[j] += 1; K[j].append(i)
Q = array('i', [i for i in range(scc) if I[i] == 0]); P = array('i'); D = array('i', [-1]*scc); J = array('i', [-1]*scc); tin = array('i', [-1]*scc); tout = array('i', [-1]*scc); tt = 0; R = array('i', [-1]*N)
for u in Q:
    P.append(u)
    for v in H[u]: I[v] -= 1; I[v] < 1 and Q.append(v)
for i in P:
    if len(SC[i]) > 1 or G[SC[i][0]][0] == SC[i][0]:
        f = [F[i]]; RS = [(i, 0, 0)]; jj = -1
        # update distance and times for this CC
        while RS:
            u, b, d = RS.pop()
            if b == 0:
                D[u] = d; RS.append((u, 1, d)); tin[u] = tt; tt += 1
                if d == 1: jj = G[SC[u][0]][0]
                J[u] = jj
                for v in K[u]: RS.append((v, 0, d+1))
            else:
                tout[u] = tt; tt += 1
        # deal with the cycle itself
        while True:
            f.append(G[f[-1]][0])
            if f[-1] == f[0]: f.pop(); break
        F[i] = f
for i in F:
    for j in range(len(F[i])): R[F[i][j]] = j

# wrap-up queries
def print(x): sys.stdout.write(str(x)+'\n')
for _ in range(Z):
    a, b = map(int, input().split()); a -= 1; b -= 1
    if R[a] != -1 and R[b] != -1: # both are cycles
        if S[a] != S[b]: print(-1)
        else: print((R[b]-R[a])%len(F[S[a]]))
    elif R[a] != -1: # S[a] is cycle but S[b] is not, cannot happen
        print(-1)
    elif R[b] != -1: # S[b] is cycle but S[a] is not, S[a] must terminate at S[b]
        if S[b] != S[J[S[a]]]: print(-1)
        else: print(D[S[a]]+(R[b]-R[J[S[a]]])%len(F[S[b]]))
    else:
        # both not cycle, must be from the same branching
        if tin[S[b]] <= tin[S[a]] <= tout[S[a]] <= tout[S[b]]: print(max(D[S[a]]-D[S[b]], -1))
        else: print(-1)