import sys; input = sys.stdin.readline; from array import *
N, Q = map(int, input().split()); S = array('i', range(N)); D = array('i', [-1]*N); M = 10**9+7
for _ in range(Q):
    a, b, c = input().split(); a = int(a)-1; b = int(b)-1
    if c[0] == 's': S[b] = min(S[b], a)
    else: D[b] = max(D[b], a)
Z = array('i', [1]+[0]*N)
for i in range(1, N+1):
    L = D[i-1]+1; H = S[i-1]
    for j in range(i-1, -1, -1):
        if L <= j <= H: Z[i] = (Z[i]+Z[j])%M
        if j: L = max(L, D[j-1]+1); H = min(H, S[j-1])
print(Z[-1]*2%M)