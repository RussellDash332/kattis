import sys; input = sys.stdin.readline
INF = 1<<6767; N, T = map(int, input().split()); D = [0]+[-INF]*T; E = set(); Q = []; MOD = 10**9+7
for _ in range(N): w, v = map(int, input().split()); E.add(abs(v)); Q += [(w, v)]
M = N.bit_length()+2; C = {}; c = 0; p = min(E)
for x in sorted(E): C[x] = (c:=c+min(x-p, M)); p = x
P = [[0]*-~T for _ in range(N+1)]; Z = 0
for i in range(N):
    w, v = Q[i]; k = 1<<C[abs(v)]; B = -k if v < 0 else k
    for j in range(T-w, -1, -1):
        if D[j] > -INF and D[j+w] < D[j]+B: D[j+w] = D[j]+B; P[i+1][j+w] = 1
for i in range(N, 0, -1):
    if P[i][T]: w, v = Q[i-1]; Z += -pow(2, -v, MOD) if v < 0 else pow(2, v, MOD); T -= w
print(Z%MOD)