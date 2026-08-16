K = [[], [], []]
for _ in range(int(input())): x, y, c = map(int, input().split()); K[c-1] += [(x, y)]
A, B, C = [*map(sorted, K)]; L = min(min(x[1] for x in i) for i in K)-2; H = max(max(x[1] for x in i) for i in K)+2
xm, xM = A[0][0], A[-1][0]; R = [(xm-0.3, H), (xM+0.2, H), (xM+0.2, H-1)]; cx = xM+0.2
while A:
    x, y = A.pop()
    if cx > x-0.2:
        if R[-1][1] != H-1: tx, ty = R[-1]; R[-1] = (tx-0.1, ty); R += [(cx:=tx-0.1, H-1)]
        R += [(cx:=x-0.2, H-1)]
    R += [(cx, y+0.2), (cx+0.3, y+0.2), (cx+0.3, y-0.2), (cx, y-0.2)]
tx, ty = R[-1]; R[-1] = (tx-0.1, ty); print(len(R))
for x, y in R: print(round(x, 1), round(y, 1))
xm, xM = B[0][0], B[-1][0]; G = [(xM+0.3, L), (xm-0.2, L), (xm-0.2, L+1)]; cx = xm-0.2
for x, y in B:
    if cx < x+0.2:
        if G[-1][1] != L+1: tx, ty = G[-1]; G[-1] = (tx+0.1, ty); G += [(cx:=tx+0.1, L+1)]
        G += [(cx:=x+0.2, L+1)]
    G += [(cx, y-0.2), (cx-0.3, y-0.2), (cx-0.3, y+0.2), (cx, y+0.2)]
tx, ty = G[-1]; G[-1] = (tx+0.1, ty); print(len(G))
for x, y in G: print(round(x, 1), round(y, 1))