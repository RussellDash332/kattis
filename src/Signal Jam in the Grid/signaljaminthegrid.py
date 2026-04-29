from heapq import *
R, C = map(int, input().split())
M = [input() for _ in '.'*R]
for i in range(R):
    for j in range(C):
        if M[i][j]>'E': s = 2*(i*C+j); M[i] = M[i].replace('S', '0')
        elif M[i][j]=='E': t = 2*(i*C+j); M[i] = M[i].replace('E', '0')
INF = float('inf'); D = [INF]*2*R*C; D[s] = 0; pq = [(0, s)]
K = ((0, 1), (1, 0), (-1, 0), (0, -1))
while pq:
    dd, vv = heappop(pq)
    if dd != D[vv]: continue
    rc, b = divmod(vv, 2); r, c = divmod(rc, C)
    for dr, dc in K:
        if R>r+dr>-1<c+dc<C and M[r+dr][c+dc]>'#':
            nn = 2*(r+dr)*C+2*(c+dc)
            if b and D[nn+1] > (new:=dd+int(M[r+dr][c+dc])): D[nn+1] = new; heappush(pq, (new, nn+1))
            if not b and D[nn] > (new:=dd+int(M[r+dr][c+dc])): D[nn] = new; heappush(pq, (new, nn))
            if not b and D[nn+1] > dd+1: D[nn+1] = dd+1; heappush(pq, (dd+1, nn+1))
z = min(D[t], D[t+1]); print([z, -1][z == INF])