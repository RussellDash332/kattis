import sys; input = sys.stdin.readline; from array import *; Z = 10**9+7
N, Q = map(int, input().split()); M = array('i', [-1]*N)
for _ in range(Q):
    a, b = map(int, input().split()); a -= 1; b -= 1
    if a < b: a, b = b, a
    M[a] = max(M[a], b)
dp = array('i', [1]*(N+1)); P = 1; k = -1
for i in range(N):
    while k < M[i]: P -= dp[k]; k += 1
    dp[i] = P%Z; P = 2*P%Z
print(dp[-2])