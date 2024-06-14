import sys; input = sys.stdin.readline; W = []; from bisect import *; X, Y = map(int, input().split()); C = 0; INF = 10**18
while (s:=input().split()):
    C += 1
    if s[0][0] == 'O':
        ok = 1; xx, yy, ww, hh = map(int, s[1:])
        for x, y, dx, dy in W:
            if (x<=xx<x+dx or xx<=x<xx+ww) and (y<=yy<y+dy or yy<=y<yy+hh): ok = 0; break
        if not ok or xx+ww > X or yy+hh > Y: print(f'Command {C}: OPEN - window does not fit')
        else: W.append((xx, yy, ww, hh))
    elif s[0][0] == 'C':
        xx, yy = map(int, s[1:]); f = 0
        for x, y, dx, dy in W:
            if x<=xx<x+dx and y<=yy<y+dy: W.remove((x, y, dx, dy)); f = 1; break
        if not f: print(f'Command {C}: CLOSE - no window at given position')
    elif s[0][0] == 'R':
        xx, yy, ww, hh = map(int, s[1:]); f = 0; ok = 1
        for i, (x, y, dx, dy) in enumerate(W):
            if x<=xx<x+dx and y<=yy<y+dy: f = (i, x, y); break
        if not f: print(f'Command {C}: RESIZE - no window at given position'); continue
        for i, (x, y, dx, dy) in enumerate(W):
            if i == f[0]: continue
            if (x<=f[1]<x+dx or f[1]<=x<f[1]+ww) and (y<=f[2]<y+dy or f[2]<=y<f[2]+hh): ok = 0; break
        if not ok or f[1]+ww > X or f[2]+hh > Y: print(f'Command {C}: RESIZE - window does not fit')
        else: W[f[0]] = (f[1], f[2], ww, hh)
    else:
        xx, yy, ww, hh = map(int, s[1:]); f = 0
        for i, (x, y, dx, dy) in enumerate(W):
            if x<=xx<x+dx and y<=yy<y+dy: f = (i, *W[i]); break
        if not f: print(f'Command {C}: MOVE - no window at given position'); continue
        G = [f]; T = [ww>0, ww<0, hh>0, hh<0].index(1); A = O = (abs(ww), abs(hh), -1)[T//2]; Gi = {*range(len(W))}
        while True:
            pr = len(Gi)
            for _, x2, y2, dx2, dy2 in G:
                for i in [*Gi]:
                    x, y, dx, dy = W[i]
                    if (y<=y2<y+dy or y2<=y<y2+dy2, x<=x2<x+dx or x2<=x<x2+dx2)[T//2] and (x2+dx2==x, x+dx==x2, y2+dy2==y, y+dy==y2)[T]: Gi.remove(i); G.append((i, *W[i]))
            if len(Gi) == pr: break
        A = min((X-max(ff[1]+ff[3] for ff in G), min(ff[1] for ff in G), Y-max(ff[2]+ff[4] for ff in G), min(ff[2] for ff in G))[T], A)
        while True:
            d = INF; ae = sorted((xx+dxx, -xx, yy+dyy, -yy)[T] for _, xx, yy, dxx, dyy in G)
            for i in Gi:
                x, y, dx, dy = W[i]; bs = bisect_left(ae, v:=(x, -x-dx, y, -y-dy)[T])
                if bs and v > ae[bs-1]: d = min(d, v-ae[bs-1])
            if d > A or d <= 0: break
            for i, (j, x, y, dx, dy) in enumerate(G): W[j] = ((x+d, x-d, x, x)[T], (y, y, y+d, y-d)[T], dx, dy); G[i] = (j, *W[j])
            while True:
                pr = len(Gi)
                for _, x2, y2, dx2, dy2 in G:
                    for i in [*Gi]:
                        x, y, dx, dy = W[i]
                        if (y<=y2<y+dy or y2<=y<y2+dy2, x<=x2<x+dx or x2<=x<x2+dx2)[T//2] and (x2+dx2==x, x+dx==x2, y2+dy2==y, y+dy==y2)[T]: Gi.remove(i); G.append((i, *W[i]))
                if len(Gi) == pr: break
            A = min((X-max(ff[1]+ff[3] for ff in G), min(ff[1] for ff in G), Y-max(ff[2]+ff[4] for ff in G), min(ff[2] for ff in G))[T], A-d)
        for i, (j, x, y, dx, dy) in enumerate(G): W[j] = ((x+A, x-A, x, x)[T], (y, y, y+A, y-A)[T], dx, dy)
        if abs(W[f[0]][T//2]-f[T//2+1]) != O: print(f'Command {C}: MOVE - moved {abs(W[f[0]][T//2]-f[T//2+1])} instead of {O}')
print(len(W), 'window(s):')
for w in W: print(*w)