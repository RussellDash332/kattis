import sys; input = sys.stdin.readline
while True:
    try: X, Y, Z, N = map(int, input().split()); ok = 1; V = 0
    except: break
    A = [[*map(int, input().split())] for _ in range(N)]; S = [[*map(int, input().split())] for _ in range(N)]
    for i in range(N):
        if not ok: break
        sx, sy, sz, ex, ey, ez = S[i]; cx, cy, cz = A[i]; V += (ex-sx+1)*(ey-sy+1)*(ez-sz+1)
        if not (sx<=cx<=ex<=X and sy<=cy<=ey<=Y and sz<=cz<=ez<=Z): ok = 0; break
        for j in range(i):
            tx, ty, tz, fx, fy, fz = S[j]
            if min(ex, fx) >= max(sx, tx) and min(ey, fy) >= max(sy, ty) and min(ez, fz) >= max(sz, tz): ok = 0; break
    ok &= V==X*Y*Z
    print('YNEOS'[1-ok::2])