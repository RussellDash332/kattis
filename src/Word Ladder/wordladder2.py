N = int(input()); W = [input().strip() for _ in range(N)]; K = len(W[0]); R = {W[i]:i for i in range(N)}; G = [[] for _ in range(N)]
for i in range(N):
    for j in range(K):
        for k in range(65, 91):
            if chr(k) != W[i][j]:
                s = W[i][:j]+chr(k)+W[i][j+1:]
                if s not in R: R[s] = len(R); W.append(s); G.append([])
                G[R[W[i]]].append(R[s]); G[R[s]].append(R[W[i]])
D = [-1]*len(G); E = [-1]*len(G); Q = [0]; D[0] = 0; R = [1]; E[1] = 0
for u in Q:
    for v in G[u]:
        if D[v] == -1: D[v] = D[u]+1; Q.append(v) if v < N else 0
for u in R:
    for v in G[u]:
        if E[v] == -1: E[v] = E[u]+1; R.append(v) if v < N else 0
ans = None; dist = D[1] if D[1] > -1 else 2000
for i in range(N, len(G)):
    if D[i] > -1 < E[i]:
        if D[i]+E[i] < dist: ans = W[i]; dist = D[i]+E[i]
        elif D[i]+E[i] == dist and ans != None: ans = min(W[i], ans)
if ans == None: print(0, dist if dist < 2000 else -1)
else: print(ans, dist)