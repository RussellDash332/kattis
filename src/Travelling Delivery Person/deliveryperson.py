import sys; input = sys.stdin.readline; from array import *; from heapq import *; P = 6
B, S, R, L, N = map(int, input().split()); E = [(P, P)]; INF = 10**9
for _ in range(N): X, Y = map(int, input().split()); X += P; Y += P; E.append((X, Y))
U = 4*(Q:=2*P+1)**2; G = [{} for _ in range(U)]; K = [(0, 1), (-1, 0), (0, -1), (1, 0)]; Z = [0]*4; D = array('i', [INF]*U*U)
for i in range(Q):
    for j in range(Q):
        for d in range(4):
            t = 4*Q*i+4*j+d
            di, dj = K[(d+1)%4]
            if Q>i+di>-1<j+dj<Q: G[t][4*Q*(i+di)+4*(j+dj)+(d+1)%4] = B+L
            di, dj = K[(d-1)%4]
            if Q>i+di>-1<j+dj<Q: G[t][4*Q*(i+di)+4*(j+dj)+(d-1)%4] = B+R
            di, dj = K[d]
            if Q>i+di>-1<j+dj<Q: G[t][4*Q*(i+di)+4*(j+dj)+d] = B+S
for s in range(U):
    D[s*U+s] = 0; pq = [s]
    while pq:
        dv = heappop(pq); dd, vv = divmod(dv, U)
        if dd != D[s*U+vv]: continue
        for nn in G[vv]:
            if D[s*U+nn] > (new:=dd+G[vv][nn]): D[s*U+nn] = new; heappush(pq, new*U+nn)
for i in range(N):
    x1, y1 = E[i]; x2, y2 = E[i+1]
    Z = [min(Z[e]+D[U*(4*Q*x1+4*y1+e)+4*Q*x2+4*y2+d] for e in range(4)) for d in range(4)]
print(min(Z))