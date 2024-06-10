s = input(); n = len(s); dp = [[1000]*n for _ in range(n)]
for i in range(n): dp[i][i] = 1
for l in range(2, n+1):
    for i in range(n-l+1):
        dp[i][i+l-1] = l
        for k in range(i, i+l-1): dp[i][i+l-1] = min(dp[i][i+l-1], dp[i][k]+dp[k+1][i+l-1])
        for k in range(1, l):
            if l%k == 0:
                ok = 1
                for m in range(k, l):
                    if s[i+m] != s[i+m%k]: ok = 0; break
                if ok: dp[i][i+l-1] = min(dp[i][i+l-1], dp[i][i+k-1])
print(dp[0][-1])