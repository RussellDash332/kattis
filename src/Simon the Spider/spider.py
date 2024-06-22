import sys; input = sys.stdin.readline; from array import *; B = 10**6

class UFDS:
    def __init__(self, N):
        self.p = [*range(N)]; self.rank = [0]*N; self.n = N
    def find(self, i):
        if self.p[i] == i: return i
        self.p[i] = self.find(self.p[i])
        return self.p[i]
    def union(self, i, j):
        x = self.find(i); y = self.find(j); self.n -= 1
        if self.rank[x] > self.rank[y]: self.p[y] = x
        else: self.p[x] = y; self.rank[y] += self.rank[x] == self.rank[y]

while True:
    try: V, E = map(int, input().split())
    except: break
    EL = []; M = array('i', [0]*V*V); U = UFDS(V); AL = [{} for _ in range(V)]; C = 0; Z = 10**9; G = [[] for _ in range(V)]
    for _ in range(E):
        a, b, w = map(int, input().split()); a -= 1; b -= 1
        if b not in AL[a]: AL[a][b] = AL[b][a] = w*(B+1)
        else: AL[a][b] = AL[b][a] = min(w, AL[a][b]//B)*B+max(w, AL[a][b]%B)
    for i in range(V):
        for j in AL[i]:
            if i < j: EL.append(AL[i][j]//B*B+1000*i+j)
    for wab in sorted(EL):
        w, ab = divmod(wab, B); a, b = divmod(ab, 1000)
        if U.find(a) != U.find(b): U.union(a, b); C += w; G[a].append((b, w)); G[b].append((a, w))
        if U.n == 1: break
    if U.n != 1: print('disconnected'); continue
    for i in range(V):
        vis = [0]*V; vis[i] = 1; st = [i]
        while st:
            u  = st.pop()
            for v, w in G[u]:
                if vis[v]: continue
                vis[v] = 1; M[i*V+v] = max(M[i*V+u], w); st.append(v)
    for i in range(V):
        for j in AL[i]:
            if i < j: Z = min(Z, C-M[i*V+j]-AL[i][j]%B)
    print(Z)