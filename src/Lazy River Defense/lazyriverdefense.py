from math import *; from collections import *
n = int(input()); P = []; B = []; Z = D = 0; L = 100
for _ in '.'*n: x, y = map(int, input().split()); P += [(x*L, y*L)]
m, b = map(int, input().split()); C = [[[] for _ in range(m)] for _ in range(n)]; R = [[] for _ in range(m)]
for _ in '.'*m: x, y, r, t = map(int, input().split()); B += [(x*L, y*L, r*L, t*L)]
for i in range(n):
    (x1, y1), (x2, y2) = P[i], P[(i+1)%n]; D += (d:=round(hypot(dx:=x2-x1, dy:=y2-y1))); U = dx**2+dy**2
    for j in range(m):
        xc, yc, r, _ = B[j]; fx = x1-xc; fy = y1-yc; V = 2*(fx*dx+fy*dy); W = fx**2+fy**2-r*r; X = V*V-4*U*W
        if X < 0: continue
        for t in ((-V+X**.5)/2/U, (-V-X**.5)/2/U): t = min(max(t, 0), 1); C[i][j].append((x1+t*(x2-x1), y1+t*(y2-y1)))
for i in range(m):
    t = []; ct = 0; pr = B[i][3]
    for j in range(n):
        (x1, y1), (x2, y2) = P[j], P[(j+1)%n]; d = round(hypot(x2-x1, y2-y1))
        C[j][i].sort(key=lambda p:hypot(p[0]-x1, p[1]-y1))
        if not C[j][i]: ct += d; continue
        (xc1, yc1), (xc2, yc2) = C[j][i]
        t1, t2 = ct+hypot(xc1-x1, yc1-y1), ct+hypot(xc2-x1, yc2-y1)
        if t and abs(t[-1][1]-t1) < 1e-7: t[-1] = (t[-1][0], t2)
        else: t.append((t1, t2))
        ct += d
    R[i] = [deque(t), [(a+D, b+D) for a, b in t], pr, 0]
if all(not R[i][0] for i in range(m)): print('safe')<exit()
while b:
    # pad sufficiently
    for i in range(m):
        if not R[i][1]: continue
        while not R[i][0] or R[i][0][-1][1] <= R[i][3]+2*R[i][2]+2*D:
            for s, e in R[i][1]:
                if R[i][0] and abs(R[i][0][-1][1]-s) < 1e-7: ls, le = R[i][0].pop(); R[i][0].append((ls, e))
                else: R[i][0].append((s, e))
            R[i][1] = [(a+D, b+D) for a, b in R[i][1]]
            while R[i][0] and R[i][0][0][1] < R[i][3]-1e-7: R[i][0].popleft()
    # select best person
    k = min(range(m), key=lambda x: max(R[x][0][0][0], R[x][3]) if R[x][0] else 1e17); px = R[k][2]; qx = R[k][0]; s, e = qx[0]; Z = max(s, R[k][3]); R[k][3] = Z+px; b -= 1
    if e-Z < px: qx.popleft()
    else: qx.popleft(); qx.appendleft((Z+px, e))
print(Z/L)