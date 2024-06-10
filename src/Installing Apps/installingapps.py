import sys; input = sys.stdin.readline
n, C = map(int, input().split()); P = []
for i in range(n): d, s = map(int, input().split()); P.append((s-d, s, d, i+1))
P.sort(); INF = 10**9; dp = [[(INF, INF, 1) for _ in range(n+1)] for _ in range(n+1)]
for i in range(n+1): dp[i][0] = (0, 0, 1)
for i in range(1, n+1):
    for j in range(1, i+1):
        w2, w, _ = dp[i-1][j-1]; dp[i][j] = dp[i-1][j]
        if (v:=max(w, w2+max(P[i-1][1], P[i-1][2]))) <= C: dp[i][j] = min(dp[i][j], (w2+P[i-1][1], v, i-1))
for k in range(n, -1, -1):
    if dp[n][k][1] <= C:
        print(k); pp = []; p = n
        while k: pp.append(P[dp[p][k][2]][3]); p = dp[p][k][2]; k -= 1
        print(*pp[::-1]); break