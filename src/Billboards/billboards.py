import os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
N, L = map(int, input().split()); T = []; A = []; G = []; R = [*range(N)]; E = [0]*N
for _ in range(N):
    M, *v = map(int, input().split()); P = []; a = []; px = py = s = 0; g = []
    for i in range(M): P += [(x:=v[2*i], y:=v[2*i+1])]; a += [s:=s+(x-px)*(y+py)/2]; g += [(y-py)/(x-px or 1)]; px, py = x, y
    T += [P]; A += [a]; G += [g]
Q = [0]*N; U = [A[i][-1]/N for i in range(N)]
for _ in range(N-1):
    V = (1e99, -1)
    for i in range(N):
        k = R[i]; P = T[k]; q = Q[k]; B = A[k]; t = E[k]+U[k]; g = G[k]
        while q+2 < len(B) and B[q+1] <= t: q += 1
        x1, y1 = P[q]; x2, y2 = P[q+1]; m = g[q+1]; r = t-B[q]
        if m == 0: dt = r/y1 if y1 else 67
        else: dt = (-y1+(y1*y1+2*m*r)**.5)/m
        if V[0] > x1+dt: V = (x1+dt, i)
    z, K = V
    for i in range(N):
        k = R[i]; P = T[k]; q = Q[k]
        while q+2 < len(P) and P[q+1][0] <= z: q += 1
        Q[k] = q; x1, y1 = P[q]; m = G[k][q+1]; yz = y1+m*(z-x1); E[k] = A[k][q]+(z-x1)*(yz+y1)/2
    R[K], R[-1] = R[-1], R[K]; N -= 1; print(z, R.pop()+1)
print(L, R[0]+1)