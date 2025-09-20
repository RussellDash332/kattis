import sys; input = sys.stdin.readline
R, C = map(int, input().split()); M = [[*map(int, input().split())] for _ in range(R)]
r0, c0, rf, cf = map(lambda x: ~-int(x), input().split()); s = r0*C+c0; t = rf*C+cf
n = R*C*2; INF = float('inf'); D = [INF]*n; D[2*s] = D[2*s+1] = 0; Q = [(0, 2*s), (0, 2*s+1)]
for dd, vv in Q:
    v = vv//2; b = vv%2; r = v//C; c = v%C; u = M[r][c]
    if dd != D[vv]: continue
    for x in range(-1, 2):
        for y in range(-1, 2):
            if (x or y) and R>r+x>-1<c+y<C and D[nn:=2*((r+x)*C+(c+y))+1-b] > dd+1: 
                z = M[r+x][c+y]
                if (u>z)-(u<z) == 2*b-1: D[nn] = dd+1; Q.append((dd+1, nn))
Z = min(D[2*t], D[2*t+1]); print([-1, Z][Z<1e9])