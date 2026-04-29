import sys; input = sys.stdin.readline
N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a:=a-1].append(b:=b-1); G[b].append(a)
T = 0; V = [0]*N; D = [-1]*N; L = [-1]*N; bridges = set()
for i in range(N):
    if not V[i]:
        S = [(2*i, -1)]
        while S:
            vs, p = S.pop(); v, s = divmod(vs, 2)
            if s&1:
                L[v] = min(L[v], L[p])
                if L[p] > D[v]: bridges.add((v, p))
            else:
                if V[v]: S.pop(); continue
                V[v] = 1; D[v] = L[v] = T; T += 1
                for to in G[v]:
                    if to == p: continue
                    if V[to]: L[v] = min(L[v], D[to])
                    else: S.append((vs^1, to)); S.append((2*to, v))

# build two-edge component graph
C = [[] for _ in range(N)]
for a in range(N):
    for b in G[a]:
        if (a,b) in bridges or (b,a) in bridges: continue
        C[a].append(b); C[b].append(a)
S = [-1]*N; c = -1
for i in range(N):
    if S[i]<0:
        S[i] = (c:=c+1); Q = [i]
        for u in Q:
            for v in C[u]:
                if S[v]<0: S[v] = c; Q.append(v)
if c < 1: print(0); exit()
D = [0]*(c+1)
for a in range(N):
    for b in G[a]:
        if S[a]-S[b]: D[S[a]] += 1; D[S[b]] += 1
print((D.count(0)*2+D.count(2)+1)//2)