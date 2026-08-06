from heapq import *
R, C, *F, x, y, X, Y = map(int, open(0).read().split())
P = [p:=0]+[p:=p+i for i in F]
T = [*{(i,v) for i in range(C) for v in (0,y,Y,R-1)}]
n = len(T)
G = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j: continue
        w = -1
        if T[i][0]==T[j][0]: w = (2*F[T[i][0]]-T[i][1]-T[j][1])*-~abs(T[i][1]-T[j][1])//2-F[T[i][0]]+T[i][1]
        elif T[i][1]==T[j][1]: w = P[max(T[i][0], T[j][0])+1]-P[min(T[i][0], T[j][0])]-F[T[i][0]]-T[i][1]*abs(T[i][0]-T[j][0])
        if ~w: G[i] += [(j, w)]
s = T.index((x, y)); INF = 10**21; D = [INF]*n; D[s] = 0; pq = [(0, s)]
while pq:
    dd, vv = heappop(pq)
    if dd != D[vv]: continue
    for nn, w in G[vv]:
        if D[nn] > (new:=dd+w): D[nn] = new; heappush(pq, (new, nn))
print(D[T.index((X, Y))]+F[x]-y)