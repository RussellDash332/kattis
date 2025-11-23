from collections import deque; INF = float('inf')
def BFS(s, t):
    d[s] = 0; q = deque([s])
    while q:
        u = q.popleft()
        if u == t: break
        for idx in AL[u]:
            v, cap, flow = EL[idx]
            if cap > flow and d[v] == -1: d[v] = d[u]+1; q.append(v)
    return d[t] != -1
def DFS(u, t, f=INF):
    if u == t or f == 0: return f
    for i in range(last[u], len(AL[u])):
        last[u] = i; v, cap, flow = EL[AL[u][i]]
        if d[v] != d[u]+1: continue
        pushed = DFS(v, t, min(f, cap-flow))
        if pushed: EL[AL[u][i]][2] += pushed; EL[AL[u][i]^1][2] -= pushed; return pushed
    return 0
def add(u, v, c):
    AL[u].append(len(EL)); EL.append([v, c, 0]); AL[v].append(len(EL)); EL.append([u, 0, 0])

g, k = map(int, input().split()); M = [-1]*k; B = [set() for _ in range(26)]; K = [[0, k] for _ in range(26)]
for _ in range(g-1):
    s, t = input().split(); C = [0]*26; R = [0]*26
    for i in range(k):
        c = ord(s[i])-97
        if t[i] == 'G': M[i] = c; C[c] += 1
        elif t[i] == 'B': B[c].add(i); R[c] += 1
        else: B[c].add(i); C[c] += 1
    for i in range(26):
        if R[i]: K[i][1] = min(K[i][1], C[i])
        K[i][0] = max(K[i][0], C[i])
V = k+29; source, sink, sup = V-2, V-1, V-3; EL, AL = [], [[] for _ in range(V)]; mf = 0; d = [-1]*V; Z = ['.']*k
add(source, sup, k-sum(p[0] for p in K))
for i in range(26):
    add(source, i, K[i][0]); add(sup, i, K[i][1]-K[i][0])
for i in range(k):
    if ~M[i]: add(M[i], i+26, 1)
    else:
        for j in range(26):
            if i not in B[j]: add(j, i+26, 1)
    add(i+26, sink, 1)
while BFS(source, sink):
    last = [0]*V; f = DFS(source, sink)
    while f: mf += f; f = DFS(source, sink)
    d = [-1]*V
for i in range(len(EL)//2):
    v, _, f = EL[2*i]; u, _, _ = EL[2*i+1]
    if u < 26 and f: Z[v-26] = chr(u+97)
print(''.join(Z))