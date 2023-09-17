from math import *
from heapq import *
INF = float('inf')
for _ in range(int(input())):
    bx1, by1, bx2, by2, x1, y1, x2, y2 = map(int, input().split())
    p = [(x1, y1), (x2, y2)]; d = gcd(bx1-bx2, by1-by2); dx = (bx2-bx1); dy = (by2-by1)
    if bx1 > bx2: bx1, by1, bx2, by2 = bx2, by2, bx1, by1
    px, py = bx1, by1
    while px < bx2: p.append((px, py)); px += 1; py += dy/dx
    if by1 > by2: bx1, by1, bx2, by2 = bx2, by2, bx1, by1
    px, py = bx1, by1
    while py < by2: p.append((px, py)); px += dx/dy; py += 1
    p.append((bx2, by2)); n = len(p); g = [[0]*n for _ in range(n)]
    g[0][1] = g[1][0] = abs(x1-x2)+abs(y1-y2)
    for i in range(2, n):
        for j in range(2): g[i][j] = g[j][i] = abs(p[i][0]-p[j][0])+abs(p[i][1]-p[j][1])
        for j in range(i+1, n): g[i][j] = g[j][i] = hypot(p[i][0]-p[j][0], p[i][1]-p[j][1])
    D = [INF]*n; D[0] = 0; pq = [(0, 0)]
    while pq:
        dd, vv = heappop(pq)
        if dd != D[vv]: continue
        for nn in range(n):
            if D[nn] > (new:=dd+g[vv][nn]): D[nn] = new; heappush(pq, (new, nn))
    print(D[1])