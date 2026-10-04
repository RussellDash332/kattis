import sys; input = sys.stdin.readline
N, K = map(int, input().split())
T = [0]*(10**6+1); C = []; P = []; D = []; F = []; U = []
s = 0
for i in range(N):
    t, c = map(int, input().split())
    for j in range(s, t+1): T[j] = i
    s = t+1; C += [c]; U += [t]
for _ in range(K):
    p, d, f = map(int, input().split())
    P += [p]; D += [d]; F += [f]
Z = [0]+[10**18]*N
for i in range(1, N+1): Z[i] = min([Z[i-1]+C[i-1], *(F[j]+Z[max(0, i-D[j], T[max(U[i-1]-P[j]+1, 0)])] for j in range(K))])
print(Z[N])