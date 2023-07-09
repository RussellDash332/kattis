import sys
INF, N = 1e18, 10**6; A, B, C, D, n, s = [0]*(N+1), [0]*(N+1), [INF]*(N+1), [INF]*(N+1), 0, 0
for l in sys.stdin:
    if n:
        a, B[n], D[n] = [*map(int, l.split())], 0, INF
        for i in range(1, n+1): A[i] = A[i-1] + a[i-1]; C[i] = min(A[i], C[i-1])
        for i in range(n-1, -1, -1): B[i] = B[i+1] + a[i]; D[i] = a[i] + min(D[i+1], 0)
        for i in range(n): s += D[i] >= 0 and (i == 0 or B[i] + C[i+1] >= 0)
        print(s); n = s = 0
    else: n = int(l)