import sys; input = sys.stdin.readline
N, K = map(int, input().split())
P = [*map(float, input().split())]
W = []; F = [1, 0]; Z = [1]+[0]*N; z = 0
for i in range(K):
    Z[i+1] = 1-P[i]
    if P[i]: F[0] *= P[i]
    else: F[1] += 1
W.append(0 if F[1] else F[0])
for i in range(K, N):
    if P[i]: F[0] *= P[i]
    else: F[1] += 1
    if P[i-K]: F[0] /= P[i-K]
    else: F[1] -= 1
    W.append(0 if F[1] else F[0])
for i in range(K, N+1): Z[i] = (1-z)*(1-P[i-1]); z += W[i-K]*Z[i-K]
print(z)