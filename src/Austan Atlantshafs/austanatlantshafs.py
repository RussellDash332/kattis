import sys; input = sys.stdin.readline
N = int(input()); G = [[] for _ in range(N)]; V = [None]*N; H = {}; M = [-1]*N; Z = [None]*N; Q = []; I = [0]*N; T = []
for _ in range(N):
    x, y, t = input().split()
    if x not in H: H[x] = len(H)
    if y not in H: H[y] = len(H)
    if _: G[H[y]].append(H[x]); I[H[x]] += 1
    if int(t) > 0: V[H[x]] = (int(t), H[x]); Q.append(H[x]); Z[H[x]] = (int(t), 1)
for i in H: M[H[i]] = i
q = [i for i in range(N) if I[i] < 1]
for u in q:
    T.append(u)
    for v in G[u]: I[v] -= 1; I[v] < 1 and q.append(v)
while T:
    i = T.pop(); w = 0
    for v in G[i]:
        if not Z[v]: continue
        if not Z[i] or Z[v][0] > Z[i][0]: Z[i] = Z[v]
        elif Z[v][0] == Z[i][0]: Z[i] = (Z[i][0], Z[i][1]+Z[v][1])
    for v in G[i]:
        if V[v]: w += V[v][0] == Z[i][0]
    if w != 1 or Z[i][1] != 1: continue
    for v in G[i]:
        if V[v] and V[v][0] == Z[i][0]: V[i], V[v] = V[v], None; break
A = {}
for i in range(N):
    if V[i]: A[V[i][1]] = i
for x in Q: print(M[A[x]])