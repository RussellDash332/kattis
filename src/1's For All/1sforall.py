n = int(input())
dp = [10**9]*(n+1)
dp[1] = 1
for k in range(2, n+1):
    for l in range(1, k//2+1):
        dp[k] = min(dp[k], dp[k-l]+dp[l])
    for l in range(2, int(k**0.5)+1):
        if k % l == 0: dp[k] = min(dp[k], dp[k//l]+dp[l])
    s = str(k)
    for i in range(len(s)-1):
        if s[i+1] != '0': dp[k] = min(dp[k], dp[int(s[:i+1])]+dp[int(s[i+1:])])
print(dp[n])