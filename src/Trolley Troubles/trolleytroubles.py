import sys; input = sys.stdin.readline; from heapq import *
R, C = map(int, input().split()); s = int(input())*C-C; n = R*C; g = [{} for _ in range(n)]; INF = float('inf'); D = [INF]*n; D[s] = 0; pq = [(0, s)]; M = [input() for _ in range(R)]; P = [-1]*n
for i in range(R):
    for j in range(C):
        if j < C-1:
            if M[i][j] < '^': g[i*C+j][i*C+j+1] = int(M[i][j] > '=')
            elif M[i][j] < 'v': g[i*C+j][i*C+j+1] = g[i*C+j][i*C+j-C] = 0
            else: g[i*C+j][i*C+j+1] = g[i*C+j][i*C+j+C] = 0
while pq:
    dd, vv = heappop(pq)
    if dd != D[vv]: continue
    for nn in g[vv]:
        if D[nn] > (new:=dd+g[vv][nn]): P[nn] = vv; D[nn] = new; heappush(pq, (new, nn))
b, k = min((D[i]+(M[i//C][C-1]=='H'), i) for i in range(C-1, n, C)); p = [k]; print(b)
while ~p[-1]: p.append(P[p[-1]])
p = p[-2::-1]
for i in range(len(p)-1):
    a, b = p[i], p[i+1]
    if a//C != b//C: print(str(a%C+1)+'ud'[a<b])