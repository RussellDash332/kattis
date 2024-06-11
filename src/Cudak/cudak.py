# P[i][j] = num of nonnegative integers <= 10**i-1 with digital sum <= j
M = 16; P = [[0]*(9*M+1) for _ in range(M+1)]; P[0][0] = 1
for i in range(1, M+1):
    for j in range(9*M-8):
        for k in range(10): P[i][j+k] += P[i-1][j]
for i in range(M+1):
    for j in range(1, 9*M+1): P[i][j] += P[i][j-1]

def f(K, S):
    K = [*map(int, str(K+1))]; K = [0]*(M-len(K))+K; m = M; z = 0; s = S
    while m:
        for i in range(K[M-m]): z += P[m-1][s-i] if s-i >= 0 else 0
        s -= K[M-m]; m -= 1
    return z

A, B, S = map(int, input().split()); print(f(B, S)-f(A-1, S)-f(B, S-1)+f(A-1, S-1))
A = [*map(int, str(A))]; A = [0]*(M-len(A))+A; B = [*map(int, str(B))]; B = [0]*(M-len(B))+B

def find(d, t, p, s):
    if s < 0 or s > 9*(M-d): return
    if d == M: print(p), exit(0)
    for i in range(A[d], (min(s, B[d]), 9)[t]+1): find(d+1, t or i!=B[d], 10*p+i, s-i)
find(0, 0, 0, S)